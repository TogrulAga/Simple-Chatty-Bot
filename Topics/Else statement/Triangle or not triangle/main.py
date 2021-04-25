angle_1 = int(input())
angle_2 = int(input())
angle_3 = int(input())

angles = [angle_1, angle_2, angle_3]

print("The triangle is valid!" if sum(angles) == 180 else "The triangle is not valid!")
