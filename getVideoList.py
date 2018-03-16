import json

data = json.load(open('20180316-125121.txt'))


text_file = open("videos.txt", "w")
for item in data["manifest"]["elements"]:
	video = item["snapInfo"]["streamingMediaInfo"]["prefixUrl"] + "media.mp4\n"
	print video
	text_file.write(video)		

	
text_file.close()