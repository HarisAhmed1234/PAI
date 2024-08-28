def transform_url(input_url):
    if input_url.startswith("http://www."):
        main_part = input_url[len("http://www."):]
        formatted_url = main_part + ".com"
        return formatted_url
    else:
        return "The URL must start with 'http://www.'."

user_input = input("Enter your URL starting with 'http://www.': ")
result = transform_url(user_input)

print(result)
