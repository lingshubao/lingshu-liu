import numpy as np
import Polygon as plg


def get_union(pa, pb):
    pa_area = pa.area()
    pb_area = pb.area()
    return pa_area + pb_area - get_intersection(pa, pb)


def get_intersection(pa, pb):
    pInt = pa & pb
    if len(pInt) == 0:
        return 0
    else:
        return pInt.area()


a = np.array([103, 825, 103, 987, 726, 987, 726, 825])
b = np.array([101, 828, 731, 828, 731, 996, 101, 996])

poly_a = plg.Polygon(a.reshape(-1, 2))
poly_b = plg.Polygon(b.reshape(-1, 2))

union = get_union(poly_a, poly_b)
inter = get_intersection(poly_a, poly_b)
IOU = inter / (union + 1e-6)
print(IOU)

