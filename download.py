import os, sys
file_path = 'pytube_module/'
sys.path.append(os.path.dirname(file_path))
from pytube import YouTube

#video storage location
store_location = 'downloaded_videos'  #enter the folder path where you want to store the video

#Asking for video link from the user
link = input("Enter the video link here: ")

#validating user input
if len(link) < 1 :
	print("Please enter a link.")
	exit()

print("Getting information.... Please Wait")
yt = YouTube(link)

#getting all the stream quality in a list
all_videos_quality = yt.streams.filter(progressive=True).order_by('resolution')

#displaying all the available stream quality to the user
i = 1
for video in all_videos_quality:
	print('['+str(i)+']',video)
	i += 1

#getting user input about downloading the stream quality
stream_quality_index = int(input("Enter the number corresponds to the stream quality you want to download: "))

#starting the downloading
print("=========Starting Download=======")
all_videos_quality[stream_quality_index-1].download(store_location)
print("=========Download Finished=======")

#displaying proper message to the user where to look for the video after downloaded.
print("Check " + store_location + " folder for the video.")