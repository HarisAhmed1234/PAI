import re

text = "Please contact us at support@example.com or sales@example.org for further information."

emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
print(emails)
