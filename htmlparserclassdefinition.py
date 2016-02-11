from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
	def __init__ (self, filename):
		self.reset()
		self.fileobj = open(filename, "w")
	def handle_data(self, data):
	    if (data != "\n"):
    		self.fileobj.write(data)

heb = open("output.html", "r")
html = heb.read()
filename = "textout.txt"
parser = MyHTMLParser(filename)
parser.feed(html)
parser.fileobj.close()

