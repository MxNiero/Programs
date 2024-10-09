import codecs
import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html_file = file.read()
        result = []

        cleaned_text = re.sub(r'<[^>]+>', '', html_file)
        cleaned_text = cleaned_text.replace("\n", "")
        cleaned_text = cleaned_text.split(" ")

        for item in cleaned_text:
            if item != '':
                result.append(item)
        cleaned_text = " ".join(result)

        print(cleaned_text)

    with open(result_file, 'w', encoding='utf-8') as file:
        file.write(cleaned_text)


delete_html_tags("draft.html", "cleaned.html")
