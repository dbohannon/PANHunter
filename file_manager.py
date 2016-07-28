import os
import sys
import fnmatch
import glob

#find_files: finds all files with @param name located in @param path and returns a list of files
#@param name = name of file, including regex
#@param path = path to file, optional - default is local directory
#@return list of files located based on given parameters

def find_files(name, path=os.getcwd()):
    #used to store list of files with full paths
    matches = []

    #expand regex in path and return list of paths 
    list_of_paths = glob.glob(path)

    #display list of paths to user
    print "Locating files in the following path(s):", list_of_paths
    print ""

    #for each path in list_of_paths, walk recursively and search for file
    for x in list_of_paths:
        for root, dirnames, filenames in os.walk(x): 
            for filename in fnmatch.filter(filenames,name):
                matches.append(os.path.join(root, filename))        
    return matches

    


