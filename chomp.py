import requests
import re

print("enter starting point:")
urlinput = input()
r = requests.get(urlinput)
with open("sitecode.html", "a") as file:
    file.write(r.text[:1000000000])
    print(urlinput+ "done")
with open("test3.html", "r") as file:
    link_pattern = r'https?://\S+'
    content=file.read()
    matches = re.findall(link_pattern, content)
    print(matches)
