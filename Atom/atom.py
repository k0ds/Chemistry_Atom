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
        bondText2 = Text("Shared electrons balance attraction and repulsion", color=YELLOW, font_size=25)
        bondText3 = Text("This allows each atom to reach a full valence shell", color=YELLOW, font_size=25).next_to(bondText2, DOWN)
       
        bondtextG = VGroup(bondText2, bondText3).next_to(atomText, DOWN)
        bondttext4 = Text("And reach stability.", color=ORANGE, font_size=30).to_edge(DOWN)
       


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

        atom1Center =  orbit1.get_center()
        atom2Center = orbit1.get_center()

        atomH = Text("H", color=WHITE, font_size=40).next_to(atom1, atom1Center)
        atomH2 = Text("H", color=WHITE, font_size=40).next_to(atom2, atom2Center)

        self.play(Create(atom2))
        self.play(atom2.animate.shift(LEFT))

       
        

        for i in range(5):


            self.play(MoveAlongPath(elec2, orbit2, rate_func=linear), MoveAlongPath(elec1, orbit1, rate_func=linear))

        self.play(atom1.animate.shift(DOWN))
        self.play(atom2.animate.shift(DOWN))

        self.play(Create(bondText))
       

        self.play(atom1.animate.next_to(atom2, RIGHT), atom2.animate.next_to(atom1, LEFT))

        self.play(elec2.animate.shift(LEFT / 2.5))
        self.play(elec1.animate.next_to(elec2, DOWN))

        electrons = VGroup(elec1, elec2)
        self.play(electrons.animate.shift(UP / 4))

        BondedAtoms = Group(atom1, atom2)

        self.play(BondedAtoms.animate.shift(LEFT))

        self.play(FadeOut(bondText))
        self.play(atomText.animate.to_edge(UP))

        self.play(FadeIn(bondText2))
        self.play(FadeIn(bondText3))
        self.play(bondtextG.animate.shift(UP/2))

        
        self.remove(proton1,proton2)
        
        self.play(atom1.animate.set_fill(color=BLUE, opacity=1))
        self.play(atom2.animate.set_fill(color=BLUE, opacity=0.98))
        self.add(orbit1.set_opacity(0.98))
        self.add(orbit2.set_opacity(0.98))
       
        

        self.add(atomH.next_to(orbit1.get_center()))
        self.add(atomH2.next_to(orbit2.get_center()))
        

        self.play(FadeIn(bondttext4))

        self.wait(10)

        

          




        

       
