version = "0.7 (BETA)"

guidetext = """Start by setting your micro SD card up, you'll 
need to select your desired firmware, title installers if 
you wish to install backups (nsps), and any additional homebrew 
or emulators you want. If you have selected a title installer 
you should also tic the 'Install Sigpatches' box.

Select your SD card, or a folder to download the files to, and
click "Install" to download the selected software and have it 
automatically placed in the right location.

Next power off your Switch, you can do this either by shutting 
it down with the power menu, or by holding the power button for
at least 12 seconds.

Finally, insert the micro SD card in your Switch, put your switch
into RCM, select a payload to inject, and push the "Inject using 
fusee" button. If this is your first time using the software, the
button will say 'PyUSB not installed, click to install', clicking
this button will install the PyUSB module from the official source 
using PIP.
"""

#file handling and fusee launching
import os, sys, subprocess
import shutil
chosensdpath = None

#archive handling
from zipfile import ZipFile
import tarfile

#GUI imports (weird import format)
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

import webbrowser
import urllib.request 
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)

#my modules
from locations import * #Get LOCATIONS_DICT, 
from format import * #Text formatting and colors
import webhandler
import homebrewexplorer

HOMEBREWDICT = webhandler.fillStringWithoutDownloading(LOCATIONS_DICT) #Testing function, populate dict with pre-downloaded jsons
#HOMEBREWDICT = webhandler.getUpdatedSoftwareLinks(LOCATIONS_DICT) #Get api jsons and populate dictionary

#populate various sub-dicts, no info changes after this point so they still match the main homebrew dict
firmwareversion = []
for softwarechunk in HOMEBREWDICT:
	if softwarechunk["group"] == "CFW":
		if not softwarechunk["softwaredisabled"]:
			firmwareversion.append(softwarechunk)

tinstaller = []
for softwarechunk in HOMEBREWDICT:
	if softwarechunk["group"] == "TITLEINSTALLER":
		if not softwarechunk["softwaredisabled"]:
			tinstaller.append(softwarechunk)

hbrew = []
for softwarechunk in HOMEBREWDICT:
	if softwarechunk["group"] == "HOMEBREW":
		if not softwarechunk["softwaredisabled"]:	
			hbrew.append(softwarechunk)

rechbrew = []
for softwarechunk in HOMEBREWDICT:
	if softwarechunk["group"] == "REC":
		if not softwarechunk["softwaredisabled"]:
			rechbrew.append(softwarechunk)

emubrew = []
for softwarechunk in HOMEBREWDICT:
	if softwarechunk["group"] == "EMULATOR":
		if not softwarechunk["softwaredisabled"]:
			emubrew.append(softwarechunk)

payloads = []
for softwarechunk in HOMEBREWDICT:
	if softwarechunk["group"] == "PAYLOADS":
		if not softwarechunk["softwaredisabled"]:
			payloads.append(softwarechunk)


fusee_path = "fusee-launcher-master"
selectedConfirmation = None


#used to install pyusb for fusee
pyusbinstalled = None

def get_path(filename):
	return os.path.join(sys.path[0], filename)

def exists(filename):
	return os.path.isfile(filename)

downloadsfolder = get_path("downloads\\")
#if downloads folder hasn't been made create it
if not exists(downloadsfolder):
	os.mkdir(downloadsfolder)


def joinpaths(prefix,suffix):
	return os.path.join(prefix,suffix)

def installPyUSB():
    try:
    	print(subprocess.call([sys.executable, "-m", "pip", "install", "pyusb"]))
    except:
    	print("Error installing pyUSB, do you have pip installed?")


def checkifpyusbinstalled():
	reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
	installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
	if "pyusb" in installed_packages:
		return True
	return False


