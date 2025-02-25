from manim import *


class PresentasiOperasiMatriks(Scene):
    def construct(self):
        # SLIDE 1 PENDAHULUAN =====================================================
        judul = Text("Presentasi Operasi Matriks", font_size=48, color=BLUE)
        self.play(Write(judul))
        self.wait(2)
        self.play(FadeOut(judul))

        anggota = Text(
            "Kelompok 1: \n\n- Muchammad Yuda Tri Ananda \n\n- Muhammad Faza Aqila \n\n- Muhammad Izzat Fauzan Putra Arya",
            font_size=36,
            color=TEAL,
        )
        self.play(Write(anggota))
        self.wait(2)
        self.play(FadeOut(anggota))

        # </SLIDE 1 PENDAHULUAN =====================================================

        # SLIDE 2 PEMBERIAN MATRIX A =====================================================
        def_matriks = Text("Matrix 3x3", font_size=40, color=GREEN)
        self.play(Write(def_matriks))
        self.wait(2)
        self.play(FadeOut(def_matriks))

        matriks_a_label = Text(
            "Diberikan sebuah matrix A berukuran 3x3:", font_size=36, color=ORANGE
        ).to_edge(UP)
        matriks_a = Matrix(
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            element_to_mobject_config={"color": YELLOW},
        )
        rankBrp = Text(f"A =", font_size=30, color=YELLOW).next_to(matriks_a, LEFT)
        self.play(Write(matriks_a_label), Write(rankBrp), Write(matriks_a))
        self.wait(2)
        self.play(FadeOut(matriks_a_label), FadeOut(rankBrp), FadeOut(matriks_a))

        # </SLIDE 2 PEMBERIAN MATRIX A =====================================================

        # SLIDE 3 OBE 1 A =====================================================
        obe_judul = Text(
            "Dengan melakukan operasi baris elementer sebanyak 3 kali \n\n maka dapat dilakukan dengan cara berikut",
            font_size=25,
            color=TEAL,
        )
        self.play(Write(obe_judul))
        self.wait(2)
        self.play(FadeOut(obe_judul))

        # obe_penjelasan = MathTex(r"H_{12}(-3)(A)", font_size=36, color=BLUE).to_edge(UP)
        title_det_saurus_a = MathTex(r"H_{12(-3)}(A)", font_size=36, color=BLUE)

        # obe_penjelasan = Text(
        #     "Contoh OBE pada Matriks A : H13(2)", font_size=36, color=BLUE
        # ).to_edge(UP)

        # Animating OBE on Matriks A

        self.play(Write(title_det_saurus_a))
        self.wait(1)
        self.play(title_det_saurus_a.animate.to_edge(UP).move_to(UP * 3.5))
        matriks_a = Matrix(
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            element_to_mobject_config={"color": YELLOW},
        )
        self.play(Write(matriks_a))
        self.wait(1)

        # 1. Swap Row 1 and Row 2
        new_matriks_a = Matrix(
            [[1, 2, 3], [-12, -15, -18], [7, 8, 9]],
            element_to_mobject_config={"color": YELLOW},
        )
        self.play(Transform(matriks_a, new_matriks_a))
        self.wait(1)

        # 2. Multiply Row 1 by 2
        new_matriks_a = Matrix(
            [[-11, -13, -15], [4, 5, 6], [7, 8, 9]],
            element_to_mobject_config={"color": YELLOW},
        )
        self.play(Transform(matriks_a, new_matriks_a))
        self.wait(1)

        # # 3. Add Row 1 to Row 2
        # new_matriks_a = Matrix(
        #     [[8, 10, 12], [9, 12, 15], [7, 8, 9]],
        #     element_to_mobject_config={"color": YELLOW},
        # )
        # self.play(Transform(matriks_a, new_matriks_a))
        # self.wait(2)
        self.play(FadeOut(matriks_a))
        self.play(title_det_saurus_a.animate.move_to(ORIGIN))
        self.play(FadeOut(title_det_saurus_a))

        # </SLIDE 3 OBE 1 A =====================================================

        # SLIDE 3 OBE 2 A =====================================================

        title_det_saurus_a = MathTex(r"K_{3(2)}(A)", font_size=36, color=BLUE)

        self.play(Write(title_det_saurus_a))
        self.wait(1)
        self.play(title_det_saurus_a.animate.to_edge(UP).move_to(UP * 3.5))

        # `1`
        matriks_a = Matrix(
            [[-11, -13, -15], [4, 5, 6], [7, 8, 9]],
            element_to_mobject_config={"color": YELLOW},
        )
        self.play(Write(matriks_a))
        self.wait(1)

        # `2`
        new_matriks_a = Matrix(
            [[-11, -13, -30], [4, 5, 12], [7, 8, 18]],
            element_to_mobject_config={"color": YELLOW},
        )
        self.play(Transform(matriks_a, new_matriks_a))
        self.wait(1)

        self.play(FadeOut(matriks_a))
        self.play(title_det_saurus_a.animate.move_to(ORIGIN))
        self.play(FadeOut(title_det_saurus_a))

        # </SLIDE 3 OBE 2 =====================================================

        # SLIDE 3 OBE 3 =====================================================

        title_det_saurus_a = MathTex(r"K_{12}(A)", font_size=36, color=BLUE)

        self.play(Write(title_det_saurus_a))
        self.wait(1)
        self.play(title_det_saurus_a.animate.to_edge(UP).move_to(UP * 3.5))

        # `1`
        matriks_a = Matrix(
            [[-11, -13, -30], [4, 5, 12], [7, 8, 18]],
            element_to_mobject_config={"color": YELLOW},
        )
        self.play(Write(matriks_a))
        self.wait(1)

        # `2`
        new_matriks_a = Matrix(
            [[-13, -11, -30], [5, 4, 12], [8, 7, 18]],
            element_to_mobject_config={"color": YELLOW},
        )
        self.play(Transform(matriks_a, new_matriks_a))
        self.wait(1)

        self.play(FadeOut(matriks_a))
        self.play(title_det_saurus_a.animate.move_to(ORIGIN))
        self.play(FadeOut(title_det_saurus_a))

        # </SLIDE 3 OBE 3 =====================================================

        # EQUIVALENN MATRIKS =====================================================

        obe_judul = Text(
            "Maka Didapatkan",
            font_size=25,
            color=TEAL,
        )
        self.play(Write(obe_judul))
        self.wait(2)
        self.play(FadeOut(obe_judul))

        title_det_saurus_a = MathTex(
            r"H_{12(-3)} K_{3(2)} K_{3(2)}(A) = C \text{, dengan matriks } C \text{ adalah}\\",
            r"\text{matriks yang ekuivalen} \approx \text{matriks } A",
            font_size=36,
            color=BLUE,
        )

        self.play(Write(title_det_saurus_a))
        self.wait(1)
        self.play(title_det_saurus_a.animate.to_edge(UP).move_to(UP * 3.5))

        matriks_a = Matrix(
            [[-13, -11, -30], [5, 4, 12], [8, 7, 18]],
            element_to_mobject_config={"color": YELLOW},
        )
        rankBrp = Text(f"C =", font_size=30, color=YELLOW).next_to(matriks_a, LEFT)
        rankBrp2 = MathTex(
            r"\approx \text{matriks } A", font_size=30, color=YELLOW
        ).next_to(matriks_a, RIGHT)
        self.play(Write(rankBrp))
        self.play(Write(matriks_a))
        self.play(Write(rankBrp2))
        self.wait(1)

        self.play(FadeOut(matriks_a), FadeOut(rankBrp), FadeOut(rankBrp2))
        self.play(title_det_saurus_a.animate.move_to(ORIGIN))
        self.play(FadeOut(title_det_saurus_a))

        # </EQUIVALENN MATRIKS =====================================================

        # SLIDE 4 RANK MATRIX A =====================================================
        rank_judul = Text("Rank Matriks A", font_size=40, color=GREEN)
        self.play(Write(rank_judul))
        self.wait(2)
        self.play(FadeOut(rank_judul))

        # Animation for finding rank
        # def create_matrix_with_rank(matrix, rank):
        #     matrix_mob = Matrix(matrix, element_to_mobject_config={"color": TEAL})
        #     rank_text = Text(f"Rank: {rank}", font_size=30, color=YELLOW).next_to(matrix_mob, RIGHT)
        #     return VGroup(matrix_mob, rank_text)

        # matrix_a_group = create_matrix_with_rank([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2)
        # matrix_b_group = create_matrix_with_rank([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 4)

        # self.play(Write(matrix_a_group))
        # self.wait(2)
        # self.play(matrix_a_group.animate.shift(UP * 2))
        # self.play(Write(matrix_b_group))
        # self.wait(2)
        # self.play(FadeOut(matrix_a_group), FadeOut(matrix_b_group))

        title = Text("Rank Matrix A").set_color(TEAL).move_to(UP * 3.5)

        m01 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        m02 = Matrix([[1, 2, 3], [0, -3, -6], [7, 8, 9]]).move_to([4, 1.5, 0])
        m03 = Matrix([[1, 2, 3], [0, -3, -6], [0, -6, -12]]).move_to([-4, -2.5, 0])
        m04 = Matrix([[1, 2, 3], [0, -3, -6], [0, 0, 0]]).move_to([4, -2.5, 0])
        matrices = [m01, m02, m03, m04]
        for m in matrices:
            m.get_brackets().set_color(YELLOW)

        eq1 = MathTex(r"H_{21(-4)}").set_color(TEAL)
        eq2 = MathTex(r"H_{31(-7)}").set_color(TEAL)
        eq3 = MathTex(r"H_{32(-2)}").set_color(TEAL)

        arrow_1 = LabeledArrow(
            start=[-1.7, 1.5, 0],
            end=[1.7, 1.5, 0],
            color=PINK,
            tip_shape=StealthTip,
            label=eq1,
        )
        arrow_2 = LabeledArrow(
            start=[1.7, 0.5, 0],
            end=[-1.7, -1.5, 0],
            color=PINK,
            tip_shape=StealthTip,
            label=eq2,
        )
        arrow_3 = LabeledArrow(
            start=[-1.7, -2.5, 0],
            end=[1.7, -2.5, 0],
            color=PINK,
            tip_shape=StealthTip,
            label=eq3,
        )

        self.add(title)
        self.play(Create(m01))
        self.play(m01.animate.move_to([-4, 1.5, 0]))
        self.play(GrowArrow(arrow_1))
        self.play(Create(m02))
        self.wait(2)
        b1 = SurroundingRectangle(m02.get_rows()[1], color=YELLOW)
        b2 = SurroundingRectangle(m02.get_rows()[2], color=YELLOW)
        self.play(Create(b1))
        self.play(Create(b2))
        self.play(FadeOut(b1), FadeOut(b2))
        self.wait(1)
        self.play(TransformFromCopy(m02, m03), GrowArrow(arrow_2))
        self.wait(2)
        self.play(TransformFromCopy(m03, m04), GrowArrow(arrow_3))
        self.wait(3)
        g = VGroup(m01, m02, m03, m04, arrow_1, arrow_2, arrow_3, eq1, eq2, eq3)
        self.play(Uncreate(g))
        self.play(title.animate.move_to(ORIGIN))
        rankBrp = Text(f"Rank: 2", font_size=30, color=YELLOW).next_to(title, RIGHT)
        self.play(Write(rankBrp))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(rankBrp))

        # </SLIDE 4 RANK MATRIX =====================================================

        # SLIDE 5 DETERMINAN MATRIKS A DENGAN METODE SARRUS =====================================================
        det_judul = Text(
            "Determinan Matriks A dengan Metode Sarrus", font_size=36, color=BLUE
        )
        title_det_saurus_a = (
            Text("Determinan Matriks A dengan Metode Sarrus", font_size=36, color=BLUE)
            .to_edge(UP)
            .move_to(UP * 3.5)
        )

        self.play(Write(det_judul))
        self.wait(2)
        self.play(FadeOut(det_judul))

        self.add(title_det_saurus_a)

        matriks_a = Matrix(
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]], element_to_mobject_config={"color": RED}
        )
        self.play(Write(matriks_a))
        self.wait(1)
        self.play(FadeOut(matriks_a))

        sarrus_formula = MathTex(
            r"|A| = (1 \cdot 5 \cdot 9) + (2 \cdot 6 \cdot 7) + (3 \cdot 4 \cdot 8) - (7\cdot 5 \cdot 3) + (8 \cdot 6 \cdot 1) + (9 \cdot 4 \cdot 2)",
            color=PURPLE,
        ).scale(0.8)
        self.play(Write(sarrus_formula))
        self.wait(2)

        determinant_a = MathTex(r"|A| = 0", color=YELLOW).scale(1.2)
        self.play(Transform(sarrus_formula, determinant_a))
        self.wait(2)
        self.play(FadeOut(sarrus_formula))
        self.play(title_det_saurus_a.animate.move_to(ORIGIN))
        self.play(FadeOut(title_det_saurus_a))

        # </SLIDE 5 DETERMINAN MATRIKS A DENGAN METODE SARRUS =====================================================

        """
        MATRIKS B =====================================================
        MATRIKS B =====================================================
        MATRIKS B =====================================================
        MATRIKS B =====================================================
        MATRIKS B =====================================================
        MATRIKS B =====================================================
        MATRIKS B =====================================================
        MATRIKS B =====================================================
        """

        # SLIDE 2 PEMBERIAN MATRIX B =====================================================
        def_matriks = Text("Matrix 4x4", font_size=40, color=GREEN)
        self.play(Write(def_matriks))
        self.wait(2)
        self.play(FadeOut(def_matriks))

        matriks_a_label = Text(
            "Diberikan sebuah matrix B berukuran 4x4:", font_size=36, color=ORANGE
        ).to_edge(UP)
        matriks_a = Matrix(
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
            element_to_mobject_config={"color": YELLOW},
        )
        rankBrp = Text(f"B =", font_size=30, color=YELLOW).next_to(matriks_a, LEFT)
        self.play(Write(matriks_a_label), Write(rankBrp), Write(matriks_a))
        self.wait(2)
        self.play(FadeOut(matriks_a_label), FadeOut(rankBrp), FadeOut(matriks_a))

        # </SLIDE 2 PEMBERIAN MATRIX  B =====================================================

        # SLIDE 3 OBE 1 B =====================================================
        obe_judul = Text(
            "Dengan melakukan operasi baris elementer sebanyak 3 kali \n\n maka dapat dilakukan dengan cara berikut",
            font_size=25,
            color=TEAL,
        )
        self.play(Write(obe_judul))
        self.wait(2)
        self.play(FadeOut(obe_judul))

        # obe_penjelasan = MathTex(r"H_{12}(-3)(A)", font_size=36, color=BLUE).to_edge(UP)
        title_det_saurus_a = MathTex(r"H_{12(2)}(B)", font_size=36, color=BLUE)

        # obe_penjelasan = Text(
        #     "Contoh OBE pada Matriks A : H13(2)", font_size=36, color=BLUE
        # ).to_edge(UP)

        # Animating OBE on Matriks A

        self.play(Write(title_det_saurus_a))
        self.wait(1)
        self.play(title_det_saurus_a.animate.to_edge(UP).move_to(UP * 3.5))
        matriks_a = Matrix(
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
            element_to_mobject_config={"color": YELLOW},
        )
        self.play(Write(matriks_a))
        self.wait(1)

        # 1. Swap Row 1 and Row 2
        new_matriks_a = Matrix(
            [[1, 2, 3, 4], [10, 12, 14, 16], [9, 10, 11, 12], [13, 14, 15, 16]],
            element_to_mobject_config={"color": YELLOW},
        )
        self.play(Transform(matriks_a, new_matriks_a))
        self.wait(1)

        # 2. Multiply Row 1 by 2
        new_matriks_a = Matrix(
            [[11, 14, 17, 20], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
            element_to_mobject_config={"color": YELLOW},
        )
        self.play(Transform(matriks_a, new_matriks_a))
        self.wait(1)

        # # 3. Add Row 1 to Row 2
        # new_matriks_a = Matrix(
        #     [[8, 10, 12], [9, 12, 15], [7, 8, 9]],
        #     element_to_mobject_config={"color": YELLOW},
        # )
        # self.play(Transform(matriks_a, new_matriks_a))
        # self.wait(2)
        self.play(FadeOut(matriks_a))
        self.play(title_det_saurus_a.animate.move_to(ORIGIN))
        self.play(FadeOut(title_det_saurus_a))

        # </SLIDE 3 OBE 1 B =====================================================

        # SLIDE 3 OBE 2 B =====================================================

        title_det_saurus_a = MathTex(r"H_{43(-1)}(B)", font_size=36, color=BLUE)

        self.play(Write(title_det_saurus_a))
        self.wait(1)
        self.play(title_det_saurus_a.animate.to_edge(UP).move_to(UP * 3.5))

        # `1`
        matriks_a = Matrix(
            [[11, 14, 17, 20], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
            element_to_mobject_config={"color": YELLOW},
        )
        self.play(Write(matriks_a))
        self.wait(1)

        # `2`
        new_matriks_a = Matrix(
            [[11, 14, 17, 20], [5, 6, 7, 8], [-9, -10, -11, -12], [13, 14, 15, 16]],
            element_to_mobject_config={"color": YELLOW},
        )
        self.play(Transform(matriks_a, new_matriks_a))
        self.wait(1)

        # `3`
        new_matriks_a = Matrix(
            [[11, 14, 17, 20], [5, 6, 7, 8], [9, 10, 11, 12], [4, 4, 4, 4]],
            element_to_mobject_config={"color": YELLOW},
        )
        self.play(Transform(matriks_a, new_matriks_a))
        self.wait(1)

        self.play(FadeOut(matriks_a))
        self.play(title_det_saurus_a.animate.move_to(ORIGIN))
        self.play(FadeOut(title_det_saurus_a))

        # </SLIDE 3 OBE 2 B =====================================================

        # SLIDE 3 OBE 3 B =====================================================

        title_det_saurus_a = MathTex(r"H_{32(-2)}(B)", font_size=36, color=BLUE)

        self.play(Write(title_det_saurus_a))
        self.wait(1)
        self.play(title_det_saurus_a.animate.to_edge(UP).move_to(UP * 3.5))

        # `1`
        matriks_a = Matrix(
            [[11, 14, 17, 20], [5, 6, 7, 8], [9, 10, 11, 12], [4, 4, 4, 4]],
            element_to_mobject_config={"color": YELLOW},
        )
        self.play(Write(matriks_a))
        self.wait(1)

        # `2`
        new_matriks_a = Matrix(
            [[11, 14, 17, 20], [-10, -12, -14, -16], [9, 10, 11, 12], [4, 4, 4, 4]],
            element_to_mobject_config={"color": YELLOW},
        )
        self.play(Transform(matriks_a, new_matriks_a))
        self.wait(1)

        # `3`
        new_matriks_a = Matrix(
            [[11, 14, 17, 20], [5, 6, 7, 8], [-1, -2, -3, -4], [4, 4, 4, 4]],
            element_to_mobject_config={"color": YELLOW},
        )
        self.play(Transform(matriks_a, new_matriks_a))
        self.wait(1)

        self.play(FadeOut(matriks_a))
        self.play(title_det_saurus_a.animate.move_to(ORIGIN))
        self.play(FadeOut(title_det_saurus_a))

        # </SLIDE 3 OBE 3 B =====================================================

        # EQUIVALENN MATRIKS =====================================================
        obe_judul = Text(
            "Maka Didapatkan",
            font_size=25,
            color=TEAL,
        )
        self.play(Write(obe_judul))
        self.wait(2)
        self.play(FadeOut(obe_judul))

        title_det_saurus_a = MathTex(
            r"H_{12(2)} H_{43(-1)} H_{32(-2)}(B) = D \text{, dengan matriks } D \text{ adalah}\\",
            r"\text{matriks yang ekuivalen} \approx \text{matriks } B",
            font_size=36,
            color=BLUE,
        )

        self.play(Write(title_det_saurus_a))
        self.wait(1)
        self.play(title_det_saurus_a.animate.to_edge(UP).move_to(UP * 3.5))

        matriks_a = Matrix(
            [[11, 14, 17, 20], [5, 6, 7, 8], [-1, -2, -3, -4], [4, 4, 4, 4]],
            element_to_mobject_config={"color": YELLOW},
        )
        rankBrp = Text(f"D =", font_size=30, color=YELLOW).next_to(matriks_a, LEFT)
        rankBrp2 = MathTex(
            r"\approx \text{matriks } B", font_size=30, color=YELLOW
        ).next_to(matriks_a, RIGHT)
        self.play(Write(rankBrp))
        self.play(Write(matriks_a))
        self.play(Write(rankBrp2))
        self.wait(1)

        self.play(FadeOut(matriks_a), FadeOut(rankBrp), FadeOut(rankBrp2))
        self.play(title_det_saurus_a.animate.move_to(ORIGIN))
        self.play(FadeOut(title_det_saurus_a))

        # </EQUIVALENN MATRIKS =====================================================

        # SLIDE 4 RANK MATRIX A =====================================================
        rank_judul = Text("Rank Matriks B", font_size=40, color=GREEN)
        self.play(Write(rank_judul))
        self.wait(2)
        self.play(FadeOut(rank_judul))

        title = Text("Rank Matrix B").set_color(TEAL).move_to(UP * 3.5)

        m01 = Matrix(
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
        )
        m02 = Matrix(
            [[1, 2, 3, 4], [0, -4, -8, -12], [9, 10, 11, 12], [13, 14, 15, 16]],
        )
        m03 = Matrix(
            [[1, 2, 3, 4], [0, -4, -8, -12], [0, -8, -16, -24], [13, 14, 15, 16]],
        ).move_to([-4, -2.5, 0])
        m04 = Matrix(
            [[1, 2, 3, 4], [0, -4, -8, -12], [0, -8, -16, -24], [0, -12, -24, -36]],
        )

        self.add(title)
        matriks_a = Matrix(
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
            element_to_mobject_config={"color": YELLOW},
        )

        rankBrp = MathTex(r"=", font_size=30, color=YELLOW).next_to(matriks_a, LEFT)
        self.play(Write(rankBrp))
        self.play(Write(matriks_a))
        self.wait(1)

        # =================================
        new_matriks_a = Matrix(
            [[1, 2, 3, 4], [0, -4, -8, -12], [9, 10, 11, 12], [13, 14, 15, 16]],
            element_to_mobject_config={"color": YELLOW},
        )
        new_rankBrp = MathTex(r"H_{21(-5)} =", font_size=30, color=YELLOW).next_to(
            matriks_a, LEFT
        )
        self.play(Transform(rankBrp, new_rankBrp))
        self.play(Transform(matriks_a, new_matriks_a))
        self.wait(1)
        # =================================

        # =================================
        new_matriks_a = Matrix(
            [[1, 2, 3, 4], [0, -4, -8, -12], [0, -8, -16, -24], [13, 14, 15, 16]],
            element_to_mobject_config={"color": YELLOW},
        )
        new_rankBrp = MathTex(r"H_{31(-9)} =", font_size=30, color=YELLOW).next_to(
            matriks_a, LEFT
        )
        self.play(Transform(rankBrp, new_rankBrp))
        self.play(Transform(matriks_a, new_matriks_a))
        self.wait(1)
        # =================================
        # =================================
        new_matriks_a = Matrix(
            [[1, 2, 3, 4], [0, -4, -8, -12], [0, -8, -16, -24], [0, -12, -24, -36]],
            element_to_mobject_config={"color": YELLOW},
        )
        new_rankBrp = MathTex(r"H_{41(-13)} =", font_size=30, color=YELLOW).next_to(
            matriks_a, LEFT
        )
        self.play(Transform(rankBrp, new_rankBrp))
        self.play(Transform(matriks_a, new_matriks_a))
        self.wait(1)
        # =================================
        # =================================
        new_matriks_a = Matrix(
            [[1, 2, 3, 4], [0, 1, 2, 3], [0, -8, -16, -24], [0, -12, -24, -36]],
            element_to_mobject_config={"color": YELLOW},
        )
        new_rankBrp = MathTex(r"H_{2(-1/4)} =", font_size=30, color=YELLOW).next_to(
            matriks_a, LEFT
        )
        self.play(Transform(rankBrp, new_rankBrp))
        self.play(Transform(matriks_a, new_matriks_a))
        self.wait(1)
        # =================================
        # =================================
        new_matriks_a = Matrix(
            [[1, 2, 3, 4], [0, 1, 2, 3], [0, 0, 0, 0], [0, -12, -24, -36]],
            element_to_mobject_config={"color": YELLOW},
        )
        new_rankBrp = MathTex(r"H_{32(-8)} =", font_size=30, color=YELLOW).next_to(
            matriks_a, LEFT
        )
        self.play(Transform(rankBrp, new_rankBrp))
        self.play(Transform(matriks_a, new_matriks_a))
        self.wait(1)
        # =================================
        # =================================
        new_matriks_a = Matrix(
            [[1, 2, 3, 4], [0, 1, 2, 3], [0, 0, 0, 0], [0, 0, 0, 0]],
            element_to_mobject_config={"color": YELLOW},
        )
        new_rankBrp = MathTex(r"H_{42(-12)} =", font_size=30, color=YELLOW).next_to(
            matriks_a, LEFT
        )
        self.play(Transform(rankBrp, new_rankBrp))
        self.play(Transform(matriks_a, new_matriks_a))
        self.wait(1)
        # =================================

        self.play(FadeOut(matriks_a), FadeOut(rankBrp))
        self.play(title.animate.move_to(ORIGIN))
        rankBrp = Text(f"Rank: 2", font_size=30, color=YELLOW).next_to(title, RIGHT)
        self.play(Write(rankBrp))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(rankBrp))

        # </SLIDE 4 RANK MATRIX =====================================================

        # SLIDE 6 DETERMINAN MATRIKS B DENGAN METODE KOFAKTOR
        matriks = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

        # Membuat matriks
        matriks_mob = Matrix(
            matriks,
            element_to_mobject_config={"color": YELLOW},
        )
        self.play(Write(matriks_mob))
        self.wait()

        # Menjelaskan ekspansi kofaktor
        penjelasan = Text(
            "Kita akan menghitung determinan menggunakan\n\nekspansi kofaktor sepanjang baris pertama",
            font_size=24,
        )
        self.play(Write(penjelasan))
        self.wait(2)
        self.play(FadeOut(penjelasan))

        # Menjelaskan matriks kofaktor
        penjelasan_kofaktor = Text(
            "Matriks kofaktor terdiri dari semua kofaktor Cij", font_size=24
        )
        formula_kofaktor = MathTex(r"C_{ij} = (-1)^{i+j} M_{ij}", font_size=24)
        deskripsi_kofaktor = Text(
            "dimana Mij adalah minor (determinan submatriks)", font_size=24
        )

        grup = VGroup(
            penjelasan_kofaktor, formula_kofaktor, deskripsi_kofaktor
        ).arrange(DOWN)
        self.play(Write(grup))
        self.wait(3)
        self.play(FadeOut(grup))

        # Menyoroti setiap elemen baris pertama dan kofaktornya
        for i in range(4):
            # Menyoroti elemen saat ini
            elemen = matriks_mob.get_entries()[i]
            self.play(elemen.animate.set_color(RED))

            # Membuat dan menampilkan matriks kofaktor
            matriks_kofaktor = [baris[:i] + baris[i + 1 :] for baris in matriks[1:]]
            kofaktor_mob = Matrix(matriks_kofaktor).scale(0.7)
            kofaktor_mob.next_to(matriks_mob, RIGHT)
            self.play(Write(kofaktor_mob))

            # Menjelaskan kofaktor saat ini
            penjelasan_kofaktor = Text(f"Kofaktor C{1}{i+1}", font_size=24).next_to(
                kofaktor_mob, UP
            )
            self.play(Write(penjelasan_kofaktor))

            # Menampilkan tanda kofaktor
            tanda = (-1) ** (i + 1)
            teks_tanda = MathTex(
                r"(-1)^{" + f"{1}+{i+1}" + r"} = " + f"{tanda}", font_size=24
            ).next_to(kofaktor_mob, DOWN)
            self.play(Write(teks_tanda))

            # Menghitung dan menampilkan minor
            nilai_minor = self.hitung_determinan_3x3(matriks_kofaktor)
            teks_minor = Text(f"Minor M{1}{i+1} = {nilai_minor}", font_size=24).next_to(
                teks_tanda, DOWN
            )
            self.play(Write(teks_minor))

            # Menampilkan perhitungan kofaktor
            nilai_kofaktor = tanda * nilai_minor
            teks_kofaktor = Text(
                f"C{1}{i+1} = {tanda} * {nilai_minor} = {nilai_kofaktor}", font_size=24
            ).next_to(teks_minor, DOWN)
            self.play(Write(teks_kofaktor))

            # Menampilkan perkalian dengan elemen matriks
            hasil = matriks[0][i] * nilai_kofaktor
            teks_hasil = Text(
                f"{matriks[0][i]} * {nilai_kofaktor} = {hasil}", font_size=24
            ).next_to(teks_kofaktor, DOWN)
            self.play(Write(teks_hasil))

            self.wait(2)

            # Membersihkan untuk iterasi berikutnya
            self.play(
                FadeOut(kofaktor_mob),
                FadeOut(penjelasan_kofaktor),
                FadeOut(teks_tanda),
                FadeOut(teks_minor),
                FadeOut(teks_kofaktor),
                FadeOut(teks_hasil),
                elemen.animate.set_color(WHITE),
            )

        # Menampilkan jumlah akhir
        jumlah_akhir = sum(
            [
                matriks[0][i]
                * (-1) ** (i + 1)
                * self.hitung_determinan_3x3(
                    [baris[:i] + baris[i + 1 :] for baris in matriks[1:]]
                )
                for i in range(4)
            ]
        )
        teks_akhir = Text(f"Determinan = {jumlah_akhir}").next_to(matriks_mob, DOWN)
        self.play(Write(teks_akhir))
        self.wait(2)
        self.play(FadeOut(matriks_mob), FadeOut(teks_akhir))

    def hitung_determinan_3x3(self, matriks):
        return (
            matriks[0][0]
            * (matriks[1][1] * matriks[2][2] - matriks[1][2] * matriks[2][1])
            - matriks[0][1]
            * (matriks[1][0] * matriks[2][2] - matriks[1][2] * matriks[2][0])
            + matriks[0][2]
            * (matriks[1][0] * matriks[2][1] - matriks[1][1] * matriks[2][0])
        )


# Untuk menjalankan skrip ini, gunakan perintah:
# manim -pql presentasi_operasi_matriks.py PresentasiOperasiMatriks
