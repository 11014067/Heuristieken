raw_battery = []

file =  open('wijk1_batterijen.txt', 'r')
for line in file: 
	if(line.split("\t")[0] != "pos"):
		list_string = line.split("\t")[0]
		list_string = list_string[1:len(list_string)-1]
		print(list_string)
		raw_battery.append([int(list_string.split(",")[0]), int(list_string.split(",")[1]), float(line.split("\t")[-1].rstrip())])

class Battery:

	def __init__(self, x, y, voltage):	
		self.x = x
		self.y = y
		self.min_x = x
		self.min_y = y
		self.voltage = voltage
		self.spare_voltage = voltage		
		
def fillBatteries(data_battery):
	new_battery = Battery(data_battery[0], data_battery[1], data_battery[2])
	return new_battery

batteries = []
for i in range(0, len(raw_battery)):
	batteries.append(fillBatteries(raw_battery[i]))		

print batteries[0].x