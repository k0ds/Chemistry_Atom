from manim import *


class Atom(Scene):
    def construct(self):
        #create 2 atoms with rotating electrons
        #make them move closer and share the electrons
        
        
        proton1 = Circle(radius=0.2, color=RED, fill_opacity=1)
        orbit1 = Circle(radius=2, color=WHITE)
        p1 = orbit1.point_at_angle(270*DEGREES)


        proton2 = Circle(radius=0.2, color=RED, fill_opacity=1)
        orbit2 = Circle(radius=2, color=WHITE)
        p2 = orbit2.point_at_angle(270*DEGREES)

        elec1 = Circle(radius=0.1, color=BLUE, fill_opacity=1).move_to(p1)
        elec2 = Circle(radius=0.1, color=BLUE, fill_opacity=1).move_to(p2)

        protontext = Text("Proton + ", font_size=20).next_to(proton1, UP)
        electrontext = Text("Electron -", font_size=20).next_to(elec1, DOWN)
        atomText = Text("Hydrogen Atom  H").next_to(orbit1, UP)
        bondText = Text("Covalent Bond, electrons are shared", color=YELLOW, font_size=25).next_to(atomText, DOWN)

        self.play(Create(proton1))
        self.play(Create(orbit1))
        self.play(Create(elec1))
        self.play(Create(protontext))
        self.play(Create(electrontext))
        self.play(Create(atomText))



        for i in range(3):
            self.play(MoveAlongPath(elec1, orbit1), rate_func=linear)
            
        self.play(atomText.animate.to_edge(UP))
        self.play(FadeOut(protontext))
        self.play(FadeOut(electrontext))
        atom1 = VGroup(proton1, orbit1, elec1)
        self.play(atom1.animate.to_edge(RIGHT))

        atom2 = VGroup(proton2, orbit2, elec2)

        self.play(Create(atom2))
        self.play(atom2.animate.shift(LEFT))

       
        

        for i in range(5):


            self.play(MoveAlongPath(elec2, orbit2, rate_func=linear), MoveAlongPath(elec1, orbit1, rate_func=linear))

        self.play(atom1.animate.shift(DOWN))
        self.play(atom2.animate.shift(DOWN))

        self.play(Create(bondText))
       

        self.play(atom1.animate.next_to(atom2, RIGHT), atom2.animate.next_to(atom1, LEFT))

        self.play(elec2.animate.shift(LEFT))
        self.play(elec1.animate.next_to(elec2, DOWN))

        #figure out how to make elec2 shift to the left less, maybe through coordinates

        self.wait(5)
        

          




        

       
