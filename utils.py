def print_text_with_indent(text):
    text = text.split("\n")

    for line in [">"+x for x in text]:
        print(line)