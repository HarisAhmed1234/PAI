import json
import os


def create_and_save_dict():
    dictionary = {}
    while True:
        name = input("Enter name (type 'done' when u want ti finish): ")
        if name.lower() == 'done':
            break
        try:
            age = int(input(f"Enter age for {name}: "))
            dictionary[name] = age
        except ValueError:
            print("Invalid input. Please enter a numeric value for age.")

    filename = 'people.json'
    try:
        with open(filename, 'w') as f_obj:
            json.dump(dictionary, f_obj, indent=4)
        print(f"Dictionary saved to {filename}")
    except IOError as e:
        print(f"Error writing to file: {e}")


def load_and_process_dict():
    filename = 'people.json'
    if not os.path.exists(filename):
        print(f"File {filename} does not exist.")
        return

    try:
        with open(filename, 'r') as f_obj:
            stu = json.load(f_obj)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error loading file: {e}")
        return

    print("Loaded Dictionary:", stu)

    if not stu:
        print("The dictionary is empty.")
        return

    max_age = max(stu.values())
    max_age_persons = [name for name, age in stu.items() if age == max_age]

    print(f"Person(s) with maximum age ({max_age}):", ', '.join(max_age_persons))

    same_age_count = sum(1 for age in stu.values() if age == max_age)

    if same_age_count > 1:
        print("Yes, there are other persons with the same maximum age.")
    else:
        print("No one else has the same age as the person with the maximum age.")


create_and_save_dict()
load_and_process_dict()
