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
        
    data.profiles = profiles
    print(profiles)
