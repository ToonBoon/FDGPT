import math
from math import pi


class Node(object):
    def __init__(self, id, weight=0, data={}):
        self.id = id
        self.w = weight
        self.data = data
        self.children = []

    def addChild(self, child):
        self.children.append(child)

    def __str__(self):
        return "i%d w%d : %s" % (self.id, self.w, [n.id for n in self.children])

    def __repr__(self):
        return "%s" % self


class Rectangle(object):

    def __init__(self, c, x, y, t):
        self.c = c
        self.x = x
        self.y = y
        self.t = t

    def offsetcenter(self, dx, dy, dt, rc, zoom):
        #print('Old values for rect (' + str(self.c[0]) + ', ' + str(self.c[1]) + ')')
        # rotate around rc
        cx = self.c[0] - rc[0]
        cy = self.c[1] - rc[1]
        newx = cx * math.cos(dt) - cy * math.sin(dt)
        newy = cx * math.sin(dt) + cy * math.cos(dt)
        # translate back and apply dx, dy
        newx *= zoom
        newy *= zoom
        newx += dx + rc[0]
        newy += dy + rc[1]
        #print('New values for rect (' + str(newx) + ', ' + str(newy) + ')')

        return (newx, newy)

    def draw(self, arcade, dx, dy, dt, rx, ry, zoom):
        arcade.draw_rectangle_filled(
            *self.offsetcenter(dx, dy, dt, (rx, ry), zoom),
                self.x * zoom,
                self.y * zoom,
                color=(255, 0, 0, 100),
                tilt_angle=(pi/2 - self.t + dt)*180/3.141592)

    def __str__(self):
        return "c%d,%d x%d y%d t%f" % (*self.c, self.x, self.y, self.t)

    def __repr__(self):
        return "%s" % self
