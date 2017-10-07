import math


def sphere_vol_area():
    print("This function computes the volume and surface area of a sphere.")
    r = eval(input("What is the radius of the sphere?: "))

    vol = (4.0 / 3.0) * math.pi * r ** 3.0

    area = 4.0 * math.pi * r ** 2.0

    print("The volume of the sphere is " + str(round(vol, 4)) + " cubic units"
          " and the surface area of the sphere is " + str(round(area, 4)) + " square units.")
sphere_vol_area()
