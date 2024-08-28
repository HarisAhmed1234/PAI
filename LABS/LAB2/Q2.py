def check_last_letter_iterative(s):
    vowels = 'aeiouAEIOU'
    last_char = ''
    
    for char in s:
        if char.isalpha():
            last_char = char
    
    if last_char in vowels:
        return f"The last letter '{last_char}' is a vowel."
    elif last_char:
        return f"The last letter '{last_char}' is a consonant."
    else:
        return "No alphabetic characters found."

user_input = input("Enter your string: ")
print(check_last_letter_iterative(user_input))
