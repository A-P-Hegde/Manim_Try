from manim import *
import numpy as np

class MagneticFieldScene(Scene):
    def magnetic_field_func(self, p):
        x, y = p[:2]
        r_squared = x**2 + y**2
        if r_squared == 0:
            return np.array([0, 0, 0])
        B0 = 2
        vec = B0 * np.array([-y / r_squared, x / r_squared, 0])
        return vec / np.linalg.norm(vec) * 0.4  # Normalize for size

    def construct(self):
        # Make plane large and fill screen
        plane = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            background_line_style={
                "stroke_color": GREY,
                "stroke_width": 0.8,
                "stroke_opacity": 0.4
            },
        ).scale(1.5)  # Zoom in

        self.add(plane)

        # Add the vector field using GrowArrow
        arrows = VGroup()
        for x in np.arange(-7, 7, 1):
            for y in np.arange(-7, 7, 1):
                pos = np.array([x, y, 0])
                vec = self.magnetic_field_func(pos)
                arrow = Arrow(
                    start=pos,
                    end=pos + vec,
                    buff=0,
                    stroke_width=2,
                    max_tip_length_to_length_ratio=0.3,
                    color=interpolate_color(BLUE, GREEN, np.linalg.norm(vec))
                )
                arrows.add(arrow)

        self.play(LaggedStart(*[GrowArrow(arrow) for arrow in arrows], lag_ratio=0.02, run_time=3))
        self.wait(2)