def injectpayload():
	#check if pyusb installed, if not ask if user wants to install it
	if not checkifpyusbinstalled():
		installpyusb = tkinter.messagebox.askyesno("Install PyUSB?", "PyUSB is required for fusee-launcher to work, install?")
		if installpyusb == True:
			spewToTextOutput("Got answer: yes")
			spewToTextOutput("Installing PyUSB.")
			installPyUSB()
			pyusbinstalled = True

	#check again to see if installed
	if checkifpyusbinstalled():
		# payloadtoinject = payloadlistbox.curselection()
		if payloadVar == None:
			spewToTextOutput("No payload selected")
			return

		payloadtoinject = payloadVar.get()
		print("injecting {}".format(payloadtoinject))
		downloadfileas = ""
		for softwarechunk in payloads:
			if softwarechunk["software"] == payloadtoinject:
				fileurl = softwarechunk["directlink"]
				filename = fileurl.rsplit('/', 1)[-1]
				downloadFile(filename, fileurl)	#regardless of zip format we need to start by downloading the file
				if not softwarechunk["itemslist"] == None: #IF WE HAVE SPECIFIED AN ITEM TO EXTRACT, IT'S A ZIP
					downloadedfilename = os.path.join(get_path(downloadsfolder), filename)
					print("File exists: {}".format(exists(downloadedfilename)))
					with ZipFile(downloadedfilename, 'r') as zipObj:
						# try:
							zipObj.extractall(get_path(downloadsfolder))
							filename = os.path.join(get_path(downloadsfolder), softwarechunk["itemslist"]["payload"])
						# except:
						# 	spewToTextOutput("Failed to unzip or copy files")	
						# 	return
				else:
					filename = get_path(os.path.join(downloadsfolder, filename))



		spewToTextOutput("Injecting payload {}".format(filename))

		fusee_file = os.path.join(fusee_path, "fusee-launcher.py")
		script_path = get_path(fusee_file)
		payload_path = filename
		print("injecting path {}".format(payload_path))
		p = subprocess.Popen([sys.executable, '-u', script_path, payload_path],
		          stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1)
		with p.stdout:
		    for line in iter(p.stdout.readline, b''):
		        spewBytesToTextOutput(line)
		p.wait()

#not used yet, will be useful for grabbing a few things
def extractTar(tarfilename, target):
	if (tarfilename.endswith("tar.gz")):
	    tar = tarfilename.open(fname, "r:gz")
	    tar.extractall(path = target)
	    tar.close()
	elif (fname.endswith("tar")):
	    tar = tarfilename.open(fname, "r:")
	    tar.extractall(path = target)
	    tar.close()



def spewToTextOutput(textToSpew):
	textoutput.config(state=NORMAL)
	textoutput.insert(END, textToSpew + "\n\n")
	textoutput.config(state=DISABLED)
	textoutput.see(END)
	print(textToSpew)

def spewBytesToTextOutput(textToSpew):
	textoutput.config(state=NORMAL)
	textoutput.insert(END, (textToSpew.decode("utf-8") + "\n\n"))
	textoutput.config(state=DISABLED)
	textoutput.see(END)
	print(textToSpew)


#update global "chosensdpath"
def setSDpath():
	global chosensdpath
	chosensdpath = filedialog.askdirectory(initialdir="/",  title='Please select a directory to install to')
	pathvalue.set(str(chosensdpath))
	spewToTextOutput("Install path set to: {}".format(str(chosensdpath)))

def downloadFile(downloadas, filetodownload):
	downloadlocation = get_path(os.path.join(downloadsfolder+downloadas))
	print("Downloading as {}".format(downloadlocation))
	spewToTextOutput("Downloading file {} from url {}".format(downloadas,filetodownload))
	# try: 
	urllib.request.urlretrieve(filetodownload, downloadlocation)
	
	# except:
	# 	spewToTextOutput("Failed to download file {}".format(downloadas))
	# 	return False
	return


def installprocess():
	result = tkinter.messagebox.askyesno("Are you sure you're ready to install?", "Are you sure you're ready to install?")
	if not(str(chosensdpath) == "None") and not(str(chosensdpath) == ""):
		if result == True:
#			try:
			spewToTextOutput("Got answer: yes")
			spewToTextOutput("Continuing.")
			
			appsToInstall = fwlistbox.curselection() #get the selected fw to install
			installfromselectionandlist(appsToInstall, firmwareversion) #install it (needs reference to list of firmware)

	 		#get chosen title installer
			appsToInstall = tilistbox.curselection()
			installfromselectionandlist(appsToInstall, tinstaller)								

			#get  homebrew
			appsToInstall = hblistbox.curselection()
			installfromselectionandlist(appsToInstall, hbrew)	

			#get recommended homebrew
			appsToInstall = reccomendedHBlistbox.curselection()
			installfromselectionandlist(appsToInstall, rechbrew)

			#get chosen emulators
			appsToInstall = emulistbox.curselection()
			installfromselectionandlist(appsToInstall, emubrew)

			if patchvar.get():
				for softwarechunk in HOMEBREWDICT:
					if softwarechunk["software"] == "sigpatches":
						fileurl = softwarechunk["directlink"]
						filename = fileurl.rsplit('/', 1)[-1]			
						downloadFile(filename,fileurl)
						spewToTextOutput("Adding sigpatches")
						installfiletosd(filename, "")

				# except:
				# 	spewToTextOutput("Unknown error in function installprocess()")
		else:
			spewToTextOutput("Got answer: no")
			spewToTextOutput("Not installing...")
	else:
		spewToTextOutput("No directory selected.")

	spewToTextOutput("SD setup finished")



