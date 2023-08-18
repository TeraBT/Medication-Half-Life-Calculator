import math
import sys

def decay_function(n_0, half_life, t):
    decay_constant = math.log(2) / half_life
    return n_0 * math.pow(math.e, - decay_constant * t)

def medication_level_calc(dose, times_per_day, half_life, duration):
    med_level = 0
    meds_taken_hours = 24 // times_per_day
    for i in range(0, duration * 24):
        med_level = decay_function(med_level, half_life, i)
        if i % meds_taken_hours:
            med_level += dose


num_sys_args = len(sys.argv)
if sys.argv[1] == "-df" and num_sys_args == 5:
    n_0 = sys.argv[2]
    half_life = sys.argv[3]
    t = sys.argv[4]
    print(decay_function(n_0, half_life, t))
elif sys.argv[1] == "-mlc" and num_sys_args == 6:
    dose = sys.argv[2]
    times_per_day = sys.argv[3]
    half_life = sys.argv[4]
    duration = sys.argv[5]
else:
    print("""USAGE: %s -df n_0 half_life t
        OR: %s - n_0 half_life t""" % (sys.argv[0]))
    