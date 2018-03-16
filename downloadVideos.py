import urllib

def downloadVideos(videosFile, downloadNo):
	test=urllib.FancyURLopener()

	with open(videosFile) as f:
		content = f.readlines()
		
	content = [x.strip() for x in content] 

	i = 0
	for x in content:
		print x
		test.retrieve(x, str(i)+".mp4")
		i += 1
		if i >= downloadNo:
			break