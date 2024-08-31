def build_message(**info):
    message = "Below is the information the user provided:\n"
    for key, value in info.items():
        message += f"{key.capitalize()}: {value}\n"

    return message

def get_user_details():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    city = input("Enter your city: ")
    profession = input("Enter your profession: ")

    return build_message(name=name, age=age, city=city, profession=profession)

message = get_user_details()
print(message)