def installfromselectionandlist(appsToInstall, dicty):
	for selection in appsToInstall:
		fileurl = dicty[selection]["directlink"]
		filename = fileurl.rsplit('/', 1)[-1]
		subfolder = dicty[selection]["subfolder"]
		downloadFile(filename,fileurl)
		spewToTextOutput("Copying {} to sd card".format(filename))

		if subfolder == None:
			installfiletosd(filename,"")	
		else:
			installfiletosd(filename,subfolder)

def installfiletosd(filetoinstall,subfolder):
	temppath = get_path(os.path.join(downloadsfolder + filetoinstall))
	print(temppath)
	if filetoinstall.endswith(".nro"):
		try:
			if keepfiles.get():
				shutil.copyfile(temppath, os.path.join(os.path.join(chosensdpath,subfolder), filetoinstall))
			else:
				shutil.move(temppath, os.path.join(os.path.join(chosensdpath,subfolder), filetoinstall))
		except: 
			print("Failed to copy {} to SD".format(filetoinstall) )

	elif filetoinstall.endswith(".zip"):
		with ZipFile(temppath, 'r') as zipObj:
			try:
				zipObj.extractall(os.path.join(chosensdpath,subfolder))
				spewToTextOutput("{} installed successfully.".format(filetoinstall))
			except:
				spewToTextOutput("Failed to unzip or copy files")
		if not keepfiles.get():
			os.remove(temppath)




#GUI Definitions
def filllistboxwithcolor(homebrewlistbox,homebrewlist):
	homebrewlistbox.bind('<<ListboxSelect>>',CurSelet)
	homebrewlistbox.config(borderwidth=0)
	homebrewlistbox.config(highlightthickness=1)
	for softwarechunk in homebrewlist:
		  # btn1 = tkinter.Button(root, text="button 1")
    	# button1_ttp = CreateToolTip(btn1, "mouse is over button 1")
		homebrewlistbox.insert(END, softwarechunk["software"])
		homebrewlistbox.itemconfig(END, foreground=listboxcolor)
		if softwarechunk["gotjson"] == False:
			homebrewlistbox.itemconfig(END, foreground=warningsoft)	
		if softwarechunk["uptodate"] == False:
			homebrewlistbox.itemconfig(END, foreground=warninghard)

#binding to get the most recently selected homebrew
lastclicked = []
def CurSelet(event):
	widget = event.widget
	selection=widget.curselection()
	try:
		picked = widget.get(selection[0])
		print(picked)

		softwarenumber = 0
		for softwarechunk in HOMEBREWDICT:
			if softwarechunk["software"] == picked:
				softwarechunknumber = softwarenumber
			softwarenumber+= 1


		homebrewexplorer.updatePage(softwarechunknumber)
	except: 
		print("nooption")

def openhelpwindow():
	guidewindow = tkinter.Toplevel(screenName=None,  baseName=None,)
	guidewindow.title("CFWSetup Guide")
	guidewindow.resizable(False, False)
	# guidewindow.iconbitmap(get_path("cfwsetupicon.ico")) Was breaking on linux/windows
	guidelabel = Message(guidewindow, text = guidetext, font=smallboldtext)
	guidelabel.grid(column = 0, row = 0, padx=(0,0), pady=(0,0))
	guidelabel.configure(background=backgroundcolor)
	guidelabel.configure(foreground=labelcolor)

# def starthbbrowser():
# 	# homebrewexplorer.startBrowser(HOMEBREWDICT, "external")


browseropen = False
def togglehbwindow():
	global browseropen
	if not browseropen:

		homebrewexplorer.startBrowserInternal(HOMEBREWDICT, 0, mainwindow, 3)
		browseropen = True
		return
	homebrewexplorer.destroyBrowserInternal()
	browseropen = False
	return


#Build Gui
COLA = 0
COLB = 1
COLC = 2


#Gotta clean this up, learned a lot since then, but it works so it's low-priority
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

#Links
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


