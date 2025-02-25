from manim import *
import numpy as np

class InnerProductExamples(Scene):
    def construct(self):
        self.run_judul()

        # INGAT KEMBALI
        recall_title = Text("INGAT KEMBALI!!", font="Times New Roman").scale(1.2)
        self.play(Write(recall_title))
        self.wait(1)
        self.play(recall_title.animate.to_edge(UP))
        
        # Definition
        norm_title = Text("PANJANG (NORM) SEBUAH VEKTOR", font="Times New Roman").scale(0.8)
        norm_title.next_to(recall_title, DOWN)
        
        # Create the definition text
        definisi = Text("DEFINISI 1", font="Times New Roman", color=BLUE).scale(0.7)
        definisi.next_to(norm_title, DOWN, buff=0.5)
        
        # Membuat definisi matematis
        norm_def = MathTex(
            r"\text{Jika }\mathbf{v}=(v_1,v_2,\ldots,v_n)\text{ adalah vektor di }\mathbb{R}^n,",
            r"\text{ maka }\textbf{norm}\text{ dari }\mathbf{v}",
            r"\text{ dinotasikan dengan }\|\mathbf{v}\|",
            r"\text{ dan didefinisikan sebagai:}"
        ).scale(0.5)
        norm_def.next_to(definisi, DOWN)
        
        # Create the formula
        formula = MathTex(r"\|\mathbf{v}\|=\sqrt{v_1^2+v_2^2+v_3^2+\cdots+v_n^2}").scale(0.8)
        formula.next_to(norm_def, DOWN)
        
        # Create coordinate system for 2D vector visualization
        plane = NumberPlane(
            x_range=[-3, 3],
            y_range=[-3, 3],
            x_length=3,
            y_length=3,
        )
        plane.move_to(ORIGIN)
        
        # Create a 2D vector
        vector = Arrow(plane.coords_to_point(0, 0), 
                      plane.coords_to_point(2, 1.5), 
                      buff=0, 
                      color=BLUE)
        
        # Add coordinates
        coords = MathTex(r"(v_1,v_2)").next_to(vector.get_end(), RIGHT, buff=0.1)
        
        # Create animations
        self.play(Write(norm_title))
        self.play(Write(definisi))
        self.play(Write(norm_def))
        self.play(Write(formula))
        self.wait()
        self.play(FadeOut(norm_title), FadeOut(definisi), FadeOut(norm_def), FadeOut(formula))
        self.play(Create(plane))
        self.play(Create(vector), Write(coords))
        
        self.wait(2)
        self.play(FadeOut(plane), FadeOut(vector), FadeOut(coords),)

        # Definition
        norm_title = Text("JARAK (DISTANCE) DUA BUAH VEKTORR", font="Times New Roman").scale(0.8)
        norm_title.next_to(recall_title, DOWN)

        # Create the definition text
        definisi = Text("DEFINISI 2", font="Times New Roman", color=BLUE).scale(0.7)
        definisi.next_to(norm_title, DOWN, buff=0.5)

        # Create the mathematical definition
        dist_def = MathTex(
            r"\text{Jika }\mathbf{u}=(u_1,u_2,\ldots,u_n)\text{ dan }\mathbf{v}=(v_1,v_2,\ldots,v_n)\text{ adalah titik di }\mathbb{R}^n,\\",
            r"\text{ maka }\textbf{jarak}\text{ antara }",
            r"\mathbf{u}\text{ dan }\mathbf{v}",
            r"\text{ dinotasikan dengan }d(\mathbf{u},\mathbf{v})\text{ dan didefinisikan sebagai:}"
        ).scale(0.5)

        # Create the formula
        dist_formula = MathTex(r"d(\mathbf{u},\mathbf{v})=\|\mathbf{u}-\mathbf{v}\|=\sqrt{(u_1-v_1)^2+(u_2-v_2)^2+\cdots+(u_n-v_n)^2}").scale(0.7)
        dist_formula.next_to(dist_def, DOWN)

        # Create animations for definitions
        self.play(Write(norm_title))
        self.play(Write(definisi))
        self.play(Write(dist_def))
        self.play(Write(dist_formula))
        self.wait()

        # Create coordinate system for distance visualization
        plane = NumberPlane(
            x_range=[-3, 3],
            y_range=[-3, 3],
            x_length=3,
            y_length=3,
        )
        plane.move_to(ORIGIN)

        # Create two points and vector
        point1 = Dot(plane.coords_to_point(1, -1), color=BLUE)
        point2 = Dot(plane.coords_to_point(-2, 1.5), color=BLUE)
        vector = Arrow(point1.get_center(), point2.get_center(), buff=0, color=BLUE)

        # Labels
        p1_label = MathTex("P_1").next_to(point1, DOWN)
        p2_label = MathTex("P_2").next_to(point2, UP)
        d_label = MathTex("d").next_to(vector, RIGHT, buff=0.2)
        distance_formula = MathTex(r"d=\|\vec{P_1P_2}\|").scale(0.8)
        distance_formula.to_edge(RIGHT).shift(LEFT)

        # Create animations for visualization
        self.play(FadeOut(dist_def), FadeOut(dist_formula), FadeOut(norm_title), FadeOut(definisi))
        self.play(Create(plane))
        self.play(
            Create(point1),
            Create(point2),
            Write(p1_label),
            Write(p2_label)
        )
        self.play(Create(vector), Write(d_label))
        self.play(Write(distance_formula))
        
        self.wait(2)
        self.play(
            FadeOut(plane), FadeOut(point1), FadeOut(point2),
            FadeOut(p1_label), FadeOut(p2_label), FadeOut(vector),
            FadeOut(d_label), FadeOut(distance_formula),
        )

        norm_title = Text("HASIL KALI TITIK (DOT PRODUCT)", font="Times New Roman").scale(0.8)
        norm_title.next_to(recall_title, DOWN)

        # Create the definition text
        definisi = Text("DEFINISI 3", font="Times New Roman", color=BLUE).scale(0.7)
        definisi.next_to(norm_title, DOWN, buff=0.5)

         # Create the dot product definition
        dot_def = MathTex(
            r"\text{Jika }\mathbf{u}\text{ dan }\mathbf{v}\text{ adalah vektor tak nol di }\mathbb{R}^2\text{ atau }\mathbb{R}^3,",
            r"\text{dan }\theta\text{ adalah sudut antara }\mathbf{u}\text{ dan }\mathbf{v},\\",
            r"\text{maka hasil kali titik (dot product)}",
            r"\text{dinotasikan dengan }\mathbf{u}\cdot\mathbf{v}\text{ dan didefinisikan sebagai:}"
        ).scale(0.5)
        dot_def.next_to(definisi, DOWN)

        # Create the formula
        dot_formula = MathTex(
            r"\mathbf{u}\cdot\mathbf{v}=\|\mathbf{u}\|\|\mathbf{v}\|\cos\theta"
        ).scale(0.8)
        dot_formula.next_to(dot_def, DOWN)

        # Add zero vector case
        zero_case = MathTex(
            r"\text{Jika }\mathbf{u}=\mathbf{0}\text{ atau }\mathbf{v}=\mathbf{0},\text{ maka }\mathbf{u}\cdot\mathbf{v}=0"
        ).scale(0.6)
        zero_case.next_to(dot_formula, DOWN)

        # Display the definitions
        self.play(Write(norm_title))
        self.play(Write(definisi))
        self.play(Write(dot_def))
        self.play(Write(dot_formula))
        self.play(Write(zero_case))
        self.wait(2)

        #  ==============================================

        # Example 1: Inner Product of Vectors
        # Judul Presentasi
        title = Text("Ruang Hasil Kali Dalam", font="Times New Roman").scale(1.5)
        subtitle = Text("(Inner Product Space)", font="Times New Roman").scale(0.8)
        subtitle.next_to(title, DOWN)
        
        self.play(Write(title))
        self.play(Write(subtitle))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))
        
        # Bagian 1: Pengertian Dasar
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
            Text("Inner Product adalah hasil kali dalam yang memenuhi:", font="Times New Roman", font_size=24),
            MathTex("1. \\langle u,v \\rangle = \\langle v,u \\rangle"),
            MathTex("2. \\langle au,v \\rangle = a\\langle u,v \\rangle"),
            MathTex("3. \\langle u+v,w \\rangle = \\langle u,w \\rangle + \\langle v,w \\rangle"),
            MathTex("4. \\langle u,u \\rangle \\geq 0")
        ).arrange(DOWN, buff=0.5)
        
        self.play(Write(inner_product_def))
        self.wait(2)
        self.play(FadeOut(inner_product_def))

        title1 = Text("Contoh 1: Inner Product dari Vektor", font="Times New Roman").scale(0.8)
        self.play(Write(title1))
        self.wait(1)
        self.play(FadeOut(title1))
        
        example1 = VGroup(
            MathTex(r"\text{Diberikan vektor } u = (2,1) \text{ dan } v = (3,4)"),
            MathTex(r"\text{Hitung inner product } \langle u,v \rangle:"),
        ).arrange(DOWN, buff=0.5)
        
        inner_product_steps = VGroup(
            MathTex(r"\langle u,v \rangle = (2)(3) + (1)(4)"),
            MathTex(r"\langle u,v \rangle = 6 + 4 = 10")
        ).arrange(DOWN, buff=0.3)
        
        self.play(Write(example1))
        self.wait(1)
        self.play(FadeOut(example1))
        self.play(Write(inner_product_steps[0]))
        self.wait(1)
        self.play(Write(inner_product_steps[1]))
        self.wait(2)
        self.play(FadeOut(inner_product_steps))
        
        # Example 2: Orthogonal Vectors
        title2 = Text("Contoh 2: Vektor Orthogonal", font="Times New Roman").scale(0.8)
        self.play(Write(title2))
        self.wait(1)
        self.play(FadeOut(title2))
        
        example2 = VGroup(
            MathTex("\\text{Diberikan vektor } u = (2,0) \\text{ dan } v = (0,2)"),
            MathTex("\\text{Hitung orthogonality:}"),
        ).arrange(DOWN, buff=0.5)
        
        self.play(Write(example2))
        self.wait(2)
        self.play(FadeOut(example2))
        
        # Create coordinate system
        axes = Axes(
            x_range=[-3, 3],
            y_range=[-3, 3],
            axis_config={"include_tip": True}
        )
        
        # Create vectors
        vector1 = Arrow(axes.c2p(0, 0), axes.c2p(2, 0), buff=0, color=BLUE)
        vector2 = Arrow(axes.c2p(0, 0), axes.c2p(0, 2), buff=0, color=RED)
        
        labels = VGroup(
            MathTex("u = (2,0)").next_to(vector1.get_end(), DOWN),
            MathTex("v = (0,2)").next_to(vector2.get_end(), RIGHT)
        )
        
        example2 = VGroup(
            MathTex("\\text{Vektor } u = (2,0) \\text{ dan } v = (0,2) \\text{ adalah orthogonal karena:}"),
            MathTex("\\langle u,v \\rangle = (2)(0) + (0)(2) = 0")
        ).arrange(DOWN, buff=0.5).to_edge(UP)
        
        self.play(Create(axes), Create(vector1), Create(vector2), Write(labels))
        self.wait(2)
        self.play( FadeOut(axes), FadeOut(vector1), FadeOut(vector2), 
                 FadeOut(labels))
        self.play(Write(example2))
        self.wait()
        self.play(FadeOut(example2))
        
        

        # Example 3: Gram-Schmidt Process
        title3 = Text("Contoh 3: Proses Gram-Schmidt", font="Times New Roman").scale(0.8)
        self.play(Write(title3))
        
        example3 = VGroup(
            MathTex("\\text{Diberikan vektor } u_1 = (1,1,0) \\text{ dan } u_2 = (1,0,1)"),
            MathTex("\\text{Orthonormalisasi menggunakan proses Gram-Schmidt:}"),
            MathTex("v_1 = u_1 = (1,1,0)"),
            MathTex("\\text{Normalisasi } v_1:"),
            MathTex("e_1 = \\frac{v_1}{||v_1||} = (\\frac{1}{\\sqrt{2}}, \\frac{1}{\\sqrt{2}}, 0)"),
            MathTex("v_2 = u_2 - \\text{proj}_{v_1}(u_2)"),
            MathTex("= (1,0,1) - \\frac{\\langle (1,0,1),(1,1,0) \\rangle}{\\langle (1,1,0),(1,1,0) \\rangle}(1,1,0)"),
            MathTex("= (1,0,1) - \\frac{1}{2}(1,1,0)"),
            MathTex("= (\\frac{1}{2},-\\frac{1}{2},1)"),
            MathTex("\\text{Normalisasi } v_2:"),
            MathTex("e_2 = \\frac{v_2}{||v_2||} = (\\frac{1}{\\sqrt{6}},-\\frac{1}{\\sqrt{6}},\\frac{2}{\\sqrt{6}})")
        ).arrange(DOWN, buff=0.3)
        
        self.play(Write(example3))
        self.wait(3)
        
        # Closing
        self.play(FadeOut(title3), FadeOut(example3))
        
        conclusion = VGroup(
            Text("Hasil Akhir:", font="Times New Roman"),
            MathTex("\\text{Basis orthonormal: }"),
            MathTex("e_1 = (\\frac{1}{\\sqrt{2}}, \\frac{1}{\\sqrt{2}}, 0)"),
            MathTex("e_2 = (\\frac{1}{\\sqrt{6}},-\\frac{1}{\\sqrt{6}},\\frac{2}{\\sqrt{6}})")
        ).arrange(DOWN, buff=0.5)
        
        self.play(Write(conclusion))
        self.wait(2)

    def run_judul(self):
        # JUDUL ============================================================
        main_title = Text("Ruang Hasil Kali Dalam", font_size=48, color=BLUE).to_edge(UP)
        subtitles = [
            "Inner Product Space",
            "Himpunan Orthonormal",
            "Proses Gram-Schmidt"
        ]
        subtitle_group = VGroup(*[Text(t, font_size=28, color=YELLOW) for t in subtitles]).arrange(DOWN, buff=0.1).next_to(main_title, DOWN, buff=0.5)
        
        self.play(Write(main_title))
        self.play(AnimationGroup(*[FadeIn(sub, shift=UP*0.5) for sub in subtitle_group], lag_ratio=0.2))

        university = Text("Universitas Diponegoro", font_size=24, color=GREEN).next_to(subtitle_group, DOWN, buff=0.5)
        self.play(FadeIn(university))
        self.wait(2)
        
        self.play(
            FadeOut(main_title),
            FadeOut(subtitle_group),
            FadeOut(university)
        )
        self.wait()

        # =============================================
        group_title = Text("Kelompok D", font_size=30)
        members = BulletedList(
            "Muchammad Yuda Tri Ananda (24060124110142)",
            "Muhammad Alfaiq Rido Salafy (24060124140148)",
            "Naufal Rayan Attallah (24060124140148)",
            font_size=24,
            color=TEAL,
        ).next_to(group_title, DOWN, aligned_edge=LEFT)

        self.play(FadeIn(group_title))
        self.play(FadeIn(members))

        self.wait(1)

        self.play(FadeOut(group_title), FadeOut(members))
        # JUDUL ======================================================
