version = "0.3 (BETA)"
thankyoutext = "A special thanks to all the users on /hbg/, /r/SwitchPirates, and gbatemp for the help, suggestions, good ideas, and support. This app is in its infancy, plans include more community homebrew and easy launching of tegraRCMgui, nut.py, and more"

from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
import tkinter
import os, sys
from zipfile import ZipFile
import webbrowser
import time
import urllib.request 
import shutil

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)

chosensdpath = None
selectedConfirmation = None
temp_folder = "temp/" #hate all you want for the unix-style slashes ;D

helplink = "https://guide.sdsetup.com/"




#FILES, DOWNLOAD LOCATIONS, CFW NAME STRINGS
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

	[
	"",
	"",
	"",
	""
	],

	[
	"",
	"",
	"",
	""
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

sigpatches_file = ["sigpatches.zip", "https://github.com/AtlasNX/Kosmos/releases/download/v11.11.1/Additional.SigPatches.espatches.zip"]


def get_path(filename):
	return os.path.join(sys.path[0], filename)

def spewToTextOutput(textToSpew):
	textoutput.config(state=NORMAL)
	textoutput.insert(END, textToSpew + "\n")
	textoutput.config(state=DISABLED)
	textoutput.see(END)
	print(textToSpew)

#update global "chosensdpath"
def setSDpath():
	global chosensdpath
	chosensdpath = filedialog.askdirectory(initialdir="/",  title='Please select a directory to install to')
	pathvalue.set(str(chosensdpath))
	spewToTextOutput("Install path set to: {}".format(str(chosensdpath)))

#used for testing
def downloadFileList(filestodownload):
	for fileURLandFileName in filestodownload:
		downloadlocation = get_path(temp_folder+fileURLandFileName[FILE_NAME])
		spewToTextOutput("Downloading file {} from url {}".format(fileURLandFileName[FILE_NAME],fileURLandFileName[URL_STRING]))
		try: 
			urllib.request.urlretrieve(fileURLandFileName[URL_STRING], downloadlocation)
			downloadedFileListLocations += downloadlocation
		
		except:
			spewToTextOutput("Failed to download file {}".format(fileURLandFileName[FILE_NAME]) )
			return False
	return

def downloadFile(downloadas, filetodownload):
	downloadlocation = get_path(temp_folder+downloadas)
	spewToTextOutput("Downloading file {} from url {}".format(downloadas,filetodownload))
	try: 
		urllib.request.urlretrieve(filetodownload, downloadlocation)
	
	except:
		spewToTextOutput("Failed to download file {}".format(downloadas))
		return False
	return

def deleteFile():
	print("test")


def openhelp():
	webbrowser.open_new(helplink)

def installprocess():
	result = tkinter.messagebox.askyesno("Are you sure you're ready to install?", "Are you sure you're ready to install?")
	if not(str(chosensdpath) == "None") and not(str(chosensdpath) == ""):
		if result == True:
#			try:
			spewToTextOutput("Got answer: yes")
			spewToTextOutput("Continuing.")

			
			#get chosen cfw
			selectedcfw = cfwversion.get()
			for flavortext, filename, fileurl in CFWFLAVORS:
				if selectedcfw == flavortext:
					spewToTextOutput("Copying {} to sd card".format(filename))
					downloadFile(filename,fileurl,)
					installfiletosd(filename,"")

	 		#get chosen title installer
			selectedinstaller = nspinstallerversion.get()
			if selectedinstaller == "None":
				spewToTextOutput("No title installer selected, skipping")
			else:
				for flavortext, filename, fileurl, subfolder in NSPINSTALLERS:
					if selectedinstaller == flavortext:
						downloadFile(filename,fileurl)
						spewToTextOutput("Copying {} to sd card".format(filename))	
						installfiletosd(filename,subfolder)

			#get chosen homebrews
			appsToInstall = hblistbox.curselection()
			for selectedApps in appsToInstall:
				fileToDownload = HOMEBREW[selectedApps][DOWNLOAD]
				downloadFile(fileToDownload, HOMEBREW[selectedApps][URLTOGET])
				spewToTextOutput("Copying {} to sd card".format(fileToDownload))
				installfiletosd(fileToDownload,HOMEBREW[selectedApps][INSTALLPATH])

			#get chosen emulators
			appsToInstall = emulistbox.curselection()
			for selectedApps in appsToInstall:
				fileToDownload = EMULATORS[selectedApps][DOWNLOAD]
				downloadFile(fileToDownload, EMULATORS[selectedApps][URLTOGET])
				spewToTextOutput("Copying {} to sd card".format(fileToDownload))
				installfiletosd(fileToDownload,EMULATORS[selectedApps][INSTALLPATH])

			if patchvar.get():
				downloadFile(sigpatches_file[0],sigpatches_file[1])
				spewToTextOutput("Adding sigpatches")
				installfiletosd(sigpatches_file[0], "")

				# except:
				# 	spewToTextOutput("Unknown error in function installprocess()")
		else:
			spewToTextOutput("Got answer: no")
			spewToTextOutput("Not installing...")
	else:
		spewToTextOutput("No directory selected.")

	spewToTextOutput("SD setup finished")


def installfiletosd(filetoinstall,subfolder):
	temppath = get_path(temp_folder+ filetoinstall)

	if filetoinstall.endswith(".nro"):
		if keepfiles.get():
			shutil.copyfile(temppath, os.path.join(os.path.join(chosensdpath,subfolder), filetoinstall))
		else:
			shutil.move(temppath, os.path.join(os.path.join(chosensdpath,subfolder), filetoinstall))

	elif filetoinstall.endswith(".zip"):
		with ZipFile(temppath, 'r') as zipObj:
			try:
				zipObj.extractall(os.path.join(chosensdpath,subfolder))
				spewToTextOutput("{} installed successfully.".format(filetoinstall))
			except:
				spewToTextOutput("Failed to unzip or copy files")
		if not keepfiles.get():
			os.remove(temppath)


#Gui setup
gridrow = 0 #variable for building the gui
mainwindow = tkinter.Tk(screenName=None,  baseName=None,  className='Pozmos installer',  useTk=1)
mainwindow.title("CFWSetup Version {}".format(version))
mainwindow.resizable(False, False)

separatorimage = get_path("separator.png")
separatorimagepath = PhotoImage(file = separatorimage)

cfwlabel = Label(mainwindow, height = 1, text = "Select Firmware Flavor:", font=('Helvetica', 14, 'bold'))
cfwlabel.grid(column = 0, row = gridrow, sticky = "w")

gridrow += 1

cfwversion = StringVar()
cfwversion.set(CFWFLAVORS[0][FLAVOR])
for flavortext, filename, fileurl in CFWFLAVORS:
    b = Radiobutton(mainwindow, text=flavortext, variable=cfwversion, value=flavortext)
    b.grid(column=0, row=gridrow, sticky = "w")
    gridrow += 1

titleinstallerlabel = Label(mainwindow, height = 1, text = "Select Title Installer", font=('Helvetica', 14, 'bold'))
titleinstallerlabel.grid(column = 0, row=gridrow,sticky = "w")
gridrow += 1


nspinstallerversion = StringVar()
nspinstallerversion.set(NSPINSTALLERS[0][FLAVOR])
for flavortext, filename, fileurl, subfolder in NSPINSTALLERS:
    b = Radiobutton(mainwindow, text=flavortext, variable=nspinstallerversion, value=flavortext)
    b.grid(column=0, row=gridrow, sticky = "w")
    gridrow += 1

sigpatchlabel = Label(mainwindow, height = 1, text = "Other:", font=('Helvetica', 14, 'bold'))
sigpatchlabel.grid(column = 0, row=gridrow, sticky = "w")
gridrow += 1

patchvar = IntVar()
patchbutton = Checkbutton(mainwindow, text="Install sigpatches? (recommended)", variable=patchvar)
patchbutton.grid(row=gridrow, sticky="w")
gridrow += 1

keepfiles = IntVar()
keepfilesbutton = Checkbutton(mainwindow, text="Keep files after installation?", variable=keepfiles)
keepfilesbutton.grid(row=gridrow, sticky="w")
gridrow += 1

separatorimageline = Label(mainwindow, image = separatorimagepath,width=300)
separatorimageline.grid(row = gridrow)
gridrow += 1



pathvalue = StringVar()
pathvalue.set("Please select your sd card")
pathtext = Label(mainwindow, height=1, width = 40, textvariable=pathvalue)
pathtext.grid(column=0, row=gridrow,sticky = "w")
gridrow += 1


setpathbutton = Button(mainwindow,text="Select SD root", command=setSDpath, height = 1, width = 40)
setpathbutton.grid(column=0, row=gridrow)
setpathbutton.configure(background = "silver")
gridrow += 1



separatorimageline2 = Label(mainwindow, image = separatorimagepath,width=300)
separatorimageline2.grid(row = gridrow)
gridrow += 1

#installbuttonimagepath = get_path("installbutton.png")
#installbuttonimage = PhotoImage(file = installbuttonimagepath)
installbutton = Button(mainwindow,text = "Install", command=installprocess, height=1, width=40)
installbutton.grid(column=0,row=gridrow)
installbutton.configure(background = "silver")
gridrow += 1


textoutput = Text(mainwindow, height=10, width = 50, font=('Helvetica', 8))
textoutput.grid(column=0, row=gridrow,rowspan = 2)
textoutput.configure({"background": "black"},)
textoutput.configure({"foreground": "white"},)
textoutput.configure(state=DISABLED)
gridrow += 2



verticalseparatorimage = get_path("hseparator.png")
verticalseparatorimagepath = PhotoImage(file = verticalseparatorimage)
verticalseparator = Label(mainwindow, image = verticalseparatorimagepath,width=3, height = 700)
verticalseparator.grid(row = 0,column = 1, sticky = "w", rowspan = gridrow)



#SECOND COLUMN
gridrow = 0

homebrewlabel = Label(mainwindow, height = 1, text = "Additional homebrew", font=('Helvetica', 14, 'bold'))
homebrewlabel.grid(column = 2, row = gridrow, padx=(10, 10))
gridrow += 1


hblistbox = Listbox(mainwindow,selectmode = MULTIPLE,exportselection=0)
hblistbox.grid(column = 2, row = gridrow, rowspan = 5, sticky="nsew")
for flavortext, filename, fileurl, subfolder in HOMEBREW:
   	hblistbox.insert(END, flavortext)
gridrow += 5

separatorimageline3 = Label(mainwindow, image = separatorimagepath,width=230)
separatorimageline3.grid(column = 2, row = gridrow,)
gridrow += 1

emulabel = Label(mainwindow, height = 1, text = "Emulators", font=('Helvetica', 14, 'bold'))
emulabel.grid(column = 2, row = gridrow, padx=(10, 10))
gridrow += 1

emulistbox = Listbox(mainwindow,selectmode = MULTIPLE,exportselection=0)
emulistbox.grid(column = 2, row = gridrow, rowspan = 5, sticky="nsew")
for flavortext, filename, fileurl, subfolder in EMULATORS:
   	emulistbox.insert(END, flavortext)
gridrow += 5
 
gridrow += 1 #to make right column match left column

separatorimageline4 = Label(mainwindow, image = separatorimagepath,width=230)
separatorimageline4.grid(column = 2, row = gridrow,)
gridrow += 1

thankyoulabel = Message(mainwindow, text = thankyoutext, font=('Helvetica', 10, 'bold'))
thankyoulabel.grid(column = 2, row = gridrow, rowspan = 4)
gridrow += 4

# postinstallbuttonimagepath = get_path("postinstallbutton.png")
# postinstallbuttonimage = PhotoImage(file = postinstallbuttonimagepath)
#postinstallbutton = Button(mainwindow,image=postinstallbuttonimage, command=openhelp, height=30, width=290)
postinstallbutton = Button(mainwindow,text="Click here for post-install instructions", command=openhelp, height=8, width=30)
postinstallbutton.grid(column=2,row=gridrow,rowspan = 3)
postinstallbutton.configure(background = "silver")
gridrow += 3

spewToTextOutput("Select your SD path to begin.")
mainwindow.mainloop()

