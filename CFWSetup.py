version = "0.6 (BETA)"

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

#tkinter doesn't include everything by default
import tkinter
from tkinter import *
import tkinter.font as tkFont
from tkinter import filedialog
from tkinter import messagebox

#file handling and fusee launching
import os, sys, subprocess
import shutil
chosensdpath = None
#archive handling 
from zipfile import ZipFile
import tarfile

#URLS, Friendly names, install paths
from locations import *
import webgrabber 

import urllib.request 
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)

HOMEBREWDICT = webgrabber.fillStringWithoutDownloading()
HOMEBREWDICT = webgrabber.getUpdatedSoftwareLinks()
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

#COLORSANDFONTS
labelfont = "Helvetica"
backgroundcolor = "darkgrey"

#used to install pyusb for fusee
pyusbinstalled = None
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

# def openusbwindow():
# 	pyusbwindow = tkinter.Tk(screenName=None,  baseName=None,  className='CFWGuide',  useTk=1)
# 	pyusbwindow.title("Install PyUSB?")
# 	pyusbwindow.resizable(False, False)
# 	pyusbwindow.iconbitmap(get_path("cfwsetupicon.ico"))
# 	pyusblabel = Message(pyusbwindow, text = "fusee-launcher requires PyUSB to work, install it?", font=(labelfont, 9, 'bold'))
# 	pyusblabel.grid(column = 0, row = 0, padx=(0,0), pady=(0,0))
# 	pyusblabel.configure(background=backgroundcolor)

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
		
		downloadFile(filename, fileurl)

		spewToTextOutput("Injecting payload {}".format(filename))

		fusee_file = os.path.join(fusee_path, "fusee-launcher.py")
		script_path = get_path(fusee_file)
		payload_path = get_path(downloadsfolder + filename)
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

def get_path(filename):
	return os.path.join(sys.path[0], filename)

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

downloadsfolder = get_path("downloads\\")
def installprocess():
	result = tkinter.messagebox.askyesno("Are you sure you're ready to install?", "Are you sure you're ready to install?")
	if not(str(chosensdpath) == "None") and not(str(chosensdpath) == ""):
		if result == True:
#			try:
			spewToTextOutput("Got answer: yes")
			spewToTextOutput("Continuing.")
			
			#get chosen cfw
			selectedcfw = cfwversion.get()
			print(selectedcfw)
			for softwarechunk in firmwareversion:
				if softwarechunk["software"] == selectedcfw:
					fileurl = softwarechunk["directlink"]
					filename = fileurl.rsplit('/', 1)[-1]
					downloadFile(filename,fileurl)
					spewToTextOutput("Copying {} to sd card".format(filename))
					installfiletosd(filename,"")

	 		#get chosen title installer
			appsToInstall = tilistbox.curselection()
			print(appsToInstall)
			for selection in appsToInstall:
				fileurl = tinstaller[selection]["directlink"]
				filename = fileurl.rsplit('/', 1)[-1]
				subfolder = tinstaller[selection]["subfolder"]
				downloadFile(filename,fileurl)
				spewToTextOutput("Copying {} to sd card".format(filename))
				if subfolder == None:
					installfiletosd(filename,"")	
				else:
					installfiletosd(filename,subfolder)										

			#get  homebrew
			appsToInstall = hblistbox.curselection()
			print(appsToInstall)
			for selection in appsToInstall:
				fileurl = hbrew[selection]["directlink"]
				filename = fileurl.rsplit('/', 1)[-1]
				subfolder = hbrew[selection]["subfolder"]
				downloadFile(filename,fileurl)
				spewToTextOutput("Copying {} to sd card".format(filename))
				if subfolder == None:
					installfiletosd(filename,"")	
				else:
					installfiletosd(filename,subfolder)		

			#get recommended homebrew
			appsToInstall = reccomendedHBlistbox.curselection()
			print(appsToInstall)
			for selection in appsToInstall:
				fileurl = rechbrew[selection]["directlink"]
				filename = fileurl.rsplit('/', 1)[-1]
				subfolder = rechbrew[selection]["subfolder"]
				downloadFile(filename,fileurl)
				spewToTextOutput("Copying {} to sd card".format(filename))
				if subfolder == None:
					installfiletosd(filename,"")	
				else:
					installfiletosd(filename,subfolder)

			#get chosen emulators
			appsToInstall = emulistbox.curselection()
			print(appsToInstall)
			for selection in appsToInstall:
				fileurl = emubrew[selection]["directlink"]
				filename = fileurl.rsplit('/', 1)[-1]
				subfolder = emubrew[selection]["subfolder"]
				downloadFile(filename,fileurl)
				spewToTextOutput("Copying {} to sd card".format(filename))
				if subfolder == None:
					installfiletosd(filename,"")	
				else:
					installfiletosd(filename,subfolder)

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

#Build Gui
COLA = 0
COLB = 1
COLC = 4
MAXCOL = 0

windowheight = 720

