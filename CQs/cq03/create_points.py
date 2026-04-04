from point import Point  #from file import object

init_point: Point = Point(2.0, 4.0)
# create a base point to test

New_Point: Point = init_point.scale(2)
print(init_point.x, init_point.y)
print(New_Point.x, New_Point.y)
init_point.scale_by(55)
print(init_point.x, init_point.y)
# Test Non-Mutating (scale)
