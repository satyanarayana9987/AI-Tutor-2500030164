# word level tokenization
text=input("Enter a Sentence: ") or "I love Learning Python."
print("text:", text)
tokens=text.split(" ")
print("tokens:", tokens)
print("length of tokens:", len(tokens))