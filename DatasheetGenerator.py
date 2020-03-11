# IMPORT MODULES
from googlesearch import search
import docx2txt
import requests
import os

# IMPORT PARTS LIST FROM DOCX FILE
pathName = input("Enter pathname: ")
partsList = docx2txt.process(pathName)
partNumbers = partsList.split('\n\n')

# MAKE DATASHEETS DIR
os.mkdir('DATASHEETS')

# SEARCH GOOGLE FOR DATASHEETS AND SAVE
count = 1
for i in partNumbers:
	# to search
	query = i + " Datasheet pdf"

	try:
		for j in search(query, tld='com', lang='en', num=1, start=0, stop=1, pause=1.0):
			# GET #1 GOOGLE PAGE
			file_URL = j

			r = requests.get(file_URL, stream = True)

			# SAVE FILE IN DATASHEET DIRECTORY IN HOME DIRECTORY
			with open("DATASHEETS/" + str(count) + "-" + i + ".pdf","wb") as pdf:
				for chunk in r.iter_content(chunk_size=1024):

			         # writing one chunk at a time to pdf file
					if chunk:
						pdf.write(chunk)
			# CHECK THAT FILE CAN BE OPENED OR RETURN EXCEPTION
			file = open("DATASHEETS/" + str(count) + "-" + i + ".pdf","r")
			print('.......writing ' + i + ' as pdf via file writer')
	except:
		print('!!!!!!!ERROR: ' + i + ' not saved, please locate manually with ' + str(count) + '- as prefix to maintain ordering')

	count += 1
