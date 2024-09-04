def replace_in_file(file_path, search_text, replace_text):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        modified_content = content.replace(search_text, replace_text)

        with open(file_path, 'w') as file:
            file.write(modified_content)

        print("Replacement complete.")
    
    except FileNotFoundError:
        print("No file founded bhai!")
    except Exception as e:
        print("UNEXPECTED ERROR BRO!: {e}")

replace_in_file('example.txt', 'old_word', 'new_word')
