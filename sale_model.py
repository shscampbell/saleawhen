import numpy as np
# from scipy import interpolate
from scipy.optimize import minimize_scalar

# quantiles = np.array([1, 2, 3, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60,
#     65, 70, 75, 80, 85, 90, 95, 97, 98, 99, 99.3, 99.6, 99.9, 99.93, 99.96,
#     99.99])
# dom = np.array([1, 3, 4, 7, 9, 11, 13, 14, 16, 18, 20, 23, 27, 30, 35, 40, 46,
#     52, 60, 70, 83, 105, 124, 141, 173, 193, 228, 313, 349, 393, 598])
# dominterp = interpolate.interp1d(quantiles, dom)

# def saletimeCalgary(quantile):
#     return round(float(dominterp(quantile)))

def gompertzsurv(time, rate, shape):
    f1 = np.exp(shape * time)
    ex = -rate / shape * (f1 - 1)
    return np.exp(ex)

def saletimeCalgary(month, brag, bath, sqft, tax, age, isapt, isflood, isfence,
                    ishottub, iscurts, isvinyl, isnctile, isnopet, quantile):
    # regression constants of the model
    shape = 0.00213
    rate = 0.0196
    rrmonth2 = 0.052
    rrmonth3 = 0.208
    rrmonth4 = 0.107
    rrmonth8 = -0.124
    rrmonth9 = -0.293
    rrmonth10 = -0.423
    rrmonth11 = -0.279
    rrbrag0 = -0.941
    rrbath0 = 0.57
    rrbath2 = 0.0789
    rrbath3 = 0.07
    rrsqft = -0.000155
    rrltax = 0.0264
    rrage = 0.0019
    rrapt = -0.354
    rrvinyl = 0.0656
    rrnctile = -0.0447
    rrflood = -0.175
    rrnopet = -0.0521
    rrhottub = 0.266
    rrcurts = 0.0973
    rrfence = 0.128

    # Calculate the linear regression parameter.
    regpar = 0
    if month == 2:
        regpar += rrmonth2
    if month == 3:
        regpar += rrmonth3
    if month == 4:
        regpar += rrmonth4
    if month == 8:
        regpar += rrmonth8
    if month == 9:
        regpar += rrmonth9
    if month == 10:
        regpar += rrmonth10
    if month == 11:
        regpar += rrmonth11
    if brag == 0:
        regpar += rrbrag0
    if bath == 0:
        regpar += rrbath0
    if bath == 2:
        regpar += rrbath2
    if bath == 3:
        regpar += rrbath3
    regpar += sqft * rrsqft
    if tax == 0:
        ltax = 0
    else:
        ltax = np.log(tax)
    regpar += ltax * rrltax
    regpar += age * rrage
    regpar += isapt*rrapt + isflood*rrflood + isfence*rrfence + \
        ishottub*rrhottub + iscurts*rrcurts + isvinyl*rrvinyl + \
        isnctile*rrnctile + isnopet*rrnopet
    regpar = np.exp(regpar)
    # The reference survival function
    refsurv = (1 - quantile/100)**(1/regpar)
    time = minimize_scalar(lambda t: abs(refsurv-gompertzsurv(t, rate, shape)),
                           method='brent')
    return round(time.x)
