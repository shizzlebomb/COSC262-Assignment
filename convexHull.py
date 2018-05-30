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
    print((listPts[k]))
    listPts.append(listPts[k])
    initial_point = listPts[k]
    #i = current position in the array
    i = 0
    # v = angle
    v = 0    
    #print(listPts)
    chull = []
    while k != len(listPts) - 1 :
        chull.append(listPts[k])
        listPts[i], listPts[k] = listPts[k], listPts[i]
        min_angle = 361
        #Check the angle betweem this point and every other point
        for j in range(i+1, len(listPts)):
            angle = theta(listPts[i], listPts[j])
            if (angle < min_angle) and (angle > v) and (listPts[j] != listPts[i]):
                min_angle = angle
                k = j
        i+= 1
        v = min_angle
    return chull
    
def theta (pointA, pointB):
    """Computes an approximation of the angle between the line
    AB and a horizontal line through A"""
    dx = pointB[0] - pointA[0]
    dy = pointB[1]  - pointA[1]
    if abs(dx) < 1.e-6 and abs(dy) < 1.e-6: 
        t = 0
    else:
        t = dy/(abs(dx) + abs(dy))
    #if dx is negitive
    if dx < 0:
        t = 2 - t
    #if dy is negitive
    elif dy < 0:
        t = 4 + t
    
    #set the angle to 360 if it is 0
    angle = t * 90
    if angle == 0:
        angle = 360
    return angle

def calculate_bottom_right_point(listPts):
    #get the first y value, assuming you van never have two points at the same position
    lowest_point_index = 0
    lowest_point = listPts[0]
    for index, point in enumerate(listPts):
        x_value, y_value = point
        if y_value < lowest_point[1]: 
            lowest_point_index = index
        elif y_value == lowest_point[1] and x_value > lowest_point[0]:
            lowest_point_index = index

    return lowest_point_index
    
    
        

def grahamscan(listPts):
    """Returns the convex hull vertices computed using the
         Graham-scan algorithm as a list of m tuples
         [(u0,v0), (u1,v1), ...]  
    """
    lowest_point_index = calculate_bottom_right_point(listPts)
    lowest_point = listPts[lowest_point_index]
    #Sort all points by angle
    simple_closed_path = sort_points_by_angle(listPts, lowest_point)
    point_stack = [
        simple_closed_path[0],
        simple_closed_path[1],
        simple_closed_path[2]
    ]
    for point in simple_closed_path[3:]:
        while not(isCCW(point_stack[-2], point_stack[-1], point)):
            popped_point = point_stack.pop()
        
        point_stack.append(point)
    return point_stack

def isCCW(pointA, pointB, pointC):
    return line_function(pointA, pointB, pointC) > 0

def line_function(pointA, pointB, pointC):
    return(
        (pointB[0] - pointA[0]) * (pointC[1] - pointA[1]) -\
        (pointB[1] - pointA[1])  * (pointC[0] - pointA[0])
        )

def sort_points_by_angle(listPts, start_point):
    points_and_angles = {}
    for point in listPts:
        #print(point)
        if point != start_point:
            point_angle = theta(point ,start_point)
            points_and_angles.update({point : point_angle})
        else:
            point_angle = 0
            points_and_angles.update({point : point_angle})
    sorted_points = sorted(points_and_angles, key=points_and_angles.__getitem__)
    return sorted_points
    
        

def amethod(listPts):
    """Returns the convex hull vertices computed using 
          the monotone algorithm
    """
    chull = []
    #lower_hull = []
    #upper_hull = []
    lower_hull = build_half(sorted(listPts))
    upper_hull = build_half(reversed(sorted(listPts)))
    
    #build the upper hull
    #sorted_list = sorted(listPts)
    #for point in sorted_list:
        #while len(lower_hull) >= 2 and not isCCW(lower_hull[-2], lower_hull[-1], point):
            #lower_hull.pop()
        #lower_hull.append(point)
        
    ##build the lower hull
    #for point in reversed(sorted(sorted_list)):
        #while (len(upper_hull) >= 2) and not isCCW(upper_hull[-2], upper_hull[-1], point):
            #upper_hull.pop()
        #upper_hull.append(point)
    
    chull = lower_hull[:-1] + upper_hull[:-1]
    return chull


def build_half(listPts):
    hull = []
    for point in listPts:
        while len(hull) >= 2 and not isCCW(hull[-2], hull[-1], point):
            hull.pop()
        hull.append(point)    
    return hull


def main():
    #listPts = readDataPts('A_3000.dat', 3000)  #File name, numPts given as example onl
    listPts =[(0.0,0.0),(1.0, 0),(1.0,1.0), (1.0, 2.0),(0.0,1.0),(0.5,0.5),(0.5, 1.5)]
    print(listPts)
    #print(giftwrap(listPts))   #You may replace these three print statements
    #print (grahamscan(listPts))   #with any code for validating your outputs
    print (amethod(listPts))     

 
if __name__  ==  "__main__":
    main()
