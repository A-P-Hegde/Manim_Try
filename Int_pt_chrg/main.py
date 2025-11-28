from manim import *

class ElecField(Scene):
    def construct(self):

        #making a NumberPlane
        plane = NumberPlane(
            x_range=[-10, 10],
            y_range=[-10, 10],
            background_line_style={"stroke_color": BLUE, "stroke_width": 1, "stroke_opacity": 1}
        ).add_coordinates()

        #add a sub NumberPlane
        subplane=NumberPlane(
            x_range=[-10, 10,0.5],
            y_range=[-10, 10,0.5],
            background_line_style={"stroke_color": BLUE, "stroke_width": 0.6, "stroke_opacity":0.7}
        )

        self.add(plane,subplane)
        self.wait(0.3)

        #Labeling the axes
        label=plane.get_axis_labels(x_label="X",y_label="Y")
        self.play(Write(label))
        self.wait(1)

        
        
        #add a point This is my point charge
        point = Dot(point=ORIGIN, radius=0.08, color=YELLOW_A)
        self.add(point)
        self.wait(1)

        #defining a function which defines electric field vector at a point
        
        def  electric_field_func(p):
            x, y = p[:2]
            r_squared = x**2 + y**2
            B0 = 2  # Scaling factor for visualization

            if r_squared == 0:
                return np.array([0, 0, 0])  # Avoid division by zero
            
            #Outputing taking directional signs into consideration
            return B0*np.array([np.sign(x)/ r_squared , np.sign(y) / r_squared, 0])
        
        #defining vector field
        vector_field = ArrowVectorField(electric_field_func,
                                        x_range=[-10,10],
                                         y_range=[-10,10] )

        #to make a random curve using few points
        pts=[
            [0,0,0],
            [0.7,0,0],
            [0.7,0.4,0],
            [1,1,0],
            [2,1.4,0],
        ]
        curve= VMobject()
        curve.set_points_smoothly(pts).set_opacity(0)

        #playing the ArrowVectorField 
        self.play(Create(vector_field), run_time=3)
        self.wait(2)

        #moving the Vector field with the point charge
        self.play(MoveAlongPath(point,curve) , run_time=6)
        self.wait(2)


