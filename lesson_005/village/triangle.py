
import simple_draw as sd

#___________КРЫША ДОМА_________

def triangle(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 150, length=length-127, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 210, length=length-127, width=3)
    v3.draw()


point_0 = sd.get_point(150, 325)
triangle(point=point_0, angle=0, length=300)
sd.pause()