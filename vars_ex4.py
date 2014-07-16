boats = 100
space_in_a_boat = 4.0
drivers = 30
passengers = 90
boat_not_driven = boats - drivers
boat_driven = drivers
boatpool_capacity = boat_driven * space_in_a_boat
average_passengers_per_boat = passengers / boat_driven

print "Thers are", boats , "boats available."
print "Thers are only", drivers, "drivers available."
print "We can transport",boatpool_capacity,"perpole tody"
print "We have",passengers,"to boatpool tody."
print "We need to put about", average_passengers_per_boat, "in each boat"
