# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Bela Jere
# Section: 507
# Assignment: 2-10
# Date: 24/8/24

t0 = 12
t1 = 85
start = 30
end = 60

#first iteration
x1 = ((-5 - 8) / (t1 - t0))*(30- t0) + 8 #linear interpolation formula

y1 = ((30 - 6) / (t1 - t0))*(30- t0) + 6 #linear interpolation formula

z1 = ((9 - 7) / (t1 - t0))*(30 - t0) + 7 #linear interpolation formula

print("At time 30.0 seconds:")
print("x1 = ", str(x1),"m")
print("y1 = ", str(y1),"m")
print("z1 = ", str(z1),"m")
print("-----------------------")

#second iteration
time_interest = ((end-start)/4)+30
x1 = ((-5 - 8) / (t1 - t0))*(time_interest - t0) + 8 #linear interpolation formula

y1 = ((30 - 6) / (t1 - t0))*(time_interest - t0) + 6 #linear interpolation formula

z1 = ((9 - 7) / (t1 - t0))*(time_interest - t0) + 7 #linear interpolation formula

print("At time ", str(time_interest), " seconds:")
print("x2 = ", str(x1),"m")
print("y2 = ", str(y1),"m")
print("z2 = ", str(z1),"m")
print("-----------------------")

#third iteration
time_interest = (2*(end-start)/4)+30
x1 = ((-5 - 8) / (t1 - t0))*(time_interest - t0) + 8 #linear interpolation formula

y1 = ((30 - 6) / (t1 - t0))*(time_interest - t0) + 6 #linear interpolation formula

z1 = ((9 - 7) / (t1 - t0))*(time_interest - t0) + 7 #linear interpolation formula

print("At time ", str(time_interest), " seconds:")
print("x3 = ", str(x1),"m")
print("y3 = ", str(y1),"m")
print("z3 = ", str(z1),"m")
print("-----------------------")

#fourth iteration
time_interest = (3*(end-start)/4)+30
x1 = ((-5 - 8) / (t1 - t0))*(time_interest - t0) + 8 #linear interpolation formula

y1 = ((30 - 6) / (t1 - t0))*(time_interest - t0) + 6 #linear interpolation formula

z1 = ((9 - 7) / (t1 - t0))*(time_interest - t0) + 7 #linear interpolation formula

print("At time ", time_interest , " seconds:")
print("x4 = ", str(x1),"m")
print("y4 = ", str(y1),"m")
print("z4 = ", str(z1),"m")
print("-----------------------")

#fifth iteration
time_interest = (4*(end-start)/4)+30
x1 = ((-5 - 8) / (t1 - t0))*(time_interest - t0) + 8 #linear interpolation formula

y1 = ((30 - 6) / (t1 - t0))*(time_interest - t0) + 6 #linear interpolation formula

z1 = ((9 - 7) / (t1 - t0))*(time_interest - t0) + 7 #linear interpolation formula

print("At time ", time_interest, " seconds:")
print("x5 = ", str(x1),"m")
print("y5 = ", str(y1),"m")
print("z5 = ", str(z1),"m")
