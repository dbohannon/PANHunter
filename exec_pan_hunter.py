import sys
import file_manager
import pan_hunter
import export

#welcome user
print ""
print "Welcome to PAN Hunter!" 
print "Follow the on-screen prompts or type 'exit' to terminate."
print ""

#program loop, request user input
while True:
	
	#get filename from user
	filename = raw_input("Enter filename or search expression: ")	

	#type exit to quit program
	if filename == "exit":
		break

	#get path from user (optional)
	path = raw_input("Enter path (relative or absulute, default is current directory): ")
	print ""

	#type exit to quit program
	if path == "exit":
		break

	#if only filename regex is given, pass to file_manager - path will be current working directory
	if (path==""):
		files = file_manager.find_files(filename)

	else:
		files = file_manager.find_files(filename, path)

	#if no files match path and regex, print error message and return to top of loop 
	if not files:
	    print "No files matching that expression!"
            print ""
	    continue

	#if files match path and regex, do the following:

	#counter used to track number of files with regex match - initialized to 0
	files_with_regex = 0

	#list used to store all results from all files
	all_file_results = []

	#loop over all files located by file_manager
	for f in files:
	    print "Searching file: "+f 
	    
	    #temp contains list of matches and corresponding line numbers located by pan_hunter() for a single file 'f'
	    result = pan_hunter.pan_hunter(f)
	    
	    #if result is empty then no regex match found, return to top of loop and go to next file; else, do the following:
	    if(len(result) == 0):
		continue
		
	    #increment counter used to track files with regex match
	    files_with_regex += 1

	    #add filename to result list
	    result.append(f)

	    #add results from individual file to all_file_results list
	    all_file_results.append(result)

	#print all_file_results	#debug 

	#print all_file_results[] and all files searched to spreadsheet 
	export.export_to_spreadsheet(all_file_results,files) 

	#print diagnostics
	print ""	
	print "Files found: "+str(len(files))  
	print "Files searched: "+str(len(files)-pan_hunter.unopened_files)
	print "Files with PAN: "+str(files_with_regex)  

	#print result message
	if (files_with_regex == 0):
		print "No PAN Located!"
		print ""
	else:
		print "PAN Located, see file 'PAN_Hunter_Results' for details!"
		print ""

