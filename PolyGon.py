# Determining if a point is inside a given polygon or not
# Polygon is a list of (x,y) pairs. This function
# returns True or False.  The algorithm used to solve given problem is called the "Ray Casting Method".

def _is_point_in_poly(self, x, y, poly):
    n = len(poly)
    inside = False

    p1x, p1y = poly[0]
    for i in range(n + 1):
        p2x, p2y = poly[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xints = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xints:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside


## Test Data
polygon = [(0,100),(100,100),(100,0),(0,0)]

point_x = 5
point_y = 5

## Calling the given function with the points and the polygon(Test data)
print _is_point_in_poly((10,10),point_x,point_y,polygon)