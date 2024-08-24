w = input("Enter a word: ")

rev_w = ""
for i in range(len(w) - 1, -1, -1):
    rev_w += w[i]

print("Reversed word:", rev_w)