HELPANDTOOLSDROPDOWN = [
	["Drive Format Tool", "https://gparted.org/",OPENFAT32],
	["Verify SD Card Is Legit", "https://www.heise.de/download/product/h2testw-50539/download",OPENSDCHECKER],
	["Firmware Downgrade Guide", "https://guide.sdsetup.com/usingcfw/manualchoiupgrade,",OPENDOWNGRADEGUIDE],
	["NXThemes Usage Guide", "https://gbatemp.net/download/nxthemes-installer.35408/",OPENNXTHEMESGUIDE],
	["Nintendo Switch Saves", "https://gbatemp.net/threads/new-switch-save-site-with-modified-saves-and-100-completed-saves.508661/",OPENSWITCHSAVES],
	["Developer Discord / Support", "https://discord.gg/cXtmY9M",OPENDISCORD],
]


gridrow = 0 #variable for building the gui
maxgrid = 0
mainwindow = tkinter.Tk(screenName=None,  baseName=None)
mainwindow.title("CFWSetup Version {}".format(version))
mainwindow.resizable(False, False)
mainwindow.configure(background=backgroundcolor)
# mainwindow.iconbitmap(get_path("cfwsetupicon.ico"))

main_menu = tkinter.Menu(mainwindow)
mainwindow.config(menu = main_menu)


main_menu.add_command(label = "Usage Guide", command = openhelpwindow)

helpandtoolsmenu = tkinter.Menu(main_menu) 
main_menu.add_cascade(label = "Help and Tools", menu = helpandtoolsmenu) # it creates the name of the sub menu
for links in HELPANDTOOLSDROPDOWN:
	main_menu.config(background = backgroundcolor)
	helpandtoolsmenu.add_command(label = links[LINKTEXT], command = links[LINKCOMMAND])

main_menu.add_command(label = "Homebrew Explorer", command = togglehbwindow,)

payloadmenu = tkinter.Menu(mainwindow)
payloadNum = 0
payloadVar = StringVar()
payloadmenu.add_command(label = "Inject", command = injectpayload)
payloadmenu.add_separator()
for softwarechunk in payloads:
	payloadmenu.add_radiobutton(label = softwarechunk["software"], variable = payloadVar, value = softwarechunk["software"])

main_menu.add_cascade(label = "Inject Payload", menu=payloadmenu)



#COLUMN A
cfwlabel = Label(mainwindow, height = 1, text = "Firmware Flavor:", font=(labelfont, 14, 'bold'),)
cfwlabel.grid(column = COLA, row = gridrow, sticky = "w",pady=(0))
cfwlabel.configure(background=backgroundcolor)
cfwlabel.configure(foreground=labelcolor)

gridrow += 1

fwlistbox = Listbox(mainwindow,exportselection=0,height=7,font = maintext,selectbackground = "gray20")
fwlistbox.grid(column = COLA, row = gridrow, rowspan = 1, columnspan=1, sticky="new",pady=(0))
fwlistbox.configure(background=selectionboxcolor)
filllistboxwithcolor(fwlistbox,firmwareversion) #build listbox
gridrow += 1

titleinstallerlabel = Label(mainwindow, height = 1, text = "Select Title Installer", font=(labelfont, 14, 'bold'))
titleinstallerlabel.grid(column = COLA, row=gridrow,sticky = "w",pady=(0))
titleinstallerlabel.configure(background=backgroundcolor)
titleinstallerlabel.configure(foreground=labelcolor)
gridrow += 1

tilistbox = Listbox(mainwindow,selectmode = MULTIPLE,exportselection=0,font = maintext,selectbackground = "gray20")
tilistbox.grid(column = COLA, row = gridrow, sticky="nsew",pady=(0))
tilistbox.configure(background=selectionboxcolor)
filllistboxwithcolor(tilistbox,tinstaller)
gridrow += 1

sigpatchlabel = Label(mainwindow, height = 1, text = "Other:", font=(labelfont, 14, 'bold'))
sigpatchlabel.grid(column = COLA, row=gridrow, sticky = "w",pady=(0))
sigpatchlabel.configure(background=backgroundcolor)
sigpatchlabel.configure(foreground=labelcolor)
gridrow += 1

patchvar = IntVar()
patchbutton = Checkbutton(mainwindow, text="Install sigpatches? (recommended)", variable=patchvar, font=smallboldtext)
patchbutton.grid(column = COLA, row=gridrow, sticky="w",pady=(0))
patchbutton.configure(background=backgroundcolor)
patchbutton.configure(selectcolor=backgroundcolor)
patchbutton.configure(activebackground=backgroundcolor)
patchbutton.configure(activeforeground=listboxcolor)
patchbutton.configure(foreground=listboxcolor)
gridrow += 1

