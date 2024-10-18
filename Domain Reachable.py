import requests

def main(event):
  
  cId = event.get("inputFields").get("id")
  domain = event.get("inputFields").get("domain")
  reachable = True
  
  try:
    url = f"http://{domain}"
    response = requests.get(url, timeout=10)
    
    if response.status_code == 200:
      reachable = True
    else:
      reachable = False
      
  except:
    reachable = False
  
  return {
    "outputFields": {
      "cId": cId,
      "domain": domain,
      "reachable": reachable
    }
  }