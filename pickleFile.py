import pickle
import os


#Adapted from https://stackoverflow.com/questions/28077573/python-appending-to-a-pickled-list
def writePickle(data):
    profilesFilename = "profiles.py"
    profiles = set()
    if os.path.exists(profilesFilename):
        with open(profilesFilename,"rb") as rfp:
            profiles = pickle.load(rfp)
        
    newProfile = data.myProfile
    #newProfile = ("Lauren","webkin","4.0","CIT","I like to ski!")
    profiles.add(newProfile)
    
    with open(profilesFilename,"wb") as wfp:
        pickle.dump(profiles,wfp)
    
    with open(profilesFilename,"rb") as rfp:
        profiles = pickle.load(rfp)
    
    otherProfiles = []
    for profile in profiles:
        if profile[0] != data.username:
            otherProfiles += [profile]
    data.otherProfiles = list(otherProfiles)
    data.profiles = profiles
    return profiles
    
def writePickle2(data):
    profilesFilename = "matches.py"
    matches = set()
    if os.path.exists(profilesFilename):
        with open(profilesFilename,"rb") as rfp:
            matches = pickle.load(rfp)
            
    newMatch = data.match
    #newMatch = ("Lauren","Bob")
    matches.add(newMatch)
    
    with open(profilesFilename,"wb") as wfp:
        pickle.dump(matches,wfp)
    
    with open(profilesFilename,"rb") as rfp:
        matches = pickle.load(rfp)
        
        data.matches = matches
        return matches
    
def writePickle3(data):
    profilesFilename = "messages.py"
    messages = set()
    if os.path.exists(profilesFilename):
        with open(profilesFilename,"rb") as rfp:
            messages = pickle.load(rfp)
    
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
    
    
    with open(profilesFilename,"wb") as wfp:
        pickle.dump(messages,wfp)
    
    with open(profilesFilename,"rb") as rfp:
        messages = pickle.load(rfp)
    
    data.messages = messages
    return messages
        
def setToString(data,tup):
    msg = "NewProfile&"
    for attribute in tup:
        msg += attribute + "&"
    msg += "\n"
    print ("sending: ", msg,)
    data.server.send(msg.encode())
    
def setToString2(data,tup):
    msg = "Match&"
    for attribute in tup:
        msg += attribute + "&"
    msg += "\n"
    print ("sending: ", msg,)
    data.server.send(msg.encode())
    
def setToString3(data,tup):
    msg = "NewMessage&"
    for attribute in tup:
        msg += attribute + "&"
    msg += "\n"
    print ("sending: ", msg,)
    data.server.send(msg.encode())
