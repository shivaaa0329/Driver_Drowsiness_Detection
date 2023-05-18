import requests
url = "https://www.fast2sms.com/dev/bulk"
payload = "sender_id=FSTSMS&message=AKULA SAI VENKATHA NAGA KARTHIK, Your Training fee amount 3000 has been received on 06-April-2022. Total fee amount - 5000, Total received amount - 3000, Total pending amount - 2000. Regards, Ramachandra College of Engineering&language=english&route=p&numbers=9491374442"
headers = {
'authorization': "QOXVBW5YTuaxgKGmAb1sPF6Mpz3cIylJEvnwLodS0kZ72iRC4H0IOCQueXWp9U6cnFBDL2Kvhxa3ASkP",
'Content-Type': "application/x-www-form-urlencoded",
'Cache-Control': "no-cache",
}
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
