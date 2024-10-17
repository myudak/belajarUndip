from manim import *


class KmapScene(Scene):
    def construct(self):

        # JUDUL ============================================================
        title = Text("Design of a BCD–to–Seven-Segment Decoder").scale(0.75).to_edge(UP)
        self.play(Write(title))

        subtitle = Text("Universitas Diponegoro", font_size=24).next_to(title, DOWN)
        self.play(FadeIn(subtitle))
        self.wait()
        self.play(FadeOut(title), FadeOut(subtitle))
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

        obe_judul = Text(
            "SPESIFIKASI",
            font_size=36,
            color=TEAL,
        )
        self.play(Write(obe_judul))
        self.wait(2)
        self.play(FadeOut(obe_judul))

        obe_judul = Text(
            "Decoder BCD-ke-seven-segment adalah rangkaian kombinasi yang menerima digit desimal\n\ndalam bentuk BCD dan menghasilkan keluaran yang tepat untuk\n\nsegmen-segmen tampilan sesuai dengan digit desimal tersebut.\n\nTerdapat tujuh keluaran dari decoder\n\n(a, b, c, d, e, f, g) yang akan\n\nmengendalikan segmen terkait pada tampilan",
            font_size=17,
            color=TEAL,
        )
        self.play(Write(obe_judul))
        self.wait(2)
        self.play(FadeOut(obe_judul))

        """
        KMAP ============================================================
        """
        # Truth Table
        TopLeftEntry = VGroup(
            Tex("A", "B", font_size=DEFAULT_FONT_SIZE).shift(DOWN * 0.6),
            Tex("C", "D", font_size=DEFAULT_FONT_SIZE).shift(RIGHT * 0.6),
        )
        Kmap = IntegerTable(
            [[1, 0, 1, 1], [0, 1, 1, 1], [0, 0, 0, 0], [1, 1, 0, 0]],
            row_labels=[
                MathTex("0", "0"),
                MathTex("0", "1"),
                MathTex("1", "1"),
                MathTex("1", "0"),
            ],
            col_labels=[
                MathTex("0", "0"),
                MathTex("0", "1"),
                MathTex("1", "1"),
                MathTex("1", "0"),
            ],
            v_buff=1.0,
            h_buff=1.0,
            top_left_entry=TopLeftEntry,
        ).shift(LEFT * 3)

        # Expressions
        expression = MathTex("a(A, B, C, D) = \Sigma_{m}(0, 2, 3, 5, 6, 7, 8, 9)")
        expression_simp = (
            MathTex(
                "A\,\overline{B}\,\overline{C}",
                "+",
                "\overline{A}\,B\,D",
                "+",
                "\overline{A}\,C",
                "+",
                "\overline{A}\,\overline{B}\,\overline{D}",
            )
            .shift(RIGHT * (config["frame_x_radius"] + Kmap.get_right()) / 2)
            .scale(0.7)
        )

        """
        MINTERM GROUP
        """
        # Ones to be surrounded

        frame1_group = VGroup(
            Kmap.get_entries_without_labels()[12:14],
        )
        frame2_group = VGroup(
            Kmap.get_entries_without_labels()[5:7],
        )
        frame3_group = VGroup(
            Kmap.get_entries_without_labels()[2:4],
            Kmap.get_entries_without_labels()[6:8],
        )
        frame4_group = VGroup(
            Kmap.get_entries_without_labels()[0:1],
        )
        frame5_group = VGroup(
            Kmap.get_entries_without_labels()[3:4],
        )

        """
        MINTERM GROUP
        """
        frame1 = SurroundingRectangle(
            VGroup(frame1_group), color=RED, buff=0.3
        ).round_corners(radius=0.2)
        frame2 = SurroundingRectangle(
            VGroup(frame2_group), color=GREEN, buff=0.3
        ).round_corners(radius=0.2)
        frame3 = SurroundingRectangle(
            VGroup(frame3_group), color=YELLOW, buff=0.3
        ).round_corners(radius=0.2)
        frame4 = SurroundingRectangle(
            VGroup(frame4_group), color=BLUE, buff=0.3
        ).round_corners(radius=0.2)
        frame5 = SurroundingRectangle(
            VGroup(frame5_group), color=BLUE, buff=0.3
        ).round_corners(radius=0.2)

        self.play(Write(expression))
        self.wait(3)
        self.play(FadeOut(expression))

        self.wait()
        self.play(Kmap.create(), run_time=5)
        self.wait(2)

        # FRAME 1 ==========================================================
        self.play(Create(frame1))

        self.wait()
        self.play(
            Indicate(TopLeftEntry[0][0]),
            Indicate(TopLeftEntry[0][1]),
            # Indicate(Kmap.get_labels()[5][0]),
            # Indicate(Kmap.get_labels()[6][0]),
            Indicate(Kmap.get_labels()[8][0]),
            Indicate(Kmap.get_labels()[8][1]),
        )

        self.wait()
        self.play(
            Indicate(TopLeftEntry[1][0]),
            Indicate(Kmap.get_labels()[1][0]),
            Indicate(Kmap.get_labels()[2][0]),
        )

        self.wait()
        self.play(Write(expression_simp[0]))
        self.wait(1)

        # FRAME 1 ==========================================================

        # FRAME 2 ==========================================================
        self.play(Create(frame2))

        self.wait()
        self.play(
            Indicate(TopLeftEntry[0][0]),
            Indicate(TopLeftEntry[0][1]),
            # Indicate(Kmap.get_labels()[5][0]),
            # Indicate(Kmap.get_labels()[6][0]),
            Indicate(Kmap.get_labels()[6][0]),
            Indicate(Kmap.get_labels()[6][1]),
        )

        self.wait()
        self.play(
            Indicate(TopLeftEntry[1][1]),
            Indicate(Kmap.get_labels()[2][1]),
            Indicate(Kmap.get_labels()[3][1]),
        )

        self.wait()
        self.play(Write(expression_simp[2]))
        self.wait(1)

        # FRAME 2 ==========================================================

        # FRAME 3 ==========================================================
        self.play(Create(frame3))

        self.wait()
        self.play(
            Indicate(TopLeftEntry[0][0]),
            # Indicate(Kmap.get_labels()[5][0]),
            # Indicate(Kmap.get_labels()[6][0]),
            Indicate(Kmap.get_labels()[5][0]),
            Indicate(Kmap.get_labels()[6][0]),
        )

        self.wait()
        self.play(
            Indicate(TopLeftEntry[1][0]),
            Indicate(Kmap.get_labels()[3][0]),
            Indicate(Kmap.get_labels()[4][0]),
        )

        self.wait()
        self.play(Write(expression_simp[4]))
        self.wait()

        # FRAME 3 ==========================================================

        # FRAME 4 ==========================================================
        self.play(Create(frame4))
        self.play(Create(frame5))

        self.wait()
        self.play(
            Indicate(TopLeftEntry[0][0]),
            Indicate(TopLeftEntry[0][1]),
            # Indicate(Kmap.get_labels()[5][0]),
            # Indicate(Kmap.get_labels()[6][0]),
            Indicate(Kmap.get_labels()[5][0]),
            Indicate(Kmap.get_labels()[5][1]),
        )

        self.wait()
        self.play(
            Indicate(TopLeftEntry[1][1]),
            Indicate(Kmap.get_labels()[1][1]),
            Indicate(Kmap.get_labels()[4][1]),
        )

        self.wait()
        self.play(Write(expression_simp[6]))
        self.wait()

        # FRAME 4 ==========================================================

        # ENDDD
        self.play(
            Write(expression_simp[1]),
            Write(expression_simp[3]),
            Write(expression_simp[5]),
            FadeOut(frame1),
            FadeOut(frame2),
            FadeOut(frame3),
            FadeOut(frame4),
            FadeOut(frame5),
            FadeOut(Kmap),
        )
        self.play(expression_simp.animate.move_to(ORIGIN))
        self.wait(3)

        """
        KMAP ============================================================
        """
