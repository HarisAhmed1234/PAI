import re

text = "The meeting is scheduled on 12/09/2023, and the project starts on 2023-09-12. Another meeting will be on Sep 12, 2023."

dates = re.findall(r'(\d{2}/\d{2}/\d{4})|(\d{4}-\d{2}-\d{2})|([A-Za-z]{3} \d{2}, \d{4})', text)
flat_dates = [date for group in dates for date in group if date]
print(flat_dates)
