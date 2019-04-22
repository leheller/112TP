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
    profiles.add(newProfile)
    
    with open(profilesFilename,"wb") as wfp:
        pickle.dump(profiles,wfp)
    
    with open(profilesFilename,"rb") as rfp:
        profiles = pickle.load(rfp)

    data.otherProfiles = list(profiles)
    data.profiles = profiles
    print("hi",data.profiles)
    return profiles
    
def writePickle2(data):
    profilesFilename = "matches.py"
    matches = set()
    if os.path.exists(profilesFilename):
        with open(profilesFilename,"rb") as rfp:
            matches = pickle.load(rfp)
            
    newMatch = data.match
    matches.add(newMatch)
    
    with open(profilesFilename,"wb") as wfp:
        pickle.dump(matches,wfp)
    
    with open(profilesFilename,"rb") as rfp:
        matches = pickle.load(rfp)
    
    data.matches = matches
    print("hello")
    print(matches)
    return matches
    
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
    
#two pickle files (profiles, messages)
#Turn set into string