gridrow = 0 #variable for building the gui
mainwindow = tkinter.Tk(screenName=None,  baseName=None,  className='CFWSetupandinjector',  useTk=1)
mainwindow.title("CFWSetup Version {}".format(version))
mainwindow.resizable(False, False)

mainwindow.iconbitmap(get_path("cfwsetupicon.ico"))

def openhelpwindow():
	guidewindow = tkinter.Tk(screenName=None,  baseName=None,  className='CFWGuide',  useTk=1)
	guidewindow.title("CFWSetup Guide")
	guidewindow.resizable(False, False)
	guidewindow.iconbitmap(get_path("cfwsetupicon.ico"))
	guidelabel = Message(guidewindow, text = guidetext, font=(labelfont, 9, 'bold'))
	guidelabel.grid(column = 0, row = 0, padx=(0,0), pady=(0,0))
	guidelabel.configure(background=backgroundcolor)

main_menu = tkinter.Menu(mainwindow)
mainwindow.config(menu = main_menu)

main_menu.add_command(label = "Usage Guide", command = openhelpwindow)

helpandtoolsmenu = tkinter.Menu(main_menu) 
main_menu.add_cascade(label = "Help and Tools", menu = helpandtoolsmenu) # it creates the name of the sub menu
for links in HELPANDTOOLSDROPDOWN:
	main_menu.config(background = backgroundcolor)
	helpandtoolsmenu.add_command(label = links[LINKTEXT], command = links[LINKCOMMAND])



payloadmenu = tkinter.Menu(mainwindow)
payloadNum = 0
payloadVar = StringVar()
payloadmenu.add_command(label = "Inject", command = injectpayload)
payloadmenu.add_separator()
for softwarechunk in payloads:
	payloadmenu.add_radiobutton(label = softwarechunk["software"], variable = payloadVar, value = softwarechunk["software"])


main_menu.add_cascade(label = "Inject Payload", menu=payloadmenu)

mainwindow.configure(background=backgroundcolor)

#COLUMN A
cfwlabel = Label(mainwindow, height = 1, text = "Select Firmware Flavor:", font=(labelfont, 14, 'bold'))
cfwlabel.grid(column = COLA, row = gridrow, sticky = "w",pady=(0))
cfwlabel.configure(background=backgroundcolor)
gridrow += 1


cfwversion = StringVar()
# cfwversion.set(cfw[0]["software"],)
loc = 0
cfwversion.set(firmwareversion[0]["software"])
for softwarechunk in firmwareversion:
	b = Radiobutton(mainwindow, text=softwarechunk["software"], variable=cfwversion, value=softwarechunk["software"])
	b.grid(column=COLA, row=gridrow, sticky = "w")
	b.configure(background=backgroundcolor)
	gridrow += 1

titleinstallerlabel = Label(mainwindow, height = 1, text = "Select Title Installer", font=(labelfont, 14, 'bold'))
titleinstallerlabel.grid(column = COLA, row=gridrow,sticky = "w",pady=(0))
titleinstallerlabel.configure(background=backgroundcolor)
gridrow += 1

tilistbox = Listbox(mainwindow,selectmode = MULTIPLE,exportselection=0)
tilistbox.grid(column = COLA, row = gridrow, rowspan = 1, sticky="nsew",pady=(0))
tilistbox.configure(background=backgroundcolor)
for softwarechunk in tinstaller:
		tilistbox.insert(END, softwarechunk["software"])

gridrow += 1		
sigpatchlabel = Label(mainwindow, height = 1, text = "Other:", font=(labelfont, 14, 'bold'))
sigpatchlabel.grid(column = COLA, row=gridrow, sticky = "w",pady=(0))
sigpatchlabel.configure(background=backgroundcolor)
gridrow += 1

patchvar = IntVar()
patchbutton = Checkbutton(mainwindow, text="Install sigpatches? (recommended)", variable=patchvar)
patchbutton.grid(column = COLA, row=gridrow, sticky="w",pady=(0))
patchbutton.configure(background=backgroundcolor)
gridrow += 1

keepfiles = IntVar()
keepfilesbutton = Checkbutton(mainwindow, text="Keep files after installation? '/temp'", variable=keepfiles)
keepfilesbutton.grid(column = COLA, row=gridrow, sticky="w",pady=(0))
keepfilesbutton.configure(background=backgroundcolor)
gridrow += 1

pathvalue = StringVar()
pathvalue.set("Please select your sd card")
pathtext = Label(mainwindow, height=1, width = 30, textvariable=pathvalue)
pathtext.grid(column= COLA, row=gridrow,pady=(0))
pathtext.configure(background=backgroundcolor)
gridrow += 1

setpathbutton = Button(mainwindow,text="Select SD root", command=setSDpath, height = 1, width = 30)
setpathbutton.grid(column= COLA, row=gridrow,pady=(0))
setpathbutton.configure(background = "silver")
gridrow += 1

