def calculate_experience_points(level):
    count = 0
    for i in range(0,level):
        count = count + i * 5
    return count
