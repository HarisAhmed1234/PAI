def CountCharactersInTheFile(filename):
    try:
        with open(r'filename',"r") as filename:
            content= file.read()
            char_count= len(content)
            word_count=len(content.split())
            print("THE NUMBER OF CHARACTERS IN THE FILE IS: {char_count}")
            print("THE NUMBER OF WORDS IN THE FILE IS: {word_count}")
    except FileNotFoundError:
        print("No file founded bhai!")
    except Exception as e:
        print("UNEXPECTED ERROR BRO!: {e}")

filename="sample.txt"
CountCharactersInTheFile(filename)

