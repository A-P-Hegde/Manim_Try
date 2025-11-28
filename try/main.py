from manim import *

class Example(ThreeDScene):
    def construct(self):
        # Create a 3D axis
        axis = ThreeDAxes()
        self.add(axis)

        #Convert the axis 
        def from_polar(r,phi,theta):
            return [r*np.cos(phi)*np.sin(theta)
                    , r*np.sin(phi)*np.sin(theta),
                    r*np.cos(theta)]

        self.set_camera_orientation(phi=70 * DEGREES, theta=135* DEGREES)
        
        line1=Line3D(ORIGIN,[3,1,2])
        new_position=[1,0,0]
        line2=Line3D(ORIGIN,from_polar(3,PI/4,PI/4))
        


        v1=Arrow(ORIGIN,[3,1,2],buff=0)
        self.play(Create(v1))
        self.play(Transform(v1,line2))
        self.wait(1)
        self.play(Transform(line2,line1))
        self.wait(1)
        pnt1=Dot3D(from_polar(2.7,PI/4,PI/4),radius=0.02)
        self.play(Create(pnt1),run_time=0.7)
        self.wait(1)