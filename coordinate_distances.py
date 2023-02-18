#Collins Wanga

import math

print("Input coordinates of two points:")
s_latitude = math.radians(float(input("Enter the starting latitude: ")))
s_longitude = math.radians(float(input("Enter the ending longitude: ")))
e_latitude = math.radians(float(input("Enter the starting latitude: ")))
e_longitude = math.radians(float(input("Enter the ending longitude: ")))

distance = 6371.01 * math.acos(math.sin(s_latitude)*math.sin(e_latitude) + math.cos(s_latitude)*math.cos(e_latitude)*math.cos(s_longitude - e_longitude))
print("The distance between the two points is %.2fkm." % distance)
