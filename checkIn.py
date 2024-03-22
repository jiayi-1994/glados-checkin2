import requests

url = "https://dujiao.huiyan-ai.cn/api/user-signIn"
headers = {
    "Authorization": "Bearer eyJUeXBlIjoiSnd0IiwidHlwIjoiSldUIiwiYWxnIjoiSFMyNTYifQ.eyJyb290IjpmYWxzZSwibmFtZSI6bnVsbCwiYXZhdGFyIjoiaHR0cHM6Ly9taW5pb3MuaHVpeWFuLWFpLmNuL2ltYWdlL3RvdXhpYW5nLnBuZyIsImlkIjoxNzcwNjQyMjYzMjc2MzA2NDM0LCJleHAiOjE3MTE1OTM3ODcsInR5cGUiOm51bGx9.ZKI_uYg0moQpygGjkN5OMuADNlhoXqtwmByZZKXQLww",
    "Content-Type": "application/json"
}
data = {
    "key1": "value1",
    "key2": "value2"
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())
