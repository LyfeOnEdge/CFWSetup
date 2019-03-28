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

