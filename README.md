# Circuit Schematic editor
Simple plugin to insert circuit schematic in [zim](https://zim-wiki.org/) using [Schemdraw](https://schemdraw.readthedocs.io/en/stable/).
This plugin is adapted from Alessandro Magni's gnuplot_ploteditor and Jaap Karssenberg's equationeditor plugin.

## Installation
1. install schemdraw package
```
sudo pip install schemdraw
```
2. install this plugins
    - copy `circuitschematiceditor.py` to `~/.local/share/zim/plugins`
    - copy `schemdraweditor.py` to `~/.local/share/zim/templates/plugins`
3. restart zim
4. enable this plugin

## How to use
see [schemdraw documentation](https://schemdraw.readthedocs.io/en/stable/usage/index.html) for more information about drawing circuits. Data stored in txt file.

### example circuitschematic.txt file
```
elm.Resistor()
elm.Capacitor()
elm.Diode()
```
you can use without `elm.`
```
Resistor()
Capacitor()
Diode()
```