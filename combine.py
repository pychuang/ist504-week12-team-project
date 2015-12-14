#!/usr/bin/python

import csv
import operator

category_dict = {}

with open("search_queries.csv") as csvfile:
	csvreader = csv.DictReader(csvfile)

	for row in csvreader:
		category_dict[int(row['index'])] = row['Category']	

newrows = [["index", "Category",
"Believable Strongly Disagree", "Believable Disagree", "Believable Neither", "Believable Agree", "Believable Strongly Agree",
"Trustworthy Strongly Disagree", "Trustworthy Disagree", "Trustworthy Neither", "Trustworthy Agree", "Trustworthy Strongly Agree",
"Accurate Strongly Disagree", "Accurate Disagree", "Accurate Neither", "Accurate Agree", "Accurate Strongly Agree",
"Complete Strongly Disagree", "Complete Disagree", "Complete Neither", "Complete Agree", "Complete Strongly Agree",
"Biased Strongly Disagree", "Biased Disagree", "Biased Neither", "Biased Agree", "Biased Strongly Agree",
]]

with open("My_Report_1_.csv") as csvfile:
	csvreader = csv.reader(csvfile)

	for row in csvreader:
		if row[0][:3] == "102":
			break
	index = 1
	newrow = [index, category_dict[index]]
	for row in csvreader:
		if row[0] == "1":
#			print index, "BELIEVE", row
			newrow.extend(row[2:7])
		elif row[0] == "2":
#			print index, "TRUST", row
			newrow.extend(row[2:7])
		elif row[0] == "3":
#			print index, "ACCURATE", row
			newrow.extend(row[2:7])
		elif row[0] == "4":
#			print index, "COMPETE", row
			newrow.extend(row[2:7])
		elif row[0] == "5":
#			print index, "BIASED", row
			newrow.extend(row[2:7])
		elif len(row[0]) > 4 and  row[0][3] == ".":
			newrows.append(newrow)
			index += 1
			if index > 100:
				break
			newrow = [index, category_dict[index]]

#		if index > 5:
#			break

#for row in newrows:
#	print row
#exit()

with open("trustworthy.csv", "wb") as csvfile:
	csvwriter = csv.writer(csvfile)

	for row in newrows:
		csvwriter.writerow(row)
