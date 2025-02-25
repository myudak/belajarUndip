from manim import *


class InnerProductPresentation(Scene):
    def construct(self):
        # Title Slide
        title = Text("Inner Product Space, Orthonormal, dan Gram-Schmidt", font_size=36)
        subtitle = Text("Disusun oleh Sukmawati Ne", font_size=24, color=BLUE).next_to(
            title, DOWN
        )
        self.play(Write(title), Write(subtitle))
        self.wait(2)
        self.clear()

        # Section 1: Inner Product Space
        section1_title = Text("Inner Product Space", font_size=30, color=YELLOW)
        self.play(FadeIn(section1_title, shift=UP))
        self.wait(1)

        definition = Tex(
            r"\textbf{Inner Product Space:} Himpunan vektor di mana terdapat operasi hasil kali dalam "
            r"dengan sifat mirip perkalian titik (Dot Product).",
            tex_environment="flushleft",
            font_size=28,
        ).next_to(section1_title, DOWN)

        self.play(Write(definition))
        self.wait(2)

        formula = MathTex(
            "(u, v) = u_1v_1 + u_2v_2 + \\dots + u_nv_n", font_size=32
        ).next_to(definition, DOWN)
        self.play(Write(formula))
        self.wait(2)

        # Example: Dot Product in R3
        example_title = Text(
            "Contoh: Dot Product di R^3", font_size=28, color=GREEN
        ).next_to(formula, DOWN)
        example_vectors = MathTex("u = (1, 2, 3), v = (4, 5, 6)", font_size=28).next_to(
            example_title, DOWN
        )
        example_calc = MathTex(
            "(u, v) = 1 \\cdot 4 + 2 \\cdot 5 + 3 \\cdot 6 = 32", font_size=28
        ).next_to(example_vectors, DOWN)

        self.play(Write(example_title), Write(example_vectors))
        self.wait(1)
        self.play(Write(example_calc))
        self.wait(2)

        self.clear()

        # Section 2: Himpunan Orthonormal
        section2_title = Text("Himpunan Orthonormal", font_size=30, color=YELLOW)
        self.play(FadeIn(section2_title, shift=UP))
        self.wait(1)

        orthogonal_def = Tex(
            r"\textbf{Orthonormal:} Himpunan vektor orthogonal (tegak lurus) dan bernorma 1.",
            tex_environment="flushleft",
            font_size=28,
        ).next_to(section2_title, DOWN)

        self.play(Write(orthogonal_def))
        self.wait(2)

        example_orthogonal = MathTex(
            "v_1 = (1, 0), v_2 = (0, 1)", font_size=28
        ).next_to(orthogonal_def, DOWN)

        orthonormal_check = MathTex(
            "|v_1| = |v_2| = 1, (v_1, v_2) = 0", font_size=28
        ).next_to(example_orthogonal, DOWN)

        self.play(Write(example_orthogonal))
        self.wait(1)
        self.play(Write(orthonormal_check))
        self.wait(2)

        self.clear()

        # Section 3: Proyeksi
        section3_title = Text("Proyeksi Vektor", font_size=30, color=YELLOW)
        self.play(FadeIn(section3_title, shift=UP))
        self.wait(1)

        projection_formula = MathTex(
            r"\text{proj}_b a = \frac{(a \cdot b)}{|b|^2}b", font_size=28
        ).next_to(section3_title, DOWN)

        self.play(Write(projection_formula))
        self.wait(2)

        example_projection = MathTex(
            "a = (2, -1, 3), b = (4, -1, 2)", font_size=28
        ).next_to(projection_formula, DOWN)

        calc_projection = MathTex(
            r"\text{proj}_b a = \frac{(2 \cdot 4 + (-1) \cdot (-1) + 3 \cdot 2)}{|b|^2}b",
            font_size=28,
        ).next_to(example_projection, DOWN)

        self.play(Write(example_projection))
        self.wait(1)
        self.play(Write(calc_projection))
        self.wait(2)

        self.clear()

        # Section 4: Gram-Schmidt Process
        section4_title = Text("Proses Gram-Schmidt", font_size=30, color=YELLOW)
        self.play(FadeIn(section4_title, shift=UP))
        self.wait(1)

        gram_schmidt_steps = Tex(
            r"\textbf{Langkah-langkah:}\\"
            r"1. Ambil $v_1 = u_1$\\"
            r"2. $v_2 = u_2 - \text{proj}_{v_1} u_2$\\"
            r"3. $v_3 = u_3 - \text{proj}_{v_1} u_3 - \text{proj}_{v_2} u_3$\\"
            r"...",
            tex_environment="flushleft",
            font_size=28,
        ).next_to(section4_title, DOWN)

        self.play(Write(gram_schmidt_steps))
        self.wait(2)

        example_gram_schmidt = MathTex(
            "u_1 = (1, 0, 0), u_2 = (1, 2, 0)", font_size=28
        ).next_to(gram_schmidt_steps, DOWN)

        orthogonal_calc = MathTex(
            "v_2 = u_2 - \text{proj}_{v_1} u_2", font_size=28
        ).next_to(example_gram_schmidt, DOWN)

        self.play(Write(example_gram_schmidt))
        self.wait(1)
        self.play(Write(orthogonal_calc))
        self.wait(2)

        self.clear()

        # Conclusion
        conclusion = Text("Terima kasih!", font_size=36, color=BLUE)
        self.play(FadeIn(conclusion, scale=1.5))
        self.wait(3)
