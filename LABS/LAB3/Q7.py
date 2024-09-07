def replace_letter_in_file(filename, wrong_letter, correct_letter):
    try:
        with open(filename, 'r') as file:
            content = file.read()

        corrected_content = content.replace(wrong_letter, correct_letter)

        print("Original content:", content)
        print("Corrected content:", corrected_content)

        with open(filename, 'w') as file:
            file.write(corrected_content)

        print(f"File has been corrected.")

    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

replace_letter_in_file('replacement_needed.txt', 'I', 'U')
