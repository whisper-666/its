import requests
user = input("[?] Username : ")
url = "https://its.whisper666.repl.co/user="+user
whisper=requests.get(url).json()
if "Done Send 10 Followers To "+user in whisper:
 print("[+] Done Send 10 Followers To "+user)
else:
 print(whisper)


