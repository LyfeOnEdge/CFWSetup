#locations.py
#FILES, DOWNLOAD LOCATIONS, CFW NAME STRINGS

	# {
	# "software" : software name
	# "githubapi": http://api.github.com/repos/AUTHOR/REPO/releases/latest
	# "projectpage": Main thread / page about project
	# "directlink": Only use this if there is a static up-to-date location or no github api, gets populated from github api
	# "subfolder" : the subfolder to install to
	# "itemslist": [List of specific items to extract from zip]
	# "author" : project author
	# "description" : project description
	# "group" : CFW, TITLEINSTALLER, REC, HOMEBREW, or EMULATORS
	# "uptodate": True or False, True if always up to date (static link or github api)
	# },

#Template:
	# {
	# "software":  
	# "githubapi":
	# "projectpage":
	# "directlink":
	# "subfolder":
	# "itemslist": None,
	# "author":
	# "image"
	# "asset" : 0,
	# "description":
	# "group":
	# "uptodate":
	# "softwaredisabled": False,
	# "gotjson": False,
	# },
teamxlogo = "https://img.fireden.net/vg/image/1543/60/1543601186577.png" #Had to get creative for this one... No github unfortunately, and I reeeeealy don't want to ship the sxos logo with cfwsetup.
blawarlogo = "http://tinfoil.io/images/release.png"

