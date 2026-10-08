import re

# Sample text containing all required patterns
text = "Call John at 9876543210 or 9123456789. Meeting is on 15/08/2024. Reach us at contact@example.com or support@test.org."

print("Original Text:\n", text)
print("-" * 50)

# 1. Check whether the text starts with 'Call'
starts_with_call = bool(re.match(r"^Call\b", text))
print("1. Starts with 'Call':", starts_with_call)

# 2. Find the first date (DD/MM/YYYY or DD-MM-YYYY)
first_date = re.search(r"\b\d{2}[/-]\d{2}[/-]\d{4}\b", text)
print("2. First date:", first_date.group() if first_date else "Not found")

# 3. Find all mobile numbers (10-digit numbers)
mobile_numbers = re.findall(r"\b\d{10}\b", text)
print("3. Mobile numbers:", mobile_numbers)

# 4. Find all e-mail IDs
email_ids = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
print("4. Email IDs:", email_ids)

# 5. Find all capitalized words
capitalized_words = re.findall(r"\b[A-Z][a-z]*\b", text)
print("5. Capitalized words:", capitalized_words)

# 6. Change the date format (from DD/MM/YYYY to YYYY-MM-DD)
changed_date_text = re.sub(
    r"\b(\d{2})/(\d{2})/(\d{4})\b", r"\3-\2-\1", text
)
print("6. Text with reformatted date:\n  ", changed_date_text)

# 7. Hide/mask the phone numbers
masked_text = re.sub(r"\b\d{10}\b", "XXXXXXXXXX", text)
print("7. Text with hidden phone numbers:\n  ", masked_text)