import schemdraw
from schemdraw.elements import *

schemdraw.theme('[% theme %]')
with schemdraw.Drawing(show=False, file='[% circuit_svg_fname %]'):
    [% schemdraw_script %]