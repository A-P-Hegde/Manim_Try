from manim import *

class ElecField(Scene):
    def construct(self):

        plane = NumberPlane(
            x_range=[-10, 10],
            y_range=[-10, 10],
            background_line_style={"stroke_color": BLUE, "stroke_width": 1, "stroke_opacity": 1}
        ).add_coordinates()

        subplane = NumberPlane(
            x_range=[-10, 10, 0.5],
            y_range=[-10, 10, 0.5],
            background_line_style={"stroke_color": BLUE, "stroke_width": 0.6, "stroke_opacity": 0.7}
        )

        self.add(plane, subplane)
        self.wait(0.3)

        label = plane.get_axis_labels(x_label="X", y_label="Y")
        self.play(Write(label))
        self.wait(1)

        # Define the curve
        pts = [
            [0, 0, 0],
            [0.7, 0, 0],
            [0.7, 0.4, 0],
            [1, 1, 0],
            [2, 1.4, 0],
        ]
        curve = VMobject().set_points_smoothly(pts)

        # Move the point charge without updating the field
        point = Dot(radius=0.08, color=YELLOW_A)
        self.add(point)

        # Electric field function (fixed origin for now to be faster)
        def electric_field_func(p):
            x, y = p[:2]
            r_squared = x**2 + y**2
            B0 = 2

            if r_squared == 0:
                return np.array([0, 0, 0])

            return B0 * np.array([np.sign(x) / r_squared, np.sign(y) / r_squared, 0])

        # Pre-calculated vector field (no redraw, much faster!)
        vector_field = ArrowVectorField(
            electric_field_func,
            x_range=[-10, 10, 2],
            y_range=[-10, 10, 2],
            colors=[RED_B, YELLOW_A, GREEN]
        )

        self.add(vector_field)

        # Animate point charge moving along the curve
        self.play(MoveAlongPath(point, curve), run_time=6, rate_func=linear)

        self.wait(2)
                                                                                                                                                                                                        
