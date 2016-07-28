import re
import mod10

#compile regex used to search for pan from all brands
regex = re.compile(r"\b(?:4[0-9]{12}(?:[0-9]{3})?)\b|\b5[12345][0-9]{14}\b|\b3[47][0-9]{13}\b|\b3(?:0[012345]|[68][0-9])[0-9]{11}\b|\b6(?:011|5[0-9]{2})[0-9]{12}\b|\b(?:2131|1800|35[0-9]{3})[0-9]{11}\b")

unopened_files = 0

#pan_hunter() - searches for PAN in file and returns any matches and line number
#@param filename - name of file to search
#@return matches - list of PAN found in file and corresponding line number
def pan_hunter(filename):

    #list used to store all regex matches in file and corresponding line number
    result = []

    #open file and store each line in the list lines
    try:
        file_object = open(filename)
    except IOError:
        print "Error: unable to open "+filename
	global unopened_files
	unopened_files+=1
	return result

    lines = file_object.readlines()
    
    #for each line, find all strings that match regex
    for x in lines:
    
        #print str(lines.index(x)+1)+": "+x        #debug

        #all matches in current line stored in temp[]
        temp = regex.findall(x)
        
        #check temp[] against mod10 and remove items if fail
        for y in temp:
            if(not mod10.check(y)):
                #print y+" failed mod10 and was removed"        #debug 
                temp.remove(y)
        
        #if no matches in current line, go to top of loop and search next line
        if (len(temp) == 0):
            continue
        
        #add line number to temp[] 
        temp.append(lines.index(x)+1)
        
        #append temp[] to result[] which contains all lines in file with regex matches in format result[temp[match1, match2, line#], ...]
        result.append(temp)
 
    #close file           
    file_object.close()

    #return regex matches, line numbers, and filename
    return result


