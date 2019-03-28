#githubgrabber
import sys, os
import json

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

HELPLINK = "https://guide.sdsetup.com/"






	# {
	# "software" : software name
	# "githubapi": http://api.github.com/repos/AUTHOR/REPO/releases/latest
	# "projectpage": Main thread / page about project
	# "directlink": Only use this if there is a static up-to-date location or no github api
	# "subfolder" : the subfolder to install to
	# "author" : project author
	# "description" : project description
	# "group" : CFW, TITLEINSTALLER, REC, HOMEBREW, or EMULATORS
	# "uptodate": True or False, True if always up to date (static link or github api)
	# },

	# {
	# "software":  
	# "githubapi":
	# "projectpage":
	# "directlink":
	# "subfolder":
	# "author":
	# "description":
	# "group":
	# "uptodate":
	# },

SOFTWARELOCATIONS = [
#CFW
	{
	"software": "Kosmos",
	"githubapi": "https://api.github.com/repos/AtlasNX/Kosmos/releases/latest",
	"projectpage": "https://github.com/AtlasNX/Kosmos/releases",
	"directlink": None,
	"subfolder": None,
	"author": "AtlasNX",
	"description": "All-in-One CFW Package for the Nintendo Switch - previously SDFilesSwitch",
	"group": "CFW",
	"uptodate": True,
	"softwaredisabled": False,
	},

	{
	"software": "Atmos",
	"githubapi": "https://api.github.com/repos/Atmosphere-NX/Atmosphere/releases/latest",
	"projectpage":"https://github.com/Atmosphere-NX/Atmosphere/releases",
	"directlink": None,
	"subfolder": None,
	"author": "SciresM",
	"description": "Atmosphère is a customized firmware for the Nintendo Switch.",
	"group": "CFW",
	"uptodate": True,
	"softwaredisabled": False,
	},


#Title Installers
	{
	"software": "Tinfoil (blawar)",
	"githubapi": None,
	"projectpage": "https://tinfoil.io",
	"directlink": "http://tinfoil.io/repo/tinfoil.latest.zip",
	"subfolder": None,
	"author": "blawar",
	"description": "Nintendo Switch Title Installer, now with .xci installation support!",
	"group": "TITLEINSTALLER",
	"uptodate": True,
	"softwaredisabled": False,
	},

	{
	"software": "Lithium (blawar)",
	"githubapi": None,
	"projectpage": "https://tinfoil.io",
	"directlink": "http://tinfoil.io/repo/lithium.latest.zip",
	"subfolder": None,
	"author": "blawar",
	"description": "Slim Nintendo Switch Title Installer, now with .xci installation support!",
	"group": "TITLEINSTALLER",
	"uptodate": True,
	"softwaredisabled": False,
	},

	{
	"software":"Tinfoil (addubz)",
	"githubapi": None,
	"projectpage": "https://github.com/Adubbz/Tinfoil",
	"directlink": "https://bsnx.lavatech.top/tinfoil/tinfoil-883e3bd.zip",
	"subfolder": "switch",
	"author": "addubz",
	"description": "Nintendo Switch Title Installer",
	"group": "TITLEINSTALLER",
	"uptodate": False,
	"softwaredisabled": False,
	},

	{
	"software": "Goldleaf (XorTroll)",
	"githubapi": None,
	"projectpage": "https://github.com/XorTroll/Goldleaf",
	"directlink": "https://bsnx.lavatech.top/goldleaf/goldleaf-d212c5a.zip",
	"subfolder": "goldleaf",
	"author": "XorTroll",
	"description": "Nintendo Switch Title Installer",
	"group": "TITLEINSTALLER",
	"uptodate": False,
	"softwaredisabled": False,
	},

	{
	"software": "Tinfoil (satelliteseeker fork)",
	"githubapi": "https://api.github.com/repos/satelliteseeker/Tinfoil/releases/latest",
	"projectpage": "https://github.com/satelliteseeker/Tinfoil/releases",
	"directlink": None,
	"subfolder": None,
	"author": "satelliteseeker",
	"description": "Tinfoil with some tweaks to make USB installation work better",
	"group": "TITLEINSTALLER",
	"uptodate": True,
	"softwaredisabled": False,
	},

#Recommended homebrew

	{
	"software": "Homebrew Store",
	"githubapi": None,#"https://api.github.com/repos/vgmoose/hb-appstore/releases/latest", THIS DOES APPEAR TO BE UP TO DATE
	"projectpage": "https://github.com/vgmoose/hb-appstore/releases",
	"directlink":"https://www.switchbru.com/appstore/zips/appstore.zip", #this one seems to more closely match surrent conditions
	"subfolder": None,
	"author": "vgmoose",
	"description": "A graphical frontend to the get package manager for downloading and managing homebrew on video game consoles, such as the Nintendo Switch and Wii U. This is a replacement to the older Wii U Homebrew App Store.",
	"group": "REC",
	"uptodate": True,
	"softwaredisabled": False,
	},

	{
	"software": "Edizon",
	"githubapi": "https://api.github.com/repos/WerWolv/EdiZon/releases/latest",
	"projectpage": "https://github.com/WerWolv/EdiZon",
	"directlink": None,
	"subfolder": None,
	"author": "WerWolv",
	"description": """EdiZon consists of 3 different main functionalities. 
		Save file management. Extraction of game saves.
			Injection of extracted game saves (Your own and your friends save files).
			Uploading of savefiles directly to https://transfer.sh.
			Batch extraction of all save files of all games on the system.
		Save file editing
			Easy to use, scriptable and easily expandable on-console save editing.
				Lua and Python script support.
			Built-in save editor updater.
		On-the-fly memory editing
			Cheat Engine like RAM editing.
			Freezing of values in RAM via Atmosphère's cheat module.
			Interface for loading, managing and updating Atmosphère cheats.
	
	All packed into one easy to use and easy to install Homebrew.""",
	"group": "REC",
	"uptodate": True,
	"softwaredisabled": False,
	},

	{
	"software": "Lockpick",
	"githubapi": "https://api.github.com/repos/shchmue/Lockpick/releases/latest",
	"projectpage": "https://github.com/shchmue/Lockpick/",
	"directlink": None,
	"subfolder": "switch",
	"author": "shchmue",
	"description": """Lockpick is a ground-up C++17 rewrite of homebrew key derivation software, namely kezplez-nx. It also dumps titlekeys. This will dump all keys through *_key_05 on firmwares below 6.2.0 and through *_key_06 on 6.2.0.

Due to key generation changes introduced in 7.0.0, Lockpick is not able to dump keys ending in 07 at all. Furthermore, unfortunately the public method to dump tsec_root_key is only available on firmware 6.2.0 so 7.x consoles can only dump through keys ending in 05.""",
	"group": "REC",
	"uptodate": True,
	"softwaredisabled": False,
	},


#HOMEBREW
	{
	"software": "pPlay Video Player",
	"githubapi": "https://api.github.com/repos/Cpasjuste/pplay/releases/latest",
	"projectpage": "https://github.com/Cpasjuste/pplay/",
	"directlink": None,
	"subfolder": "switch",
	"author": "Cpasjuste",
	"description": "pPlay is a video player for the Nintendo Switch. pPlay support most popular video formats, have subtitles (embedded ass) and http streaming support.",
	"group": "HOMEBREW",
	"uptodate": True,
	"softwaredisabled": False,
	},

	{
	"software": "JKS's Save Manager",
	"githubapi": "https://api.github.com/repos/J-D-K/JKSV/releases/latest",
	"projectpage": "https://github.com/J-D-K/JKSV/",
	"directlink": None,
	"subfolder": "switch",
	"author": "J-D-K",
	"description": """WIP Save manager for the Switch, JKSV on Switch started as a small project/port to test some things and get familiar with libnx. A list of what it currently can do:

Dump and restore save data.
	This includes the ability to dump and restore to/from any location on SD by pressing minus and using the Advanced Mode.
Dump system save data
	Pressing all four shoulder buttons at once will rescan and include the previously unlisted system saves.
	Dumping this data is allowed, but writing back is not.
Open and explore bis storage partitions via the Extras menu
	BIS Storage is opened inside a basic filebrowser. The partition's listing is on the left. Your SD is on the right.
	Only copying to SD and file properties work on BIS partitions. Writing to and deleting are disabled for now.
Misc Extras:
	NAND Dumping
	Ability to remove downloaded firmware updates from NAND.
	Terminating processes by ID. Allowing you to dump normally unopenable system archives.
	Mount by System Save ID. Normally used when the terminated process makes JKSV unable to rescan titles without the Switch crashing.""",
	"group": "HOMEBREW",
	"uptodate": True,
	"softwaredisabled": False,
	},

	{
	"software":  "NX-Shell",
	"githubapi": "https://api.github.com/repos/joel16/NX-Shell/releases/latest",
	"projectpage": "https://github.com/joel16/NX-Shell/",
	"directlink": None,
	"subfolder": "NX-Shell",
	"author": "joel16",
	"description": "Work in progress port of 3DShell (Multi purpose file manager) to the Nintendo Switch.",
	"group": "HOMEBREW",
	"uptodate": True,
	"softwaredisabled": False,
	},

	{
	"software": "Calculator-NX",
	"githubapi": "https://api.github.com/repos/thomleg50/Calculator-NX/releases/latest",
	"projectpage": "https://github.com/thomleg50/Calculator-NX/",
	"directlink": None,
	"subfolder": "switch",
	"author": "thomleg50",
	"description": "A simple calculator for Switch !",
	"group": "HOMEBREW",
	"uptodate": True,
	"softwaredisabled": False,
	},

	{
	"software": "NxThemesInstaller",
	"githubapi": "https://api.github.com/repos/exelix11/SwitchThemeInjector/releases/latest",
	"projectpage": "https://github.com/exelix11/SwitchThemeInjector/",
	"directlink": None,
	"subfolder": "Switch",
	"author": "exelix11",
	"description": """The Switch theme injector project is composed of three parts:

Switch theme injector (Windows app): An app to create and edit custom themes
NXThemes installer: An homebrew app that runs on the switch itself and can be used to install and manage themes.
Switch theme injector online (also called WebInjector): A port of the windows injector as a web app, it lacks some features like image to DDS conversion.
The main objective is to develop a complete toolset to create and install custom themes on the switch. As the console os doesn't implement custom themes natively most of this is done by patching system SZS files to get the desidered aspect.

Unfortunately SZS files from the switch os contain copyrighted data so to make theme sharing legal the nxtheme format has been developed, it's 100% legal and works on every firmware, unless you're dealing with making your own patches and custom layouts you should only use nxtheme files.""",
	"group": "HOMEBREW",
	"uptodate": True,
	"softwaredisabled": False,
	},

	{
	"software": "Gag-Order",
	"githubapi": "https://api.github.com/repos/Adubbz/Gag-Order/releases/latest",
	"projectpage": "https://github.com/Adubbz/Gag-Order/",
	"directlink": None,
	"subfolder": "switch",
	"author": "Adubbz",
	"description": "A homebrew application which patches the 'Supernag' on the Nintendo Switch.",
	"group": "HOMEBREW",
	"uptodate": True,
	"softwaredisabled": False,
	},

	{
	"software": "2048",
	"githubapi": None,#"https://api.github.com/repos/FlagBrew/2048/releases/latest",
	"projectpage": "https://github.com/FlagBrew/2048/",
	"directlink": "https://www.switchbru.com/appstore/zips/2048.zip",
	"subfolder": "switch",
	"author": "FlagBrew",
	"description": "2048 port for Switch Homebrew",
	"group": "HOMEBREW",
	"uptodate": True,
	"softwaredisabled": False,
	},
	# {
	# "software": "2048",
	# "githubapi": "https://api.github.com/repos/FlagBrew/2048/releases/latest",
	# "projectpage": "https://github.com/FlagBrew/2048/",
	# "directlink": None,
	# "subfolder": "switch",
	# "author": "FlagBrew",
	# "description": "2048 port for Switch Homebrew",
	# "group": "HOMEBREW",
	# "uptodate": True,
	# },
	
#EMULATOR
	{
	"software": "khedGB",
	"githubapi": None, #no releases on his page
	"projectpage": "https://github.com/khedoros/khedgb",
	"directlink": "https://www.switchbru.com/appstore/zips/khedgb.zip", #up to date app store
	"subfolder": None,
	"author": "khedoros",
	"description": "Adventures in Game Boy emulation (Or, What Khedoros Likes To Do In His Not-so-abundant Free Time). Honestly, it's working better than I would have thought. A lot of these ideas would be good to carry over to my NES emulator to fix some longstanding bugs, while simultaneously improving compatibility and code quality.",
	"group": "EMULATOR",
	"uptodate": True,
	"softwaredisabled": False,
	},

	{
	"software": "VBA Next",
	"githubapi": None,#"https://api.github.com/repos/RSDuck/vba-next-switch/releases/latest", author said this was their last
	"projectpage": "https://github.com/RSDuck/vba-next-switch",
	"directlink": "https://github.com/RSDuck/vba-next-switch/releases/download/0.7/vba-next.zip",
	"subfolder": "switch",
	"author": "RSDuck",
	"description": """A VBA-M port for Nintendo Switch. It's based of the libretro port(the actual emulator) and 3DSGBA(the GUI, although heavily refactored).

After porting 3DSGBA(which often crashed probably because of a huge amount of memory leaks), I tried porting mGBA which ran not so well. That's why I decided to experiment with a lighter less accurate emulator, which lead to this port.""",
	"group": "EMULATOR",
	"uptodate":  True,
	"softwaredisabled": False,
	},
# 	{
# 	"software": "VBA Next",
# 	"githubapi": "https://api.github.com/repos/RSDuck/vba-next-switch/releases/latest",
# 	"projectpage": "https://github.com/RSDuck/vba-next-switch",
# 	"directlink": None,
# 	"subfolder": "switch",
# 	"author": "RSDuck",
# 	"description": """A VBA-M port for Nintendo Switch. It's based of the libretro port(the actual emulator) and 3DSGBA(the GUI, although heavily refactored).

# After porting 3DSGBA(which often crashed probably because of a huge amount of memory leaks), I tried porting mGBA which ran not so well. That's why I decided to experiment with a lighter less accurate emulator, which lead to this port.""",
# 	"group": "EMULATOR",
# 	"uptodate":  True,
# 	},


#Other
	{
	"software": "Hekete",
	"githubapi": "https://api.github.com/repos/CTCaer/hekate/releases/latest",
	"projectpage": "https://github.com/CTCaer/hekate/",
	"directlink": None,
	"author": "CTCaer",
	"description": """Custom Nintendo Switch bootloader, firmware patcher, and more.
This version supports booting ALL current OS/CS CFW, Linux chainloading and payload tools.
No more SD card removals""",
	"group": "PAYLOADS",
	"uptodate": True,
	"softwaredisabled": False,
	},
	
	{
	"software": "fusee-primary",
	"githubapi": "https://api.github.com/repos/Atmosphere-NX/Atmosphere/releases/latest",
	"projectpage": "https://github.com/Atmosphere-NX/Atmosphere/",
	"directlink": None,
	"author": "SciresM",
	"description": "Bootloader for Atmosphere",
	"group": "PAYLOADS",
	"uptodate": True,
	"jsonname" : "fusee-primary.bin",
	"softwaredisabled": False,
	},

	{
	"software": "SXOS Payload",
	"githubapi": None,
	"projectpage": "https://team-xecuter.com/",
	"directlink": "ttps://sx.xecuter.com/download/payload.bin",
	"author": "team-xecuter",
	"description": "Launcher for SXOS",
	"group": "PAYLOADS",
	"uptodate": True,
	"softwaredisabled": False,
	},

	{
	"software": "sigpatches",
	"githubapi": None, #yet, added this at last moment, will be dynamic next version
	"projectpage": None,
	"directlink": "https://github.com/AtlasNX/Kosmos/releases/download/v11.11.1/Additional.SigPatches.espatches.zip",
	"subfolder": None,
	"author": None,
	"description": None,
	"group": "Patches",
	"uptodate": False,
	"softwaredisabled": False,
	},

	# {
	# "software": "ReiNX Payload",
	# "githubapi": None,
	# "projectpage": "https://reinx.guide/",
	# "directlink": "",
	# "author": "ReiNX Team",
	# "description": "Launcher for ReiNX",
	# "group": "PAYLOADS",
	# "uptodate": True,
	# }

	#"https://www.switchbru.com/appstore/zips/ReiNX.zip"
]



