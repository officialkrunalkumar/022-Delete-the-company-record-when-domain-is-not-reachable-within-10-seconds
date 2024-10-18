import requests
import os

def main(event):
  
  token = os.getenv("RevOps")
  cId = event.get("inputFields").get("cId")
  
  url = f"https://api.hubapi.com/crm/v3/objects/companies/{cId}"
  
  headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
  }
  
  response = requests.delete(url, headers=headers)
  