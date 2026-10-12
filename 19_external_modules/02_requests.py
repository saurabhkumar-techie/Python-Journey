import requests

r = requests.get('https://api.github.com/users/codewithharry')

with open("codewithharry.txt", "w") as f:
    f.write(r.text)