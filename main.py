import requests
url = "https://s3.amazonaws.com/tcmg476/http_access_log"

r = requests.get(url, stream = True)

with open("python.txt","wb") as textfile:
   for chunk in r.iter_content(chunk_size=1024):

       if chunk:
           textfile.write(chunk)
result={
"total_requests":0,
"past_year_data":0,
}

file = open("python.txt")

for line in file:
   if(len(line)>=56):
       result["total_requests"]+=1
       data=line.split()
       date = data[3][1::].split(':')
       


print(result)