keepfiles = IntVar()
keepfilesbutton = Checkbutton(mainwindow, text="Keep files after installation? '/downloads''", variable=keepfiles, font=smallboldtext,)
keepfilesbutton.grid(column = COLA, row=gridrow, sticky="nsw",pady=(0))
keepfilesbutton.configure(background=backgroundcolor)
keepfilesbutton.configure(selectcolor=backgroundcolor)
keepfilesbutton.configure(activebackground=backgroundcolor)
keepfilesbutton.configure(activeforeground=listboxcolor)
keepfilesbutton.configure(foreground=listboxcolor)
gridrow += 1

textoutput = Text(mainwindow, height=10, width = 90, font=consoletextfont)
textoutput.grid(column= COLA, row=gridrow,rowspan = 4,columnspan = 2)
textoutput.configure({"background": consolecolor},)
textoutput.configure({"foreground": consoletextcolor},)
textoutput.configure(state=DISABLED)
gridrow += 4

pathvalue = StringVar()
pathvalue.set("Please select your sd card")
setpathbutton = Button(mainwindow,textvariable=pathvalue, command=setSDpath, height = 1, width = 53, font=boldtext)
setpathbutton.grid(column= COLA, row=gridrow,columnspan = 2,pady=(0))
setpathbutton.configure(background = selectionboxcolor)
setpathbutton.configure(foreground = bigbuttontextcolor)
gridrow += 1

installbutton = Button(mainwindow,text = "Install", command=installprocess, height=1, width=53,font=(boldtext))
installbutton.grid(column= COLA,row=gridrow,columnspan = 2,pady=(0))
installbutton.configure(background = installbuttoncolor)
installbutton.configure(foreground = bigbuttontextcolor)


if maxgrid < gridrow:
	maxgrid = gridrow

#COLUMN B
gridrow = 0

reccomendedHomebrewLabel = Label(mainwindow, height = 1, text = "Recommended homebrew", font=(labelfont, 14, 'bold'))
reccomendedHomebrewLabel.grid(column = COLB, row = gridrow,pady=(0),sticky="news")
reccomendedHomebrewLabel.configure(background=backgroundcolor)
reccomendedHomebrewLabel.configure(foreground=labelcolor)
gridrow += 1

reccomendedHBlistbox = Listbox(mainwindow,selectmode = MULTIPLE,exportselection=0,height=7,font = maintext,selectbackground = "gray20")
reccomendedHBlistbox.grid(column = COLB,  row = gridrow, rowspan = 1, columnspan=1, sticky="ew",pady=(0))
reccomendedHBlistbox.configure(background=selectionboxcolor)
filllistboxwithcolor(reccomendedHBlistbox,rechbrew)
gridrow += 1

homebrewLabel = Label(mainwindow, height = 1, text = "Additional homebrew", font=(labelfont, 14, 'bold'))
homebrewLabel.grid(column = COLB, row = gridrow,pady=(0))
homebrewLabel.configure(background=backgroundcolor)
homebrewLabel.configure(foreground=labelcolor)
gridrow += 1

hblistbox = Listbox(mainwindow,selectmode = MULTIPLE,exportselection=0,font = maintext,selectbackground = "gray20")
hblistbox.grid(column = COLB, row = gridrow, rowspan = 1, sticky="nsew",pady=(0))
hblistbox.configure(background=selectionboxcolor)
filllistboxwithcolor(hblistbox,hbrew)
gridrow += 1

emulabel = Label(mainwindow, height = 1, text = "Emulators", font=(labelfont, 14, 'bold'))
emulabel.grid(column = COLB, row = gridrow,pady=(0))
emulabel.configure(background=backgroundcolor)
emulabel.configure(foreground=labelcolor)
gridrow += 1

emulistbox = Listbox(mainwindow,selectmode = MULTIPLE,exportselection=0, height = 2,font = maintext,selectbackground = "gray20")
emulistbox.grid(column = COLB, row = gridrow, rowspan = 2, sticky="nsew",pady=(0))
emulistbox.configure(background=selectionboxcolor)
filllistboxwithcolor(emulistbox,emubrew)
gridrow += 2

if maxgrid < gridrow:
	maxgrid = gridrow

#COLC


spewToTextOutput("Select your SD path to begin.")


mainwindow.mainloop()