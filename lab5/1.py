import re
text = input()
pattern = '^a.*b$'
if re.search(pattern, text):
    print("matches!")
else: print("nope!")

