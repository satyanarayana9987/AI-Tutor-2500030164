word =input("Enter a word: ") or "Python"

print("word:", word)
print("length=", len(word))

characters = list(word)

print("characters in the given word :", characters)
pairs=list(zip(characters, characters[1:]))

print("adjacent pairs:", pairs)