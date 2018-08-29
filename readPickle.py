import pickle
from sys import argv


_file = argv[1]


periods = [3, 5, 6, 7, 8, 10, 15, 20, 25, 30, 35, 40]
#periods = [5]
p = pickle.load( open( _file, "rb"))
pasy = open("./pasyanos.dat", "w")

for i in p:
    for per in periods:
        try:
            index = i.get_period_index(per)
            vel   = i.v[index]
            if vel > 0: 
                line = str(i.station1.coord[0]) +" "+ str(i.station1.coord[1]) + " 0 " + str(i.station2.coord[0]) +" "+ str(i.station2.coord[1]) +" "+ "%.3f" % vel +" "+ str(per) + " R " + "1 " +str(i.station1.name) +" "+ str(i.station2.name) + "\n"
		print line
		pasy.write(line)
        except:
            print "Period: %d has no valid velocity" % per
pasy.close()
    
