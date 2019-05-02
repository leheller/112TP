#The functions in this file write data into three separate pickle files and 
#turn other data types into strings to be sent to the server
###########
#pickleFile.py citation comment
#lines 9-149: original code
#lines 130,131,139,140,148,149 adapted from sockets manual on 112 website (https://kdchin.gitbooks.io/sockets-module-manual/)
#individual pickle functions found on python.org (https://docs.python.org/3/library/pickle.html)
###########
import pickle
import os

#Sorting algorithm to bring best possible matches to the front of the list
def sorting(data, s):
    college = []
    rest = []
    #separates profiles by if they are in the same college as the user or not
    #stores them in the list as the difference in GPA
    for ppl in s:
        if len(ppl) > 1:
            if ppl[3] == data.school:
                diff = abs(float(ppl[2])-float(data.GPA))
                college.append(diff)
            else: 
                diff = abs(float(ppl[2])-float(data.GPA))
                rest.append(diff)
    #sorts each list by difference in GPA
    college.sort()
    rest.sort()
    #replaces GPA difference with entire matching profile
    for ppl in s:
        if len(ppl) > 1:
            diff = abs(float(ppl[2])-float(data.GPA))
            if ppl[3] == data.school:
                for i in range(len(college)):
                    if college[i] == diff:
                        college[i] = ppl
            else:
                for i in range(len(rest)):
                    if rest[i] == diff:
                        rest[i] = ppl
    #adds lists back together
    data.otherProfiles = college + rest
    

#Saves new profiles to a pickle file and retreives every profile to be saved in init
def writePickle(data):
    profilesFilename = "profiles.py"
    profiles = set()
    #Retreives what is currently stored in pickle file
    if os.path.exists(profilesFilename):
        with open(profilesFilename,"rb") as rfp:
            profiles = pickle.load(rfp)
    #Adds new profile
    newProfile = data.myProfile
    profiles.add(newProfile)
    #Puts set of profiles into pickle file
    with open(profilesFilename,"wb") as wfp:
        pickle.dump(profiles,wfp)
    #Retreives entire set of profiles including new ones
    with open(profilesFilename,"rb") as rfp:
        profiles = pickle.load(rfp)
    #Creates list of profiles that are not current user
    otherProfiles = []
    for profile in profiles:
        if len(profile)>1 and profile[0] != data.username:
            otherProfiles += [profile]
    #Saves sorted list of profiles to init
    sorting(data, otherProfiles)
    data.profiles = profiles
    return profiles

#Saves new matches to a pickle file and retreives every match to be saved in init
def writePickle2(data):
    profilesFilename = "matches.py"
    matches = set()
    #Retreives what is currently stored in pickle file
    if os.path.exists(profilesFilename):
        with open(profilesFilename,"rb") as rfp:
            matches = pickle.load(rfp)
    #Adds new match         
    newMatch = data.match
    if data.match2 != ():
        matches.add(data.match2)
    matches.add(newMatch)
    #Puts set of profiles into pickle file
    with open(profilesFilename,"wb") as wfp:
        pickle.dump(matches,wfp)
    #Retreives modified set
    with open(profilesFilename,"rb") as rfp:
        matches = pickle.load(rfp)
    #Puts all matches in init
    data.matches = matches
    return matches

#Saves new messages to a pickle file and retreives every message to be saved in init    
def writePickle3(data):
    profilesFilename = "messages.py"
    messages = set()
    #Retreives current set of messages
    if os.path.exists(profilesFilename):
        with open(profilesFilename,"rb") as rfp:
            messages = pickle.load(rfp)
    #Adds updated messages to set (messages in form: [(User1,User2,message,message,...),(user2,user1,message,message,...)])
    for elem in data.messages:
        check = False
        if len(elem) > 2:
            for elem2 in messages:
                if elem[0] == elem2[0] and elem[1] == elem2[1]:
                    messages.remove(elem2)
                    messages.add(elem)
                    check = True
            if check == False:
                messages.add(elem)
    #Saves set to pickle file
    with open(profilesFilename,"wb") as wfp:
        pickle.dump(messages,wfp)
    #Loads updated set of messages
    with open(profilesFilename,"rb") as rfp:
        messages = pickle.load(rfp)
    #Puts all messages in init
    data.messages = messages
    return messages

#Turns new profiles into a string and sends to server        
def setToString(data,tup):
    msg = "NewProfile&"
    for attribute in tup:
        msg += attribute + "&"
    msg += "\n"
    print ("sending: ", msg,)
    data.server.send(msg.encode())

#Turns new matches into a string and sends to server     
def setToString2(data,tup):
    msg = "Match&"
    for attribute in tup:
        msg += attribute + "&"
    msg += "\n"
    print ("sending: ", msg,)
    data.server.send(msg.encode())

#Turns new messages into a string and sends to server     
def setToString3(data,tup):
    msg = "NewMessage&"
    for attribute in tup:
        msg += attribute + "&"
    msg += "\n"
    print ("sending: ", msg,)
    data.server.send(msg.encode())
