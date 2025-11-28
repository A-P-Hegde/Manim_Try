from manim import *

class ScaleVectorFieldFunction(Scene):
    def construct(self):

        #adding Numberplane
        plane = NumberPlane(
            x_range=[-10, 10,1],
            y_range=[-10, 10,1],
            background_line_style={"stroke_color": BLUE, "stroke_width": 1, "stroke_opacity": 0.7}
        )

        self.add(plane)

        # add ur function here
        func = lambda pos: np.tan(pos[0])*RIGHT

        #making vector field with the function
        vector_field = ArrowVectorField(func)  #add it if u wish
        #self.add(vector_field)
        self.wait()

        #adding scale factor to the vector field     remember uve not displayed the vector field here
        func = VectorField.scale_func(func, 0.5)

        #making a arrow field
        field=ArrowVectorField(func)

        self.play(GrowArrow(var) for var in field)
        self.wait()



        