#This first command opens the downloaded log file needed to parse
file = open('http_access_log.txt','r') 
#This counts all of the total requests in the log file
count = 0 
#This counts all of the requests made in the last six months
Past_6_Months = 0

#this converts the text in the log to a variable that you can use and reference
May = "May"
June = "Jun"
July = "Jul"
August = "Aug"
September = "Sep"
October = "Oct"
Year = "1995"

#takes reads the attached file
Content = file.read()
#Separates the file into a list to help identify if it has a month in it.
List1 = Content.split('\n')


#This goes through each request line to add into the count if it suits my criteria 
for lines in List1:
    if lines:
        #this takes the list that has been split and searches for the criteria, here it's may.
        #if may is listed here, the code adds it to the past 6 months count. 

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


    #count will add all of these together and add it to the total count
    count +=1

#this code gives the output of the number of requests in the last six months
print("Total Requests in the past six months {" + str(Past_6_Months) + "}")

#prints complete number of total requests in the entire file
print("Total Requests {" + str(count) + "}")

#the following code closes the log file
file.close()