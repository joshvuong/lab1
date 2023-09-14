import requests

print(requests.__version__)

resp = requests.get("https://raw.githubusercontent.com/joshvuong/lab1/master/lab1.py")

f = open('file1.txt', 'w')
f.write(resp.text)

print(resp.text)
