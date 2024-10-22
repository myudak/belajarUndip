from manim import *


class AwalAnimation(Scene):
    def run_judul(self):
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

    def run_spesifikasi(self):
        obe_judul = Text(
            "SPESIFIKASI",
            font_size=36,
            color=TEAL,
        )
        self.play(Write(obe_judul))
        self.wait(2)
        self.play(FadeOut(obe_judul))

        obe_judul = Text(
            "Decoder BCD-ke-seven-segment adalah rangkaian kombinasi yang menerima digit desimal\n\ndalam bentuk BCD dan menghasilkan keluaran yang tepat untuk\n\nsegmen-segmen tampilan sesuai dengan digit desimal tersebut.\n\nTerdapat tujuh keluaran dari decoder\n\n(a, b, c, d, e, f, g) yang akan mengendalikan segmen terkait pada tampilan",
            font_size=17,
            color=TEAL,
        )
        self.play(Write(obe_judul))
        self.wait(2)
        self.play(FadeOut(obe_judul))
        self.wait()

    def run_formulasi_tabel(self):
        # Colors for ON and OFF states
        on_color = YELLOW
        off_color = DARK_GRAY

        # Create the 7 segments as rectangles (without the decimal point)
        segments = [
            Rectangle(width=0.6, height=0.1),  # Top (a)
            Rectangle(width=0.1, height=0.6),  # Top-right (b)
            Rectangle(width=0.1, height=0.6),  # Bottom-right (c)
            Rectangle(width=0.6, height=0.1),  # Bottom (d)
            Rectangle(width=0.1, height=0.6),  # Bottom-left (e)
            Rectangle(width=0.1, height=0.6),  # Top-left (f)
            Rectangle(width=0.6, height=0.1),  # Middle (g)
        ]

        # Set initial positions for each segment
        segments[0].move_to([0, 0.75, 0])  # Top (a)
        segments[1].move_to([0.35, 0.4, 0])  # Top-right (b)
        segments[2].move_to([0.35, -0.4, 0])  # Bottom-right (c)
        segments[3].move_to([0, -0.75, 0])  # Bottom (d)
        segments[4].move_to([-0.35, -0.4, 0])  # Bottom-left (e)
        segments[5].move_to([-0.35, 0.4, 0])  # Top-left (f)
        segments[6].move_to([0, 0, 0])  # Middle (g)

        # Group all segments together
        led_display = VGroup(*segments)

        # Initialize all segments as OFF
        for segment in segments:
            segment.set_fill(off_color, opacity=1)
            segment.set_stroke(width=0.5)

        # Create the BCD input to 7-segment table
        table_data = [
            ["0", "0", "0", "0", "1", "1", "1", "1", "1", "1", "0"],  # 0
            ["0", "0", "0", "1", "0", "1", "1", "0", "0", "0", "0"],  # 1
            ["0", "0", "1", "0", "1", "1", "0", "1", "1", "0", "1"],  # 2
            ["0", "0", "1", "1", "1", "1", "1", "1", "0", "0", "1"],  # 3
            ["0", "1", "0", "0", "0", "1", "1", "0", "0", "1", "1"],  # 4
            ["0", "1", "0", "1", "1", "0", "1", "1", "0", "1", "1"],  # 5
            ["0", "1", "1", "0", "1", "0", "1", "1", "1", "1", "1"],  # 6
            ["0", "1", "1", "1", "1", "1", "1", "0", "0", "0", "0"],  # 7
            ["1", "0", "0", "0", "1", "1", "1", "1", "1", "1", "1"],  # 8
            ["1", "0", "0", "1", "1", "1", "1", "1", "0", "1", "1"],  # 9
        ]

        # Create the table (header and data)
        table = Table(
            [["A", "B", "C", "D", "a", "b", "c", "d", "e", "f", "g"]] + table_data,
            include_outer_lines=True,
        )

        # Set positions for table and display
        table.scale(0.5).to_edge(LEFT)
        led_display.next_to(table, RIGHT, buff=1)

        # Display the table and the 7-segment display
        self.play(Create(table), Create(led_display))

        # Animate the segments for each BCD input
        for i, row in enumerate(table_data):
            bcd_input = row[:4]  # BCD part (A, B, C, D)
            segments_state = row[4:]  # Segment part (a-g)

            # Highlighting which row in the table is being processed
            self.play(table.get_rows()[i + 1].animate.set_fill(YELLOW, opacity=0.3))

            # Turn on/off the segments based on the table row
            for j, segment in enumerate(segments):
                if segments_state[j] == "1":
                    segment.set_fill(on_color)
                else:
                    segment.set_fill(off_color)

            # Update the display with new segment states
            self.wait(1)
            self.play(FadeToColor(led_display, WHITE))
            # self.wait(1)

            # Reset the table row highlight after delay
            self.play(table.get_rows()[i + 1].animate.set_fill(WHITE, opacity=1))

        self.play(FadeOut(table), FadeOut(led_display))
        self.wait(1)

    def run_kmap1(self):
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
        self.wait()
        self.play(FadeOut(expression))

        self.wait()
        self.play(Kmap.create(), run_time=5)
        self.wait()

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
        self.play(expression_simp.animate.scale(1.4).move_to(ORIGIN))
        self.wait()
        self.play(FadeOut(expression_simp))

        """
        /KMAP ============================================================
        """

    def run_kmap2(self):
        """
        B
        KMAP ============================================================
        """
        # Truth Table
        TopLeftEntry = VGroup(
            Tex("A", "B", font_size=DEFAULT_FONT_SIZE).shift(DOWN * 0.6),
            Tex("C", "D", font_size=DEFAULT_FONT_SIZE).shift(RIGHT * 0.6),
        )
        Kmap = IntegerTable(
            [[1, 1, 1, 1], [1, 0, 1, 0], [0, 0, 0, 0], [1, 1, 0, 0]],
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
        expression = MathTex("b(A, B, C, D) = \Sigma_{m}(0, 1, 2, 3, 4, 7, 8,9)")
        expression_simp = (
            MathTex(
                "\overline{A}\,\overline{B}",
                "+",
                "\overline{A}\,\overline{C}\,\overline{D}",
                "+",
                "\overline{A}\,C\,D",
                "+",
                "\overline{B}\,\overline{C}",
            )
            .shift(RIGHT * (config["frame_x_radius"] + Kmap.get_right()) / 2)
            .scale(0.7)
        )

        """
        MINTERM GROUP
        """
        # Ones to be surrounded

        frame1_group = VGroup(
            Kmap.get_entries_without_labels()[0:4],
        )
        frame2_group = VGroup(
            Kmap.get_entries_without_labels()[0:1],
            Kmap.get_entries_without_labels()[4:5],
        )
        frame3_group = VGroup(
            Kmap.get_entries_without_labels()[2:3],
            Kmap.get_entries_without_labels()[6:7],
        )
        frame4_group = VGroup(
            Kmap.get_entries_without_labels()[0:2],
        )
        frame5_group = VGroup(
            Kmap.get_entries_without_labels()[12:14],
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
        self.wait()
        self.play(FadeOut(expression))

        self.wait()
        self.play(Kmap.create(), run_time=5)
        self.wait()

        # FRAME 1 ==========================================================
        self.play(Create(frame1))

        self.wait()
        self.play(
            Indicate(TopLeftEntry[0][0]),
            Indicate(TopLeftEntry[0][1]),
            Indicate(Kmap.get_labels()[5][0]),
            Indicate(Kmap.get_labels()[5][1]),
        )

        # self.wait()
        # self.play(
        #     Indicate(TopLeftEntry[1][0]),
        #     Indicate(TopLeftEntry[1][1]),
        #     Indicate(Kmap.get_labels()[1][0]),
        #     Indicate(Kmap.get_labels()[1][1]),
        # )

        self.wait()
        self.play(Write(expression_simp[0]))
        self.wait(1)

        # /FRAME 1 ==========================================================

        # FRAME 2 ==========================================================
        self.play(Create(frame2))

        self.wait()
        self.play(
            Indicate(TopLeftEntry[0][0]),
            Indicate(Kmap.get_labels()[5][0]),
            Indicate(Kmap.get_labels()[6][0]),
        )

        self.wait()
        self.play(
            Indicate(TopLeftEntry[1][0]),
            Indicate(TopLeftEntry[1][1]),
            Indicate(Kmap.get_labels()[1][0]),
            Indicate(Kmap.get_labels()[1][1]),
        )

        self.wait()
        self.play(Write(expression_simp[2]))
        self.wait(1)

        # /FRAME 2 ==========================================================

        # FRAME 3 ==========================================================
        self.play(Create(frame3))

        self.wait()
        self.play(
            Indicate(TopLeftEntry[0][0]),
            Indicate(Kmap.get_labels()[5][0]),
            Indicate(Kmap.get_labels()[6][0]),
        )

        self.wait()
        self.play(
            Indicate(TopLeftEntry[1][0]),
            Indicate(TopLeftEntry[1][1]),
            Indicate(Kmap.get_labels()[3][0]),
            Indicate(Kmap.get_labels()[3][1]),
        )

        self.wait()
        self.play(Write(expression_simp[4]))
        self.wait()

        # /FRAME 3 ==========================================================

        # FRAME 4 ==========================================================
        self.play(Create(frame4))
        self.play(Create(frame5))

        self.wait()
        self.play(
            Indicate(TopLeftEntry[0][1]),
            Indicate(Kmap.get_labels()[8][1]),
        )

        self.wait()
        self.play(
            Indicate(TopLeftEntry[1][0]),
            Indicate(Kmap.get_labels()[1][0]),
            Indicate(Kmap.get_labels()[2][0]),
        )

        self.wait()
        self.play(Write(expression_simp[6]))
        self.wait()

        # /FRAME 4 ==========================================================

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
        self.play(expression_simp.animate.scale(1.4).move_to(ORIGIN))
        self.wait(2)
        self.play(FadeOut(expression_simp))

        """
        B
        /KMAP ============================================================
        """

    def run_kmap3(self):
        # Truth Table
        TopLeftEntry = VGroup(
            Tex("A", "B", font_size=DEFAULT_FONT_SIZE).shift(DOWN * 0.6),
            Tex("C", "D", font_size=DEFAULT_FONT_SIZE).shift(RIGHT * 0.6),
        )
        Kmap = IntegerTable(
            [[1, 1, 1, 0], [1, 1, 1, 1], [0, 0, 0, 0], [1, 1, 0, 0]],
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
        expression = MathTex("c(A, B, C, D) = \Sigma_{m}(0, 1, 3, 4, 5, 6, 7, 8, 9)")
        expression_simp = (
            MathTex(
                "\overline{A}\,B",
                "+",
                "\overline{A}\,D",
                "+",
                "\overline{B}\,\overline{C}",
            )
            .shift(RIGHT * (config["frame_x_radius"] + Kmap.get_right()) / 2)
            .scale(0.7)
        )

        """
        MINTERM GROUP
        """
        # Ones to be surrounded

        frame1_group = VGroup(
            Kmap.get_entries_without_labels()[4:8],
        )
        frame2_group = VGroup(
            Kmap.get_entries_without_labels()[1:3],
            Kmap.get_entries_without_labels()[4:7],
        )
        # frame3_group = VGroup(
        #     Kmap.get_entries_without_labels()[2:3],
        #     Kmap.get_entries_without_labels()[6:7],
        # )
        frame4_group = VGroup(
            Kmap.get_entries_without_labels()[0:2],
        )
        frame5_group = VGroup(
            Kmap.get_entries_without_labels()[12:14],
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
        # frame3 = SurroundingRectangle(
        #     VGroup(frame3_group), color=YELLOW, buff=0.3
        # ).round_corners(radius=0.2)
        frame4 = SurroundingRectangle(
            VGroup(frame4_group), color=BLUE, buff=0.3
        ).round_corners(radius=0.2)
        frame5 = SurroundingRectangle(
            VGroup(frame5_group), color=BLUE, buff=0.3
        ).round_corners(radius=0.2)

        self.play(Write(expression))
        self.wait()
        self.play(FadeOut(expression))

        self.wait()
        self.play(Kmap.create(), run_time=5)
        self.wait()

        # FRAME 1 ==========================================================
        self.play(Create(frame1))

        self.wait()
        self.play(
            Indicate(TopLeftEntry[0][0]),
            Indicate(TopLeftEntry[0][1]),
            Indicate(Kmap.get_labels()[6][0]),
            Indicate(Kmap.get_labels()[6][1]),
        )

        # self.wait()
        # self.play(
        #     Indicate(TopLeftEntry[1][0]),
        #     Indicate(TopLeftEntry[1][1]),
        #     Indicate(Kmap.get_labels()[1][0]),
        #     Indicate(Kmap.get_labels()[1][1]),
        # )

        self.wait()
        self.play(Write(expression_simp[0]))
        self.wait(1)

        # /FRAME 1 ==========================================================

        # FRAME 2 ==========================================================
        self.play(Create(frame2))

        self.wait()
        self.play(
            Indicate(TopLeftEntry[0][0]),
            Indicate(Kmap.get_labels()[5][0]),
            Indicate(Kmap.get_labels()[6][0]),
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

        # /FRAME 2 ==========================================================

        # FRAME 3 ==========================================================
        # self.play(Create(frame3))

        # self.wait()
        # self.play(
        #     Indicate(TopLeftEntry[0][0]),
        #     Indicate(Kmap.get_labels()[5][0]),
        #     Indicate(Kmap.get_labels()[6][0]),
        # )

        # self.wait()
        # self.play(
        #     Indicate(TopLeftEntry[1][0]),
        #     Indicate(TopLeftEntry[1][1]),
        #     Indicate(Kmap.get_labels()[3][0]),
        #     Indicate(Kmap.get_labels()[3][1]),
        # )

        # self.wait()
        # self.play(Write(expression_simp[4]))
        # self.wait()

        # /FRAME 3 ==========================================================

        # FRAME 4 ==========================================================
        self.play(Create(frame4))
        self.play(Create(frame5))

        self.wait()
        self.play(
            Indicate(TopLeftEntry[0][1]),
            Indicate(Kmap.get_labels()[8][1]),
        )

        self.wait()
        self.play(
            Indicate(TopLeftEntry[1][0]),
            Indicate(Kmap.get_labels()[1][0]),
            Indicate(Kmap.get_labels()[2][0]),
        )

        self.wait()
        self.play(Write(expression_simp[4]))
        self.wait()

        # /FRAME 4 ==========================================================

        # ENDDD
        self.play(
            Write(expression_simp[1]),
            Write(expression_simp[3]),
            # Write(expression_simp[5]),
            FadeOut(frame1),
            FadeOut(frame2),
            # FadeOut(frame3),
            FadeOut(frame4),
            FadeOut(frame5),
            FadeOut(Kmap),
        )
        self.play(expression_simp.animate.scale(1.4).move_to(ORIGIN))
        self.wait(2)
        self.play(FadeOut(expression_simp))

        """
        /KMAP ============================================================
        """

    def run_kmap4(self):
        # Truth Table
        TopLeftEntry = VGroup(
            Tex("A", "B", font_size=DEFAULT_FONT_SIZE).shift(DOWN * 0.6),
            Tex("C", "D", font_size=DEFAULT_FONT_SIZE).shift(RIGHT * 0.6),
        )
        Kmap = IntegerTable(
            [[1, 0, 1, 1], [0, 1, 0, 1], [0, 0, 0, 0], [1, 1, 0, 0]],
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
        expression = MathTex("d(A, B, C, D) = \Sigma_{m}(0, 2, 3, 5, 6, 8, 9)")
        expression_simp = (
            MathTex(
                "A\,\overline{B}\,\overline{C}",
                "+",
                "\overline{A}\,\overline{B}\,C",
                "+",
                "\overline{A}\,C\,\overline{D}",
                "+",
                "\overline{A}\,\overline{B}\,\overline{D}",
                "+",
                "\overline{A}\,B\,\overline{C}\,D",
            )
            .shift(RIGHT * (config["frame_x_radius"] + Kmap.get_right()) / 2)
            .scale(0.5)
        )

        """
        MINTERM GROUP
        """
        # Ones to be surrounded

        frame1_group = VGroup(
            Kmap.get_entries_without_labels()[12:14],
        )
        frame2_group = VGroup(
            Kmap.get_entries_without_labels()[2:4],
        )
        frame3_group = VGroup(
            Kmap.get_entries_without_labels()[3:4],
            Kmap.get_entries_without_labels()[7:8],
        )
        frame4_group = VGroup(
            Kmap.get_entries_without_labels()[0:1],
        )
        frame5_group = VGroup(
            Kmap.get_entries_without_labels()[3:4],
        )
        frame6_group = VGroup(
            Kmap.get_entries_without_labels()[5:6],
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
        frame6 = SurroundingRectangle(
            VGroup(frame6_group), color=PURPLE, buff=0.3
        ).round_corners(radius=0.2)

        self.play(Write(expression))
        self.wait()
        self.play(FadeOut(expression))

        self.wait()
        self.play(Kmap.create(), run_time=5)
        self.wait()

        # FRAME 1 ==========================================================
        self.play(Create(frame1))

        self.wait()
        self.play(
            Indicate(TopLeftEntry[0][0]),
            Indicate(TopLeftEntry[0][1]),
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

        # /FRAME 1 ==========================================================

        # FRAME 2 ==========================================================
        self.play(Create(frame2))

        self.wait()
        self.play(
            Indicate(TopLeftEntry[0][0]),
            Indicate(TopLeftEntry[0][1]),
            Indicate(Kmap.get_labels()[5][0]),
            Indicate(Kmap.get_labels()[5][1]),
        )

        self.wait()
        self.play(
            Indicate(TopLeftEntry[1][0]),
            Indicate(Kmap.get_labels()[3][0]),
            Indicate(Kmap.get_labels()[4][0]),
        )

        self.wait()
        self.play(Write(expression_simp[2]))
        self.wait(1)

        # /FRAME 2 ==========================================================

        # FRAME 3 ==========================================================
        self.play(Create(frame3))

        self.wait()
        self.play(
            Indicate(TopLeftEntry[0][0]),
            Indicate(Kmap.get_labels()[5][0]),
            Indicate(Kmap.get_labels()[6][0]),
        )

        self.wait()
        self.play(
            Indicate(TopLeftEntry[1][0]),
            Indicate(TopLeftEntry[1][1]),
            Indicate(Kmap.get_labels()[4][0]),
            Indicate(Kmap.get_labels()[4][1]),
        )

        self.wait()
        self.play(Write(expression_simp[4]))
        self.wait()

        # /FRAME 3 ==========================================================

        # FRAME 4 ==========================================================
        self.play(Create(frame4))
        self.play(Create(frame5))

        self.wait()
        self.play(
            Indicate(TopLeftEntry[0][0]),
            Indicate(TopLeftEntry[0][1]),
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

        # /FRAME 4 ==========================================================

        # FRAME 5 ==========================================================
        self.play(Create(frame6))

        self.wait()
        self.play(
            Indicate(TopLeftEntry[0][0]),
            Indicate(TopLeftEntry[0][1]),
            Indicate(Kmap.get_labels()[6][0]),
            Indicate(Kmap.get_labels()[6][1]),
        )

        self.wait()
        self.play(
            Indicate(TopLeftEntry[1][0]),
            Indicate(TopLeftEntry[1][1]),
            Indicate(Kmap.get_labels()[2][0]),
            Indicate(Kmap.get_labels()[2][1]),
        )

        self.wait()
        self.play(Write(expression_simp[8]))
        self.wait()

        # /FRAME 5 ==========================================================

        # ENDDD
        self.play(
            Write(expression_simp[1]),
            Write(expression_simp[3]),
            Write(expression_simp[5]),
            Write(expression_simp[7]),
            FadeOut(frame1),
            FadeOut(frame2),
            FadeOut(frame3),
            FadeOut(frame4),
            FadeOut(frame5),
            FadeOut(frame6),
            FadeOut(Kmap),
        )
        self.play(expression_simp.animate.scale(2).move_to(ORIGIN))
        self.wait(2)
        self.play(FadeOut(expression_simp))

        """
        /KMAP ============================================================
        """

    def run_kmap5(self):
        # Truth Table
        TopLeftEntry = VGroup(
            Tex("A", "B", font_size=DEFAULT_FONT_SIZE).shift(DOWN * 0.6),
            Tex("C", "D", font_size=DEFAULT_FONT_SIZE).shift(RIGHT * 0.6),
        )
        Kmap = IntegerTable(
            [[1, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 0], [1, 0, 0, 0]],
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
        expression = MathTex("e(A, B, C, D) = \Sigma_{m}(0, 2, 6, 8)")
        expression_simp = (
            MathTex(
                "\overline{A}\,C\,\overline{D}",
                "+",
                "\overline{B}\,\overline{C}\,\overline{D}",
            )
            .shift(RIGHT * (config["frame_x_radius"] + Kmap.get_right()) / 2)
            .scale(1)
        )

        """
        MINTERM GROUP
        """
        # Ones to be surrounded

        frame1_group = VGroup(
            Kmap.get_entries_without_labels()[3:4],
            Kmap.get_entries_without_labels()[7:8],
        )
        # frame2_group = VGroup(
        #     Kmap.get_entries_without_labels()[0:1],
        #     Kmap.get_entries_without_labels()[12:13],
        # )
        # frame3_group = VGroup(
        #     Kmap.get_entries_without_labels()[2:3],
        #     Kmap.get_entries_without_labe ls()[6:7],
        # )
        frame4_group = VGroup(
            Kmap.get_entries_without_labels()[0:1],
        )
        frame5_group = VGroup(
            Kmap.get_entries_without_labels()[12:13],
        )

        """
        MINTERM GROUP
        """
        frame1 = SurroundingRectangle(
            VGroup(frame1_group), color=RED, buff=0.3
        ).round_corners(radius=0.2)
        # frame2 = SurroundingRectangle(
        #     VGroup(frame2_group), color=GREEN, buff=0.3
        # ).round_corners(radius=0.2)
        # frame3 = SurroundingRectangle(
        #     VGroup(frame3_group), color=YELLOW, buff=0.3
        # ).round_corners(radius=0.2)
        frame4 = SurroundingRectangle(
            VGroup(frame4_group), color=BLUE, buff=0.3
        ).round_corners(radius=0.2)
        frame5 = SurroundingRectangle(
            VGroup(frame5_group), color=BLUE, buff=0.3
        ).round_corners(radius=0.2)

        self.play(Write(expression))
        self.wait()
        self.play(FadeOut(expression))

        self.wait()
        self.play(Kmap.create(), run_time=5)
        self.wait()

        # FRAME 1 ==========================================================
        self.play(Create(frame1))

        self.wait()
        self.play(
            Indicate(TopLeftEntry[0][0]),
            Indicate(Kmap.get_labels()[5][0]),
            Indicate(Kmap.get_labels()[6][0]),
        )

        self.wait()
        self.play(
            Indicate(TopLeftEntry[1][0]),
            Indicate(TopLeftEntry[1][1]),
            Indicate(Kmap.get_labels()[4][0]),
            Indicate(Kmap.get_labels()[4][1]),
        )

        self.wait()
        self.play(Write(expression_simp[0]))
        self.wait(1)

        # /FRAME 1 ==========================================================

        # FRAME 2 ==========================================================
        # self.play(Create(frame2))

        # self.wait()
        # self.play(
        #     Indicate(TopLeftEntry[0][0]),
        #     Indicate(Kmap.get_labels()[5][0]),
        #     Indicate(Kmap.get_labels()[6][0]),
        # )

        # self.wait()
        # self.play(
        #     Indicate(TopLeftEntry[1][1]),
        #     Indicate(Kmap.get_labels()[2][1]),
        #     Indicate(Kmap.get_labels()[3][1]),
        # )

        # self.wait()
        # self.play(Write(expression_simp[2]))
        # self.wait(1)

        # /FRAME 2 ==========================================================

        # FRAME 3 ==========================================================
        # self.play(Create(frame3))

        # self.wait()
        # self.play(
        #     Indicate(TopLeftEntry[0][0]),
        #     Indicate(Kmap.get_labels()[5][0]),
        #     Indicate(Kmap.get_labels()[6][0]),
        # )

        # self.wait()
        # self.play(
        #     Indicate(TopLeftEntry[1][0]),
        #     Indicate(TopLeftEntry[1][1]),
        #     Indicate(Kmap.get_labels()[3][0]),
        #     Indicate(Kmap.get_labels()[3][1]),
        # )

        # self.wait()
        # self.play(Write(expression_simp[4]))
        # self.wait()

        # /FRAME 3 ==========================================================

        # FRAME 4 ==========================================================
        self.play(Create(frame4))
        self.play(Create(frame5))

        self.wait()
        self.play(
            Indicate(TopLeftEntry[0][1]),
            Indicate(Kmap.get_labels()[5][1]),
            Indicate(Kmap.get_labels()[8][1]),
        )

        self.wait()
        self.play(
            Indicate(TopLeftEntry[1][0]),
            Indicate(TopLeftEntry[1][1]),
            Indicate(Kmap.get_labels()[1][0]),
            Indicate(Kmap.get_labels()[1][1]),
        )

        self.wait()
        self.play(Write(expression_simp[2]))
        self.wait()

        # /FRAME 4 ==========================================================

        # ENDDD
        self.play(
            Write(expression_simp[1]),
            # Write(expression_simp[3]),
            # Write(expression_simp[5]),
            FadeOut(frame1),
            # FadeOut(frame2),
            # FadeOut(frame3),
            FadeOut(frame4),
            FadeOut(frame5),
            FadeOut(Kmap),
        )
        self.play(expression_simp.animate.scale(1.4).move_to(ORIGIN))
        self.wait(2)
        self.play(FadeOut(expression_simp))

        """
        /KMAP ============================================================
        """

    def run_kmap6(self):
        # Truth Table
        TopLeftEntry = VGroup(
            Tex("A", "B", font_size=DEFAULT_FONT_SIZE).shift(DOWN * 0.6),
            Tex("C", "D", font_size=DEFAULT_FONT_SIZE).shift(RIGHT * 0.6),
        )
        Kmap = IntegerTable(
            [[1, 0, 0, 0], [1, 1, 0, 1], [0, 0, 0, 0], [1, 1, 0, 0]],
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
        expression = MathTex("f(A, B, C, D) = \Sigma_{m}(0, 4 , 5, 6, 8, 9)")
        expression_simp = (
            MathTex(
                "\overline{A}\,B\,\overline{C}",
                "+",
                "\overline{B}\,\overline{C}\,\overline{D}",
                "+",
                "A\,\overline{B}\,\overline{C}",
                "+",
                "\overline{A}\,B\,\overline{D}",
            )
            .shift(RIGHT * (config["frame_x_radius"] + Kmap.get_right()) / 2)
            .scale(0.7)
        )

        """
        MINTERM GROUP
        """
        # Ones to be surrounded

        frame1_group = VGroup(
            Kmap.get_entries_without_labels()[4:6],
        )
        frame2_group = VGroup(
            Kmap.get_entries_without_labels()[0:1],
        )
        frame3_group = VGroup(
            Kmap.get_entries_without_labels()[12:13],
        )
        frame4_group = VGroup(
            Kmap.get_entries_without_labels()[12:14],
        )
        frame5_group = VGroup(
            Kmap.get_entries_without_labels()[4:5],
        )
        frame6_group = VGroup(
            Kmap.get_entries_without_labels()[7:8],
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
            VGroup(frame3_group), color=GREEN, buff=0.3
        ).round_corners(radius=0.2)
        frame4 = SurroundingRectangle(
            VGroup(frame4_group), color=BLUE, buff=0.3
        ).round_corners(radius=0.2)
        frame5 = SurroundingRectangle(
            VGroup(frame5_group), color=YELLOW, buff=0.3
        ).round_corners(radius=0.2)
        frame6 = SurroundingRectangle(
            VGroup(frame6_group), color=YELLOW, buff=0.3
        ).round_corners(radius=0.2)

        self.play(Write(expression))
        self.wait()
        self.play(FadeOut(expression))

        self.wait()
        self.play(Kmap.create(), run_time=5)
        self.wait()

        # FRAME 1 ==========================================================
        self.play(Create(frame1))

        self.wait()
        self.play(
            Indicate(TopLeftEntry[0][0]),
            Indicate(TopLeftEntry[0][1]),
            Indicate(Kmap.get_labels()[6][0]),
            Indicate(Kmap.get_labels()[6][1]),
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

        # /FRAME 1 ==========================================================

        # FRAME 2 ==========================================================
        self.play(Create(frame2))
        self.play(Create(frame3))

        self.wait()
        self.play(
            Indicate(TopLeftEntry[0][1]),
            Indicate(Kmap.get_labels()[5][1]),
            Indicate(Kmap.get_labels()[8][1]),
        )

        self.wait()
        self.play(
            Indicate(TopLeftEntry[1][0]),
            Indicate(TopLeftEntry[1][1]),
            Indicate(Kmap.get_labels()[1][0]),
            Indicate(Kmap.get_labels()[1][1]),
        )

        self.wait()
        self.play(Write(expression_simp[2]))
        self.wait()

        # /FRAME 2 ==========================================================

        # FRAME 3 ==========================================================
        self.play(Create(frame4))

        self.wait()
        self.play(
            Indicate(TopLeftEntry[0][0]),
            Indicate(TopLeftEntry[0][1]),
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
        self.play(Write(expression_simp[4]))
        self.wait()

        # /FRAME 3 ==========================================================

        # FRAME 4 ==========================================================
        self.play(Create(frame5))
        self.play(Create(frame6))

        self.wait()
        self.play(
            Indicate(TopLeftEntry[0][0]),
            Indicate(TopLeftEntry[0][1]),
            Indicate(Kmap.get_labels()[6][0]),
            Indicate(Kmap.get_labels()[6][1]),
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

        # /FRAME 4 ==========================================================

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
            FadeOut(frame6),
            FadeOut(Kmap),
        )
        self.play(expression_simp.animate.scale(1.4).move_to(ORIGIN))
        self.wait(2)
        self.play(FadeOut(expression_simp))

        """
        /KMAP ============================================================
        """

    def run_kmap7(self):
        # Truth Table
        TopLeftEntry = VGroup(
            Tex("A", "B", font_size=DEFAULT_FONT_SIZE).shift(DOWN * 0.6),
            Tex("C", "D", font_size=DEFAULT_FONT_SIZE).shift(RIGHT * 0.6),
        )
        Kmap = IntegerTable(
            [[1, 0, 1, 1], [1, 1, 0, 1], [0, 0, 0, 0], [1, 1, 0, 0]],
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
        expression = MathTex("g(A, B, C, D) = \Sigma_{m}(2, 3, 4, 5, 6, 8, 9)")
        expression_simp = (
            MathTex(
                "\overline{A}\,B\,\overline{C}",
                "+",
                "A\,\overline{B}\,\overline{C}",
                "+",
                "\overline{A}\,\overline{B}\,C",
                "+",
                "\overline{A}\,B\,\overline{D}",
            )
            .shift(RIGHT * (config["frame_x_radius"] + Kmap.get_right()) / 2)
            .scale(0.7)
        )

        """
        MINTERM GROUP
        """
        # Ones to be surrounded

        frame1_group = VGroup(
            Kmap.get_entries_without_labels()[4:6],
        )
        frame2_group = VGroup(
            Kmap.get_entries_without_labels()[12:14],
        )
        frame3_group = VGroup(
            Kmap.get_entries_without_labels()[2:4],
        )
        frame4_group = VGroup(
            Kmap.get_entries_without_labels()[4:5],
        )
        frame5_group = VGroup(
            Kmap.get_entries_without_labels()[7:8],
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
        self.wait()
        self.play(FadeOut(expression))

        self.wait()
        self.play(Kmap.create(), run_time=5)
        self.wait()

        # FRAME 1 ==========================================================
        self.play(Create(frame1))

        self.wait()
        self.play(
            Indicate(TopLeftEntry[0][0]),
            Indicate(TopLeftEntry[0][1]),
            Indicate(Kmap.get_labels()[6][0]),
            Indicate(Kmap.get_labels()[6][1]),
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

        # /FRAME 1 ==========================================================

        # FRAME 2 ==========================================================
        self.play(Create(frame2))

        self.wait()
        self.play(
            Indicate(TopLeftEntry[0][0]),
            Indicate(TopLeftEntry[0][1]),
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
        self.play(Write(expression_simp[2]))
        self.wait(1)

        # /FRAME 2 ==========================================================

        # FRAME 3 ==========================================================
        self.play(Create(frame3))

        self.wait()
        self.play(
            Indicate(TopLeftEntry[0][0]),
            Indicate(TopLeftEntry[0][1]),
            Indicate(Kmap.get_labels()[5][0]),
            Indicate(Kmap.get_labels()[5][1]),
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

        # /FRAME 3 ==========================================================

        # FRAME 4 ==========================================================
        self.play(Create(frame4))
        self.play(Create(frame5))

        self.wait()
        self.play(
            Indicate(TopLeftEntry[0][0]),
            Indicate(TopLeftEntry[0][1]),
            Indicate(Kmap.get_labels()[6][0]),
            Indicate(Kmap.get_labels()[6][1]),
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

        # /FRAME 4 ==========================================================

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
        self.play(expression_simp.animate.scale(1.4).move_to(ORIGIN))
        self.wait()
        self.play(FadeOut(expression_simp))

        """
        /KMAP ============================================================
        """

    def tulis_judul(self, text):
        obe_judul = Text(
            text,
            font_size=36,
            color=TEAL,
        )
        self.play(Write(obe_judul))
        self.wait(2)
        self.play(FadeOut(obe_judul))

    def tulis_deskripsi_judul(self, text):
        obe_judul = Text(
            text,
            font_size=17,
            color=TEAL,
        )
        self.play(Write(obe_judul))
        self.wait(2)
        self.play(FadeOut(obe_judul))
        self.wait()


class KmapScene(AwalAnimation):
    def construct(self):

        RUN_JUDUL = 1
        RUN_SPESIFIKASI = 1
        RUN_FORMULASI = 1
        RUN_KMAP_1 = 1
        RUN_KMAP_2 = 1
        RUN_KMAP_3 = 1
        RUN_KMAP_4 = 1
        RUN_KMAP_5 = 1
        RUN_KMAP_6 = 1
        RUN_KMAP_7 = 1

        if RUN_JUDUL:
            self.run_judul()
        if RUN_SPESIFIKASI:
            self.run_spesifikasi()
        if RUN_FORMULASI:
            self.tulis_judul("FORMULASI")
            self.tulis_deskripsi_judul(
                "setiap digit BCD akan menyalakan segmen-segmen yang sesuai untuk tampilan desimal.\n\nSebagai contoh, BCD 0011 merepresen-tasikan digit desimal 3,\n\nyang akan menyalakan segmen a, b, c, d, dan g. Tabel kebenaran\n\nini mengasumsikan bahwa sinyal logika 1 menyalakan seg-men\n\ndan sinyal logika 0 mematikan segmen. Beberapa tampilan seven-segment\n\nbekerja sebaliknya, di mana segmen menyala dengan sinyal logika 0.\n\nDalam kasus ini, keluaran dari decoder harus dikomplemenkan."
            )
            self.run_formulasi_tabel()

        self.tulis_judul("OPTIMISASI")

        if RUN_KMAP_1:
            self.run_kmap1()

        if RUN_KMAP_2:
            self.run_kmap2()

        if RUN_KMAP_3:
            self.run_kmap3()

        if RUN_KMAP_4:
            self.run_kmap4()

        if RUN_KMAP_5:
            self.run_kmap5()

        if RUN_KMAP_6:
            self.run_kmap6()

        if RUN_KMAP_7:
            self.run_kmap7()

        self.tulis_judul("Full Circuit")
        self.tulis_judul("Kesimpulan")
