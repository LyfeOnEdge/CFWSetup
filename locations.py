#locations.py
#FILES, DOWNLOAD LOCATIONS, CFW NAME STRINGS

import webbrowser
#Links
def deleteFile():
	print("test")

def openhelp():
	webbrowser.open_new(HELPLINK)

def OPENFAT32():
	webbrowser.open_new(FAT32GUIDE[LINKSTRING])

def OPENSDCHECKER():
	webbrowser.open_new(SDCARDCHECKER[LINKSTRING])

def OPENDOWNGRADEGUIDE():
	webbrowser.open_new(DOWNGRADEGUIDE[LINKSTRING])

def OPENNXTHEMESGUIDE():
	webbrowser.open_new(NXTHEMESGUIDE[LINKSTRING])

def OPENSWITCHSAVES():
	webbrowser.open_new(SWITCHSAVES[LINKSTRING])

def OPENDISCORD():
	webbrowser.open_new(DEVELOPERDISCORD[LINKSTRING])

def OPENGBATEMP():
	webbrowser.open_new("https://gbatemp.net/threads/cfwsetup-all-in-one-python-app.534138/")

HELPLINK = "https://guide.sdsetup.com/"

CFWFLAVORS = [
	[
	"Kosmos (atmos 0.8.5 base) ",
	"kosmos.zip", 
	"https://github.com/AtlasNX/Kosmos/releases/download/v11.11.1/KosmosV11111.zip"
	],

	[
	"Atmos (stock 0.8.5)", 
	"atmos.zip", 
	"https://github.com/Atmosphere-NX/Atmosphere/releases/download/0.8.5/atmosphere-0.8.5-master-b42d16cf+hbl-2.1+hbmenu-3.0.1.zip"
	],
]


#FORMAT FRIENDLY NAME, DOWNLOAD NAME, DOWNLOAD URL, INSTALL PATH
FLAVOR = 0
DOWNLOAD = 1
URLTOGET= 2
INSTALLPATH = 3
NSPINSTALLERS = [
	[
	"None", 
	None,
	None,
	None
	],


	[
	"Tinfoil (blawar)",
	"lithium.zip",
	"http://tinfoil.io/repo/tinfoil.latest.zip",
	""
	],

	[
	"Lithium (blawar)",
	"tinfoilblawar.zip",
	"http://tinfoil.io/repo/lithium.latest.zip",
	""
	],

	[
	"Tinfoil (addubz)",
	"addubztinfoil.zip",
	"https://bsnx.lavatech.top/tinfoil/tinfoil-883e3bd.zip",
	"switch"
	],

	[
	"Goldleaf (XorTroll)",
	"xortrollgoldleaf.zip",
	"https://bsnx.lavatech.top/goldleaf/goldleaf-d212c5a.zip",
	"goldleaf"
	],

	[
	"Tinfoil (satelliteseeker fork)",
	"satellitetinfoil.nro",
	"https://github.com/satelliteseeker/Tinfoil/releases/download/v0.2.1-USB-fix2/Tinfoil.nro",
	""
	],

	[
	"ZeroTwoXci",
	"zerotwoxci.nro",
	"https://gitlab.com/2168/zerotwoxci/uploads/581949b862704dda4c2c85150a5c670b/zerotwoxci.nro",
	""],

]

HOMEBREW = [
	[
	"Homebrew Store (incl. w/ Kosmos)",
	"appstore.zip",
	"https://www.switchbru.com/appstore/zips/appstore.zip",
	""
	],

	[
	"pPlay Video Player v 1.5",
	"pplay.zip,",
	"https://github.com/Cpasjuste/pplay/releases/download/v1.5/pplay-1.5_switch.zip",
	"switch"
	],

	[
	"JKS's Save Manager",
	"JKSV.nro",
	"https://github.com/J-D-K/JKSV/releases/download/01%2F08%2F2019/JKSV.nro",
	""
	],

	[
	"EdiZon Save Manager (incl. w/ Kosmos)",
	"SD.zip",
	"https://github.com/WerWolv/EdiZon/releases/download/v3.0.1/SD.zip",
	""
	],


	[
	"NX-Shell",
	"NX-Shell.nro",
	"https://github.com/joel16/NX-Shell/releases/download/1.20/NX-Shell.nro",
	"switch"
	],

	[
	"Calculator-NX",
	"Calculator-NX_0.8.nro",
	"https://github.com/thomleg50/Calculator-NX/releases/download/0.8/Calculator-NX_0.8.nro",
	"switch"
	],

	[
	"NxThemesInstaller",
	"NxThemesInstaller.nro",
	"https://github.com/exelix11/SwitchThemeInjector/releases/download/v-3.7/NxThemesInstaller.nro",
	"switch"
	],

	[
	"Gag-Order",
	"gag-order.nro",
	"https://github.com/Adubbz/Gag-Order/releases/download/0.1.0/gag-order.nro",
	"switch"
	],

	[
	"Lockpick",
	"Lockpick.nro",
	"https://github.com/shchmue/Lockpick/releases/download/v1.2.2/Lockpick.nro",
	"switch"
	],

	[
	"2048",
	"2048.nro",
	"https://github.com/FlagBrew/2048/releases/download/1.0.0/2048.nro",
	"switch"
	],

]

