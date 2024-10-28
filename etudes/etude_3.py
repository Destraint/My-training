file = input("""Напиши название файла (не забудь про нужное тебе расширение):
""")
text = open(file, "w")
lines = []
print(f"Напишите текст, он появится в файле {file}:")
while True:
    word = input()
    if word == "end":
        break
    lines.append(word)
word = "\n".join(lines)
text.writelines(word)
text.close()
