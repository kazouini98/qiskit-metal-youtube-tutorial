from re import L
from qiskit_metal import draw, Dict
from qiskit_metal.qlibrary import QComponent


class MyQComponent2(QComponent):

    default_options = Dict(
        width='0.5mm',
        height='0.1mm',
        pos_x='0mm',
        pos_y='0mm',
        layer='1'
    )

    def make(self):
        p=self.parse_options(
        ) # short-handle alias for the options interpreter

        rect = draw.rectangle(p.width, p.height, p.pos_x, p.pos_y)
        self.add_qgeometry(
        'poly', {'my_polygon': rect},
        layer=p.layer,
        substract=False
        )
        self.add_pin('in', rect.exterior.coords[:-3:-1], p.height)

class MyQComponent3(QComponent):


    default_options = Dict(
        width='0.5mm',
        height='0.1mm',
        pos_x='0mm',
        pos_y='0mm',
        layer='1'
    )

    # name perfix of component + import of the render-specific default_options
    component_metadata = Dict(
        short_name='Trace',  # define the short name
        _qgeometry_table_path='False',  # wirebonds
        _qgeometry_table_poly='True',  # created a poly
        _qgeometry_table_junction='False'
    )

    def make(self):
        p=self.parse_options(
        ) # short-handle alias for the options interpreter

        rect = draw.rectangle(p.width, p.height, p.pos_x, p.pos_y)
        self.add_qgeometry(
        'poly', {'my_polygon': rect},
        layer=p.layer,
        substract=False
        )
        self.add_pin('in', rect.exterior.coords[:-3:-1], p.height)



class MyQComponent4(QComponent):

    default_options = Dict(
        width='0.5mm',
        height='0.1mm',
        gap= '0.02mm',
        pos_x='0mm',
        pos_y='0mm',
        layer='1'
    )

    # ok

    component_metadata = Dict(
        short_name='Trace',  # define the short name
        _qgeometry_table_path='True',  # wirebonds
        _qgeometry_table_poly='False',  # created a poly
        _qgeometry_table_junction='False'  # GDS
    )

    def make(self):
        p=self.parse_options(
        ) # short-handle alias for the options interpreter

        # the False substract (+ve)
        line = draw.LineString([(-p.width/2, 0), (p.width/2, 0)])
        line = draw.translate(line, p.pos_x, p.pos_y)
        self.add_qgeometry(
            'path', {'trace': line},
            width=p.height,
            layer=p.layer,
            substract=False
        )

        # the True substract (-ve)
        line2 = draw.LineString([((-p.width/2)-2*p.gap, 0), ((p.width/2)+2*p.gap, 0)])
        line2 = draw.translate(line2, p.pos_x, p.pos_y)
        self.add_qgeometry(
            'path', {'cut': line2},
            width=p.height + 2*p.gap,
            layer=p.layer,
            substract=True
        )
        self.add_pin('in', line.coords[::-1], p.height, input_as_norm=True)

