from manim import *
import numpy as np


class Main(Scene):
    def create_vector_scene(self):
        ax = Axes(x_range=[-3, 3], y_range=[-3, 3], axis_config={"include_tip": True})

        vector1 = Arrow(ax.c2p(0, 0), ax.c2p(2, 1), buff=0, color=BLUE)
        vector2 = Arrow(ax.c2p(0, 0), ax.c2p(1, 2), buff=0, color=RED)

        vector1_label = MathTex(r"\vec{u}").next_to(vector1.get_end(), RIGHT)
        vector2_label = MathTex(r"\vec{v}").next_to(vector2.get_end(), UP)

        return VGroup(ax, vector1, vector2, vector1_label, vector2_label)

    def create_practice_problems(self):
        return VGroup(
            Text("Soal Latihan:", font="Times New Roman", color=YELLOW),
            MathTex(
                r"\text{1. Hitunglah sudut antara vektor } u = (1,2) \text{ dan } v = (2,1)"
            ),
            MathTex(
                r"\text{2. Tentukan basis orthonormal untuk subspace yang direntang oleh:}"
            ),
            MathTex(r"\{(1,1,0), (1,0,1), (0,1,1)\}"),
            MathTex(
                r"\text{3. Tentukan proyeksi orthogonal } (3,2,1) \text{ pada } (1,1,1)"
            ),
        ).arrange(DOWN, buff=0.5)

    def show_inner_product_intro(self):
        title = Text("Ruang Hasil Kali Dalam", font="Times New Roman").scale(1.5)
        subtitle = Text("(Inner Product Space)", font="Times New Roman").scale(0.8)
        subtitle.next_to(title, DOWN)

        self.play(Write(title))
        self.play(Write(subtitle))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))

        inner_product_def = VGroup(
            Text(
                "Inner Product adalah hasil kali dalam yang memenuhi:",
                font="Times New Roman",
            ),
            MathTex(r"1. \langle u,v \rangle = \langle v,u \rangle"),
            MathTex(r"2. \langle au,v \rangle = a\langle u,v \rangle"),
            MathTex(
                r"3. \langle u+v,w \rangle = \langle u,w \rangle + \langle v,w \rangle"
            ),
            MathTex(r"4. \langle u,u \rangle \geq 0"),
        ).arrange(DOWN, buff=0.5)

        self.play(Write(inner_product_def))
        self.wait(2)
        self.play(FadeOut(inner_product_def))

    def show_projections(self):
        ax = Axes(x_range=[-3, 3], y_range=[-3, 3], axis_config={"include_tip": True})

        vector_a = Arrow(ax.c2p(0, 0), ax.c2p(2, 1), buff=0, color=BLUE)
        vector_b = Arrow(ax.c2p(0, 0), ax.c2p(1, 2), buff=0, color=RED)

        label_a = MathTex(r"\vec{a}").next_to(vector_a.get_end(), RIGHT)
        label_b = MathTex(r"\vec{b}").next_to(vector_b.get_end(), UP)

        proj_line = DashedLine(ax.c2p(2, 1), ax.c2p(1.2, 2.4), color=GREEN)

        proj_vector = Arrow(ax.c2p(0, 0), ax.c2p(0.6, 1.2), buff=0, color=GREEN)

        proj_formula = MathTex(
            r"\text{proj}_b(a) = \frac{\langle a,b \rangle}{\langle b,b \rangle}b"
        ).to_edge(UP)

        self.play(Create(ax))
        self.play(Create(vector_a), Write(label_a))
        self.play(Create(vector_b), Write(label_b))
        self.wait()

        self.play(Write(proj_formula))
        self.play(Create(proj_line), Create(proj_vector))
        self.wait(2)

    def show_inner_product_example(self):
        title = Text("Contoh Soal: Inner Product", font="Times New Roman").scale(1.2)

        problem = VGroup(
            Text("Hitunglah hasil kali dalam dari vektor:", font="Times New Roman"),
            MathTex(r"u = (2,1,3)"),
            MathTex(r"v = (1,-1,2)"),
        ).arrange(DOWN, buff=0.5)

        solution = VGroup(
            Text("Penyelesaian:", font="Times New Roman"),
            MathTex(r"\langle u,v \rangle = u_1v_1 + u_2v_2 + u_3v_3"),
            MathTex(r"= (2)(1) + (1)(-1) + (3)(2)"),
            MathTex(r"= 2 - 1 + 6"),
            MathTex(r"= 7"),
        ).arrange(DOWN, buff=0.5)

        self.play(Write(title))
        self.wait()
        self.play(title.animate.to_edge(UP))

        self.play(Write(problem))
        self.wait(2)

        self.play(problem.animate.to_edge(LEFT))
        solution.next_to(problem, RIGHT, buff=1)
        self.play(Write(solution))
        self.wait(3)

    def show_orthonormal_example(self):
        title = Text("Contoh Soal: Orthonormal Vectors", font="Times New Roman").scale(
            1.2
        )

        problem = VGroup(
            Text("Tentukan apakah vektor berikut orthonormal:", font="Times New Roman"),
            MathTex(r"u = (\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}, 0)"),
            MathTex(r"v = (-\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}, 0)"),
        ).arrange(DOWN, buff=0.5)

        solution = VGroup(
            Text("Langkah 1: Cek orthogonality", font="Times New Roman"),
            MathTex(
                r"\langle u,v \rangle = (\frac{1}{\sqrt{2}})(-\frac{1}{\sqrt{2}}) + (\frac{1}{\sqrt{2}})(\frac{1}{\sqrt{2}}) + (0)(0)"
            ),
            MathTex(r"= -\frac{1}{2} + \frac{1}{2} + 0 = 0"),
            Text("Langkah 2: Cek normal (||u|| = ||v|| = 1)", font="Times New Roman"),
            MathTex(
                r"||u|| = \sqrt{(\frac{1}{\sqrt{2}})^2 + (\frac{1}{\sqrt{2}})^2 + 0^2} = 1"
            ),
            MathTex(
                r"||v|| = \sqrt{(-\frac{1}{\sqrt{2}})^2 + (\frac{1}{\sqrt{2}})^2 + 0^2} = 1"
            ),
            Text(
                "Kesimpulan: Vektor u dan v orthonormal",
                font="Times New Roman",
                color=GREEN,
            ),
        ).arrange(DOWN, buff=0.5)

        self.play(Write(title))
        self.wait()
        self.play(title.animate.to_edge(UP))

        self.play(Write(problem))
        self.wait(2)

        self.play(problem.animate.to_corner(UL))
        solution.next_to(problem, DOWN, buff=1)
        self.play(Write(solution))
        self.wait(3)

    def show_gram_schmidt_example(self):
        title = Text("Contoh Soal: Proses Gram-Schmidt", font="Times New Roman").scale(
            1.2
        )

        problem = VGroup(
            Text("Orthonormalisasi basis berikut:", font="Times New Roman"),
            MathTex(r"u_1 = (1,0,0)"),
            MathTex(r"u_2 = (1,1,0)"),
            MathTex(r"u_3 = (1,1,1)"),
        ).arrange(DOWN, buff=0.5)

        solution = VGroup(
            Text("Langkah 1: v₁ = u₁", font="Times New Roman"),
            MathTex(r"v_1 = (1,0,0)"),
            Text("Langkah 2: Hitung v₂", font="Times New Roman"),
            MathTex(r"v_2 = u_2 - \text{proj}_{v_1}(u_2)"),
            MathTex(
                r"= (1,1,0) - \frac{\langle (1,1,0),(1,0,0)\rangle}{\langle (1,0,0),(1,0,0)\rangle}(1,0,0)"
            ),
            MathTex(r"= (1,1,0) - (1)(1,0,0)"),
            MathTex(r"= (0,1,0)"),
            Text("Langkah 3: Hitung v₃", font="Times New Roman"),
            MathTex(r"v_3 = u_3 - \text{proj}_{v_1}(u_3) - \text{proj}_{v_2}(u_3)"),
            MathTex(r"= (1,1,1) - (1)(1,0,0) - (1)(0,1,0)"),
            MathTex(r"= (0,0,1)"),
        ).arrange(DOWN, buff=0.3)

        normalization = VGroup(
            Text("Normalisasi:", font="Times New Roman"),
            MathTex(r"e_1 = \frac{v_1}{||v_1||} = (1,0,0)"),
            MathTex(r"e_2 = \frac{v_2}{||v_2||} = (0,1,0)"),
            MathTex(r"e_3 = \frac{v_3}{||v_3||} = (0,0,1)"),
        ).arrange(DOWN, buff=0.3)

        self.play(Write(title))
        self.wait()
        self.play(title.animate.to_edge(UP))

        self.play(Write(problem))
        self.wait(2)

        self.play(problem.animate.to_corner(UL))
        solution.next_to(problem, RIGHT, buff=1)
        self.play(Write(solution))
        self.wait(2)

        normalization.next_to(solution, DOWN, buff=1)
        self.play(Write(normalization))
        self.wait(3)

    def show_projection_example(self):
        title = Text("Contoh Soal: Proyeksi Vektor", font="Times New Roman").scale(1.2)

        problem = VGroup(
            Text("Tentukan proyeksi vektor a pada vektor b:", font="Times New Roman"),
            MathTex(r"a = (2,-1,3)"),
            MathTex(r"b = (4,-1,2)"),
        ).arrange(DOWN, buff=0.5)

        solution = VGroup(
            Text("Langkah 1: Hitung ⟨a,b⟩", font="Times New Roman"),
            MathTex(
                r"\langle a,b \rangle = (2)(4) + (-1)(-1) + (3)(2) = 8 + 1 + 6 = 15"
            ),
            Text("Langkah 2: Hitung ||b||²", font="Times New Roman"),
            MathTex(r"||b||^2 = 16 + 1 + 4 = 21"),
            Text("Langkah 3: Hitung proyeksi", font="Times New Roman"),
            MathTex(r"\text{proj}_b(a) = \frac{\langle a,b \rangle}{||b||^2}b"),
            MathTex(r"= \frac{15}{21}(4,-1,2)"),
            MathTex(r"\approx (2.86, -0.71, 1.43)"),
        ).arrange(DOWN, buff=0.5)

        self.play(Write(title))
        self.wait()
        self.play(title.animate.to_edge(UP))

        self.play(Write(problem))
        self.wait(2)

        self.play(problem.animate.to_corner(UL))
        solution.next_to(problem, RIGHT, buff=1)
        self.play(Write(solution))
        self.wait(3)

    def show_practice_problems(self):
        practice_problems = self.create_practice_problems()
        self.play(Write(practice_problems))
        self.wait(3)

        tips = VGroup(
            Text("Tips Mengerjakan:", font="Times New Roman", color=BLUE),
            MathTex(r"\bullet \text{ Gunakan rumus cosinus untuk sudut antar vektor}"),
            MathTex(
                r"\bullet \text{ Ikuti langkah Gram-Schmidt untuk orthonormalisasi}"
            ),
            MathTex(
                r"\bullet \text{ Ingat rumus proyeksi: } \text{proj}_v(u) = \frac{\langle u,v \rangle}{||v||^2} \cdot v"
            ),
        ).arrange(DOWN, buff=0.3)

        tips.next_to(practice_problems, DOWN, buff=1)
        self.play(Write(tips))
        self.wait(3)

    def construct(self):
        # Show introduction and basic concepts
        self.show_inner_product_intro()
        self.clear()

        # Show projections
        self.show_projections()
        self.clear()

        # Show inner product example
        self.show_inner_product_example()
        self.clear()

        # Show orthonormal example
        self.show_orthonormal_example()
        self.clear()

        # Show Gram-Schmidt example
        self.show_gram_schmidt_example()
        self.clear()

        # Show projection example
        self.show_projection_example()
        self.clear()

        # Show practice problems
        self.show_practice_problems()
        self.clear()

        # Show closing
        closing = Text("Terima Kasih", font="Times New Roman").scale(1.5)
        self.play(Write(closing))
        self.wait(2)
