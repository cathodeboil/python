import requests
import re

print("enter starting point:")
urlinput = input()
r = requests.get(urlinput)
with open("sitecode.html", "a") as file:
    file.write(r.text[:1000000000])
    print(urlinput+ "done")
with open("sitecode.html", "r") as file:
    link_pattern = r'https?://\S+'
    content=file.read()
    matches = list(re.findall(link_pattern, content))
    print(matches)
    with open ("list.txt", "a") as file:
        for items in matches:
            file.write('%s\n' %items)
