from manim import *
import numpy as np

class InnerProductPresentation(Scene):
    def construct(self):

        # Bagian 1: Pengertian Dasar
        title = Text("Ruang Hasil Kali Dalam", font="Times New Roman").scale(1.5)
        subtitle = Text("(Inner Product Space)", font="Times New Roman").scale(0.8)
        subtitle.next_to(title, DOWN)
        
        self.play(Write(title))
        self.play(Write(subtitle))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))
        
 
        
        def create_vector_scene():
            ax = Axes(
                x_range=[-3, 3],
                y_range=[-3, 3],
                axis_config={"include_tip": True}
            )
            
            vector1 = Arrow(ax.c2p(0, 0), ax.c2p(2, 1), buff=0, color=BLUE)
            vector2 = Arrow(ax.c2p(0, 0), ax.c2p(1, 2), buff=0, color=RED)
            
            vector1_label = MathTex("\\vec{u}").next_to(vector1.get_end(), RIGHT)
            vector2_label = MathTex("\\vec{v}").next_to(vector2.get_end(), UP)
            
            return VGroup(ax, vector1, vector2, vector1_label, vector2_label)
        
        # Inner Product Definition
        inner_product_def = VGroup(
            Text("Inner Product adalah hasil kali dalam yang memenuhi:", font="Times New Roman"),
            MathTex("1. \\langle u,v \\rangle = \\langle v,u \\rangle"),
            MathTex("2. \\langle au,v \\rangle = a\\langle u,v \\rangle"),
            MathTex("3. \\langle u+v,w \\rangle = \\langle u,w \\rangle + \\langle v,w \\rangle"),
            MathTex("4. \\langle u,u \\rangle \\geq 0")
        ).arrange(DOWN, buff=0.5)
        
        self.play(Write(inner_product_def))
        self.wait(2)
        self.play(FadeOut(inner_product_def))
        
        # Bagian 2: Visualisasi Vektor
        vector_scene = create_vector_scene()
        self.play(Create(vector_scene))
        self.wait(2)
        
        # Rumus Dot Product
        dot_product = MathTex(
            "\\langle u,v \\rangle = u_1v_1 + u_2v_2 + ... + u_nv_n"
        ).to_edge(UP)
        
        self.play(Write(dot_product))
        self.wait(2)
        
        # Bagian 3: Orthonormal Vectors
        orthonormal_title = Text("Vektor Orthonormal", font="Times New Roman").to_edge(UP)
        
        orthonormal_def = VGroup(
            MathTex("\\text{Dua vektor } u \\text{ dan } v \\text{ orthogonal jika:}"),
            MathTex("\\langle u,v \\rangle = 0"),
            MathTex("\\text{Vektor normal jika:}"),
            MathTex("||u|| = 1")
        ).arrange(DOWN, buff=0.5)
        
        self.play(
            FadeOut(vector_scene),
            FadeOut(dot_product),
            Write(orthonormal_title),
            Write(orthonormal_def)
        )
        self.wait(2)
        
        # Bagian 4: Proses Gram-Schmidt
        gram_schmidt_title = Text("Proses Gram-Schmidt", font="Times New Roman").to_edge(UP)
        
        gram_schmidt_process = VGroup(
            MathTex("v_1 = u_1"),
            MathTex("v_2 = u_2 - \\text{proj}_{v_1}(u_2)"),
            MathTex("v_3 = u_3 - \\text{proj}_{v_1}(u_3) - \\text{proj}_{v_2}(u_3)"),
            MathTex("\\text{dengan: } \\text{proj}_a(b) = \\frac{\\langle b,a \\rangle}{\\langle a,a \\rangle}a")
        ).arrange(DOWN, buff=0.5)
        
        self.play(
            FadeOut(orthonormal_title),
            FadeOut(orthonormal_def),
            Write(gram_schmidt_title),
            Write(gram_schmidt_process)
        )
        self.wait(3)
        
        # Penutup
        closing = Text("Terima Kasih", font="Times New Roman").scale(1.5)
        self.play(
            FadeOut(gram_schmidt_title),
            FadeOut(gram_schmidt_process),
            Write(closing)
        )
        self.wait(2)

class Projections(Scene):
    def construct(self):
        # Membuat sistem koordinat
        ax = Axes(
            x_range=[-3, 3],
            y_range=[-3, 3],
            axis_config={"include_tip": True}
        )
        
        # Membuat vektor
        vector_a = Arrow(ax.c2p(0, 0), ax.c2p(2, 1), buff=0, color=BLUE)
        vector_b = Arrow(ax.c2p(0, 0), ax.c2p(1, 2), buff=0, color=RED)
        
        # Label vektor
        label_a = MathTex("\\vec{a}").next_to(vector_a.get_end(), RIGHT)
        label_b = MathTex("\\vec{b}").next_to(vector_b.get_end(), UP)
        
        # Proyeksi
        proj_line = DashedLine(
            ax.c2p(2, 1),
            ax.c2p(1.2, 2.4),
            color=GREEN
        )
        
        proj_vector = Arrow(
            ax.c2p(0, 0),
            ax.c2p(0.6, 1.2),
            buff=0,
            color=GREEN
        )
        
        # Formula proyeksi
        proj_formula = MathTex(
            "\\text{proj}_b(a) = \\frac{\\langle a,b \\rangle}{\\langle b,b \\rangle}b"
        ).to_edge(UP)
        
        # Animasi
        self.play(Create(ax))
        self.play(Create(vector_a), Write(label_a))
        self.play(Create(vector_b), Write(label_b))
        self.wait()
        
        self.play(Write(proj_formula))
        self.play(Create(proj_line), Create(proj_vector))
        self.wait(2)