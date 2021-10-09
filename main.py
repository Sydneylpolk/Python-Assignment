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
  
"total":0,
   
"day":{},
   
"week":{},
   
"month":{},
   
"non_successful":0,
   
"redirected":0,
   
"frequency":{},
   
#max requests/list of all files containing the same number of requests   
"highest_requested":[0,[]], 

#min requests/list of all files containing the smae number of requests.
"lowest_requested":[0,[]] 
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
       result["total"]+=1
       data=line.split()
       date = data[3][1::].split(':')
         
       if not (date_day == date[0]):
           date_day = date[0]
           days += 1
         
           if(days%7 == 0):
               week = date_day
               
       if date[0] in result["day"]:
           result["day"][date[0]]+=1
       else:
           result["day"][date[0]]=0
      
       if week in result["week"]:
           result["week"][week]+=1
       else:
           result["week"][week] = 0
       month = date[0][3::]
      
       if month not in months_done:
           file_name = month[:3:]+month[4::]
         
           if(len(file_name)) == 7:
               month_file = open(month[:3:]+month[4::]+".txt",'w')
               print(file_name)
           months_done.append(month)
       month_file.write(line)
      
       if month in result["month"]:
           result["month"][month]+=1
       else:
           result["month"][month]=0
            
        #this code checks to see if the number 4 or 3 are in the code area to decide if it has been redirected or not successful. Ex: Error 404 (not_successful)
       if data[-2][0]=="4":
           result["non_successful"]+=1
         
       if data[-2][0]=="3":
           result["redirected"]+=1
            
       if data[6] in result["frequency"]:
           result["frequency"][data[6]]+=1
       else:
           result["frequency"][data[6]]=1

#This code is used to creat the most/least frequent requested files.           
maxm=result["frequency"]["index.html"]

minm=result["frequency"]["index.html"]

maxlist=["index.html"]

minlist=["index.html"]

for i in result["frequency"]:
   
   if result["frequency"][i] > maxm:
       maxm = result["frequency"][i]
       maxlist=[i]
      
   if result["frequency"][i] < minm:
       minm = result["frequency"][i]
       minlist=[i]
  
   if result["frequency"][i] == maxm:
       maxlist.append(i)
  
   if result["frequency"][i] == minm:
       minlist.append(i)

result["highest_requested"]=[maxm,maxlist]

result["lowest_requested"]=[minm,minlist]

print(result)
