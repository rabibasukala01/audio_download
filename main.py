import youtube_dl
import pafy


with open("links.txt", 'r') as f:
    urls = f.readlines()

for index, url in enumerate(urls):
    result = pafy.new(url)
    audio = result.getbestaudio()
    audio.download()
    print(f"\n{index+1}/{len(urls)}=============DONE\n")
   # print("ALL DONE")
