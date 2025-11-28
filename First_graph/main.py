from manim import *

class Circle_now(Scene):
    def construct(self):

        grid=NumberPlane(
            x_range=(-25, 25, 1),  # X-axis: from -25 to 25, step size 1
            y_range=(-25, 25, 1),  # Y-axis: from -25 to 25, step size 1
            background_line_style={"stroke_color": BLUE, "stroke_width": 1, "stroke_opacity": 0.7}
        )
        sub_grid=NumberPlane(
            x_range=(-10, 10, 0.5),  # X-axis: from -10
            y_range=(-10,10,0.5),
            background_line_style={"stroke_color": BLUE,"stroke_width":0.5, "stroke_opacity": 0.5}
        )
        
        vector1=Arrow(ORIGIN,[2,2,0], buff=0, color=RED)
        vector2=Arrow(ORIGIN,[2,0,0], buff=0, color=YELLOW)
        vector3=Arrow(ORIGIN,[4,2,0], buff=0, color=BLUE)

        dot1=Dot(ORIGIN)
        origin_text=Text("(0,0)").next_to(vector1.get_start(),DOWN)
        arrow1_text=Text("(2,2)").next_to(vector1.get_end(),UP)
        arrow2_text=Text("(2,0)").next_to(vector2.get_end(),DOWN)


        self.add(grid,sub_grid)

        self.play(Create(vector1,run_time=1.5))
        self.add(origin_text,arrow1_text)
        self.wait(0.5)
        self.play(Create(vector2,run_time=1.5))       
        self.add(arrow2_text) 
        self.wait(1)
        
        self.remove(origin_text,arrow1_text,arrow2_text)

        self.play(vector1.animate.shift(RIGHT*2),run_time=1)
        self.wait(1)

        self.play(Create(vector3,run_time=1))
        self.wait(0.5)

        self.play(vector1.animate.set_opacity(0),vector2.animate.set_opacity(0),run_time=1)
        self.wait(1)




