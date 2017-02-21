import PolyGon

#Case: Test method Validating the given function for a point(4,2) that is lying INSIDE a polygon
def test_is_point_in_poly():
    # polygon = [(0, 5), (5, 5), (5, 0), (0, 0)]
    verify = PolyGon._is_point_in_poly((4,2), 4,2, [(0, 5), (5, 5), (5, 0), (0, 0)])
    assert verify == True

#Validating a function for a point(10,12) that is lying outside a polygon
def test_is_point_inner_poly():
    verify = PolyGon._is_point_in_poly((10,12),10,12,[(0, 10), (10, 10), (10, 0), (0, 0)])
    assert verify == False

#Validating a function for a point(5,9) that is lying inside a polygon
def test_is_point_inside_poly():
    # polygon = [(0,10),(10,10),(10,0),(0,0)]
    verify = PolyGon._is_point_in_poly((5,9), 5, 9, [(0, 10), (10, 10), (10, 0), (0, 0)])
    assert verify == True

#Validating a function for a point(-33.416032, -70.593016). Point represents the following information.
# That is, Original represenation of the above point be longitude = '-70.593016' is the "x" value and latitude = '-33.416032'
# is "y" value in above point and below they are reversed. When testing the function with the following test data,
# Point(-33.416032, -70.593016) lie outside the polygon

def test_is_point_lie_in_poly():
    verify = PolyGon._is_point_in_poly((-33.416032, -70.593016), -33.416032, -70.593016,
                                           [(-33.416032, -70.593016), (-33.415370, -70.589604),
                                            (-33.417340, -70.589046), (-33.417949, -70.592351),
                                            (-33.416032, -70.593016)])
    assert verify == False

#Case: Test method Validating a given function for a point(-10,1) in Quadrant(II)(in planar co-ordinate system/axis)
# which lie OUTSIDE the given polygon(text data) as shown below when running against given function returns 'False'(As expected)
def test_is_point_lie_OUT_poly():
    verify = PolyGon._is_point_in_poly((-10,1),-10,1,[(0,10),(10,10),(10,0),(0,0)])
    assert verify == False

# Test method Validating a given function for a point(2,2) that lies 'ON' the polygon
def test_is_point_lie_ON_poly():
    verify = PolyGon._is_point_in_poly((2,2),2,2,[(0,0), (0,2), (2,2), (2,0)])
    assert verify ==  True


#Case: Test method Validating a given function for a point(90,90) that coincides or 'ON' the below polygon
#Test data - 1
def test_is_point_ON_poly():
    verify = PolyGon._is_point_in_poly((90,90),90,90,[(0,100),(100,100),(100,0),(0,0)])
    assert verify == True

## Test Data - 2
#polygon = [(0,100),(100,100),(100,0),(0,0)], POINT(100,100)
#point_x = 100, point_y = 100   -- Given function returns 'True' as expected

#Observation for the case:
# Changing the order of points in a POLYGON can have significant impact on current algorithm.
# For example, When running the given function for the following order of vertices of a below convex polygon(test data)
#[(0,0), (0,100), (100,0), (100,100)] against a point(90,90) - Given Function is returning 'False'



# Case: Test method Validating a given function for a point(9,0) that lies 'ON the edge/side' of the polygon
def test_is_point_lie_on_polygon():
    verify = PolyGon._is_point_in_poly((9,0),9,0,[(0,10),(10,10),(10,0),(0,0)])
    assert verify == True

#Observation for the case:
# So, Given function is not solving the above case. Even though, The point 9,0 is not inside the polygon
#[(0,10),(10,10),(10,0),(0,0)] It's on the edge. Points exactly on the edge
# can be considered IN or OUT depending on the current algorithm for the function. Ultimately,
# Type of the polygon also matters when using 'Ray Casting algorithm' approach to solve the current problem using given function