LOCATIONS_DICT = [

	{
	"software": "Atmos",
	"githubapi": "https://api.github.com/repos/Atmosphere-NX/Atmosphere/releases/latest",
	"projectpage":"https://github.com/Atmosphere-NX/Atmosphere/releases",
	"directlink": None,
	"subfolder": None,
	"itemslist": None,
	"asset" : 0,
	"author": "SciresM",
	"image" : None,
	"description": "Atmosphère is a customized firmware for the Nintendo Switch.",
	"group": "CFW",
	"uptodate": True,
	"softwaredisabled": False,
	"softwaredownloaded": False,
	"gotjson": False,
	},

	{
	"software": "Kosmos",
	"githubapi": "https://api.github.com/repos/AtlasNX/Kosmos/releases/latest",
	"projectpage": "https://github.com/AtlasNX/Kosmos/releases",
	"directlink": None,
	"subfolder": None,
	"itemslist": None,
	"asset" : 0,
	"author": "AtlasNX",
	"image" : None,
	"description": "All-in-One CFW Package for the Nintendo Switch - previously SDFilesSwitch",
	"group": "CFW",
	"uptodate": True,
	"softwaredisabled": False,
	"softwaredownloaded": False,
	"gotjson": False,
	},

	{
	"software": "ReiNX",
	"githubapi": "https://api.github.com/repos/Reisyukaku/ReiNX/releases/latest",
	"projectpage": "https://github.com/Reisyukaku/ReiNX",
	"directlink": None,
	"subfolder": None,
	"itemslist": None,
	"asset" : 0,
	"author": "Add this",
	"image" : None,
	"description": "A modular Switch custom firmware",
	"group": "CFW",
	"uptodate": True,
	"softwaredisabled": False,
	"softwaredownloaded": False,
	"gotjson": False,
	},

	{
	"software": "Argon-NX SD Files",
	"githubapi": "https://api.github.com/repos/Guillem96/argon-nx/releases/latest",
	"projectpage": "https://github.com/Guillem96/argon-nx/",
	"directlink": None,
	"subfolder": None,
	"itemslist": None,
	"author": "Guillem96",
	"image" : None,
	"asset" : 1,
	"description": """
What Argon is?
	Argon is a noble gas. "Argon" comes from Greek "Argon", neuter of "argos" meaning lazy , idle or inactive. Argon recieved this name because of its chemical inactivity.

	Argon NX is an immutable payload which is injected to your Nintendo Switch via Fusee Gelee exploit.

Purpose
	The purpose of Argon NX is to stay immutable, so you can always inject it, without caring about other payloads getting updated (Always use ArgonNX for TegraSmash, TegraGUI, TrinkedM0...).

How can it be immutable?
	When Argon NX is injected, it automatically launches the payload.bin locacted at argon directory on your SD Card root.

	If payload.bin is not present or VOLUME DOWN button is pressed on payload injection, Argon NX will list all payloads located at argon/payloads, and you will be able to select one of them to launch it.
""",
	"group": "CFW",
	"uptodate": True,
	"softwaredisabled": False,
	"gotjson": False,
	},

	{
	"software": "SX OS 2.5.3",
	"githubapi": None,
	"projectpage": "https://sx.xecuter.com/",
	"directlink": "https://sx.xecuter.com/download/SXOS_v2.5.3.zip",
	"subfolder": None,
	"itemslist": None,
	"asset" : 0,
	"author": "Team Xecuter",
	"image" : teamxlogo,
	"description": "A (paid) custom OS for the Switch",
	"group": "CFW",
	"uptodate": False,
	"softwaredisabled": False,
	"softwaredownloaded": False,
	"gotjson": False,
	},

	{
	"software": "SX OS 2.6.1 BETA",
	"githubapi": None,
	"projectpage": "https://sx.xecuter.com/",
	"directlink": "https://sx.xecuter.com/download/SXOS_beta_v2.6.1.zip",
	"subfolder": None,
	"itemslist": None,
	"asset" : 0,
	"author": "Team Xecuter",
	"image" : teamxlogo,
	"description": "A (paid) custom OS for the Switch, BETA VERSION",
	"group": "CFW",
	"uptodate": False,
	"softwaredisabled": False,
	"softwaredownloaded": False,
	"gotjson": False,
	},



#Title Installers
	{
	"software": "Tinfoil (blawar)",
	"githubapi": None,
	"projectpage": "http://tinfoil.io",
	"directlink": "http://tinfoil.io/repo/tinfoil.latest.zip",
	"subfolder": None,
	"itemslist": None,
	"asset" : 0,
	"author": "blawar",
	"image" : blawarlogo,
	"description": "Nintendo Switch Title Installer, now with .xci installation support!",
	"group": "TITLEINSTALLER",
	"uptodate": True,
	"softwaredisabled": False,
	"softwaredownloaded": False,
	"gotjson": False,
	},

	{
	"software": "Lithium (blawar)",
	"githubapi": None,
	"projectpage": "https://tinfoil.io",
	"directlink": "http://tinfoil.io/repo/lithium.latest.zip",
	"subfolder": None,
	"itemslist": None,
	"asset" : 0,
	"author": "blawar",
	"image" : blawarlogo,
	"description": "Slim Nintendo Switch Title Installer, now with .xci installation support!",
	"group": "TITLEINSTALLER",
	"uptodate": True,
	"softwaredisabled": False,
	"softwaredownloaded": False,
	"gotjson": False,
	},

	{
	"software":"Tinfoil (addubz)",
	"githubapi": None,
	"projectpage": "https://github.com/Adubbz/Tinfoil",
	"directlink": "https://bsnx.lavatech.top/tinfoil/tinfoil-883e3bd.zip",
	"subfolder": "switch",
	"itemslist": None,
	"asset" : 0,
	"author": "addubz",
	"image" : "https://avatars0.githubusercontent.com/u/2765389?s=460&v=4",
	"description": "Nintendo Switch Title Installer",
	"group": "TITLEINSTALLER",
	"uptodate": False,
	"softwaredisabled": False,
	"softwaredownloaded": False,
	"gotjson": False,
	},

	{
	"software": "Goldleaf (XorTroll)",
	"githubapi": None,
	"projectpage": "https://github.com/XorTroll/Goldleaf",
	"directlink": "https://bsnx.lavatech.top/goldleaf/goldleaf-d212c5a.zip",
	"subfolder": "goldleaf",
	"itemslist": None,
	"asset" : 0,
	"author": "XorTroll",
	"image" :  "https://avatars0.githubusercontent.com/u/2765389?s=460&v=4",
	"description": "Nintendo Switch Title Installer",
	"group": "TITLEINSTALLER",
	"uptodate": False,
	"softwaredisabled": False,
	"softwaredownloaded": False,
	"gotjson": False,
	},

	{
	"software": "Tinfoil (satelliteseeker fork)",
	"githubapi": "https://api.github.com/repos/satelliteseeker/Tinfoil/releases/latest",
	"projectpage": "https://github.com/satelliteseeker/Tinfoil/releases",
	"directlink": None,
	"subfolder": None,
	"itemslist": None,
	"asset" : 0,
	"author": "satelliteseeker",
	"image" : None,
	"description": "Tinfoil with some tweaks to make USB installation work better",
	"group": "TITLEINSTALLER",
	"uptodate": True,
	"softwaredisabled": False,
	"softwaredownloaded": False,
	"gotjson": False,
	},

#Recommended homebrew

	{
	"software": "Homebrew Store",
	"githubapi": "https://api.github.com/repos/vgmoose/hb-appstore/releases/latest", 
	"projectpage": "https://github.com/vgmoose/hb-appstore/releases",
	"directlink":None,
	"subfolder": None,
	"itemslist": None,
	"asset" : 0,
	"author": "vgmoose",
	"image" : None,
	"description": "A graphical frontend to the get package manager for downloading and managing homebrew on video game consoles, such as the Nintendo Switch and Wii U. This is a replacement to the older Wii U Homebrew App Store.",
	"group": "REC",
	"uptodate": True,
	"softwaredisabled": False,
	"softwaredownloaded": False,
	"gotjson": False,
	},

	{
	"software": "Edizon",
	"githubapi": "https://api.github.com/repos/WerWolv/EdiZon/releases/latest",
	"projectpage": "https://github.com/WerWolv/EdiZon",
	"directlink": None,
	"subfolder": None,
	"itemslist": None,
	"asset" : 0,
	"author": "WerWolv",
	"image" : None,
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
	"softwaredownloaded": False,
	"gotjson": False,
	},

	{
	"software": "Lockpick",
	"githubapi": "https://api.github.com/repos/shchmue/Lockpick/releases/latest",
	"projectpage": "https://github.com/shchmue/Lockpick/",
	"directlink": None,
	"subfolder": "switch",
	"itemslist": None,
	"asset" : 0,
	"author": "shchmue",
	"image" : None,
	"description": """Lockpick is a ground-up C++17 rewrite of homebrew key derivation software, namely kezplez-nx. It also dumps titlekeys. This will dump all keys through *_key_05 on firmwares below 6.2.0 and through *_key_06 on 6.2.0.

Due to key generation changes introduced in 7.0.0, Lockpick is not able to dump keys ending in 07 at all. Furthermore, unfortunately the public method to dump tsec_root_key is only available on firmware 6.2.0 so 7.x consoles can only dump through keys ending in 05.""",
	"group": "REC",
	"uptodate": True,
	"softwaredisabled": False,
	"softwaredownloaded": False,
	"gotjson": False,
	},


#HOMEBREW

	{
	"software": "2048",
	"githubapi": "https://api.github.com/repos/FlagBrew/2048/releases/latest",
	"projectpage": "https://github.com/FlagBrew/2048/",
	"directlink": None,
	"subfolder": "switch",
	"itemslist": None,
	"asset" : 0,
	"author": "FlagBrew",
	"image" : "https://avatars0.githubusercontent.com/u/42673825?s=200&v=4",
	"description": "2048 port for Switch Homebrew",
	"group": "HOMEBREW",
	"uptodate": True,
	"softwaredisabled": False,
	"softwaredownloaded": False,
	"gotjson": False,
	},

	{
	"software": "Calculator-NX",
	"githubapi": "https://api.github.com/repos/thomleg50/Calculator-NX/releases/latest",
	"projectpage": "https://github.com/thomleg50/Calculator-NX/",
	"directlink": None,
	"subfolder": "switch",
	"itemslist": None,
	"asset" : 0,
	"author": "thomleg50",
	"image" : None,
	"description": "A simple calculator for Switch !",
	"group": "HOMEBREW",
	"uptodate": True,
	"softwaredisabled": False,
	"softwaredownloaded": False,
	"gotjson": False,
	},

	{
	"software": "Gag-Order",
	"githubapi": "https://api.github.com/repos/Adubbz/Gag-Order/releases/latest",
	"projectpage": "https://github.com/Adubbz/Gag-Order/",
	"directlink": None,
	"subfolder": "switch",
	"itemslist": None,
	"asset" : 0,
	"author": "Adubbz",
	"image" : None,
	"description": "A homebrew application which patches the 'Supernag' on the Nintendo Switch.",
	"group": "HOMEBREW",
	"uptodate": True,
	"softwaredisabled": False,
	"softwaredownloaded": False,
	"gotjson": False,
	},
	# {
	# "software": "2048",
	# "githubapi": "https://api.github.com/repos/FlagBrew/2048/releases/latest",
	# "projectpage": "https://github.com/FlagBrew/2048/",
	# "directlink": None,
	# "subfolder": "switch",
	# "itemslist": None,
	# "author": "FlagBrew",
	# "description": "2048 port for Switch Homebrew",
	# "group": "HOMEBREW",
	# "uptodate": True,
	# "softwaredisabled": False,
	# "softwaredownloaded": False,
	# "gotjson": False,
	# }


	{
	"software": "JKS's Save Manager",
	"githubapi": "https://api.github.com/repos/J-D-K/JKSV/releases/latest",
	"projectpage": "https://github.com/J-D-K/JKSV/",
	"directlink": None,
	"subfolder": "switch",
	"itemslist": None,
	"asset" : 0,
	"author": "J-D-K",
	"image" : "https://raw.githubusercontent.com/J-D-K/JKSV/master/romfs/img/icn/icnDrk.png",
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
	"softwaredownloaded": False,
	"gotjson": False,
	},

	{
	"software":  "NX-Shell",
	"githubapi": "https://api.github.com/repos/joel16/NX-Shell/releases/latest",
	"projectpage": "https://github.com/joel16/NX-Shell/",
	"directlink": None,
	"subfolder": "NX-Shell",
	"itemslist": None,
	"asset" : 0,
	"author": "joel16",
	"image" : None,
	"description": "Work in progress port of 3DShell (Multi purpose file manager) to the Nintendo Switch.",
	"group": "HOMEBREW",
	"uptodate": True,
	"softwaredisabled": False,
	"softwaredownloaded": False,
	"gotjson": False,
	},

	{
	"software": "NxThemesInstaller",
	"githubapi": "https://api.github.com/repos/exelix11/SwitchThemeInjector/releases/latest",
	"projectpage": "https://github.com/exelix11/SwitchThemeInjector/",
	"directlink": None,
	"subfolder": "Switch",
	"itemslist": None,
	"asset" : 0,
	"author": "exelix11",
	"image" : None,
	"description": """The Switch theme injector project is composed of three parts:

Switch theme injector (Windows app): An app to create and edit custom themes
NXThemes installer: An homebrew app that runs on the switch itself and can be used to install and manage themes.
Switch theme injector online (also called WebInjector): A port of the windows injector as a web app, it lacks some features like image to DDS conversion.
The main objective is to develop a complete toolset to create and install custom themes on the switch. As the console os doesn't implement custom themes natively most of this is done by patching system SZS files to get the desidered aspect.

Unfortunately SZS files from the switch os contain copyrighted data so to make theme sharing legal the nxtheme format has been developed, it's 100% legal and works on every firmware, unless you're dealing with making your own patches and custom layouts you should only use nxtheme files.""",
	"group": "HOMEBREW",
	"uptodate": True,
	"softwaredisabled": False,
	"softwaredownloaded": False,
	"gotjson": False,
	},

	{
	"software": "pPlay Video Player",
	"githubapi": "https://api.github.com/repos/Cpasjuste/pplay/releases/latest",
	"projectpage": "https://github.com/Cpasjuste/pplay/",
	"directlink": None,
	"subfolder": "switch",
	"itemslist": None,
	"asset" : 0,
	"author": "Cpasjuste",
	"image" : "https://raw.githubusercontent.com/Cpasjuste/pplay/master/data/read_only/skin/pplay.png",
	"description": "pPlay is a video player for the Nintendo Switch. pPlay support most popular video formats, have subtitles (embedded ass) and http streaming support.",
	"group": "HOMEBREW",
	"uptodate": True,
	"softwaredisabled": False,
	"softwaredownloaded": False,
	"gotjson": False,
	},

	{
	"software": "SwitchIdent (Command Line Interface)",
	"githubapi": "https://api.github.com/repos/joel16/SwitchIdent/releases/latest",
	"projectpage": "https://github.com/joel16/SwitchIdent/",
	"directlink": None,
	"subfolder": "switch",
	"itemslist": None,
	"asset" : 0, 
	"author": "joel16",
	"image" : None,
	"description": "This is yet another identity tool that is continuing the series of <device name here>ident. This tool allows users to get various bits of information from your Nintendo Switch device, hence the name 'ident' as in identifying your Nintendo Switch.",
	"group": "HOMEBREW",
	"uptodate": True,
	"softwaredisabled": False,
	"gotjson": False,
	},

	{
	"software": "SwitchIdent (GUI)",
	"githubapi": "https://api.github.com/repos/joel16/SwitchIdent/releases/latest",
	"projectpage": "https://github.com/joel16/SwitchIdent/",
	"directlink": None,
	"subfolder": "switch",
	"itemslist": "None",
	"asset" : 1,
	"author": "joel16",
	"image" : None,
	"description": "This is yet another identity tool that is continuing the series of <device name here>ident. This tool allows users to get various bits of information from your Nintendo Switch device, hence the name 'ident' as in identifying your Nintendo Switch.",
	"group": "HOMEBREW",
	"uptodate": True,
	"softwaredisabled": False,
	"gotjson": False,
	},

	{
	"software":  "Checkpoint",
	"githubapi": "https://api.github.com/repos/FlagBrew/Checkpoint/releases/latest",
	"projectpage": "https://github.com/FlagBrew/Checkpoint/",
	"directlink": None,
	"subfolder": None,
	"itemslist": None,
	"author": "FlagBrew",
	"image" : None,
	"asset" : 2,
	"description": "A fast and simple homebrew save manager for 3DS and Switch written in C++.",
	"group": "HOMEBREW",
	"uptodate": True,
	"softwaredisabled": False,
	"gotjson": False,
	},

	
#EMULATOR
	{
	"software": "khedGB",
	"githubapi": None, #no releases on his page
	"projectpage": "https://github.com/khedoros/khedgb",
	"directlink": "https://www.switchbru.com/appstore/zips/khedgb.zip", #up to date app store
	"subfolder": None,
	"itemslist": None,
	"asset" : 0,
	"author": "khedoros",
	"image" : "https://www.switchbru.com/appstore/packages/khedgb/icon.png",
	"description": "Adventures in Game Boy emulation (Or, What Khedoros Likes To Do In His Not-so-abundant Free Time). Honestly, it's working better than I would have thought. A lot of these ideas would be good to carry over to my NES emulator to fix some longstanding bugs, while simultaneously improving compatibility and code quality.",
	"group": "EMULATOR",
	"uptodate": True,
	"softwaredisabled": False,
	"softwaredownloaded": False,
	"gotjson": False,
	},

	{
	"software": "VBA Next",
	"githubapi": "https://api.github.com/repos/RSDuck/vba-next-switch/releases/latest", 
	"projectpage": "https://github.com/RSDuck/vba-next-switch",
	"directlink": None,
	"subfolder": "switch",
	"itemslist": None,
	"asset" : 0,
	"author": "RSDuck",
	"image" : None,
	"description": """A VBA-M port for Nintendo Switch. It's based of the libretro port(the actual emulator) and 3DSGBA(the GUI, although heavily refactored).

After porting 3DSGBA(which often crashed probably because of a huge amount of memory leaks), I tried porting mGBA which ran not so well. That's why I decided to experiment with a lighter less accurate emulator, which lead to this port.""",
	"group": "EMULATOR",
	"uptodate":  True,
	"softwaredisabled": False,
	"softwaredownloaded": False,
	"gotjson": False,
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
#	"softwaredisabled": False,
# 	"softwaredownloaded": False,
# 	},


#Other
	{
	"software": "Hekete",
	"githubapi": "https://api.github.com/repos/CTCaer/hekate/releases/latest",
	"projectpage": "https://github.com/CTCaer/hekate/",
	"directlink": None,
	"subfolder": None,
	"itemslist": None,
	"asset" : 0,
	"author": "CTCaer",
	"image" : None,
	"description": """Custom Nintendo Switch bootloader, firmware patcher, and more.
This version supports booting ALL current OS/CS CFW, Linux chainloading and payload tools.
No more SD card removals""",
	"group": "PAYLOADS",
	"uptodate": True,
	"softwaredisabled": False,
	"softwaredownloaded": False,
	"gotjson": False,
	},
	
	{
	"software": "fusee-primary",
	"githubapi": "https://api.github.com/repos/Atmosphere-NX/Atmosphere/releases/latest",
	"projectpage": "https://github.com/Atmosphere-NX/Atmosphere/",
	"directlink": None,
	"subfolder": None,
	"itemslist": None,
	"asset" : 0,
	"author": "SciresM",
	"image" : None,
	"description": "Bootloader for Atmosphere",
	"group": "PAYLOADS",
	"uptodate": True,
	"jsonname" : "fusee-primary.bin",
	"softwaredisabled": False,
	"softwaredownloaded": False,
	"gotjson": False,
	},

	{
	"software": "ReiNX Payload",
	"githubapi": "https://api.github.com/repos/Reisyukaku/ReiNX/releases/latest",
	"projectpage": "https://reinx.guide/",
	"directlink": None,
	"subfolder": None,
	"itemslist": {"payload" : "ReiNX.bin"},
	"asset" : 0,
	"author": "ReiNX Team",
	"image" : None,
	"description": "Launcher for ReiNX",
	"group": "PAYLOADS",
	"uptodate": True,
	"softwaredisabled": False,	
	"softwaredownloaded": False,
	"gotjson": False,
	},

	{
	"software": "Argon-NX payload",
	"githubapi": "https://api.github.com/repos/Guillem96/argon-nx/releases/latest",
	"projectpage": "https://github.com/Guillem96/argon-nx/",
	"directlink": None,
	"subfolder": None,
	"itemslist": None,
	"author": "Guillem96",
	"image" : None,
	"asset" : 1,
	"description": """
What Argon is?
	Argon is a noble gas. "Argon" comes from Greek "Argon", neuter of "argos" meaning lazy , idle or inactive. Argon recieved this name because of its chemical inactivity.

	Argon NX is an immutable payload which is injected to your Nintendo Switch via Fusee Gelee exploit.

Purpose
	The purpose of Argon NX is to stay immutable, so you can always inject it, without caring about other payloads getting updated (Always use ArgonNX for TegraSmash, TegraGUI, TrinkedM0...).

How can it be immutable?
	When Argon NX is injected, it automatically launches the payload.bin locacted at argon directory on your SD Card root.

	If payload.bin is not present or VOLUME DOWN button is pressed on payload injection, Argon NX will list all payloads located at argon/payloads, and you will be able to select one of them to launch it.
""",
	"group": "PAYLOADS",
	"uptodate": True,
	"softwaredisabled": False,
	"gotjson": False,
	},

	{
	"software": "SXOS Payload",
	"githubapi": None,
	"projectpage": "https://team-xecuter.com/",
	"directlink": "https://sx.xecuter.com/download/payload.bin",
	"subfolder": None,
	"itemslist": None,
	"asset" : 0,
	"author": "team-xecuter",
	"image" : teamxlogo,
	"description": "Launcher for SXOS",
	"group": "PAYLOADS",
	"uptodate": True,
	"softwaredisabled": False,
	"softwaredownloaded": False,
	"gotjson": False,
	},


	{
	"software": "Lockpick RCM",
	"githubapi": "https://api.github.com/repos/shchmue/Lockpick_RCM/releases/latest",
	"projectpage": "https://github.com/shchmue/Lockpick_RCM/",
	"directlink": None,
	"subfolder": None,
	"itemslist": None,
	"author": "schmue",
	"image" : None,
	"asset" : 0,
	"description": """Lockpick_RCM is a bare metal Nintendo Switch payload that derives encryption keys for use in Switch file handling software like hactool, hactoolnet/LibHac, ChoiDujour, etc. without booting Horizon OS.

Due to changes imposed by firmware 7.0.0, Lockpick homebrew can no longer derive the latest keys. In the boot-time environment however, there are fewer limitations.""",
	"group":"PAYLOADS",
	"uptodate": True,
	"softwaredisabled": False,
	"gotjson": False,
	},

	{
	"software": "biskeydumpv8 (7.0+)",
	"githubapi": None,
	"projectpage": "https://switchtools.sshnuke.net/",
	"directlink": "https://files.sshnuke.net/biskeydumpv8.zip",
	"subfolder": None,
	"itemslist": None,
	"author": "rajkosto",
	"image" : "https://avatars1.githubusercontent.com/u/205276?s=400&v=4",
	"asset" : 0,
	"description": """Dumps all your Switch BIS keys for eMMC contents decryption, to be used as a fusee payload.

With all your BIS keys and your RawNand.bin (or the physical eMMC attached via microSD reader or using a mass storage gadget mode in u-boot/linux) you can explore/modify your eMMC partitions using my HacDiskMount tool below""",
	"group":"PAYLOADS",
	"uptodate": True,
	"softwaredisabled": False,
	"gotjson": False,

	},
#other switch content
	{
	"software": "sigpatches",
	"githubapi": None, #yet, added this at last moment, will be dynamic next version
	"projectpage": "https://gbatemp.net/threads/i-heard-that-you-guys-need-some-sweet-patches-for-atmosphere.521164/",
	"directlink": "https://github.com/AtlasNX/Kosmos/releases/download/v11.11.1/Additional.SigPatches.espatches.zip",
	"subfolder": None,
	"itemslist": None,
	"asset" : 0,
	"author": None,
	"image" : "https://avatars1.githubusercontent.com/u/205276?s=400&v=4",
	"description":"""Ok, Here you are
and No, they are just IPS patches, they don't contain anything illegal

es patches are Rajkosto ones, Credits goes to him

FAQ:
Q: What are patches?
A: Patches are modifications in firmware that changes it's default behavior, usually using for disabling/bypassing some checks

Q: What do these patches do?
A:
1- Running custom (unsigned, modified) nsps(ncas) such as homebrew nsps and converted xcis to nsps (nosigchk+acid, fs)
2- Installing fake (unsigned, modified) tickets (es)
3- nocmac, fs""",
	"group": "Patches",
	"uptodate": False,
	"softwaredisabled": False,
	"softwaredownloaded": False,
	"gotjson": False,
	},



#other tools
	# { Future plans for nut server integration
	# "software": "blawar nut server"
	# "githubapi": "https://api.github.com/repos/blawar/nut/releases/latest",
	# "projectpage": "https://github.com/blawar/nut",
	# "directlink": None,
	# "subfolder": None,
	# "itemslist": None,
	# "asset" : 0,
	# "author": "blawar",
	# "description": """This is a program that automatically downloads all games from the CDN, and organizes them on the file system as backups. You can only play games that you have legally purchased / have a title key for. Nut also provides a web interface for browsing your collection.

	# You should copy nut.default.conf to nut.conf and make all of your local edits in nut.conf.

	# If you only wish to rename / organize files, and not download anything, edit nut.conf and set all downloading options to false. Your NSP files should have the titleid as a part of the filename in brackets.

	# It can download any titles you do not have a key for (for archiving), by enabling sansTitleKey in nut.conf. These titles are saved with the .nsx file extension, and can be unlocked at a later time when a title key is found.
	# """,
	# "group": "SOFTWARE",
	# "uptodate": True,
	# "softwaredisabled": False,
	# "gotjson": False,
	# },


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



