
import requests
url = "https://s3.amazonaws.com/tcmg476/http_access_log"

r = requests.get(url, stream = True)

with open("python.txt","wb") as textfile:
   for chunk in r.iter_content(chunk_size=1024):

   #writing one chunk at a time to pdf file
       if chunk:
           textfile.write(chunk)
result={
"total_requests":0,
"per_day":{},
"per_week":{},
"per_month":{},
"not_successful":0,
"redirected_elsewhere":0,
"request_frequency":{},
"most_requested":[0,[]], #max requests/list of all files containing the same number of requests
"least_requested":[0,[]] #min requests/list of all files containing the smae number of requests.
}
file = open("python.txt")

date_day = None
days = 0
week = None
months_done = []
