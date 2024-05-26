import re

input_text = ""

while True:
    try:
        line = input()
        if line .strip() == "":
            break
        input_text += line + "\n"
    except EOFError:
        break

pattern = r'\b[A-Z0-9][a-zA-Z0-9]*\b'
match = re.findall(pattern, input_text)

uniques_words = set(match)
result = len(uniques_words)

print(result)