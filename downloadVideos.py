import urllib
test=urllib.FancyURLopener()

with open("videos.txt") as f:
	content = f.readlines()
	
content = [x.strip() for x in content] 

i = 0
for x in content:
	print x
	test.retrieve(x, str(i)+".mp4")
	i += 1
	if i >= 10:
		break