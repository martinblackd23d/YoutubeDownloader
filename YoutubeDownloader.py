import youtube_dl
#import time
import threading

dl_dir = 'C:\\Users\\Martin\\Desktop\\ydl\\'


class ydl_logger(object):
	def debug(self, msg):
		msglist = msg.split(' ')
		for i in msglist:
			if 'B/s' in i:
				ilist = i.split('.')
				rates.append(int(ilist[0]))
				print(ilist[0])
	def Udebug(self, msg):
		print(msg)
	def warning(self, msg):
		print(msg)
	def error(self, msg):
		print(msg)

def ydl_hook(d):
	#print(d['status'])
	if d['status'] == 'finished':
		print('Done downloading, now converting...')

ydl_opts = {
	'format': 'bestaudio/best',
#	'download_archive': dl_dir + 'downloaded_songs.txt',comment out later
	'outtmpl': dl_dir + '%(title)s.%(ext)s',
	'postprocessors': [{
		'key': 'FFmpegExtractAudio',
		'preferredcodec': 'mp3',
		'preferredquality': '192'
		}],
	'logger': ydl_logger(),
	'progress_hooks': [ydl_hook]
	}




def process_query(query):
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		return ydl.extract_info(f'ytsearch:{query}', download=False)['entries'][0]['webpage_url']

#dl_query('how to train your dragon soundtrack')


def dl_url(url):
	#start = time.time()
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([url])
		#info = ydl.extract_info(url, download=False)
	#end = time.time()
	#print('Finished downloading')
	#print(url)
	#print(info['title'])
	#print('Time taken: ' + str(end - start) + ' s')


#dl_url('https://www.youtube.com/watch?v=LDU_Txk06tM')
#print(process_query('crab rave'))

def download_playlist(url):
	list = []
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		info = ydl.extract_info(url, download=False)
	ydl_opts['outtpml'] = dl_dir + info['title'] +'\\%(title)s.%(ext)s'
	print(ydl_opts['outtpml'])
	#return
	for i in info['entries']:
		list.append(i['webpage_url'])
	#print(list)
	threads = []
	#print(list)
	for i in list:
		#print(i)
		x = threading.Thread(target = dl_url, args = (i,))
		threads.append(x)
		x.start()
	for i in threads:
		i.join()
	print('all downloads completed')

download_playlist('https://www.youtube.com/playlist?list=OLAK5uy_kEdVyJVdqM3RLBPquQh37hTq0VfAlumDE')