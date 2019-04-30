#Sorting algorithm
def sorting(data, s):
    college = []
    rest = []
    for ppl in s:
        if ppl[3] == data.school:
            diff = abs(float(ppl[2])-float(data.GPA))
            college.append(diff)
        else: 
            diff = abs(float(ppl[2])-float(data.GPA))
            rest.append(diff)
    college.sort()
    rest.sort()
    for ppl in s:
        diff = abs(float(ppl[2])-float(data.GPA))
        if ppl[3] == data.school:
            for i in range(len(college)):
                if college[i] == diff:
                    college[i] = ppl
        else:
            for i in range(len(rest)):
                if rest[i] == diff:
                    rest[i] = ppl
    data.otherProfiles = college + rest
    
#Supermatch algorithm
def autoMatch(data):
    for ppl in data.otherProfiles:
        diff = abs(float(ppl[2])-float(data.GPA))
        if ppl[3] == data.school and diff <= 0.2:
            sched1 = createSchedule(data.myProfile[5])
            sched2 = createSchedule(data.otherProfiles[0][5])
            closestTime = 100
            for day in sched1:
                time1 = ""
                for c in sched1[day]:
                    if c in "1234567890":
                        time1 += c
                time1 = int(time1)
                time2 = "  "
                for c in sched2[day]:
                    if c in "1234567890":
                        time2 += c
                time2 = int(time2)
                if sched1[day] == sched2[day]:
                    day,time = day[:-1] + "  ",sched1[day]
                    data.match = (data.myProfile[0],ppl[0],day,time,"SUPERMATCH")
                    data.match2 = (ppl[0],data.myProfile[0],day,time,"SUPERMATCH")
                    data.matches.add(data.match)
                    data.matches.add(data.match2)
                    writePickle2(data)
                    setToString2(data,data.match)
                    setToString2(data,data.match2)
                    writePickle2(data)
                
  

######
#TO DO:

#write supermatch algorithm
#fix bio line issue
#camera screen
#Get rid of duplicate dates/highlight date and message if already matched
#Clean up code
#Citations
#Reset users
#Make users
#Readme file
#TP3
######