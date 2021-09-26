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

months_done = []
for line in file:
   if(len(line)>=56):
       result["total_requests"]+=1
       data=line.split()
       date = data[3][1::].split(':')
         
month = date[0][3::]
if month not in months_done:
     file_name = month[:3:]+month[4::]
     if(len(file_name)) == 7:
        month_file = open(month[:3:]+month[4::]+".txt",'w')
print(file_name)

months_done.append(month)
month_file.write(line)

if month in result["past_6_month"]:
     result["past_6_month"][month]+=1
else:
     result["past_6_month"][month]=0
       


print(result)
