import math

def get_angle(point1, point2):
    "Finds the angle between two points"
    x1, y1 = point1
    x2, y2 = point2
    x = x1 - x2
    y = y2 - y1
    
    #this part gives values to prevent divide by zero errors
    if x1 == x2:
        if y1 > y2:
            return 0.0
        else:
            return 3.14159265359
    if y1 == y2:
        if x1 > x2:
            return 4.71238898038 # pi * 1.5
        else:
            return 1.57079632679 # pi * 0.5

    #and then the angle is worked out based on which quater it is in
    #all the angle gets returned in degrees, i don't think this has any benifits
    #but it's easier to think about for now
    if (x2 > x1) and (y2 < y1):
        x = x2 - x1
        y = y1 - y2
        return math.atan(x/float(y))
    if (x2 > x1) and (y2 > y1):
        x = x1 - x2
        y = y1 - y2
        return 3.14159265359-math.atan(x/float(y))
    if (x1 > x2) and (y2 > y1):
        x = x2 - x1
        y = y1 - y2
        return 3.14159265359+math.atan(x/float(y))
    if (x1 > x2) and (y2 < y1):
        x = x1 - x2
        y = y1 - y2
        return 3.14159265359*2-math.atan(x/float(y))




def get_distance(point1, point2):
    """Finds the distance between two points. """
    x1, y1 = point1
    x2, y2 = point2
    x = abs(x2 - x1)
    y = abs(y2 - y1)
    distance = (x**2 + y**2)**0.5
    return distance