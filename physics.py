
print("\n1. FINAL VELOCITY (v = u + at)")
u = float(input("Enter initial velocity (u): "))
a = float(input("Enter acceleration (a): "))
t = float(input("Enter time (t): "))

v = u + (a * t)
print("Final velocity =", v, "m/s")


print("\n2. DISPLACEMENT (s = ut + 1/2at²)")
u = float(input("Enter initial velocity (u): "))
a = float(input("Enter acceleration (a): "))
t = float(input("Enter time (t): "))

s = (u * t) + (0.5 * a * t ** 2)
print("Displacement =", s, "m")



print("\n3. FORCE (F = ma)")
m = float(input("Enter mass (m): "))
a = float(input("Enter acceleration (a): "))

F = m * a
print("Force =", F, "N")


print("\n4. WORK DONE (W = F × d)")
F = float(input("Enter force (F): "))
d = float(input("Enter distance (d): "))

W = F * d
print("Work done =", W, "J")


print("\n5. POWER (P = W/t)")
W = float(input("Enter work done (W): "))
t = float(input("Enter time (t): "))

if t != 0:
    P = W / t
    print("Power =", P, "W")
else:
    print("Time cannot be zero.")
