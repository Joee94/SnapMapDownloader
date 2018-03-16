import json

def getVideoListFromJSON(fileName):
	data = json.load(open(fileName))


	text_file = open("videos.txt", "w")
	for item in data["manifest"]["elements"]:
		video = item["snapInfo"]["streamingMediaInfo"]["prefixUrl"] + "media.mp4\n"
		print video
		text_file.write(video)		

		
	text_file.close()