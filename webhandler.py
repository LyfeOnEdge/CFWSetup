#githubgrabber
import sys, os
import json
import webbrowser
import urllib.request 
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)

def get_path(filename):
	return os.path.join(sys.path[0], filename)

def joinpaths(prefix,suffix):
	return os.path.join(prefix,suffix)
downloadsfolder = get_path("downloads")

if not os.path.exists(downloadsfolder):
	os.mkdir(downloadsfolder)

def downloadfile(url,target):
	urllib.request.urlretrieve(url, target)

#get jason, add and update keywords if json download successfully
json_file_list = []
def getUpdatedSoftwareLinks(dicttopopulate):
	for softwarechunk in dicttopopulate:
		githubjsonlink = softwarechunk["githubapi"]
		softwarename = softwarechunk["software"]
		if githubjsonlink == None:
			print("direct download, skipping {}".format(softwarename))
			softwarechunk["gotjson"] = True,
		else:
			downloadas = joinpaths(downloadsfolder, softwarename + ".json")
			try:
				urllib.request.urlretrieve(githubjsonlink,downloadas)
				print("Successfully downloaded {} to {}".format(githubjsonlink, downloadas))
				json_file_list.append(softwarename)
				softwarechunk["gotjson"] = True,
				with open(downloadas) as json_file:
					assetsmember = 0
					if softwarename == "Kosmos":
						assetsmember = 1  #hacky way to get the right asset for kosmos, will deal with a assestnumber keyword later
					jfile = json.load(json_file)
					try:
						githubasset = softwarechunk["asset"]
						softwarechunk["directlink"] = jfile["assets"][githubasset]["browser_download_url"]
						if softwarechunk["image"] == None:
							softwarechunk["image"] = jfile["author"]["avatar_url"]
					except:
						print("Failed to add directlink for {}".format(softwarename))

			except:
				print("failed to download json for {}".format(softwarename))
				exists = os.path.isfile(downloadas)
				if exists:
					print("Falling back on older version")
					with open(downloadas) as json_file:
						assetsmember = 0
						if softwarename == "Kosmos":
							assetsmember = 1 #hacky way to get the right asset for kosmos, will deal with a assestnumber keyword later
						jfile = json.load(json_file)
						try:
							githubasset = softwarechunk["asset"]
							softwarechunk["directlink"] = jfile["assets"][githubasset]["browser_download_url"]
							softwarechunk["softwaredownloaded"] = ["fallback"],
							if softwarechunk["image"] == None:
								softwarechunk["image"] = jfile["author"]["avatar_url"]
						except:
							print("Failed to add directlink for {}".format(softwarename))
				else:
					print("no fallback version for {} software will be unavailable".format(softwarename))
					softwarechunk["softwaredisabled"] = True,


	return dicttopopulate

# for testing
def fillStringWithoutDownloading(dicttopopulate):
	for softwarechunk in dicttopopulate:
		githubjsonlink = softwarechunk["githubapi"]
		softwarename = softwarechunk["software"]
		softwarechunk["gotjson"] = True,
		if githubjsonlink == None:
			print("direct download, skipping {}".format(softwarename))
		else:
			downloadas = joinpaths(downloadsfolder, softwarename + ".json")
			json_file_list.append(softwarename)

			try:
				with open(downloadas) as json_file:
					assetsmember = 0
					if softwarename == "Kosmos":
						assetsmember = 1 #hacky way to get the right asset for fusee-primary.bin, will probably add an assetsmember tag to the dictionaries
					jfile = json.load(json_file)
					try:
						githubasset = softwarechunk["asset"]
						softwarechunk["directlink"] = jfile["assets"][githubasset]["browser_download_url"]
						softwarechunk["image"] = jfile["author"]["avatar_url"]
						if softwarechunk["image"] == None:
							softwarechunk["image"] = jfile["author"]["avatar_url"]
					except:
						print("Failed to add directlink for {}".format(softwarename))
			except:
				print("Json not available, {}".format(softwarename))
				softwarechunk["softwaredisabled"] = True,
	return dicttopopulate
