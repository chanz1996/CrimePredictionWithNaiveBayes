import csv
def decide_id(row):
	if(row[0] == "aggravated-assault"):
		row[7]=1
	elif(row[0] == "all-other-crimes"):
		row[7] = 3
	elif(row[0] == "larceny"):
		row[7] = 5
	elif(row[0] == "theft-from-motor-vehicle"):
		row[7] = 5
	elif(row[0] == "public-disorder"):
		row[7] = 4
	elif(row[0] == "drug-alcohol"):
		row[7] = 2
	elif(row[0] == "sexual-assault"):
		row[7] = 1
	elif(row[0] == "other-crimes-against-persons"):
		row[7] = 3
	elif(row[0] == "auto-theft"):
		row[7] = 5
	elif(row[0] == "burglary"):
		row[7] = 5
	elif(row[0] == "robbery"):
		row[7] = 5
	elif(row[0] == "white-collar-crime"):
		row[7] = 6
	elif(row[0] == "arson"):
		row[7] = 3
	elif(row[0] == "murder"):
		row[7] = 3
def timebucket(row):
	time=row[1].split()[1:]
	time[0]=time[0].split(":")
	if(time[1]=="PM"):
		if(int(time[0][0])!=12):
			time[0][0]=str(int(time[0][0])+12)	
	elif(time[1]=="AM"):
		if(time[0][0]=="12"):
			time[0][0]="00"
	time=time[0]
	
	buckets={"T1":[['1', '00', '00'],['4', '59', '59']],"T2":[['5', '00', '00'],['8', '59', '59']],"T3":[['9', '00', '00'],['12', '59', '59']],"T4":[['13', '00', '00'],['16', '59', '59']],"T5":[['17', '00', '00'],['20', '59', '59']],"T6":[['21', '00', '00'],['23', '59', '59']],"T6":[['0', '00', '00'],['1', '59', '59']]}
	for key in buckets.keys():
		lower=buckets[key][0]
		higher=buckets[key][1]
		if(int(time[0])>=int(lower[0]) and int(time[0])<=int(higher[0])):
			row[8]=key
	print(time)
	
	

with open ('new_denver_dataset.csv' , 'rb') as csvfile:
	reader = csv.reader(csvfile)
	data = []
	
	count=0
	for row in reader:
		if(count==0):
			count=1
		else:
			decide_id(row)
			timebucket(row)
			data_month = row[1][0]+row[1][1]
			data_day = row[1][3]+row[1][4]
			data_time = row[1][11:22]
			row[4] = data_month
			row[5] = data_day
			row[6] = data_time
			data.append(row)
b = open('test.csv', 'w')
a = csv.writer(b)
a.writerows(data)
b.close()
"""



"""


		
		



