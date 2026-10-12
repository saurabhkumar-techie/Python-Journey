import re
text = "The quick brown fox jumps over the lazy dog."
# https://regexr.com/

# Search for a pattern
# match = re.search("brown", text)
# print(match)
# if match:
#     print("Match found!")
#     print("Start index:", match.start())
#     print("End index:", match.end())

# Find all occurrences of a pattern
# matches = re.findall("the", text, re.IGNORECASE) # Case-insensitive search
# print("Matches:", matches)

new_text = re.sub("fox", "cat", text)
print("New text:", new_text)