import re

sentence = "Start a sentence and then bring it to an end"

pattern = re.compile(r"[A-Z][a-z]+")
matches = pattern.finditer(sentence)

for match in matches:
    print(match)