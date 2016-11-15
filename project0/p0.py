##########################
#
# p0.py
# creates a PPM image file
# 
# Austin Schey
# CS 250-001
# 1/8/2014
# 
##########################


import sys

def main():
    height = int(sys.argv[1])
    if height <= 1280:
        print_ppm(height)
    else:
        print("The image must be at most 1280 pixels high!", file=sys.stderr)


def print_ppm(height):
    width = height * 2
    maxCrimsonIndex = height
    maxWhiteIndex = width
    blackIndex = 0
    with open("image.ppm", "w") as f:
        f.write("P3\n")
        f.write(str(width) + " " + str(height) + "\n")
        f.write("255\n")

        for i in range(height):
            for j in range(width):
                if j == blackIndex or j == blackIndex + height:
                    f.write("0 0 0 \n")
                elif j < maxCrimsonIndex:
                    f.write("134 0 0 \n")
                elif j < maxWhiteIndex:
                    f.write("255 255 255 \n")
                else:
                    f.write("128 128 128 \n")
    
            maxCrimsonIndex -= 1
            maxWhiteIndex -= 1
            blackIndex += 1


main()
