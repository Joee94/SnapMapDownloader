import moviepy.editor as mp
with open("videos.txt") as f:
	content = f.readlines()
	
content = [x.strip() for x in content] 

clips = []

for i in content:
	clips.append(mp.VideoFileClip(i))

concat_clip = mp.concatenate_videoclips(clips)
concat_clip.write_videofile("final.mp4")