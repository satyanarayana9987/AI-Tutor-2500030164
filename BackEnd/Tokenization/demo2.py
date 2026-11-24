text = input("Enter a Sentence: ") or "I love programming in Python."

print("length=", len(text))
print("characters in the given text :")
for ch in text:
    print(ch,end=",")