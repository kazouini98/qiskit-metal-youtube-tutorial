
# Floating transmon.
The floating transmon is a QGeometry.
### Criterias of a Qcomponenct
QGeometry contain 3 different criterias which are:
    * path: center lines that helps us to create a path
            a False subtract will be a metal
            a True subtract will be a cutout
    * poly: creates the chapes for us and it also has False and True Subtract
    * junction: it is a vector line string (so, they are represented differently depending on what we are rendering) for example in GDS this part is replaced by my_other_junction file

### Pins
* Contact  point between two QComponents
* Have position and direction
* Routing Algo uses pins as start-end points
* Two pins can be connected so they create a net
* the pins are called nets in qiskit-metal

### Creating a Geometry
* We only need to create a make() function
* __init__() and rebuild() are enherited from the QComponent class

### Making Connections
auto rounding/pass finder:
how to connects points A and B without hitting obstacles with cpw
















