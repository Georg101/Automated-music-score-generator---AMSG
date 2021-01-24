import re


f = open("notes.score", "r")
read = f.read()



text = read
if re.search(r"ch", text):
    print("Match found")
else:
    print("Match not found")

if re.search(r"dc", text):
    print("Match found")
else:
    print("Match not found")

if re.search(r"cd", text):
    print("Match found")
else:
    print("Match not found")

if re.search(r"hc", text):
    print("Match found")
else:
    print("Match not found")
