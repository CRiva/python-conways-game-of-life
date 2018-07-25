from graphics import *
import time
from math import *
from random import *

WIDTH = 750
HEIGHT = 750
NODE_DIAMETER = 5
NODE_RADIUS = NODE_DIAMETER/2
ROW_LENGTH = WIDTH/NODE_DIAMETER
COLUMN_LENGTH = HEIGHT/NODE_DIAMETER


class Node():

    def __init__(self, status, x, y, circle):
        self.status = status
        self.x = x
        self.y = y
        self.circle = circle

    def step(self):
        neighbors = self.count_neighbors()
        if self.status == 3:
            if neighbors == 8:
                self.status = 1
                self.circle.setFill(color_rgb(0, 255, 0))
            if neighbors == 6:
                self.status = 2
                self.circle.setFill(color_rgb(255, 0, 0))
        if self.status == 2:
            if neighbors > 4:
                self.status = 1
                self.circle.setFill(color_rgb(0, 255, 0))
        if self.status == 1:
            if neighbors < 2:
                self.status = 0
                self.circle.setFill(color_rgb(0, 0, 0))
            if neighbors > 3:
                self.status = 0
                self.circle.setFill(color_rgb(0, 0, 0))
            if neighbors > 3 and neighbors < 7:
                self.status = 3
                self.circle.setFill(color_rgb(0, 0, 255))
        elif self.status == 0:
            if neighbors == 3:
                self.status = 1
                self.circle.setFill(color_rgb(0, 255, 0))
            if neighbors > 5:
                self.status = 2
                self.circle.setFill(color_rgb(255, 0, 0))
        return self.status

    def count_neighbors(self):
        count = 0
        for i in range(-1, 2, 1):
            for j in range(-1, 2, 1):
                # print "My node is (%s, %s), checking location is (%s, %s) and my status is %s" % (self.x, self.y, (self.x+i), (self.y+j), MAP[i][j].status)
                if i == 0 and j == 0:
                    continue
                if MAP[(self.x+i) % ROW_LENGTH][(self.y+j) % COLUMN_LENGTH].status > 0:
                    count += 1
        return count


def make_map():
    tmp = []
    for i in range(ROW_LENGTH):
        tmp.append([])
        for j in range(COLUMN_LENGTH):
            status = int(round(random() * .55))
            pt1 = Point(i*(NODE_DIAMETER), j*(NODE_DIAMETER))
            pt2 = Point(i*(NODE_DIAMETER)+NODE_DIAMETER, j*(NODE_DIAMETER)+NODE_DIAMETER)
            cir = Rectangle(pt1, pt2)
            if status == 0:
                cir.setFill(color_rgb(0, 0, 0))
            else:
                cir.setFill(color_rgb(0, 255, 0))
            tmp[i].append(Node(status, i, j, cir))
    return tmp


MAP = make_map()


# for row in MAP:
#     print(["%s, %s" % (node.x, node.y) for node in row])


def setup_window():
    win = GraphWin("My Window", WIDTH, HEIGHT, autoflush=False)
    win.setBackground(color_rgb(0, 0, 0))
    return win


def update_players(window):
    for row in MAP:
        for node in row:
            node.circle.draw(window)


def main(steps):
    window = setup_window()
    update_players(window)
    step = 0
    while step < steps:
        for row in MAP:
            for node in row:
                node.step()
        update(10)
        step += 1


main(1000)
