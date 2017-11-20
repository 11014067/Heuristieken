from classesWijk import House, Battery

def download_data(x)
	house_file = 'Wijk_informatie/wijk' + x + '_huizen.csv'
	battery_file = 'Wijk_informatie/wijk' + x + '_batterijen.txt'

	# download the raw house data in a list	
	xyvolt= []
	i = 0
	with open(house_file, 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter = ',')
		for row in reader:
			if row[0] != "x":
				xyvolt.append([int(row[0]), int(row[1]), float(row[2]), int(i)])
		i += 1
	
	# stores the data into classes
	def fillHouses(xy_house):
		new_house = House(xy_house[0], xy_house[1], xy_house[2], xy_house[3])
		return new_house
	
	houses = []
	for i in range(0, len(xyvolt)):
		houses.append(fillHouses(xyvolt[i]))
		
	# download the raw battery data in a list		
	raw_battery = []
	file =  open(battery_file, 'r')
	for line in file: 
		if(line.split("\t")[0] != "pos"):
			list_string = line.split("\t")[0]
			list_string = list_string[1:len(list_string)-1]
			raw_battery.append([int(list_string.split(",")[0]), int(list_string.split(",")[1]), float(line.split("\t")[-1].rstrip())])
	
	# stores the data into classes	
	def fillBatteries(data_battery):
		new_battery = Battery(data_battery[0], data_battery[1], data_battery[2])
		return new_battery
	
	batteries = []
	for i in range(0, len(raw_battery)):
		batteries.append(fillBatteries(raw_battery[i]))
		batteries[i].add_name(i)
		print("Battery {} on index {} has x = {}".format(batteries[i].name, i, batteries[i].x))
	return [batteries, houses]