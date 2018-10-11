import numpy as np
from scipy import interpolate

quantiles = np.array([1, 2, 3, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60,
    65, 70, 75, 80, 85, 90, 95, 97, 98, 99, 99.3, 99.6, 99.9, 99.93, 99.96,
    99.99])
dom = np.array([1, 3, 4, 7, 9, 11, 13, 14, 16, 18, 20, 23, 27, 30, 35, 40, 46,
    52, 60, 70, 83, 105, 124, 141, 173, 193, 228, 313, 349, 393, 598])
dominterp = interpolate.interp1d(quantiles, dom)

# def saletimeCalgary(quantile):
#     return round(float(dominterp(quantile)))

def saletimeCalgary(month, brag, bath, sqft, tax, age, isapt, isflood, isfence,
                    ishottub, iscurts, isvinyl, isnctile, quantile):
    # regression constants of the model

    return round(float(dominterp(quantile)))
