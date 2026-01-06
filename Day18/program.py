import requests 
#pip install requests

def check_status(url):
  if not url.startswith("http"):
    url=f"https://{url}"

  try:
    response = request.get(url, timeout=3)
    print(f"URL: {url}")
    print(f"Status Code: {response.status_code}")
    if response.status_code==200:
      print("success (200 OK)!")
    else:
      print("failed or redirected.")
  except request.exceptions.RequestException:
    print("Not connect or request time out :")

target_url= input("Enter a website URL : ")
check_status(target_url)
