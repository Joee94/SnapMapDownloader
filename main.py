import getLocationJSON
import sys
import getVideoList
import downloadVideos
import concatenateVideoClips
from geopy.geocoders import Nominatim
geolocator = Nominatim()

location = raw_input("Location: ") 
epoch = raw_input("Epoch: ") 
output = raw_input("Output file: ") 
downloadNo = int(raw_input("Download Number: "))

location = geolocator.geocode(location)

getLocationJSON.GetJSON(location.latitude, location.longitude, epoch, output)

continueSelector = raw_input("Would you like to get the video list?: ")

if continueSelector != 'y':
	sys.exit()

downloadNo = getVideoList.getVideoListFromJSON(output)


continueSelector2 = raw_input("JSON file retrieved, Would you like to continue?: ")

if continueSelector2 != 'y':
	sys.exit()

downloadVideos.downloadVideos("videos.txt", downloadNo)

continueSelector2 = raw_input("Videos downloaded, Would you like to continue?: ")

if continueSelector2 != 'y':
	sys.exit()


concatenateVideoClips.concatenateClips(downloadNo)