import moviepy.editor as mp

def concatenateClips(downloadNo):
	#with open("videos.txt") as f:
	#	content = f.readlines()
	#	
	#content = [x.strip() for x in content] 

	content = map(str, range(downloadNo))
	content = [s + '.mp4' for s in content]
	print content

	clips = []

	for i in content:
		clips.append(mp.VideoFileClip(i))
		clips[-1].resize((360, 640))

	concat_clip = mp.concatenate_videoclips(clips, method='compose')
	concat_clip.write_videofile("final.mp4", fps=60)
