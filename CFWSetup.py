version = "0.2 (BETA)"


from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
import tkinter
import os, sys
from zipfile import ZipFile
import webbrowser
import time
import urllib.request 

chosensdpath = None
selectedConfirmation = None
temp_folder = "temp/" #hate all you want for the unix-style slashes ;D

helplink = "https://guide.sdsetup.com/"


#DEFINITIONS
FILE_NAME = 0
URL_STRING = 1

#FILES, DOWNLOAD LOCATIONS, CFW NAME STRINGS
CFWFLAVORS = [
	["Kosmos (atmos 0.8.5) ","kosmos.zip", "https://github.com/AtlasNX/Kosmos/releases/download/v11.11.1/KosmosV11111.zip"],
	["Atmos (vanilla 0.8.5)", "atmos.zip", "https://github.com/Atmosphere-NX/Atmosphere/releases/download/0.8.5/atmosphere-0.8.5-master-b42d16cf+hbl-2.1+hbmenu-3.0.1.zip"],
]

#FORMAT FRIENDLY NAME, DOWNLOAD NAME, DOWNLOAD URL, INSTALL PATH
NSPINSTALLERS = [
	["None", None, None, None],
	["Tinfoil (blawar)","lithium.zip", "http://tinfoil.io/repo/lithium.latest.zip",""],
	["Lithium (blawar)","tinfoilblawar.zip", "http://tinfoil.io/repo/tinfoil.latest.zip",""],
	["Tinfoil (addubz)","addubztinfoil.zip", "https://bsnx.lavatech.top/tinfoil/tinfoil-883e3bd.zip","switch"],
	["Goldleaf (XorTroll)","xortrollgoldleaf.zip","https://bsnx.lavatech.top/goldleaf/goldleaf-d212c5a.zip","goldleaf"],
	#goldleaf and addubz tinfoil currently throw a 403: forbidden
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

def openhelp():
	webbrowser.open_new(helplink)

def installprocess():
	result = tkinter.messagebox.askyesno("Are you sure you're ready to install?", "Are you sure you're ready to install?")
	if len(str(chosensdpath)) > 1:
		if result == True:
#			try:
			spewToTextOutput("Got answer: yes")
			spewToTextOutput("Continuing.")

			#get chosen cfw
			selectedcfw = cfwversion.get()
			for flavortext, filename, fileurl in CFWFLAVORS:
				if selectedcfw == flavortext:
					spewToTextOutput("Downloading and copying {} to sd card".format(filename))
					downloadFile(filename,fileurl,)
					installziptosd(filename,"")

	 		#get chosen title installer
			selectedinstaller = nspinstallerversion.get()
			if selectedinstaller == "None":
				spewToTextOutput("No title installer selected, skipping")
			else:
				for flavortext, filename, fileurl, subfolder in NSPINSTALLERS:
					if selectedinstaller == flavortext:
						spewToTextOutput("Downloading and copying {} to sd card".format(filename))
						downloadFile(filename,fileurl)
						installziptosd(filename,subfolder)

			if patchvar.get():
				downloadFile(sigpatches_file[0],sigpatches_file[1])
				installziptosd(sigpatches_file[0], "")

				# except:
				# 	spewToTextOutput("Unknown error in function installprocess()")
		else:
			spewToTextOutput("Got answer: no")
			spewToTextOutput("Not installing...")
	else:
		spewToTextOutput("No directory selected.")

	spewToTextOutput("SD setup finished")


def installziptosd(ziptoinstall,subfolder):
	textoutput.config(state=NORMAL)
	textoutput.insert(END, "Copying {} to {}".format(ziptoinstall, chosensdpath))
	textoutput.config(state=DISABLED)
	textoutput.see(END)

	with ZipFile(get_path(temp_folder+ ziptoinstall), 'r') as zipObj:
		try:
			zipObj.extractall(os.path.join(chosensdpath,subfolder))
			spewToTextOutput("{} installed successfully.".format(ziptoinstall))
		except:
			spewToTextOutput("Failed to unzip or copy files")




#Gui setup
gridrow = 0; #variable for building the gui
mainwindow = tkinter.Tk(screenName=None,  baseName=None,  className='Pozmos installer',  useTk=1)
mainwindow.title("CFWSetup Version {}".format(version))
mainwindow.resizable(False, False)

separatorimage = get_path("separator.png")
separatorimagepath = PhotoImage(file = separatorimage)

cfwlabel = Label(mainwindow, height = 1, text = "Select Firmware Flavor:", font=('Helvetica', 14, 'bold'))
cfwlabel.grid(column = 0, row = gridrow, sticky = "w")
gridrow += 1

cfwversion = StringVar()
cfwversion.set(CFWFLAVORS[0][0])
for flavortext, filename, fileurl in CFWFLAVORS:
    b = Radiobutton(mainwindow, text=flavortext, variable=cfwversion, value=flavortext)
    b.grid(column=0, row=gridrow, sticky = "w")
    gridrow += 1

hbrewlabel = Label(mainwindow, height = 1, text = "Select Title Installer", font=('Helvetica', 14, 'bold'))
hbrewlabel.grid(column = 0, row=gridrow, sticky = "w")
gridrow += 1

nspinstallerversion = StringVar()
nspinstallerversion.set(NSPINSTALLERS[0][0])
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


separatorimageline = Label(mainwindow, image = separatorimagepath)
separatorimageline.grid(row = gridrow)
gridrow += 1



pathvalue = StringVar()
pathvalue.set("Please select your sd card")
pathtext = Label(mainwindow, height=1, width = 60, textvariable=pathvalue)
pathtext.grid(column=0, row=gridrow,)
gridrow += 1


setpathbutton = Button(mainwindow,text="Select SD root", command=setSDpath, height = 1, width = 60)
setpathbutton.grid(column=0, row=gridrow,)
gridrow += 1



separatorimageline2 = Label(mainwindow, image = separatorimagepath)
separatorimageline2.grid(row = gridrow)
gridrow += 1

#installbuttonimagepath = get_path("installbutton.png")
#installbuttonimage = PhotoImage(file = installbuttonimagepath)
installbutton = Button(mainwindow,text = "Install", command=installprocess, height=1, width=60)
installbutton.grid(column=0,row=gridrow,columnspan = 2,sticky = "w")
gridrow += 1


textoutput = Text(mainwindow, height=10, width = 50)
textoutput.grid(column=0, row=gridrow,columnspan = 2,rowspan = 2)
textoutput.config(state=DISABLED)
gridrow += 2

postinstallbuttonimagepath = get_path("postinstallbutton.png")
postinstallbuttonimage = PhotoImage(file = postinstallbuttonimagepath)
postinstallbutton = Button(mainwindow,image=postinstallbuttonimage, command=openhelp, height=30, width=400)
postinstallbutton.grid(column=0,row=gridrow,columnspan = 1,rowspan = 2)
gridrow += 2

spewToTextOutput("Select your SD path to begin.")
mainwindow.mainloop()

