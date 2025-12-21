#
# Circuit Schematic editor
#
# Zim plugin for inserting Circuit schematic using python schemdraw package
# Author: block315 <block315ccc@gmail.com>
#
#

import glob

from zim.plugins import PluginClass
from zim.plugins.base.imagegenerator import \
	ImageGeneratorClass, BackwardImageGeneratorObjectType

from zim.newfs import LocalFile, TmpFile
from zim.templates import get_template
from zim.applications import Application, ApplicationError

# TODO put these commands in preferences

try:
	import schemdraw
	import schemdraw.elements as elm
except ImportError:
	schemdraw = None

class InsertCircuitPlugin(PluginClass):

	plugin_info = {
		'name': _('Insert Circuit Schematic'), # T: plugin name
		'description': _('''\
This plugin provides an circuit schematic diagram editor for zim based on Schemdraw package.

'''), # T: plugin description
		'help': 'Plugins:Equation Editor',
		'author': 'block315',
	}

	plugin_preferences = (
		('theme', 'choice', _('Theme'), "default", ("default", "dark", "solarizedd", "solarizedl", "onedork", "oceans16", "monokai", "gruvboxl", "gruvboxd", "grade3", "chesterish")),
    )

	@classmethod
	def check_dependencies(klass):
		has_schemdraw = schemdraw is not None
		return (has_schemdraw), [('has_schemdraw', has_schemdraw, True)]

class BackwardSchematicImageObjectType(BackwardImageGeneratorObjectType):

	name = 'image+circuit'
	label = _('Schemdraw')
	syntax = None
	scriptname = 'circuitschematic.txt'

class EquationGenerator(ImageGeneratorClass):

	imagefile_extension = '.svg'

	def __init__(self, plugin, notebook, page):
		ImageGeneratorClass.__init__(self, plugin, notebook, page)
		self.preferences = plugin.preferences
		self.template = get_template('plugins', 'schemdraweditor.py')
		self.attachment_folder = notebook.get_attachments_dir(page)
		self.schemdrawfile = TmpFile('circuitschematic.txt')

	def generate_image(self, text):
		print("Incoming texts", type(text), text)
		text = text.replace("\n", "\n    ")
		schemdrawfile = self.schemdrawfile
		svgfile = LocalFile(schemdrawfile.path[:-4] + '.svg')

		template_vars = {
			'schemdraw_script': text,
			'circuit_svg_fname': svgfile.path,
			'theme': self.preferences['theme']
		}
		if self.attachment_folder and self.attachment_folder.exists():
			template_vars['attachment_folder'] = self.attachment_folder.path
		else:
			template_vars['attachment_folder'] = ''

		lines = []
		self.template.process(lines, template_vars)
		schemdrawfile.writelines(lines)
		print('>>>%s<<<' % schemdrawfile.read())

		# Call Schemdraw
		try:
			_python_for_schemdraw = Application(('python',))
			_python_for_schemdraw.run(args=(schemdrawfile.basename, ), cwd=schemdrawfile.parent())
		except ApplicationError:
			return None, None
		else:
			return svgfile, None

	def cleanup(self):
		path = self.schemdrawfile.path
		for path in glob.glob(path[:-4] + '.*'):
			LocalFile(path).remove()