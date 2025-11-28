from manim import *
import numpy as np

class constant_theta_surface(ThreeDScene):
    def construct(self):
        # Create 3D Axes
        axes = ThreeDAxes()
        x_label = Text("X").next_to(axes.x_axis.get_end(), UP)
        y_label = Text("Y").next_to(axes.y_axis.get_end(), OUT)
        z_label = Text("Z").next_to(axes.z_axis.get_end(), RIGHT)

        #setting camera position
        self.set_camera_orientation(phi=70 * DEGREES, theta=45* DEGREES)
        
        # Add axes
        self.add(axes,x_label,y_label,z_label)
        self.wait(1)

        #function to change angle to radians
        def to_rad(angle):
            return angle * np.pi/180
        
        #Convert the axis from polar to rectangular
        def from_polar(r,phi,theta):
            return [r*np.cos(phi)*np.sin(theta)
                    , r*np.sin(phi)*np.sin(theta),
                    r*np.cos(theta)]
        
        #Add sphere
        
        #sphere=Sphere(ORIGIN,3,[30,30]).set_opacity(0.3)
        #self.play(Create(sphere),run_time=3)
        #self.wait(1)

        #Add part of a sphere
        half_sphere = Surface(
            lambda u, v: np.array([
                3*np.cos(u) * np.sin(v),  # X-coordinate
                3*np.sin(u) * np.sin(v),  # Y-coordinate
                3*np.cos(PI/4)             # Z-coordinate 
            ]),
            u_range=[0, 2*PI],         #rotation around Z-axis
            v_range=[0, PI/4],        # part of sphere
            resolution=(20, 20),      # Adjust smoothness
            color=BLUE
        ).set_opacity(0.5).set_fill(BLUE)  # Set transparency if needed
        
        #Add surface
        csa_cone=Surface(
            lambda u, v: np.array([
                v*np.cos(u) * np.sin(PI/4),  # X-coordinate
                v*np.sin(u) * np.sin(PI/4),  # Y-coordinate
                v*np.cos(PI/4)               # Z-coordinate
                ]),
                u_range=[0, 2*PI],         #rotation around Z-axis
                v_range=[0, 3],        # part of sphere
                resolution=(20, 20),      # Adjust smoothness
                color=BLUE
        ).set_opacity(0.5).set_fill(BLUE)
        #makes the part sphere
        self.play(Create(half_sphere),Create(csa_cone),run_time=5)
        self.wait(1)

        
        # #Moving camera
        # self.move_camera(phi=70 * DEGREES, theta=150* DEGREES,run_time =2)
        # self.wait(2)
                                                    
        