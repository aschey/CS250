from image import read_ppm, PortablePixMap
from sys import argv, stderr
def main():
	if len(argv) < 2:
		print("Usage: python3 main.py [options] <filename>")
		print("Options include: flip, flop, grayscale")
		exit()
	options = ["flip","flop","grayscale"]
	image = read_ppm(argv[-1])
	if len(argv) > 2:
		for i in argv[1:-1]:
			if i not in options:
				print("Error: invalid option", file=stderr)
				exit()
	if options[0] in argv:
		image.flip()
	if "flop" in argv:
		image.flop()
	if "grayscale" in argv:
		image.grayscale()
	print(image)
if __name__ == '__main__':
	main()
