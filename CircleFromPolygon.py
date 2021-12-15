#We can see a circle as a regular polygon of infinite edges
#The more edges, the closer the perimeter gets to the value of pi
import math
import matplotlib.pyplot as plt

class position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(pos1, pos2):   #simple pythagoras
    
    x = math.fabs(pos1.x - pos2.x)
    y = math.fabs(pos1.y - pos2.y)

    x = x*x
    y = y*y

    return math.sqrt(x + y)

xs=[]
ys=[]

for i in range(3,1408,8):   #jumping every 8 to speed-up the process

    angle = 360/i

    #find edge 1
    x1 = math.sin(math.radians(angle))
    y1 = math.cos(math.radians(angle))

    #find edge2
    x2 = math.sin(math.radians(angle*2))
    y2 = math.cos(math.radians(angle*2));
    
    dist = distance(position(x1,y1),position(x2,y2))
    
    dist*= i #perimeter of the polygonr
    dist/= 2 #value of pi

    print("Angle:",angle,". Perim:",dist)

    xs.append(angle)
    ys.append(dist)

plt.plot(xs,ys)
plt.show()