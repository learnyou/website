# This file was *autogenerated* from the file nq-bijection.sage
from sage.all_cmdline import *   # import sage library
_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_6 = Integer(6); _sage_const_4 = Integer(4); _sage_const_100 = Integer(100); _sage_const_0p0 = RealNumber('0.0'); _sage_const_0p2 = RealNumber('0.2'); _sage_const_0p4 = RealNumber('0.4'); _sage_const_15 = Integer(15); _sage_const_0p03 = RealNumber('0.03'); _sage_const_20 = Integer(20); _sage_const_156 = Integer(156)#!/usr/bin/env sage

import numpy as np

class Point:
    def __init__(self, x, y, derivative):
        self.x = x
        self.y = y
        self.derivative = derivative

def quadrant(x,y):
    if (_sage_const_0  < x) and (_sage_const_0  < y):
        return _sage_const_1 
    elif (_sage_const_0  > x) and (_sage_const_0  < y):
        return _sage_const_2 
    elif (_sage_const_0  > x) and (_sage_const_0  > y):
        return _sage_const_3 
    elif (_sage_const_0  < x) and (_sage_const_0  > y):
        return _sage_const_4 
    else:
        return _sage_const_1 

def rotate90(x, y):
    matr = [[_sage_const_0 , -_sage_const_1 ], [_sage_const_1 , _sage_const_0 ]]
    matrresult = list(np.dot([x,y], matr))
    return matrresult

def nq(n):
    if n == _sage_const_0 :
        return Point(_sage_const_0 , _sage_const_1 , (_sage_const_1 , _sage_const_0 ))
    else:
        oldpoint = nq(n-_sage_const_1 ) 
        corner = abs(oldpoint.x) == abs(oldpoint.y)
        if quadrant(oldpoint.x, oldpoint.y) == _sage_const_2 :
            corner = oldpoint.y + oldpoint.x == _sage_const_1 
        odx, ody = oldpoint.derivative
        if corner:
            (dx, dy) = list(rotate90(*oldpoint.derivative))
        else:
            (dx, dy) = oldpoint.derivative
        newcoords = (oldpoint.x + dx, oldpoint.y + dy)
        return Point(newcoords[_sage_const_0 ], newcoords[_sage_const_1 ], (dx, dy))

points = []                     # Empty list of points
labels = []                     # Empty list of labels
point_color='red'
label_color='black'
line_color='blue'
font_size=_sage_const_15 
my_ticks=[range(-_sage_const_100 ,_sage_const_100 )] * _sage_const_2 
my_pointsize=_sage_const_100 
my_x_arrowcut=_sage_const_0p0 
my_y_arrowcut=_sage_const_0p0 
my_arrowcut=_sage_const_0p2 
my_arrowparams={
    'color': line_color,
    'width': _sage_const_2 ,
    'arrowsize': _sage_const_4 ,
}

# We're going to use a pretty limited set of inputs, from 0 to 10,
# inclusive
fake_x = _sage_const_0 
for x in range(_sage_const_0 , _sage_const_156 ):
    # We're going to append the vector (x, q(x)) to the list of
    # points.
    point = nq(fake_x)
    if point.y == _sage_const_0 :
        fake_x = fake_x + _sage_const_1 
        point=nq(fake_x)
    points.append((point.x, point.y))

    # Next, we need to create a label
    t = text('$' + str(point) + '$',
             (point.x+_sage_const_0p03 , point.y-_sage_const_0p4 ),
             rgbcolor=label_color,
             fontsize=_sage_const_20 ,
             horizontal_alignment='left'
            )
    labels.append(t)        # Add the label to the list
    fake_x = fake_x + _sage_const_1 

print(points)

# Next, we need to plot the points
plt = list_plot(points,
                pointsize=my_pointsize,
                ticks=[_sage_const_1 ,_sage_const_1 ],
                color=point_color,
                axes_labels=['x', 'y']
               )

lines = list_plot(points, plotjoined=True, color=line_color)
# for a in range(1, len(points)):
#     thispoint = points[a]
#     prevpoint = points[a-1]
#     x_difference = thispoint[0] - prevpoint[0] 
#     y_difference = thispoint[1] - prevpoint[1]
#     new_prevpoint,new_thispoint = list(prevpoint),list(thispoint)

#     if x_difference < 0:
#         new_prevpoint[0] = prevpoint[0] - my_x_arrowcut
#         new_thispoint[0] = thispoint[0] + my_x_arrowcut
#     elif x_difference > 0:
#         new_prevpoint[0] = prevpoint[0] + my_x_arrowcut
#         new_thispoint[0] = thispoint[0] - my_x_arrowcut
#     elif y_difference < 0:
#         new_prevpoint[1] = prevpoint[1] - my_y_arrowcut
#         new_thispoint[1] = thispoint[1] + my_y_arrowcut
#     elif y_difference > 0:
#         new_prevpoint[1] = prevpoint[1] + my_y_arrowcut
#         new_thispoint[1] = thispoint[1] - my_y_arrowcut
#     lines.append(arrow(new_prevpoint, new_thispoint,
#                        **my_arrowparams))

plt.fontsize(font_size)
(plt+lines).save("nq-bijection.png")
plt.save("nq-bijection-nolines.png")

t = var('t')
naive = sum([arrow((i+my_arrowcut,_sage_const_1 ), (i+_sage_const_1 -my_arrowcut, _sage_const_1 ),
                   **my_arrowparams) for i in range(_sage_const_0 ,_sage_const_6 )])
q = plt+naive
q.set_axes_range(xmax=_sage_const_6 )
q.save('nq-bijection-naive.png')
