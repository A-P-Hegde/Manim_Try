from manim import *
import numpy as np

class ParaboloidSurface(ThreeDScene):
    def construct(self):
        # Coefficients
        a = 1
        b = 1
        c = 0

        # Create 3D axes
        axes = ThreeDAxes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            z_range=[0, 50, 5],  # Z values are positive because of the square
        )

        # Define the surface: S = (a*x + b*y + c)^2
        def surface_func(u, v):
            x = u
            y = v
            S = (a * x + b * y + c) ** 2
            z = S
            return np.array([x, y, z])

        # Create the surface
        surface = Surface(
            lambda u, v: surface_func(u, v),
            u_range=[-5, 5],
            v_range=[-5, 5],
            resolution=(30, 30),
            fill_opacity=0.75,
            checkerboard_colors=[BLUE_D, BLUE_E],  # Optional color choice
        )

        # Camera orientation
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES, zoom=0.7)

        # Add to the scene
        self.add(axes, surface)

        # Rotate the camera to visualize better
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(6)
        self.stop_ambient_camera_rotation()

