class Color(object):
	def __init__(self, red, green, blue):
		self.red = red
		self.green = green
		self.blue = blue

	def getRed(self):
		"""
		returns the color's red value
		"""
		return self.red

	def getGreen(self):
		"""
		returns the color's green value
		"""
		return self.green

	def getBlue(self):
		"""
		returns the color's blue value
		"""
		return self.blue

	def __str__(self):
		return " ".join(map(str, [self.red, self.green, self.blue]))
		
		
class PortablePixMap(object):
	def __init__(self, magic_number, width, height, maxColorVal, pixelData):
		super().__init__()
		self._magic_number = magic_number
		self._width = width
		self._height = height
		self._area = width * height
		self._maxColorVal = maxColorVal
		self._pixelData = pixelData

	def _swap(self, array, index1, index2):
		"""
		swaps the two values at the respective indexes
		"""
		temp = array[index1]
		array[index1] = array[index2]
		array[index2] = temp

	def flip(self):
		"""
		flips the image vertically
		"""
		for i in range(self._height // 2):
			self._swap(self._pixelData, i, self._height - i - 1)

	def flop(self):
		"""
		flops the image horizontally
		"""
		for i in range(self._height):
			for j in range(self._width // 2):
				self._swap(self._pixelData[i], j, self._width - j - 1)

	def grayscale(self):
		"""
		converts the image to grayscale
		"""
		for row in self._pixelData:
			for i in range(len(row)):
				grayValue = int(row[i].getRed() * 0.2126 + 
					row[i].getGreen() * 0.7152 + row[i].getBlue() * 0.0722)
				row[i] = Color(grayValue, grayValue, grayValue)

	def __str__(self):
		"""
		returns a string representation of the object
		"""
		string = str(self._magic_number) + "\n"
		string += str(self._width) + " "
		string += str(self._height) + "\n"
		string += str(self._maxColorVal) + "\n"
		for row in self._pixelData:
			for pixel in row:
				string += str(pixel) + "\n"
		return string

class Scanner(object):
	def __init__(self, file_object):
		self.file = file_object
		self.buffer = list()
	
	def next_token(self):
		"""
		reads the next token in the file
		"""
		# there are no tokens left on the current line, so read in the next line
		if self.buffer == []:
			self.buffer = self.file.readline().split()
		# if there are still no tokens left, the file is empty
		if self.buffer == []:
			return None
		return self.buffer.pop(0)

	def next_int(self):
		"""
		reads the next int in the file
		"""
		token = self.next_token()
		if token != None:
			return int(token)


def read_ppm(filename):
	image = open(filename, "r")
	scan = Scanner(image)
	magic_number = scan.next_token()
	if magic_number != "P3":
		raise ValueError("invalid magic number")
	width = scan.next_int()
	if width < 0:
		raise ValueError("invalid width")
	height = scan.next_int()
	if height < 0:
		raise ValueError("invalid height")
	maxColorVal = scan.next_int()
	if maxColorVal < 0:
		raise ValueError("invalid maximum color value")
	pixelData = list()
	row = list()
	numPixels = 0
	while True:
		red = scan.next_int()
		if red == None:
			break
		if red < 0 or red > maxColorVal:
			raise ValueError("red color value out of bounds")
		green = scan.next_int()
		if green < 0 or green > maxColorVal:
			raise ValueError("green color value out of bounds")
		blue = scan.next_int()
		if blue < 0 or blue > maxColorVal:
			raise ValueError("blue color value out of bounds")
		row.append(Color(red, green, blue))
		if (numPixels + 1) % width == 0:
			pixelData.append(row)
			row = list()
		numPixels += 1
	if numPixels != width * height:
		raise ValueError("number of pixels does not match expected area")
	return PortablePixMap(magic_number, width, height, maxColorVal, pixelData)