import http.client

conn = http.client.HTTPSConnection("dujiao.huiyan-ai.cn")
payload = ''
headers = {
   'Authorization': 'Bearer eyJUeXBlIjoiSnd0IiwidHlwIjoiSldUIiwiYWxnIjoiSFMyNTYifQ.eyJyb290IjpmYWxzZSwibmFtZSI6IjE3NjA2NjcxMTAzIiwiYXZhdGFyIjoiaHR0cHM6Ly9taW5pb3MuaHVpeWFuLWFpLmNuL2ltYWdlL3RvdXhpYW5nLnBuZyIsImlkIjoxNzkwNTU3Njk4MjEyODU5OTA1LCJleHAiOjE3MTYzNDE5OTcsInR5cGUiOjF9.jDua3b2-V2lwUFctuAtNmfCR29jSyJ2urFusD8xgtMc',
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
   'Accept': '*/*',
   'Host': 'dujiao.huiyan-ai.cn',
   'Connection': 'keep-alive',
   'Cookie': 'sl-session=2kD1TPRD/mV+hVoVHI4FRA=='
}
conn.request("POST", "/api/user-signIn", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
