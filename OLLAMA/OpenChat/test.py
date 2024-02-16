import requests
import json

url= "http://localhost:11434/api/generate"

headers = {
    'Content-Type' : 'application/json'
}


data = {
    "model": "llama2",
    "prompt": "Why is the sky blue?"
}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    print(response.text)

else:
    print("Error:", response.status_code, response.text)