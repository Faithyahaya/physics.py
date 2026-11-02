def final_velocity(u, a, t):
    return u + (a * t)

def displacement(u, a, t):

    return (u * t) + (0.5 * a * t ** 2)


def force(m, a):
    return m * a


def work_done(force, distance):
    return force * distance


def power(work, time):
    if time == 0:
        raise ValueError("Time cannot be zero")
    return work / time


print("Final Velocity:", final_velocity(10, 2, 4), "m/s")
print("Displacement:", displacement(10, 2, 4), "m")
print("Force:", force(5, 2), "N")
print("Work Done:", work_done(20, 5), "J")
print("Power:", power(100, 4), "W")
