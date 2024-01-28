from graphics import *
from math import sin, cos, pi, sqrt

def verify_points_distance(p1, p2):
    return sqrt((p2.getX() - p1.getX()) ** 2 + (p2.getY() - p1.getY()) ** 2)

#verifica um click dentro de um círculo
def verify_inside_click(circle, click):
    distance = verify_points_distance(circle.getCenter(), click)
    if distance <= circle.getRadius():
        return True
    return False

#verifica colisão entre dois círculos
def verify_colision_circles(circle, circle_2):
    centers_distance = verify_points_distance(circle.getCenter(), circle_2.getCenter())
    if centers_distance <= circle.getRadius() + circle_2.getRadius():
        return True
    return False

#verifica se um círculo está completamente dentro do outro
def verify_inside_circle(circle, circle_2):
    centers_distance = verify_points_distance(circle.getCenter(), circle_2.getCenter())
    if centers_distance <= abs(circle.getRadius() - circle_2.getRadius()):
        return True
    return False

#verifica colisão entre círculo e retângulo
def verify_colision_circle_rectangle(circle, rectangle):    
    for i in range(360):
        x = circle.getCenter().getX() + circle.getRadius() * cos(i * (pi / 180))
        y = circle.getCenter().getY() - circle.getRadius() * sin(i * (pi / 180))
        if x >= rectangle.getP1().getX() and x <= rectangle.getP2().getX():  
            if y >= rectangle.getP1().getY() and y <= rectangle.getP2().getY():
                return True
    return False

#verifica colisão entre círculo e linha
def verify_colision_circle_line(circle, line):
    point_1 = line.getP1()
    point_2 = line.getP2()
    circle_center = circle.getCenter()

    (p1x, p1y), (p2x, p2y), (cx, cy) = (point_1.getX(), point_1.getY()), (point_2.getX(), point_2.getY()), (circle_center.getX(), circle_center.getY())
    (x1, y1), (x2, y2) = (p1x - cx, p1y - cy), (p2x - cx, p2y - cy)
    dx, dy = (x2 - x1), (y2 - y1)
    dr = (dx ** 2 + dy ** 2)**.5
    big_d = x1 * y2 - x2 * y1
    discriminant = circle.getRadius() ** 2 * dr ** 2 - big_d ** 2
    
    if discriminant > 0:
        intersections = [
            (cx + (big_d * dy + sign * (-1 if dy < 0 else 1) * dx * discriminant**.5) / dr ** 2,
             cy + (-big_d * dx + sign * abs(dy) * discriminant**.5) / dr ** 2)
            for sign in ((1, -1) if dy < 0 else (-1, 1))]
        fraction_along_segment = [(xi - p1x) / dx if abs(dx) > abs(dy) else (yi - p1y) / dy for xi, yi in intersections]
        intersections = [pt for pt, frac in zip(intersections, fraction_along_segment) if 0 <= frac <= 1]

        if len(intersections) > 0:
            return True
    return False

#verifica colisão entre círculo e retângulo
def verify_colision_circle_rectangle2(circle, rectangle):
    p1 = rectangle.getP1()
    p2 = rectangle.getP2()

    poligono = Polygon(Point(p1.getX(), p1.getY()), Point(p2.getX(), p1.getY()), Point(p2.getX(), p2.getY()), Point(p1.getX(), p2.getY()))
    if verify_colision_circle_polygon(circle, poligono):
        return True
    return False
    
#verifica colisão entre círculo e polígono
def verify_colision_circle_polygon(circle, polygon):
    points = polygon.getPoints()
    for i in range(len(points)):
        point_1 = points[i]
        point_2 = points[(i + 1) % len(points)]
        if verify_colision_circle_line(circle, Line(point_1, point_2)):
            return True
    return False



