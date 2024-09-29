from manim import *


class PresentasiOperasiMatriks(Scene):
    def construct(self):
        self.setup_colors()  # Function to set consistent colors
        self.show_introduction()
        self.show_matrix_definition("A", [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3)
        self.perform_and_show_obe(
            "A",
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [
                ("H_{12(-3)}", [[-11, -13, -15], [4, 5, 6], [7, 8, 9]]),
                ("K_{3(2)}", [[-11, -13, -30], [4, 5, 12], [7, 8, 18]]),
                ("K_{12}", [[-13, -11, -30], [5, 4, 12], [8, 7, 18]]),
            ],
        )
        self.show_equivalent_matrix("A", [[-13, -11, -30], [5, 4, 12], [8, 7, 18]], "C")
        self.show_matrix_rank("A", [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2)
        self.calculate_determinant_sarrus("A", [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

        self.show_matrix_definition(
            "B", [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 4
        )
        self.perform_and_show_obe(
            "B",
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
            [
                (
                    "H_{12(2)}",
                    [[11, 14, 17, 20], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
                ),
                (
                    "H_{43(-1)}",
                    [[11, 14, 17, 20], [5, 6, 7, 8], [9, 10, 11, 12], [4, 4, 4, 4]],
                ),
                (
                    "H_{32(-2)}",
                    [[11, 14, 17, 20], [5, 6, 7, 8], [-1, -2, -3, -4], [4, 4, 4, 4]],
                ),
            ],
        )

        self.show_equivalent_matrix(
            "B", [[11, 14, 17, 20], [5, 6, 7, 8], [-1, -2, -3, -4], [4, 4, 4, 4]], "D"
        )
        self.show_matrix_rank(
            "B", [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 2
        )
        self.calculate_determinant_cofactor(
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        )

    def setup_colors(self):
        self.title_color = BLUE
        self.matrix_color = YELLOW
        self.highlight_color = RED
        self.explanation_color = TEAL
        self.arrow_color = PINK

    def show_introduction(self):
        title = Text("Presentasi Operasi Matriks", font_size=48, color=self.title_color)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        members = Text(
            "Kelompok 1: \n\n- Muchammad Yuda Tri Ananda \n\n- Muhammad Faza Aqila \n\n- Muhammad Izzat Fauzan Putra Arya",
            font_size=36,
            color=self.explanation_color,
        )
        self.play(Write(members))
        self.wait(2)
        self.play(FadeOut(members))

    def show_matrix_definition(self, matrix_name, matrix_data, size):
        title = Text(f"Matrix {size}x{size}", font_size=40, color=GREEN)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        matrix_label = Text(
            f"Diberikan sebuah matrix {matrix_name} berukuran {size}x{size}:",
            font_size=36,
            color=ORANGE,
        ).to_edge(UP)
        matrix = Matrix(
            matrix_data,
            element_to_mobject_config={"color": self.matrix_color},
        )
        matrix_name_text = Text(
            f"{matrix_name} =", font_size=30, color=self.matrix_color
        ).next_to(matrix, LEFT)
        self.play(Write(matrix_label), Write(matrix_name_text), Write(matrix))
        self.wait(2)
        self.play(FadeOut(matrix_label), FadeOut(matrix_name_text), FadeOut(matrix))

    def perform_and_show_obe(self, matrix_name, original_matrix, operations):
        title = Text(
            "Dengan melakukan operasi baris elementer sebanyak 3 kali \n\n maka dapat dilakukan dengan cara berikut",
            font_size=25,
            color=self.explanation_color,
        )
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        current_matrix = original_matrix
        for operation_name, result_matrix in operations:
            operation_title = MathTex(
                f"{operation_name}({matrix_name})", font_size=36, color=self.title_color
            )
            self.play(Write(operation_title))
            self.wait(1)
            self.play(operation_title.animate.to_edge(UP).move_to(UP * 3.5))

            matrix_obj = Matrix(
                current_matrix, element_to_mobject_config={"color": self.matrix_color}
            )
            self.play(Write(matrix_obj))
            self.wait(1)

            new_matrix_obj = Matrix(
                result_matrix, element_to_mobject_config={"color": self.matrix_color}
            )
            self.play(Transform(matrix_obj, new_matrix_obj))
            self.wait(1)

            self.play(FadeOut(matrix_obj))
            self.play(operation_title.animate.move_to(ORIGIN))
            self.play(FadeOut(operation_title))
            current_matrix = result_matrix

    def show_equivalent_matrix(
        self, original_matrix_name, equivalent_matrix, equivalent_matrix_name
    ):
        title = Text(
            "Maka Didapatkan",
            font_size=25,
            color=self.explanation_color,
        )
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        explanation = MathTex(
            r"\text{Operasi OBE}(",
            f"{original_matrix_name}",
            r") = ",
            f"{equivalent_matrix_name}",
            r"\text{, dengan matriks }",
            f"{equivalent_matrix_name}",
            r"\text{ adalah}\\",
            r"\text{matriks yang ekuivalen} \approx \text{matriks }",
            f"{original_matrix_name}",
            font_size=36,
            color=self.title_color,
        )

        self.play(Write(explanation))
        self.wait(1)
        self.play(explanation.animate.to_edge(UP).move_to(UP * 3.5))

        matrix_obj = Matrix(
            equivalent_matrix, element_to_mobject_config={"color": self.matrix_color}
        )
        matrix_name_text = Text(
            f"{equivalent_matrix_name} =", font_size=30, color=self.matrix_color
        ).next_to(matrix_obj, LEFT)
        equivalent_text = MathTex(
            r"\approx \text{matriks }",
            f"{original_matrix_name}",
            font_size=30,
            color=self.matrix_color,
        ).next_to(matrix_obj, RIGHT)

        self.play(Write(matrix_name_text))
        self.play(Write(matrix_obj))
        self.play(Write(equivalent_text))
        self.wait(1)

        self.play(
            FadeOut(matrix_obj), FadeOut(matrix_name_text), FadeOut(equivalent_text)
        )
        self.play(explanation.animate.move_to(ORIGIN))
        self.play(FadeOut(explanation))

    def show_matrix_rank(self, matrix_name, matrix_data, rank):
        title = Text(f"Rank Matriks {matrix_name}", font_size=40, color=GREEN)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        title = (
            Text(f"Rank Matrix {matrix_name}")
            .set_color(self.explanation_color)
            .move_to(UP * 3.5)
        )

        m01 = Matrix(matrix_data)
        m02 = Matrix([[1, 2, 3], [0, -3, -6], [7, 8, 9]]).move_to([4, 1.5, 0])
        m03 = Matrix([[1, 2, 3], [0, -3, -6], [0, -6, -12]]).move_to([-4, -2.5, 0])
        m04 = Matrix([[1, 2, 3], [0, -3, -6], [0, 0, 0]]).move_to([4, -2.5, 0])
        matrices = [m01, m02, m03, m04]
        for m in matrices:
            m.get_brackets().set_color(self.matrix_color)

        eq1 = MathTex(r"H_{21(-4)}").set_color(self.explanation_color)
        eq2 = MathTex(r"H_{31(-7)}").set_color(self.explanation_color)
        eq3 = MathTex(r"H_{32(-2)}").set_color(self.explanation_color)

        arrow_1 = LabeledArrow(
            start=[-1.7, 1.5, 0],
            end=[1.7, 1.5, 0],
            color=self.arrow_color,
            tip_shape=StealthTip,
            label=eq1,
        )
        arrow_2 = LabeledArrow(
            start=[1.7, 0.5, 0],
            end=[-1.7, -1.5, 0],
            color=self.arrow_color,
            tip_shape=StealthTip,
            label=eq2,
        )
        arrow_3 = LabeledArrow(
            start=[-1.7, -2.5, 0],
            end=[1.7, -2.5, 0],
            color=self.arrow_color,
            tip_shape=StealthTip,
            label=eq3,
        )

        self.add(title)
        self.play(Create(m01))
        self.play(m01.animate.move_to([-4, 1.5, 0]))
        self.play(GrowArrow(arrow_1))
        self.play(Create(m02))
        self.wait(2)
        b1 = SurroundingRectangle(m02.get_rows()[1], color=self.matrix_color)
        b2 = SurroundingRectangle(m02.get_rows()[2], color=self.matrix_color)
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
        rank_text = Text(
            f"Rank: {rank}", font_size=30, color=self.matrix_color
        ).next_to(title, RIGHT)
        self.play(Write(rank_text))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(rank_text))

    def calculate_determinant_sarrus(self, matrix_name, matrix_data):
        title = Text(
            f"Determinan Matriks {matrix_name} dengan Metode Sarrus",
            font_size=36,
            color=self.title_color,
        )
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        title = (
            Text(
                f"Determinan Matriks {matrix_name} dengan Metode Sarrus",
                font_size=36,
                color=self.title_color,
            )
            .to_edge(UP)
            .move_to(UP * 3.5)
        )
        self.add(title)

        matrix = Matrix(
            matrix_data, element_to_mobject_config={"color": self.highlight_color}
        )
        self.play(Write(matrix))
        self.wait(1)
        self.play(FadeOut(matrix))

        a, b, c = matrix_data[0]
        d, e, f = matrix_data[1]
        g, h, i = matrix_data[2]

        sarrus_formula = MathTex(
            r"|",
            matrix_name,
            r"| = (",
            f"{a}",
            r" \cdot ",
            f"{e}",
            r" \cdot ",
            f"{i}",
            r") + (",
            f"{b}",
            r" \cdot ",
            f"{f}",
            r" \cdot ",
            f"{g}",
            r") + (",
            f"{c}",
            r" \cdot ",
            f"{d}",
            r" \cdot ",
            f"{h}",
            r") - (",
            f"{g}",
            r"\cdot ",
            f"{e}",
            r" \cdot ",
            f"{c}",
            r") + (",
            f"{h}",
            r" \cdot ",
            f"{f}",
            r" \cdot ",
            f"{a}",
            r") + (",
            f"{i}",
            r" \cdot ",
            f"{d}",
            r" \cdot ",
            f"{b}",
            ")",
            color=PURPLE,
        ).scale(0.8)
        self.play(Write(sarrus_formula))
        self.wait(2)

        determinant = (
            (a * e * i)
            + (b * f * g)
            + (c * d * h)
            - (g * e * c)
            - (h * f * a)
            - (i * d * b)
        )

        determinant_result = MathTex(
            rf"|{matrix_name}| = {determinant}", color=self.matrix_color
        ).scale(1.2)
        self.play(Transform(sarrus_formula, determinant_result))
        self.wait(2)
        self.play(FadeOut(sarrus_formula))
        self.play(title.animate.move_to(ORIGIN))
        self.play(FadeOut(title))

    def calculate_determinant_cofactor(self, matrix):
        # Membuat matriks
        matrix_mob = Matrix(matrix)
        self.play(Write(matrix_mob))
        self.wait()

        # Menjelaskan ekspansi kofaktor
        explanation = Text(
            "Kita akan menghitung determinan menggunakan ekspansi kofaktor sepanjang baris pertama",
            font_size=24,
        ).set_color(self.explanation_color)
        self.play(Write(explanation))
        self.wait(2)
        self.play(FadeOut(explanation))

        # Menjelaskan matriks kofaktor
        explanation_cofactor = Text(
            "Matriks kofaktor terdiri dari semua kofaktor Cij", font_size=24
        ).set_color(self.explanation_color)
        formula_cofactor = MathTex(
            r"C_{ij} = (-1)^{i+j} M_{ij}", font_size=24
        ).set_color(self.explanation_color)
        description_cofactor = Text(
            "dimana Mij adalah minor (determinan submatriks)", font_size=24
        ).set_color(self.explanation_color)

        group = VGroup(
            explanation_cofactor, formula_cofactor, description_cofactor
        ).arrange(DOWN)
        self.play(Write(group))
        self.wait(3)
        self.play(FadeOut(group))

        # Menyoroti setiap elemen baris pertama dan kofaktornya
        for i in range(4):
            # Menyoroti elemen saat ini
            element = matrix_mob.get_entries()[i]
            self.play(element.animate.set_color(self.highlight_color))

            # Membuat dan menampilkan matriks kofaktor
            cofactor_matrix = [row[:i] + row[i + 1 :] for row in matrix[1:]]
            cofactor_mob = Matrix(cofactor_matrix).scale(0.7)
            cofactor_mob.next_to(matrix_mob, RIGHT)
            self.play(Write(cofactor_mob))

            # Menjelaskan kofaktor saat ini
            explanation_cofactor = (
                Text(f"Kofaktor C{1}{i+1}", font_size=24)
                .set_color(self.explanation_color)
                .next_to(cofactor_mob, UP)
            )
            self.play(Write(explanation_cofactor))

            # Menampilkan tanda kofaktor
            sign = (-1) ** (i + 1)
            sign_text = (
                MathTex(r"(-1)^{" + f"{1}+{i+1}" + r"} = " + f"{sign}", font_size=24)
                .set_color(self.explanation_color)
                .next_to(cofactor_mob, DOWN)
            )
            self.play(Write(sign_text))

            # Menghitung dan menampilkan minor
            minor_value = self.calculate_determinant_3x3(cofactor_matrix)
            minor_text = (
                Text(f"Minor M{1}{i+1} = {minor_value}", font_size=24)
                .set_color(self.explanation_color)
                .next_to(sign_text, DOWN)
            )
            self.play(Write(minor_text))

            # Menampilkan perhitungan kofaktor
            cofactor_value = sign * minor_value
            cofactor_text = (
                Text(
                    f"C{1}{i+1} = {sign} * {minor_value} = {cofactor_value}",
                    font_size=24,
                )
                .set_color(self.explanation_color)
                .next_to(minor_text, DOWN)
            )
            self.play(Write(cofactor_text))

            # Menampilkan perkalian dengan elemen matriks
            result = matrix[0][i] * cofactor_value
            result_text = (
                Text(f"{matrix[0][i]} * {cofactor_value} = {result}", font_size=24)
                .set_color(self.explanation_color)
                .next_to(cofactor_text, DOWN)
            )
            self.play(Write(result_text))

            self.wait(2)

            # Membersihkan untuk iterasi berikutnya
            self.play(
                FadeOut(cofactor_mob),
                FadeOut(explanation_cofactor),
                FadeOut(sign_text),
                FadeOut(minor_text),
                FadeOut(cofactor_text),
                FadeOut(result_text),
                element.animate.set_color(WHITE),
            )

        # Menampilkan jumlah akhir
        final_sum = sum(
            [
                matrix[0][i]
                * (-1) ** (i + 1)
                * self.calculate_determinant_3x3(
                    [row[:i] + row[i + 1 :] for row in matrix[1:]]
                )
                for i in range(4)
            ]
        )
        final_text = (
            Text(f"Determinan = {final_sum}")
            .set_color(self.explanation_color)
            .next_to(matrix_mob, DOWN)
        )
        self.play(Write(final_text))
        self.wait(2)

    def calculate_determinant_3x3(self, matrix):
        return (
            matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
            - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
            + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
        )


# Untuk menjalankan skrip ini, gunakan perintah:
# manim -pql presentasi_operasi_matriks.py PresentasiOperasiMatriks
