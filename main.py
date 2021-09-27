#This first command opens the downloaded log file needed to parse
file = open('http_access_log.txt','r') 
#This counts all of the total requests in the log file
count = 0 
#This counts all of the requests made in the last six months
Past_6_Months = 0

#this converts the text in the log to a variable that you can use and reference
April = "Apr"
May = "May"
June = "Jun"
July = "Jul"
August = "Aug"
September = "Sep"
October = "Oct"
Year = "1995"

#takes the file and separates it line by line
Content = file.read()
List1 = Content.split('\n')


#This goes through each request line to add into the count if it suits my criteria 
for lines in List1:
    if lines:
        
        if April in List1[count]:
            Past_6_Months +=1

        if May in List1[count]:
            Past_6_Months +=1

        if June in List1[count]:
            Past_6_Months +=1

        if July in List1[count]:
            Past_6_Months +=1

        if August in List1[count]:
            Past_6_Months +=1

        if September in List1[count]:
            Past_6_Months +=1

#This last function is different because there are two octobers listed in the log file.
#This will make sure it is only added if it is the last October before the year ended.
        if October in List1[count]:
            if Year in List1[count]:
                Past_6_Months +=1


    #count will add all of these together
    count +=1

#these two codes give the output of each string
print("Total Requests {" + str(count) + "}")
print("Total Requests in the past six months {" + str(Past_6_Months) + "}")

#the following code closes the log file
file.close()