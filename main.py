
import requests
url = "https://s3.amazonaws.com/tcmg476/http_access_log"

r = requests.get(url, stream = True)
