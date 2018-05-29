"""
   Convex Hull Assignment: COSC262 (2018)
   Student Name: Samuel Dravitzki
   Usercode: 62070502
"""

def readDataPts(filename, N):
    """Reads the first N lines of data from the input file
          and returns a list of N tuples
          [(x0,y0), (x1, y1), ...]
    """
    new_file = open(filename)
    new_file_lines = new_file.readlines()
    listPts = []
    for i in range(0, N):
        file_line = new_file_lines[i]
        x_value, y_value = file_line.split()
        point_tuple = (float(x_value), float(y_value))
        listPts.append(point_tuple)
    return listPts


def giftwrap(listPts):
    """Returns the convex hull vertices computed using the
          giftwrap algorithm as a list of m tuples
          [(u0,v0), (u1,v1), ...]    
    """
    k = calculate_bottom_right_point(listPts)
    listPts.append(listPts[k])
    #i = current position in the array
    i = 0
    # v = angle
    v = 0    
    print(listPts)
    chull = set()
    while k != len(listPts) - 1:
        print("---------------------------------------------------")
        #im not sure if im meant to be using listPts here
        print('i = ' + str(i) + ' k = ' + str(k))
        listPts[i], listPts[k] = listPts[k], listPts[i]
        min_angle = 361
        print("min angle " + str(min_angle))
        print("v is " + str(v))
        print("i is " + str(listPts[i]))
        #Check the angle betweem this point and every other point
        for j in range(i+1, len(listPts)):
            print("angle = theta(" + str(listPts[i]) + ", " + str(listPts[j]) + ") = " + str(theta(listPts[i], listPts[j])))
            angle = theta(listPts[i], listPts[j])
            print(listPts[j])
            print(angle)
            if (angle <= min_angle) and (angle >= v) and (listPts[j] != listPts[i]):
                min_angle = angle
                k = j
            print("min angle is now " + str(min_angle))
        print("k is  " + str(listPts[k]))
        chull.add(listPts[k])
        i+= 1
        v = min_angle
        print("---------------------------------------------------")
    print(chull)
    return chull
    
def theta (pointA, pointB):
    """Computes an approximation of the angle between the line
    AB and a horizontal line through A"""
    dx = pointB[0] - pointA[0]
    dy = pointB[1]  - pointA[1]
    t = 0
    if abs(dx) < 1.e-6 and abs(dy) < 1.e-6: 
        t = 0
    else:
        t = dy/(abs(dx) + abs(dy))
    #if dx is negitive
    if dx < 0:
        t = 2 - t
    if dy < 0:
        t = 4 + t
    return t * 90

def calculate_bottom_right_point(listPts):
    #get the first y value, assuming you van never have two points at the same position
    lowest_point = listPts[0]
    for point in listPts[1:]:
        x_value, y_value = point
        if y_value < lowest_point[1]: 
            lowest_point = point
        elif y_value == lowest_point[1] and x_value > lowest_point[0]:
            lowest_point = point

    index_of_point = listPts.index(lowest_point)
    return index_of_point
    
    
        

def grahamscan(listPts):
    """Returns the convex hull vertices computed using the
         Graham-scan algorithm as a list of m tuples
         [(u0,v0), (u1,v1), ...]  
    """
    #Your implementation goes here
    return  chull


def amethod(listPts):
    """Returns the convex hull vertices computed using 
          a third algorithm
    """
    #Your implementation goes here    
    return chull


def main():
    listPts = readDataPts('test.dat', 5)  #File name, numPts given as example onl
    print(listPts)
    print(giftwrap(listPts))   #You may replace these three print statements
    #print (grahamscan(listPts))   #with any code for validating your outputs
    #print (amethod(listPts))     

 
if __name__  ==  "__main__":
    main()
