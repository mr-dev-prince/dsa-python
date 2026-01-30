# if a string is concatenated with itself, the resulting string contains all the rotations of that string
# abc : rotations = [cab, bac, abc] --> abcabc

def rotate(s, goal):
    news = s + s
    return goal in news