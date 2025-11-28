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
                3*np.cos(v)               # Z-coordinate 
            ]),
            u_range=[0, PI/2],         #rotation around Z-axis
            v_range=[0, PI/2],        # part of sphere
            resolution=(10, 10),      # Adjust smoothness
            color=BLUE
        ).set_opacity(0.5).set_fill(BLUE)  # Set transparency if needed
        
        #makes the part sphere
        self.play(Create(half_sphere),run_time=3)
        self.wait(1)

        #makes an arrow to the sphere 
        v1=Arrow(ORIGIN,from_polar(3,PI/4,PI/4),buff=0)
        self.play(Create(v1),run_time=2)

        #transforms the arrow to a line segment
        line1=Line3D(ORIGIN,from_polar(3,PI/4,PI/4),0.02,resolution=20)
        self.play(Transform(v1,line1),run_time=2)
        self.wait(1)
        
        #This is to mark the point of dr
        pnt1=Dot3D(from_polar(2.7,PI/4,PI/4),radius=0.02,color=YELLOW)
        self.play(Create(pnt1),run_time=0.7)

        #This is the constant theta surface here the surface is also very small
        smal_surf=Surface(
            lambda u, v: np.array([
                u*np.cos(v)*np.sin(PI/4),  # X-coordinate
                u*np.sin(v)*np.sin(PI/4),  # Y-coordinate
                u*np.cos(PI/4)               # Z-coordinate
                ]),
                u_range=[2.7,3],         #rotation around Z-axis
                v_range=[PI/4,PI/4 + to_rad(10)],        # part of sphere
                resolution=(10, 10),      # Adjust smoothness
        ).set_fill(PINK)

        #here the line sweeps the small area (constant theta area)
        line3=Line3D(ORIGIN,from_polar(3,PI/4 + to_rad(10),PI/4),resolution=20)
        self.play(Create(smal_surf), Transform(line1,line3))
        self.wait(1)
        
        # #Moving camera
        # self.move_camera(phi=70 * DEGREES, theta=150* DEGREES,run_time =2)
        # self.wait(2)
                                                    
        