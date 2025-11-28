from manim import *
import numpy as np

class MultiDentedSphere(ThreeDScene):
    def construct(self):
        # Set camera position
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # Add axes for reference
        axes = ThreeDAxes()
        self.add(axes)

        # Define dent parameters: (theta, phi, radius, depth)
        dents = [
            (PI / 3, PI / 2, 0.4, 0.3),     # Dent 1Prelo
            (PI / 2, PI / 4, 0.5, 0.4),     # Dent 2
            (2 * PI / 3, 3 * PI / 4, 0.3, 0.2), # Dent 3
            (PI / 4, 5 * PI / 4, 0.6, 0.5), # Dent 4
            (PI / 1.8, PI / 1.2, 0.4, 0.3), # Dent 5
        ]

        # Function that calculates the radius, including all dents
        def dent_function(theta, phi):
            base_r = 2  # Normal radius of the sphere
            total_dent = 0

            for dent_theta, dent_phi, dent_radius, dent_depth in dents:
                # Angular distance from current point to dent center
                angular_distance = np.sqrt(
                    (theta - dent_theta)**2 + (phi - dent_phi)**2
                )

                # Exponential falloff for smooth dents
                dent_effect = np.exp(- (angular_distance / dent_radius)**2)

                # Sum the dent effects
                total_dent += dent_depth * dent_effect

            # Subtract the combined dents from the base radius
            r = base_r - total_dent
            return r

        # Parametric function mapping (theta, phi) to (x, y, z)
        def dented_sphere(theta, phi):
            r = dent_function(theta, phi)
            x = r * np.sin(theta) * np.cos(phi)
            y = r * np.sin(theta) * np.sin(phi)
            z = r * np.cos(theta)
            return np.array([x, y, z])

        # Create the surface
        dented_surface = Surface(
            lambda u, v: dented_sphere(
                interpolate(0, PI, u),       # theta
                interpolate(0, 2 * PI, v)    # phi
            ),
            u_range=[0, 1],
            v_range=[0, 1],
            resolution=(15, 13),
            fill_opacity=0.85,
            checkerboard_colors=[BLUE_D, BLUE_E],
        )

        # Add a dot at the origin to represent a point charge
        point_charge = Dot3D(point=ORIGIN, color=RED, radius=0.1)

        # Add the surface and the point to the scene
        self.add(dented_surface, point_charge)

        # Rotate the surface for a better view
        self.play(Rotate(dented_surface, angle=2 * PI, axis=UP, run_time=8))
        self.wait()

        
