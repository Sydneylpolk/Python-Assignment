import requests
url = "https://s3.amazonaws.com/tcmg476/http_access_log"

r = requests.get(url, stream = True)

with open("python.txt","wb") as textfile:
   for chunk in r.iter_content(chunk_size=1024):

   #writing one chunk at a time to pdf file
       if chunk:
           textfile.write(chunk)
#creates a dictionary called result
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
#creating lists for date_day and day
#parsing the file for the criteria in the read me. 
#If the criteria is found in the line, it adds one to the vairable
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
        #this code checks to see if the number 4 or 3 are in the code area to decide if it has been redirected or not successful. Ex: Error 404 (not_successful)
       if data[-2][0]=="4":
           result["not_successful"]+=1
       if data[-2][0]=="3":
           result["redirected_elsewhere"]+=1
       if data[6] in result["request_frequency"]:
           result["request_frequency"][data[6]]+=1
       else:
           result["request_frequency"][data[6]]=1

#This code is used to creat the most/least frequent requested files.           
maxm=result["request_frequency"]["index.html"]
minm=result["request_frequency"]["index.html"]
maxlist=["index.html"]
minlist=["index.html"]
for i in result["request_frequency"]:
   if result["request_frequency"][i] > maxm:
       maxm = result["request_frequency"][i]
       maxlist=[i]
   if result["request_frequency"][i] < minm:
       minm = result["request_frequency"][i]
       minlist=[i]
  
   if result["request_frequency"][i] == maxm:
       maxlist.append(i)
  
   if result["request_frequency"][i] == minm:
       minlist.append(i)

result["most_requested"]=[maxm,maxlist]
result["least_requested"]=[minm,minlist]

print(result)
