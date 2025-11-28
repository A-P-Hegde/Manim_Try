from manim import *
import numpy as np

# ============================================================
# HELPER: Compute angle alpha between direction and array axis
# ============================================================
def angle_from_array_axis(u, v):
    # Direction unit vector in spherical coordinates
    x = np.sin(v) * np.cos(u)
    y = np.sin(v) * np.sin(u)
    z = np.cos(v)

    r = np.array([x, y, z])
    axis = np.array([1, 0, 0])   # X-axis

    cos_alpha = np.clip(np.dot(r, axis), -1, 1)
    return np.arccos(cos_alpha)


# ============================================================
# ARRAY FACTOR
# ============================================================
def array_factor(alpha, N, d, wavelength, delta=np.pi):
    beta = 2 * np.pi / wavelength
    psi = beta * d * np.cos(alpha) + delta

    if np.isclose(psi, 0):
        return N

    return np.abs(np.sin(N * psi / 2) / np.sin(psi / 2))


# ============================================================
# MAIN SCENE
# ============================================================
class BroadsideArrayPattern(ThreeDScene):
    def construct(self):

        axes = ThreeDAxes()
        x_label = Text("X").next_to(axes.x_axis.get_end(), UP)
        y_label = Text("Y").next_to(axes.y_axis.get_end(), OUT)
        z_label = Text("Z").next_to(axes.z_axis.get_end(), RIGHT)
        self.set_camera_orientation(phi=65 * DEGREES, theta=30 * DEGREES)

        self.add(axes,x_label,y_label,z_label)
        # --------------------------------------------------------
        # PARAMETERS
        # --------------------------------------------------------
        wavelength = 1.0
        N = 4
        d = wavelength / 2

        # --------------------------------------------------------
        # Antenna positions on X-axis
        # --------------------------------------------------------
        positions = np.linspace(-d, d, N)
        antennas = VGroup(
            *[Sphere(radius=0.08, color=YELLOW).move_to([x, 0, 0]) for x in positions]
        )
        self.add(antennas)

        # --------------------------------------------------------
        # 3D Array Pattern Surface (Manim v0.19 requires Surface)
        # --------------------------------------------------------
        def surface_func(u, v):
            alpha = angle_from_array_axis(u, v)
            R = array_factor(alpha, N, d, wavelength)

            # Spherical → Cartesian
            x = R * np.sin(v) * np.cos(u)
            y = R * np.sin(v) * np.sin(u)
            z = R * np.cos(v)

            return np.array([x, y, z])

        array_pattern = Surface(
            surface_func,
            u_range=[0, 2 * np.pi],
            v_range=[0, np.pi],
            resolution=(40, 20),
            fill_color=BLUE,
            fill_opacity=0.5,   # v0.19 supports this
            stroke_opacity=0.1,
        ).scale(1)

        self.play(FadeIn(array_pattern), run_time=2)

        # --------------------------------------------------------
        # Move camera around (v0.19 way)
        # --------------------------------------------------------
        self.move_camera(theta=120 * DEGREES, phi=70 * DEGREES, run_time=5)

        self.wait(1)
