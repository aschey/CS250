class XmlFinder(object):
	def __init__(self, filename):
		self._filename = filename
		self._file = None

	def find(self, tag):
		self._file = open(self._filename, "r")
		return self._find_helper(tag)

	def _find_helper(self, tag, result=" "):
		if result == tag:
			return True
		nextChar = self._file.read(1)
		if nextChar == "":
			return False
		if result[-1] == ">":
			result = ""
		return self._find_helper(tag, result.strip()+nextChar)

def main():
	xf = XmlFinder("test.xml")
	print(xf.find("<to>"))
	print(xf.find("</note>"))
	print(xf.find("</to>"))
	print(xf.find("<note>"))
	print(xf.find("</to/>"))

if __name__ == '__main__':
	main()	