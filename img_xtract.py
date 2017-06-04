import urllib.request as u
import re
from time import sleep as s
import math as M
from sys import *
import random

print("\n\t\t\t --- XKCD Image Downloader --- \n")
n = int(input('\nEnter number of random images to download : '))

if n > 20:
	print("\nLimit exceeded ! Try next time !\n")
	exit()

url = "https://xkcd.com/"

num = M.floor(random.random()*(n*20))+1					#Generate random number for image url

name = 'pic'

for i in range(n):
	num+=i
	url += str(num)
	try:	
		data = u.urlopen(url).read()
		newdata = data.decode("utf")
	except u.HTTPError:
		print("\nSorry, File does not exist !")			#if any HTTP errors occured
	m = re.search('embed',newdata)
	start = m.end()+7
	
	m1 = re.search('<div id="transcript',newdata)
	end = m1.start()-1
	
	url = url.replace(str(num),'')
	if '.jpg' in newdata[start:end]:
		u.urlretrieve(newdata[start:end],(name+str(i+1)+'.jpg'))		#Download and save the image as local .jpg file
	else:
		u.urlretrieve(newdata[start:end],(name+str(i+1)+'.png'))		#Download and save the image as local .png file
	print("\nSuccessfully downloaded pic"+str(i+1)+" !")
print('\n')