#some of the githubs for the emulators are down / use 7z format
#I'll be adding the 7z ones later.
EMULATORS = [

	[
	"khedGB",
	"khedgb.zip",
	"https://www.switchbru.com/appstore/zips/khedgb.zip",
	""
	],

	[
	"VBA Next",
	"vba-next.zip",
	"https://github.com/RSDuck/vba-next-switch/releases/download/0.7/vba-next.zip",
	"switch"
	],

	#need to deal with subfolder on this one
	# [
	# "ScummVM",
	# "scummvm.zip",
	# "https://github.com/Cpasjuste/scummvm/releases/download/2.12-2/scummvm_switch_2.12-2.zip",
	# ""
	# ],
]

#https://wiki.gbatemp.net/wiki/List_of_Switch_payloads
PAYLOADNAME = 0
PAYLOADFILE = 1
PAYLOADURL = 2
PAYLOADS = [
	[
	"Hekete 4.9.1",
	"Hekete 4.9.1.zip",
	"https://github.com/CTCaer/hekate/releases/download/v4.9.1_/hekate_ctcaer_4.9.1.zip",
	],

	[
	"Fusee-Primary",
	"fusee-primary.bin",
	"https://github.com/Atmosphere-NX/Atmosphere/releases/download/0.8.5/fusee-primary.bin"
	]

	#future support for 1-click installs
	# [
	# "Lakka",
	# "lakka.tar.gz"
	# "https://ctcaer.com/lakka/stable/Lakka-Switch.arm-2.2-devel-20181004171647-r28346-g2df642137.tar.gz"
	# ]

]

sigpatches_file = ["sigpatches.zip", "https://github.com/AtlasNX/Kosmos/releases/download/v11.11.1/Additional.SigPatches.espatches.zip"]


LINKTEXT = 0
LINKSTRING = 1
LINKCOMMAND = 2
FAT32GUIDE = [
"Drive Format Tool",
"https://gparted.org/"
]

SDCARDCHECKER = [
"Verify SD Card Is Legit",
"https://www.heise.de/download/product/h2testw-50539/download"
]

DOWNGRADEGUIDE = [
"Firmware Downgrade Guide",
"https://guide.sdsetup.com/usingcfw/manualchoiupgrade",
]

NXTHEMESGUIDE = [
"NXThemes Usage Guide",
"https://gbatemp.net/download/nxthemes-installer.35408/"
]

SWITCHSAVES = [
"Nintendo Switch Saves",
"https://gbatemp.net/threads/new-switch-save-site-with-modified-saves-and-100-completed-saves.508661/"
]

DEVELOPERDISCORD = [
"Developer Discord / Support",
"https://discord.gg/cXtmY9M"
]


HELPANDTOOLSDROPDOWN = [
	["Drive Format Tool", "https://gparted.org/",OPENFAT32],
	["Verify SD Card Is Legit", "https://www.heise.de/download/product/h2testw-50539/download",OPENSDCHECKER],
	["Firmware Downgrade Guide", "https://guide.sdsetup.com/usingcfw/manualchoiupgrade,",OPENDOWNGRADEGUIDE],
	["NXThemes Usage Guide", "https://gbatemp.net/download/nxthemes-installer.35408/",OPENNXTHEMESGUIDE],
	["Nintendo Switch Saves", "https://gbatemp.net/threads/new-switch-save-site-with-modified-saves-and-100-completed-saves.508661/",OPENSWITCHSAVES],
	["Developer Discord / Support", "https://discord.gg/cXtmY9M",OPENDISCORD],
]

