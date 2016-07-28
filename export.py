import xlwt
import time

#global variable - current row number in workbook
row = 1

#exports all files searched, result[] and corresponding filename to spreadsheet
def export_to_spreadsheet(all_file_results, files):

	#declare global variable within function
	global row 
	row = 1

	#create Excel workbook
	workbook = xlwt.Workbook()

	#create fonts
	font0 = xlwt.Font()
	font0.bold = True
	style0 = xlwt.XFStyle()
	style0.font = font0

	font1 = xlwt.Font()
	font1.colour_index =0x0A
	style1 = xlwt.XFStyle()
	style1.font = font1

	font3 = xlwt.Font()
	style3 = xlwt.XFStyle()
	style3.font = font3

	#create headers for sheet1
	sheet1 = workbook.add_sheet("PANs_Located")
	sheet1.write(0,0,"Full Path", style=style0)
	sheet1.write(0,1,"File Name", style=style0)
	sheet1.write(0,2,"Line#", style=style0)
	sheet1.write(0,3,"Full PAN", style=style0)
	sheet1.write(0,4,"Masked PAN", style=style0)

	#write PAN_Hunter results to workbook
	for file_results in all_file_results:

		#pop last item in file_results[] and store value as full_filename
		full_filename = file_results.pop()
		#remove path from filename and store value as short_filename
		short_filename = strip_filename(full_filename)

		for line_results in file_results:
			#pop last item in line_results[] and store value as line 
			line = line_results.pop()

			for pan in line_results:		
				sheet1.write(row, 0, full_filename, style=style3)
				sheet1.write(row, 1, short_filename, style=style3)
				sheet1.write(row, 2, line, style=style3)  
				sheet1.write(row, 3, pan, style=style1)
				sheet1.write(row, 4, mask_num(pan), style=style3)
				#increment row counter
				row+=1

	#format column width
	sheet1.col(0).width = 15000
	sheet1.col(2).width = 1500
	sheet1.col(3).width = 5000
	sheet1.col(4).width = 4000

	#create headers for sheet2
	sheet2 = workbook.add_sheet("Files_Searched")
	sheet2.write(0,0,"Files searched (including path)", style=style0)
	
	#write files searched to workbook, sheet2
	row=1
	for f in files:
		sheet2.write(row, 0, f, style=style3)
		row+=1

	#format column width
	sheet2.col(0).width = 30000


	#save workbook
	timestring = time.strftime("%m%d%Y-%H%M%S")	
	workbook.save("PAN_Hunter_Results_"+timestring+".xls")

#mask all digits except last four
def mask_num(number): 
	length = len(number)
	str_number = str(number)
        return ("*" * (length-4)) + str_number[length-4:length] 
	
#Takes filname with path and returns filename without path
def strip_filename(filename):
	#split path to file by directory
	result = filename.split("/")
	#return last item in list (i.e., filename)
	return result.pop()
