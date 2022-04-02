

from requests import get
from bs4 import BeautifulSoup
import requests
import random
import re

user_agent_list = [
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0'
]

user_agent = random.choice(user_agent_list)
headers = {'User-Agent': user_agent}


def scrape_videos(url):

	req = requests.get(url)
	send = BeautifulSoup(req.text, "html.parser")
	search = send.find_all("script")
	key = '"videoId":"'
	data = re.findall(key + r"([^*]{11})", str(search))

	return data

if __name__ == "__main__":
	url = str(input("Paste link: "))
	name = str(input("Set name: "))
	vid = scrape_videos(url)
	vid = vid[::3]
	vid = vid[:-1]


	with open (name + ".m3u8", "a", encoding="utf-8") as files:
		files.write(str('#EXTM3U' + '\n'))

	for i, id in enumerate(vid, start = 1):
		url = 'https://www.youtube.com/watch?v=' + id
		print(url)
		r = get(url).text
		soup = BeautifulSoup(r, "html.parser")
		tile = soup.title.string
		title = tile[:len(tile)-10]

		with open (name + ".m3u8", "a", encoding="utf-8") as files:
			files.write(str('\n' + '#EXTINF:' + str(i) + ', ' + title + '\n' + 'https://www.youtube.com/watch?v=' + id + '\n'))
print('Done)')
	

	