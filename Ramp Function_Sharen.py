import cmath
import math
import numpy as np
import matplotlib.pyplot as plt

#Assignment Python for SSCP4333
#Sharen Rajenthiran
#Ramp function


t_res = 0.1   #step time
t_start = 0  #starting time
t_stop = 10 #stopping time
t2_stop = -10  #different stopping time from -10
N = int(t_stop-t_start/t_res+1)    #number of points
t = np.linspace(t_start, t_stop, N)   #t array
t2 = np.linspace(t_start, t2_stop, N)  #t2 array with different stopping time
t_general = np.linspace(-10,10, N)     #t_general array from -10 to 10


r = np.zeros(N)       #some 0 arrays for ramp function
r1 = np.zeros(N)
r2 = np.zeros(N)
r3 = np.zeros(N)
r_even = np.zeros(N)
r_odd = np.zeros(N)


for i in range(len(t)):
    if t[i] >= 0:
        r[i] = t[i]
    elif t[i]<0:
        r[i] = 0


t_shift = np.linspace(2,2, N)   #t-shift array

#print("if r(t-2): ")     #shifting for r(t-2)

for n in range(len(t)):
    if 0<=t[n]<=2:
        r1[n] = 0
    elif t[n]>=2:
        r1[n] = t[n]-t_shift[n]
        # print("t: ", t[n], "r: ", r1[n])

#print("if r(2-t): ")    #shifting for r(2-t)

for j in range(len(t)):
    if t[j]<=2:
        r2[j] = t_shift[j]-t[j]
        #print("t: ", t[j], "r: ", r2[j])
    elif t[j]>2:
        r2[j] = 0

#print("if r(-t): ")    #reflection for r(-t)

for a in range(len(t)):
    if t2[a] <= 0:
        r3[a] = -t2[a]
        #print("t: ", t2[a], "r: ", r3[a])
    elif t2[a] > 0:
        r3[a] = 0


#For r_even

for b in range(len(t)):
    if t_general[b]>=0:
        r_even[b] = 1/2*t_general[b]
        # print("t: ", t_general[b], "r_even: " , r_even[b])
    elif t_general[b] < 0:
        r_even[b] = -1/2*t_general[b]
        # print("t: ", t_general[b], "r_even: ", r_even[b])

#For r_odd


for c in range(len(t)):
    if t_general[c] >= 0:
        r_odd[c] = 1/2*t_general[c]
        # print("t: ", t_general[c], "r_odd: ", r_odd[c])
    elif t_general[c] < 0:
        r_odd[c] = 1/2*t_general[c]
        # print("t: ", t_general[c], "r_odd: ", r_odd[c])


# r_even(t) + r_odd(t) = r(t)


plt.figure()
plt.plot(t_general,r_even, t_general, r_odd, t, r)
plt.grid()
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Ramp function")
plt.legend(["r_even(t)", "r_odd(t)", "r_even(t)+r_odd(t)"], loc = "upper left")



plt.figure()
plt.plot(t,r1,t,r2,t,r)
plt.grid()
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Ramp function")
plt.legend(["r(t-2)", "r(2-t)", "r(t)"], loc = "upper left")

plt.show()



