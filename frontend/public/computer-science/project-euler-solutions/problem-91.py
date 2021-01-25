import numpy as np
import matplotlib.pyplot as plt


CAP = 50

#This caclculates the number of trnalges whose axis is on the x or y axis
#This is easily Proven
numRightTriags = 3*CAP**2

#This calculates all of the points for which the right angle is not on the x or y axsis
#(The following is derived by thniking of the line normal to the line that connects the orgin to the point which also intersects at that same point)
for x1 in range(1, CAP+1):
    for y1 in range(1, CAP+1):
        m = -1*x1
        b = (x1**2 + y1**2)
        for x2 in range(0, min(x1+((y1**2)/x1)+1, CAP+1)):
            if (m*x2 + b)%y1 == 0 and (m*x2 + b)/y1 <= CAP and (not (x1==x2 and y1==((m*x2 + b)/y1))):
                y2 = (m*x2 + b)/y1
                print (0,0), (x1, y1), (x2, y2)
                numRightTriags += 1

print numRightTriags

#Time for an interesting visualization:
"""
TODO: Make the bouds on this actually work... Plot each triangle
def genPlotData(m, b, h=0.01):
    t = np.arange(0.0, CAP+h, h)
    y = m*t+b
    y[y < 0] =  np.nan
    return t, y


for x1 in range(1, CAP+1):
    for y1 in range(1, CAP+1):
        m = -1*x1
        b = (x1**2 + y1**2)
        for x2 in range(0, min(x1+((y1**2)/x1)+1, CAP+1)):
            if (m*x2 + b)%y1 == 0 and (m*x2 + b)/y1 <= CAP and (not (x1==x2 and y1==((m*x2 + b)/y1))):
                t, yrange = genPlotData(m, b)
                plt.plot(t, yrange, '-')

plt.grid(True)
plt.show()
"""
