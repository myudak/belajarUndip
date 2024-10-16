from manim import *


class KarnaughMap(Scene):
    def construct(self):
        # Title and Author
        title = Text("Design of a BCD–to–Seven-Segment Decoder").scale(0.75).to_edge(UP)
        self.play(Write(title))

        subtitle = Text("Universitas Diponegoro", font_size=24).next_to(title, DOWN)
        self.play(FadeIn(subtitle))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))
        self.wait(2)

        # Group Members
        group_title = Text("Kelompok D", font_size=30)
        members = BulletedList(
            "Muchammad Yuda Tri Ananda (24060124110142)",
            "Muhammad Alfaiq Rido Salafy (24060124140148)",
            "Naufal Rayan Attallah (24060124140148)",
            font_size=24,
        ).next_to(group_title, DOWN, aligned_edge=LEFT)

        self.play(FadeIn(group_title))
        self.play(FadeIn(members))

        self.wait(2)

        self.play(FadeOut(group_title), FadeOut(members))

        # Display Karnaugh Map for 'a' output
        km_title = Text("Karnaugh Map for a(A, B, C, D)").scale(0.6).shift(UP * 2)
        self.play(Write(km_title))

        # Create the K-map table
        kmap = (
            MathTable(
                [
                    [r"D \ C", "00", "01", "11", "10"],
                    ["00", "1", "1", "1", "1"],
                    ["01", "0", "1", "0", "0"],
                    ["11", "1", "1", "0", "1"],
                    ["10", "0", "1", "1", "1"],
                ],
                include_outer_lines=True,
            )
            .scale(0.7)
            .shift(DOWN * 0.5)
        )

        self.play(Create(kmap))

        # K-map groupings and logic
        grouping = MathTex(
            r"\overline{A}C + A\overline{B}\overline{C} + \overline{A}BD + \overline{A}\overline{B}\overline{D}"
        )
        grouping.next_to(kmap, DOWN, aligned_edge=LEFT).scale(0.6)
        self.play(Write(grouping))

        self.wait(2)
