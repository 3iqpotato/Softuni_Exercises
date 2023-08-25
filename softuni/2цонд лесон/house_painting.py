house_height = float(input())
house_lenght = float(input())
house_height_roof = float(input())

# walls

side_wall_meters = house_height * house_lenght
window = 1.5 * 1.5
two_side_walls_meters = (side_wall_meters * 2) - (window * 2)
front_wall = house_height * house_height
front_door = 1.2 * 2
front_and_back_walls = (front_wall * 2) - front_door
full_area = front_and_back_walls + two_side_walls_meters
green_paint = full_area / 3.4

# roof
two_side_roofs = 2 * (house_height * house_lenght)
two_roof_triangles = 2 * (house_height_roof * house_height / 2)
full_area1 = two_roof_triangles + two_side_roofs
red_paint = full_area1 / 4.3

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")


