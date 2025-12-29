import schemdraw
from schemdraw.elements import *
import schemdraw.elements as elm
from schemdraw import logic
from schemdraw.logic import *

schemdraw.theme('[% theme %]')
with schemdraw.Drawing(show=False, file='[% circuit_svg_fname %]'):
    [% schemdraw_script %]