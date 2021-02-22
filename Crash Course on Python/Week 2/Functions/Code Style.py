#This function to calculate the area of a rectangle is not very readable. Can you refactor it, and then call the function to calculate the area with base of 5 and height of 6?

def rectangle_area(base, height):
	# the area is base*height
	area = base*height  
	print("The area is " + str(area))

rectangle_area(5, 6)