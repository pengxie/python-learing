tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print "xie\apeng"
print "abcdef\rde" # \r is a return,anwser: dec
print "=" * 10
print "xie\fpeng" #\f fen ye fu
a = 0
while (a < 2):
	for i in ["xie","peng","wo","ai","ni"]:
		print "%s\t" % i
		a = a + 1
