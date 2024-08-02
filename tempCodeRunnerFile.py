import requests
a = "}@@zb"
url = "https://d1rov3aw0q2u2y.cloudfront.net/?"
for j in range(ord('0'),ord("z")):
	a=chr(j)+a
	r = requests.get(url+a)
	if('Wrong' in r.text):
		continue
	else:
		print("Finish")
		print(chr(j))
		break