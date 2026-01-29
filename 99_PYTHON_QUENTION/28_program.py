# You are given the length and width of a 4-sided polygon. The polygon can either be a rectangle or a square.
# If it is a square, print its area. If it is a rectangle, print its perimeter.

# Example(Input1, Input2 --> Output):

# 6, 10 --> 32
# 3, 3 --> 9


def area_or_perimeter(l,w):
    return l*w if l==w else 2*(l+w)





lenght = int(input("Enter the leght :"))
width = int(input("Enter the width :"))
print(area_or_perimeter(lenght,width))





























