import json


def json_to_markdown(json_data):
    markdown_content = []

    for question in json_data.get("soal", []):
        nomor = question.get("nomor", "No number")
        soal_cerita = question.get("soalCerita", {}).get("text", "")
        soal_text = question.get("soal", {}).get("text", "")
        soal_image_urls = question.get("soalCerita", {}).get("imageUrls", [])
        options = question.get("opsiSoal", [])

        markdown_content.append(f"### Question {nomor}\n")

        if soal_cerita:
            markdown_content.append(f"**Story:** {soal_cerita}\n")

        for url in soal_image_urls:
            markdown_content.append(f"![]({url})\n")

        markdown_content.append(f"**Question:** {soal_text}\n")

        markdown_content.append("**Options:**\n")
        for idx, option in enumerate(options, start=1):
            option_text = option.get("text", "")
            option_image_urls = option.get("imageUrls", [])
            markdown_content.append(f"- {idx}. {option_text}")
            for url in option_image_urls:
                markdown_content.append(f"![]({url})\n")

        markdown_content.append("\n")

    return "\n".join(markdown_content)


input_file = "input.json"
output_file = "output.md"

with open(input_file, "r") as f:
    data = json.load(f)


markdown_output = json_to_markdown(data)


with open(output_file, "w") as f:
    f.write(markdown_output)

print(f"Markdown output has been saved to {output_file}")