textoutput = Text(mainwindow, height=10, width = 80, font=(labelfont, 8))
textoutput.grid(column= COLA, row=gridrow,rowspan = 4,columnspan = 2)
textoutput.configure({"background": "black"},)
textoutput.configure({"foreground": "white"},)
textoutput.configure(state=DISABLED)
gridrow += 4

installbutton = Button(mainwindow,text = "Install", command=installprocess, height=1, width=75,font=(labelfont, 9, 'bold'))
installbutton.grid(column= COLA,row=gridrow,columnspan = 2,pady=(10))
installbutton.configure(background = "grey")
gridrow += 1


if gridrow > MAXCOL:
	MAXCOL = gridrow

#COLUMN B
gridrow = 0

reccomendedHomebrewLabel = Label(mainwindow, height = 1, text = "Recommended homebrew", font=(labelfont, 14, 'bold'))
reccomendedHomebrewLabel.grid(column = COLB, row = gridrow,pady=(0))
reccomendedHomebrewLabel.configure(background=backgroundcolor)
gridrow += 1

reccomendedHBlistbox = Listbox(mainwindow,selectmode = MULTIPLE,exportselection=0,height=1)
reccomendedHBlistbox.grid(column = COLB, row = gridrow, rowspan = 2, sticky="nsew")
reccomendedHBlistbox.configure(background=backgroundcolor)
for softwarechunk in rechbrew:
   		reccomendedHBlistbox.insert(END, softwarechunk["software"])
gridrow += 2

homebrewLabel = Label(mainwindow, height = 1, text = "Additional homebrew", font=(labelfont, 14, 'bold'))
homebrewLabel.grid(column = COLB, row = gridrow,pady=(0))
homebrewLabel.configure(background=backgroundcolor)
gridrow += 1

hblistbox = Listbox(mainwindow,selectmode = MULTIPLE,exportselection=0)
hblistbox.grid(column = COLB, row = gridrow, rowspan = 1, sticky="nsew",pady=(0))
hblistbox.configure(background=backgroundcolor)
for softwarechunk in hbrew:
   	hblistbox.insert(END, softwarechunk["software"])
gridrow += 1

# separatorimageline3 = Label(mainwindow, image = separatorimagepath,width=230)
# separatorimageline3.grid(column = COLB, row = gridrow,)
# gridrow += 1

emulabel = Label(mainwindow, height = 1, text = "Emulators", font=(labelfont, 14, 'bold'))
emulabel.grid(column = COLB, row = gridrow,pady=(0))
emulabel.configure(background=backgroundcolor)
gridrow += 1

emulistbox = Listbox(mainwindow,selectmode = MULTIPLE,exportselection=0, height = 2)
emulistbox.grid(column = COLB, row = gridrow, rowspan = 4, sticky="nsew",pady=(0))
emulistbox.configure(background=backgroundcolor)
for softwarechunk in emubrew:
   	emulistbox.insert(END, softwarechunk["software"])
gridrow += 4



#Try to implement  something like this
#  tix_Balloon102.py
# Tkinter extension module tix comes with Python27 and Python3+
# tix has addtional widgets like ...
# tix.Balloon (acts like a tooltip)
# 
# try:
#     # Python2
#     import Tix as tix
# except ImportError:
#     # Python3
#     import tkinter.tix as tix
# root = tix.Tk()
# def hello():
#     label['text'] = 'Hello World'
#     #label.config(text='Hello World')
# def bye():
#     label['text'] = 'Bye Cruel World'
# label = tix.Label(root, width=40, relief=tix.SUNKEN, bd=1)
# btn1 = tix.Button(root, text="Hello", command=hello)
# btn2 = tix.Button(root, text="Bye", command=bye)
# # create balloon (tooltip) instance
# balloon = tix.Balloon(root)
# # bind balloon to buttons
# balloon.bind_widget(btn1, balloonmsg='Click to show Hallo')
# balloon.bind_widget(btn2, balloonmsg='Click to show Bye')
# # layout, stack vertically
# label.pack()
# btn1.pack(pady=8)
# btn2.pack(pady=8)
# root.mainloop()


# #COLUMN C
# gridrow = 0


# thankyoulabel = Message(mainwindow, text = thankyoutext, font=(labelfont, 9, 'bold'))
# thankyoulabel.grid(column = COLC, row = gridrow, rowspan = 4,padx=(0,0),sticky="n")
# thankyoulabel.configure(background=backgroundcolor)
# gridrow += 4


# discordbutton = Button(mainwindow,text = "Developer Discord", command=openhelp, height=6, width=30)
# discordbutton.grid(column= COLC,row=gridrow, sticky="n")
# discordbutton.configure(background = "silver")
# gridrow += 1


# gbatempbutton = Button(mainwindow,text = "GBAtemp thread", command=OPENGBATEMP, height=1, width=30)
# gbatempbutton.grid(column= COLC,row=gridrow)
# gbatempbutton.configure(background = "silver")
# gridrow += 1

spewToTextOutput("Select your SD path to begin.")
mainwindow.mainloop()

