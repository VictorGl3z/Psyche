def area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area


sword_length = 1.0
axe_length = 0.5
spear_length = 2.0

# don't touch above this line

sword_area = area_of_circle(sword_length)
axe_area = area_of_circle(axe_length)
spear_area = area_of_circle(spear_length)

# don't touch below this line

print("Sword length:", sword_length, "meters.")
print("Sword attack area:", sword_area, "square meters")

print("Axe length:", axe_length, "meters.")
print("Axe attack area:", axe_area, "square meters")

print("Spear length:", spear_length, "meters.")
print("Spear attack area:", spear_area, "square meters")
