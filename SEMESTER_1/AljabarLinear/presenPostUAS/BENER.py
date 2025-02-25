from manim import *
import numpy as np

class AljabarLinierPresentasi(Scene):
    def construct(self):
        self.run_judul()

        self.transformasi_linier()
        self.matriks_transformasi()
        self.kernel_dan_jangkauan()

        self.run_akhir()

    def transformasi_linier(self):
        # Bagian 1: Transformasi Linier
        title = Text("Transformasi Linier", font_size=40)
        subtitle = Text("Definisi dan Konsep Dasar", font_size=30)
        subtitle.next_to(title, DOWN)
        
        self.play(Write(title))
        self.play(Write(subtitle))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))

        # Definisi
        definisi = VGroup(
            Text("Transformasi Linier adalah fungsi T: V → W", font_size=30),
            Text("yang memenuhi dua sifat:", font_size=30),
            Text("1. T(u + v) = T(u) + T(v)", font_size=30),
            Text("2. T(cu) = cT(u)", font_size=30)
        ).arrange(DOWN, aligned_edge=LEFT)
        
        self.play(Write(definisi))
        self.wait(2)

        # Contoh Visualisasi
        axes = Axes(
            x_range=[-3, 3],
            y_range=[-3, 3],
            axis_config={"color": BLUE},
        )
        
        vector1 = Arrow(start=axes.coords_to_point(0, 0),
                       end=axes.coords_to_point(2, 1),
                       color=YELLOW)
        vector2 = Arrow(start=axes.coords_to_point(0, 0),
                       end=axes.coords_to_point(1, 2),
                       color=RED)
        
        self.play(FadeOut(definisi))
        self.play(Create(axes), Create(vector1), Create(vector2))
        
        # Transformasi rotasi 90 derajat
        matrix = np.array([[0, -1], [1, 0]])
        
        def rotate_vector(vector, matrix):
            coords = np.array([vector.get_end()[0], vector.get_end()[1]])
            new_coords = np.dot(matrix, coords)
            return Arrow(
                start=axes.coords_to_point(0, 0),
                end=axes.coords_to_point(new_coords[0], new_coords[1]),
                color=vector.get_color()
            )
        
        vector1_rotated = rotate_vector(vector1, matrix)
        vector2_rotated = rotate_vector(vector2, matrix)
        
        self.play(
            Transform(vector1, vector1_rotated),
            Transform(vector2, vector2_rotated)
        )
        self.wait(2)
        
        # Clear scene
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

        # Contoh 4: Transformasi Linear P2 ke R^2
        contoh4_title = Text("Contoh 4", font_size=35)
        contoh4_text = MathTex(
            r"T: P_2 \rightarrow \mathbb{R}^2, (P_2: \text{Polinom orde-2})",
            r"T(a + bx + cx^2) = \begin{pmatrix} a-b \\ a-c \end{pmatrix}"
        ).scale(0.8)
        contoh4_text.arrange(DOWN)
        
        self.play(Write(contoh4_title))
        self.wait()
        self.play(contoh4_title.animate.to_edge(UP))
        self.play(Write(contoh4_text))
        self.wait(2)

        # Create coordinate system for R^2
        axes = Axes(
            x_range=[-4, 4],
            y_range=[-4, 4],
            axis_config={"color": BLUE},
            tips=True
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        grid = NumberPlane(
            x_range=[-4, 4],
            y_range=[-4, 4],
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 1,
                "stroke_opacity": 0.4
            }
        )
        
        # Move existing text up to make room for visualization
        VGroup(contoh4_title, contoh4_text).shift(UP * 2)
        
        # Add coordinate system
        self.play(
            Create(grid),
            Create(axes),
            Create(axes_labels)
        )

        self.play(FadeOut(contoh4_text))
        
        # Bagian a: T(1-2x+x^2)
        soal_a = MathTex(
            r"\text{a. } T(1-2x+x^2) = ?",
            r"\text{Penyelesaian:}"
        ).scale(0.8)
        soal_a.arrange(DOWN, aligned_edge=LEFT)
        soal_a.next_to(contoh4_text, DOWN, buff=0.5)
        
        langkah_a = MathTex(
            r"T(1-2x+x^2) &= T(1 + (-2)x + 1x^2) \\",
            r"&= \begin{pmatrix} 1-(-2) \\ 1-1 \end{pmatrix} \\",
            r"&= \begin{pmatrix} 3 \\ 0 \end{pmatrix}"
        ).scale(0.8)
        langkah_a.next_to(soal_a, DOWN)
        
        self.play(Write(soal_a))
        self.wait()
        self.play(Write(langkah_a))
        
        # Add vector visualization
        result_vector = Arrow(
            start=axes.coords_to_point(0, 0),
            end=axes.coords_to_point(3, 0),
            color=YELLOW,
            buff=0
        )
        vector_label = MathTex(r"(3,0)").next_to(result_vector.get_end(), RIGHT)
        
        self.play(
            Create(result_vector),
            Write(vector_label)
        )
        self.wait(2)

        self.play(FadeOut(soal_a), FadeOut(langkah_a))
        
        # Bagian b: Apakah T merupakan transformasi linear?
        soal_b = MathTex(
            r"\text{b. Apakah } T \text{ merupakan transformasi linear?}",
            r"\text{Penyelesaian: Ya, karena memenuhi dua sifat berikut:}"
        ).scale(0.8)
        soal_b.arrange(DOWN, aligned_edge=LEFT)
        # soal_b.next_to(langkah_a, DOWN, buff=0.5)
        
        sifat = VGroup(
            MathTex(r"1. \text{ } T(u+v) = T(u) + T(v)"),
            MathTex(r"2. \text{ } T(cu) = cT(u)")
        ).arrange(DOWN, aligned_edge=LEFT).scale(0.8)
        sifat.next_to(soal_b, DOWN)
        
        # Example vectors for linearity visualization
        vector_u = Arrow(start=axes.coords_to_point(0, 0), end=axes.coords_to_point(2, 1), color=RED, buff=0)
        vector_v = Arrow(start=axes.coords_to_point(0, 0), end=axes.coords_to_point(1, -1), color=GREEN, buff=0)
        vector_sum = Arrow(start=axes.coords_to_point(0, 0), end=axes.coords_to_point(3, 0), color=BLUE, buff=0)
        
        # Labels for vectors
        label_u = MathTex(r"T(u)").next_to(vector_u.get_end(), RIGHT).set_color(RED)
        label_v = MathTex(r"T(v)").next_to(vector_v.get_end(), RIGHT).set_color(GREEN)
        label_sum = MathTex(r"T(u+v)").next_to(vector_sum.get_end(), RIGHT).set_color(BLUE)
        
        self.play(Write(soal_b))
        self.play(Write(sifat))
        
        # Animate linearity property
        self.play(
            Create(vector_u),
            Write(label_u)
        )
        self.play(
            Create(vector_v),
            FadeOut(soal_b), FadeOut(sifat), FadeOut(vector_label),
            Write(label_v)
        )
        self.play(
            Create(vector_sum),
            Write(label_sum)
        )
        self.wait(2)
        
        # Clear scene for next section
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

    def matriks_transformasi(self):
        # Bagian 2: Matriks Transformasi
        title = Text("Matriks Transformasi", font_size=40)
        self.play(Write(title))
        self.wait()
        self.play(FadeOut(title))

        matrix = MathTex(r"""
        A = \begin{bmatrix} 
        a & b \\
        c & d
        \end{bmatrix}
        """)
        
        explanation = VGroup(
            Text("Matriks transformasi merepresentasikan", font_size=30),
            Text("transformasi linier dalam bentuk matriks", font_size=30)
        ).arrange(DOWN)
        
        explanation.next_to(matrix, DOWN)
        
        self.play(Write(matrix))
        self.play(Write(explanation))
        self.wait(2)

        # Grid visualization
        axes = Axes(
            x_range=[-3, 3],
            y_range=[-3, 3],
            axis_config={"color": BLUE},
        )
        
        grid = NumberPlane(
            x_range=[-3, 3],
            y_range=[-3, 3],
            background_line_style={
                "stroke_color": GRAY,
                "stroke_opacity": 0.5
            }
        )
        
        self.play(FadeOut(matrix), FadeOut(explanation))

        self.play(Create(axes), Create(grid))
        
        # Shear transformation
        matrix = np.array([[1, 1], [0, 1]])
        transformed_grid = grid.copy()
        transformed_grid.apply_matrix(matrix)
        
        self.play(
            Transform(grid, transformed_grid),
            run_time=2
        )
        self.wait(2)
        
        # Clear scene
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

        # Membuat judul
        title = Text("Transformasi Linear", font_size=40)
        title.to_edge(UP)
        
        # Membuat definisi matematika
        definition = MathTex(
            r"T: V \rightarrow W,\quad T(\vec{u}) = A\vec{u}",
            font_size=36
        )
        definition.next_to(title, DOWN, buff=0.5)
        
        # Menambahkan penjelasan dalam bahasa Indonesia
        penjelasan = Text(
            "untuk setiap u ∈ V",
            font_size=24
        )
        penjelasan.next_to(definition, DOWN, buff=0.3)
        
        # Membuat sistem koordinat
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=6,
            y_length=6,
            axis_config={"include_numbers": True}
        )
        axes.to_edge(DOWN)
        
        # Membuat vektor untuk demonstrasi transformasi
        vector = Arrow(
            axes.coords_to_point(0, 0),
            axes.coords_to_point(2, 1),
            buff=0,
            color=BLUE
        )
        
        # Membuat matriks A untuk transformasi
        matrix_A = Matrix([
            [2, 0],
            [0, 1.5]
        ])
        matrix_A.scale(0.8)
        matrix_A.next_to(axes, LEFT)
        matrix_label = Text("A = ", font_size=24)
        matrix_label.next_to(matrix_A, LEFT)
        
        # Menambahkan label matriks transformasi
        matriks_text = Text("Matriks Transformasi", font_size=24)
        matriks_text.next_to(matrix_A, UP)
        
        # Urutan animasi
        self.play(Write(title))
        self.play(Write(definition))
        self.play(Write(penjelasan))
        self.wait()
        self.play(FadeOut(definition), FadeOut(penjelasan))
        
        self.play(Create(axes))
        self.play(GrowArrow(vector))
        self.wait()
        
        # Menampilkan matriks transformasi
        self.play(
            Write(matrix_label),
            Write(matrix_A),
            Write(matriks_text)
        )
        
        # Menerapkan transformasi
        transformed_vector = Arrow(
            axes.coords_to_point(0, 0),
            axes.coords_to_point(4, 1.5),
            buff=0,
            color=RED
        )
        
        self.play(
            Transform(vector, transformed_vector),
            rate_func=smooth
        )
        
        # Menambahkan teks dimensi
        dim_text = Text("Ukuran Matriks: m x n", font_size=24)
        dim_explanation = MathTex(r"\text{Jika } T: \mathbb{R}^n \to \mathbb{R}^m", font_size=20)
        dim_text.to_edge(RIGHT)
        dim_explanation.next_to(dim_text, UP)
        
        self.play(
            Write(dim_explanation),
            Write(dim_text)
        )
        
        self.wait(2)
        self.play(
            FadeOut(title),
            FadeOut(dim_explanation),
            FadeOut(dim_text),  
            *[FadeOut(mob) for mob in self.mobjects]
        )

        # Title
        title = Text("Contoh 1: Mencari Matriks Transformasi", font_size=36)
        title.to_edge(UP)
        
        # Initial transformation definition
        initial_def = MathTex(
            r"T: \mathbb{R}^2 \rightarrow \mathbb{R}^3",
            r"\text{ didefinisikan oleh:}"
        )
        initial_def.next_to(title, DOWN)

        # The transformation equation
        transform_eq = MathTex(
            r"T\begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} x-y \\ -x \\ y \end{bmatrix}"
        )
        transform_eq.next_to(initial_def, DOWN)

        # Step 1: Matrix form explanation
        step1 = Text("Langkah 1: Mencari komponen matriks transformasi", font_size=24)
        step1.next_to(transform_eq, DOWN, buff=0.5)

        # Breaking down components
        components = MathTex(
            r"x-y &= 1x + (-1)y \\",
            r"-x &= (-1)x + 0y \\",
            r"y &= 0x + 1y"
        )
        components.next_to(step1, DOWN)

        # Final matrix
        final_matrix = MathTex(
            r"A = \begin{bmatrix} 1 & -1 \\ -1 & 0 \\ 0 & 1 \end{bmatrix}"
        )
        final_matrix.move_to(ORIGIN)

        # Animations
        self.play(Write(title))
        self.wait(1)
        
        self.play(Write(initial_def))
        self.wait(1)
        
        self.play(Write(transform_eq))
        self.wait(1)
        
        self.play(Write(step1))
        self.wait(1)
        
        # Animate components appearing one by one
        self.play(Write(components))
        self.wait(1)

        # Final matrix revelation
        final_text = Text("Jadi Matriks Transformasi:", font_size=24)
        final_text.next_to(final_matrix, UP)
        
        self.play(FadeOut(step1), FadeOut(components), FadeOut(transform_eq), FadeOut(initial_def))
        self.play(
            Write(final_text),
            Write(final_matrix)
        )
        self.wait(1)
        self.play( FadeOut(final_text), FadeOut(final_matrix))

        # Create visual representation of transformation
        axes_2d = Axes(
            x_range=[-3, 3],
            y_range=[-3, 3],
            axis_config={"include_numbers": True}
        ).scale(0.4)
        
        axes_3d = ThreeDAxes(
            x_range=[-3, 3],
            y_range=[-3, 3],
            z_range=[-3, 3],
        ).scale(0.4)

        # Position the coordinate systems
        axes_2d.to_edge(LEFT, buff=1)
        axes_3d.to_edge(RIGHT, buff=1)

        # Add labels
        domain_label = MathTex(r"\text{Domain } (\mathbb{R}^2)", font_size=20)
        codomain_label = MathTex(r"\text{Codomain } (\mathbb{R}^3)", font_size=20)
        
        domain_label.next_to(axes_2d, DOWN)
        codomain_label.next_to(axes_3d, DOWN)

        # Create vector
        vector_2d = Arrow(
            axes_2d.coords_to_point(0, 0),
            axes_2d.coords_to_point(1, 1),
            buff=0,
            color=BLUE
        )

        # Show coordinate systems and vector
        self.play(
            Create(axes_2d),
            Create(axes_3d),
            Write(domain_label),
            Write(codomain_label)
        )
        self.wait(1)

        self.play(GrowArrow(vector_2d))
        self.wait(2)

        # clear
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

    def kernel_dan_jangkauan(self):
        # Bagian 3: Kernel dan Jangkauan
        title = Text("Kernel dan Jangkauan", font_size=40)
        self.play(Write(title))
        self.wait()
        self.play(FadeOut(title))

        # Title
        title = Text("DEFINISI KERNEL", font_size=40, weight=BOLD)
        title.to_edge(UP)
        
        # First line of definition
        def1 = Tex(
            r"Misalkan $T : V \rightarrow W$ merupakan transformasi linear.",
            font_size=32
        )
        def1.next_to(title, DOWN, buff=0.7)
        
        # Second line of definition
        def2 = Tex(
            r"Semua unsur di $V$ yang dipetakan ke vektor nol di $W$\\",
            r"dinamakan ", r"kernel (dari) $T$.",
            font_size=32
        )
        def2.next_to(def1, DOWN, buff=0.3)
        def2[1:].set_color(YELLOW)
        
        # Notation
        notation = Tex(r"Notasi: $ker(T)$", font_size=32)
        notation.next_to(def2, DOWN, buff=0.5)
        
        # Mathematical definition
        math_def = MathTex(
            r"Ker(T) = \{ \bar{u} \in V \mid T(\bar{u}) = \bar{0} \}",
            font_size=36
        )
        math_def.next_to(notation, DOWN, buff=0.7)

       
        
        # Create coordinate systems for visualization
        axes_v = Axes(
            x_range=[-3, 3],
            y_range=[-3, 3],
            axis_config={"include_numbers": True}
        ).scale(0.4)
        
        axes_w = Axes(
            x_range=[-3, 3],
            y_range=[-3, 3],
            axis_config={"include_numbers": True}
        ).scale(0.4)
        
        # Position the coordinate systems
        axes_group = VGroup(axes_v, axes_w).arrange(RIGHT, buff=2)
        axes_group.move_to(ORIGIN)
        
        # Labels for spaces
        v_label = Tex("V", font_size=32).next_to(axes_v, DOWN)
        w_label = Tex("W", font_size=32).next_to(axes_w, DOWN)
        
        # Vector in kernel (will be mapped to zero)
        kernel_vector = Arrow(
            axes_v.coords_to_point(0, 0),
            axes_v.coords_to_point(2, 1),
            buff=0,
            color=BLUE
        )
        
        # Zero vector in W
        zero_vector = Dot(axes_w.coords_to_point(0, 0), color=RED)
        
        # Curved arrow showing transformation
        curved_arrow = CurvedArrow(
            start_point=axes_v.coords_to_point(2, 1),
            end_point=axes_w.coords_to_point(0, 0),
            color=YELLOW
        )
        
        # Animation sequence
        self.play(Write(title))
        self.wait(0.5)
        
        self.play(Write(def1))
        self.wait()
        
        self.play(Write(def2))
        self.wait()
        
        self.play(Write(notation))
        self.wait()
        
        self.play(Write(math_def))
        self.wait()

        self.play( FadeOut(def1), FadeOut(def2), FadeOut(notation), FadeOut(math_def) )
        
        self.play(
            Create(axes_v),
            Create(axes_w),
            Write(v_label),
            Write(w_label)
        )
        self.wait()
        
        # Show vector and its transformation
        self.play(GrowArrow(kernel_vector))
        self.wait()
        
        self.play(Create(curved_arrow))
        self.wait()
        
        self.play(Create(zero_vector))
        self.wait()
        
        # Add explanation text
        explanation = Tex(
            r"Vektor di $V$ yang dipetakan ke $\bar{0}$ di $W$\\",
            r"adalah elemen dari $ker(T)$",
            font_size=28
        )
        explanation.next_to(axes_group, DOWN)
        self.play(Write(explanation))
        
        self.wait(2)

        # clear
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

        # Title
        title = Text("Contoh 1: Mencari Kernel Transformasi", font_size=36)
        title.to_edge(UP)
        
        # Problem statement
        problem = MathTex(
            r"T: P_2 \rightarrow \mathbb{R}^2 \text{ didefinisikan oleh}",
            font_size=32
        )
        problem.next_to(title, DOWN)
        
        transform = MathTex(
            r"T(a+bx+cx^2) = \begin{pmatrix} a-b \\ a-c \end{pmatrix}",
            font_size=32
        )
        transform.next_to(problem, DOWN)
        
        # Options
        options = VGroup(
            MathTex(r"s_1 = 1+x+x^2"),
            MathTex(r"s_2 = 1+2x+x^2")
        ).arrange(DOWN, buff=0.5)
        options.next_to(transform, DOWN, buff=0.7)
        
        # Step by Step Solution
        steps_title = Text("Langkah-langkah Penyelesaian:", font_size=28)
        steps_title.next_to(title, DOWN)
        
        # Step 1: Test s₁
        step1 = VGroup(
            Text("1. Uji s₁ = 1 + x + x²:", font_size=24),
            MathTex(r"T(1+x+x^2) = \begin{pmatrix} 1-1 \\ 1-1 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}")
        ).arrange(DOWN, aligned_edge=LEFT)
        step1.next_to(steps_title, DOWN, aligned_edge=LEFT)
        
        # Step 2: Test s₂
        step2 = VGroup(
            Text("2. Uji s₂ = 1 + 2x + x²:", font_size=24),
            MathTex(r"T(1+2x+x^2) = \begin{pmatrix} 1-2 \\ 1-1 \end{pmatrix} = \begin{pmatrix} -1 \\ 0 \end{pmatrix}")
        ).arrange(DOWN, aligned_edge=LEFT)
        step2.next_to(step1, DOWN, buff=0.5, aligned_edge=LEFT)
        
        # Conclusion
        conclusion = VGroup(
            Text("Kesimpulan: ", font_size=19),
            Text("s₁ = 1 + x + x²", font_size=19, color=YELLOW, weight=BOLD),
            Text(" adalah elemen Ker(T)", font_size=19),
            Text("karena T(s₁) menghasilkan vektor nol", font_size=19)
        ).arrange(RIGHT, buff=0.1)
        conclusion.set_width(config.frame_width - 1)
        conclusion.next_to(step2, DOWN, buff=0.7)
        
        # Animations
        self.play(Write(title))
        self.wait()
        
        self.play(Write(problem))
        self.wait()
        
        self.play(Write(transform))
        self.wait()
        
        self.play(Write(options))
        self.wait()

        self.play(
            FadeOut(problem),
            FadeOut(transform),
            FadeOut(options)
        )
        self.wait()
        
        self.play(Write(steps_title))
        self.wait()
        
        # Animate step 1
        self.play(Write(step1))
        self.wait()
        
        # Create visualization for s₁
        axes = Axes(
            x_range=[-2, 2],
            y_range=[-2, 2],
            axis_config={"include_numbers": True}
        ).scale(0.4)
        axes.to_edge(RIGHT)
        
        dot = Dot(axes.coords_to_point(0, 0), color=YELLOW)
        vector_text = Text("T(s₁)", font_size=24).next_to(dot, RIGHT)
        
        self.play(
            Create(axes),
            Create(dot),
            Write(vector_text)
        )
        self.wait()
        self.play(FadeOut(vector_text))
        
        # Animate step 2
        self.play(Write(step2))
        vector2 = Arrow(
            axes.coords_to_point(0, 0),
            axes.coords_to_point(-1, 0),
            buff=0,
            color=RED
        )
        vector2_text = Text("T(s₂)", font_size=24).next_to(vector2, RIGHT)
        
        self.play(
            GrowArrow(vector2),
            Write(vector2_text)
        )
        self.wait()
        
        # Show conclusion
        self.play(Write(conclusion))
        self.wait(2)

        # CLEAR
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

        # Title and initial statement
        title = Text("Teorema Kernel dan Subruang", font_size=36)
        title.to_edge(UP)
        
        # First property
        property1 = VGroup(
            Text("Jelas bahwa vektor nol pada daerah asal", font_size=28),
            Text("transformasi merupakan unsur kernel T.", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT)
        property1.next_to(title, DOWN, buff=0.7)
        
        # Second property
        property2 = VGroup(
            Text("Tetapi, tak semua transformasi linear mempunyai", font_size=28),
            Text("vektor tak nol sebagai unsur kernel T.", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT)
        property2.next_to(property1, DOWN, buff=0.5)
        
        # Theorem box
        theorem_box = VGroup(
            Text("Teorema:", font_size=32, weight=BOLD),
            MathTex(r"\text{Jika } T: V \rightarrow W \text{ adalah transformasi linear}"),
            MathTex(r"\text{maka } Ker(T) \text{ merupakan subruang dari } V")
        ).arrange(DOWN, aligned_edge=LEFT)
        theorem_box.next_to(property2, DOWN, buff=0.7)
        
        box = SurroundingRectangle(theorem_box, buff=0.3, color=BLUE)
        
        # Consequence
        consequence = VGroup(
            Text("Karena Ker(T) merupakan subruang", font_size=28),
            Text("→ T mempunyai Basis Ker(T)", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT)
        consequence.next_to(title, DOWN, buff=0.7)
        
        # Visual demonstration
        # Create vector space V
        axes_v = Axes(
            x_range=[-3, 3],
            y_range=[-3, 3],
            axis_config={"include_numbers": True}
        ).scale(0.4)
        
        # Create vector space W
        axes_w = Axes(
            x_range=[-3, 3],
            y_range=[-3, 3],
            axis_config={"include_numbers": True}
        ).scale(0.4)
        
        # Position the spaces
        spaces = VGroup(axes_v, axes_w).arrange(RIGHT, buff=2)
        spaces.next_to(consequence, DOWN, buff=0.7)
        
        # Labels
        v_label = Text("V", font_size=24).next_to(axes_v, DOWN)
        w_label = Text("W", font_size=24).next_to(axes_w, DOWN)
        
        # Kernel visualization (as a line through origin in V)
        kernel_line = Line(
            axes_v.coords_to_point(0, -2),
            axes_v.coords_to_point(0, 2),
            color=YELLOW
        )
        kernel_label = Text("Ker(T)", font_size=24).next_to(kernel_line, LEFT)
        
        # Zero vector in W
        zero_point = Dot(axes_w.coords_to_point(0, 0), color=RED)
        zero_label = Text("0", font_size=24).next_to(zero_point, DOWN)
        
        # Animation sequence
        self.play(Write(title))
        self.wait()
        
        self.play(Write(property1))
        self.wait()
        
        self.play(Write(property2))
        self.wait()
        
        self.play(
            Write(theorem_box),
            Create(box)
        )
        self.wait()

        self.play(
            FadeOut(property1),
            FadeOut(property2),
            FadeOut(theorem_box),
            FadeOut(box)
        )
        self.wait()
        
        self.play(Write(consequence))
        self.wait()
        
        # Animate spaces
        self.play(
            Create(axes_v),
            Create(axes_w),
            Write(v_label),
            Write(w_label)
        )
        self.wait()
        
        # Show kernel
        self.play(
            Create(kernel_line),
            Write(kernel_label)
        )
        self.wait()
        
        # Show zero vector in W
        self.play(
            Create(zero_point),
            Write(zero_label)
        )
        
        # Add demonstration vectors
        vectors = VGroup()
        for t in [-1, -0.5, 0.5, 1]:
            vector = Arrow(
                axes_v.coords_to_point(0, 0),
                axes_v.coords_to_point(0, t),
                buff=0,
                color=BLUE_C
            )
            vectors.add(vector)
        
        self.play(Create(vectors))
        
        # Add final note
        final_note = Text(
            "Ker(T) adalah subruang yang semua vektornya\n"
            "dipetakan ke vektor nol di W",
            font_size=24
        ).next_to(spaces, DOWN)
        
        self.play(Write(final_note))
        self.wait(2)

        # CLEAR
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

    def run_judul(self):
        # JUDUL ============================================================
        main_title = Text("ALJABAR LINIER", font_size=48, color=BLUE).to_edge(UP)
        subtitles = [
            "Transformasi Linier",
            "Matriks Transformasi",
            "Kernel dan Jangkauan"
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
        group_title = Text("Kelompok 11", font_size=30)
        members = BulletedList(
            "Muchammad Yuda Tri Ananda (24060124110142)",
            "Nayla Husna (24060124140158)",
            "Muchammad Rajib Tafrichan 24060124140141",
            font_size=24,
            color=TEAL,
        ).next_to(group_title, DOWN, aligned_edge=LEFT)

        self.play(FadeIn(group_title))
        self.play(FadeIn(members))

        self.wait(1)

        self.play(FadeOut(group_title), FadeOut(members))
        # JUDUL ======================================================

    def run_akhir(self):
        akhir = Text("TERIMAKASIH", font_size=48, color=BLUE).to_edge(ORIGIN)
        self.play(Write(akhir))
        self.wait(2)