#Not Available due to dev
	# [
	# "Goldleaf",
	# "https://api.github.com/repos/XorTroll/Goldleaf/releases/latest",
	# ],

#	
	# [
	# "pplay",
	# "https://api.github.com/repos/Cpasjust/pplay/releases/latest",
	# ],

	# [
	# "Scummvm",
	# "https://api.github.com/repos/Cpasjuste/scummvm/releases/",
	# ],


def downloadfile(url,target):
	urllib.request.urlretrieve(url, target)

#get jason, add and update keywords if json download successfully
json_file_list = []
def getUpdatedSoftwareLinks():
	for softwarechunk in SOFTWARELOCATIONS:
		githubjsonlink = softwarechunk["githubapi"]
		softwarename = softwarechunk["software"]
		if githubjsonlink == None:
			print("direct download, skipping {}".format(softwarename))
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
						softwarechunk["directlink"] = jfile["assets"][assetsmember]["browser_download_url"]
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
							softwarechunk["directlink"] = jfile["assets"][assetsmember]["browser_download_url"]
						except:
							print("Failed to add directlink for {}".format(softwarename))
				else:
					print("no fallback version for {} software will be unavailable".format(softwarename))
					softwarechunk["softwaredisabled"] = True,

	return SOFTWARELOCATIONS

#for testing
def fillStringWithoutDownloading():
	for softwarechunk in SOFTWARELOCATIONS:
		githubjsonlink = softwarechunk["githubapi"]
		softwarename = softwarechunk["software"]
		if githubjsonlink == None:
			print("direct download, skipping {}".format(softwarename))
		else:
			downloadas = joinpaths(downloadsfolder, softwarename + ".json")
			json_file_list.append(softwarename)
			softwarechunk["gotjson"] = True,

			with open(downloadas) as json_file:
				assetsmember = 0
				if softwarename == "Kosmos":
					assetsmember = 1 #hacky way to get the right asset for fusee-primary.bin, will probably add an assetsmember tag to the dictionaries
				jfile = json.load(json_file)
				try:
					softwarechunk["directlink"] = jfile["assets"][assetsmember]["browser_download_url"]
				except:
					print("Failed to add directlink for {}".format(softwarename))
	return SOFTWARELOCATIONS


# def getcfw():
# 	cfws = {}
# 	for softwarechunk in SOFTWARELOCATIONS:
# 		if softwarechunk["group"] == "CFW":
# 			cfws.append(softwarechunk)
# 	return(cfws)


