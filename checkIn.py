import http.client

conn = http.client.HTTPSConnection("dujiao.huiyan-ai.cn")
payload = ''
headers = {
   'Authorization': 'Bearer eyJUeXBlIjoiSnd0IiwidHlwIjoiSldUIiwiYWxnIjoiSFMyNTYifQ.eyJyb290IjpmYWxzZSwibmFtZSI6bnVsbCwiYXZhdGFyIjoiaHR0cHM6Ly9taW5pb3MuaHVpeWFuLWFpLmNuL2ltYWdlL3RvdXhpYW5nLnBuZyIsImlkIjoxNzcwNjQyMjYzMjc2MzA2NDM0LCJleHAiOjE3MTE1OTM3ODcsInR5cGUiOm51bGx9.ZKI_uYg0moQpygGjkN5OMuADNlhoXqtwmByZZKXQLww',
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
