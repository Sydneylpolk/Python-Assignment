
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
for line in file:
   if(len(line)>=56):
       result["total_requests"]+=1
       data=line.split()
       date = data[3][1::].split(':')
       if not (date_day == date[0]):
           date_day = date[0]
           days += 1
           if(days%7 == 0):
               week = date_day
       if date[0] in result["per_day"]:
           result["per_day"][date[0]]+=1
       else:
           result["per_day"][date[0]]=0
      
       if week in result["per_week"]:
           result["per_week"][week]+=1
       else:
           result["per_week"][week] = 0
       month = date[0][3::]
       if month not in months_done:
           file_name = month[:3:]+month[4::]
           if(len(file_name)) == 7:
               month_file = open(month[:3:]+month[4::]+".txt",'w')
               print(file_name)
           months_done.append(month)
       month_file.write(line)
       if month in result["per_month"]:
           result["per_month"][month]+=1
       else:
           result["per_month"][month]=0
       if data[-2][0]=="4":
           result["not_successful"]+=1
       if data[-2][0]=="3":
           result["redirected_elsewhere"]+=1
       if data[6] in result["request_frequency"]:
           result["request_frequency"][data[6]]+=1
       else:
           result["request_frequency"][data[6]]=1
