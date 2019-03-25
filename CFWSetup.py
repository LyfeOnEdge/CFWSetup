version = "0.3 (BETA)"
thankyoutext = "A special thanks to all the users on Amiibru, /hbg/, /r/SwitchPirates, and gbatemp for the help, suggestions, good ideas, and support. This app is in its infancy, plans include additional community homebrew, nut.py integration, always-up-to-date downloads and more. If you have questions comments, or suggestions use the links below to join my discord or GBAtemp thread."

guidetext = """Start by setting your micro SD card up, you'll 
need to select your desired firmware, a title installer if 
you wish to install backups (nsps), any additional homebrew 
or emulators you want. If you have selected a title installer 
you should also tic the 'Install Sigpatches' box.

Select your SD card, or a folder to download the files to, and
click "Install" to download the selected software and have it 
automatically placed in the right location.

Next power off your Switch, you can do this either by shutting 
it down with the power menu, or by holding the power button for
at least 12 seconds.

Finally, insert the micro SD card in your Switch, select a 
payload to inject, and push the "Inject using fusee" button. If
this is your first time using the software, the button will say 
'PyUSB not installed, click to install', clicking this button
install the PyUSB module from the official source using PIP.
"""



#tkinter doesn't include everything by default
import tkinter
from tkinter import *
import tkinter.font as tkFont

#file handling and fusee launching
import os, sys, subprocess
import shutil
chosensdpath = None
temp_folder = "temp\\" #hate all you want for the unix-style slashes ;D 
#archive handling 
from zipfile import ZipFile
import tarfile

#remote file grabbing 
import urllib.request 
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)


#URLS, Friendly names, install paths
from locations import *

selectedConfirmation = None

#Link to the SDSetup guide


fusee_path = "fusee-launcher-master"


#COLORSANDFONTS
labelfont = "Helvetica"
backgroundcolor = "darkgrey"




#used to install pyusb for fusee
pyusbinstalled = None
def installPyUSB():
    try:
    	print(subprocess.call([sys.executable, "-m", "pip", "install", "pyusb"]))
    	payloadbuttontext.set("Inject using fusee")
    except:
    	print("Error installing pyUSB, do you have pip installed?")


def checkifpyusbinstalled():
	reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
	installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
	if "pyusb" in installed_packages:
		return True
	return False

def injectpayload():
	if pyusbinstalled:
		payloadtoinject = payloadlistbox.curselection()
		downloadfileas = ""
		fileToDownload = PAYLOADS[payloadtoinject[0]][PAYLOADURL]
		downloadfileas = PAYLOADS[payloadtoinject[0]][PAYLOADFILE]
		downloadPayload(downloadfileas, fileToDownload)

		spewToInjectorOutput("Injecting payload {}".format(PAYLOADS[payloadtoinject[0]][PAYLOADNAME]))

		fusee_file = os.path.join(fusee_path, "fusee-launcher.py")
		script_path = get_path(fusee_file)
		payload_path = get_path(temp_folder+ downloadfileas)
		p = subprocess.Popen([sys.executable, '-u', script_path, payload_path],
		          stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1)
		with p.stdout:
		    for line in iter(p.stdout.readline, b''):
		        spewBytesToInjectorOutput(line)
		p.wait()
	else:
		installPyUSB()

		appsToInstall = hblistbox.curselection()
		for selectedApps in appsToInstall:
			fileToDownload = HOMEBREW[selectedApps][DOWNLOAD]
			downloadFile(fileToDownload, HOMEBREW[selectedApps][URLTOGET])
			spewToTextOutput("Copying {} to sd card".format(fileToDownload))
			installfiletosd(fileToDownload,HOMEBREW[selectedApps][INSTALLPATH])


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

def spewToInjectorOutput(textToSpew):
	injectoroutput.config(state=NORMAL)
	injectoroutput.insert(END, textToSpew+ "\n\n")
	injectoroutput.config(state=DISABLED)
	injectoroutput.see(END)
	print(textToSpew)

def spewBytesToInjectorOutput(textToSpew):
	injectoroutput.config(state=NORMAL)
	injectoroutput.insert(END, (textToSpew.decode("utf-8") + "\n\n"))
	injectoroutput.config(state=DISABLED)
	injectoroutput.see(END)
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

def downloadPayload(downloadas, filetodownload):
	downloadlocation = get_path(temp_folder+downloadas)
	spewToInjectorOutput("Downloading file {} from url {}".format(downloadas,filetodownload))
	try: 
		urllib.request.urlretrieve(filetodownload, downloadlocation)
	
	except:
		spewToInjectorOutput("Failed to download file {}".format(downloadas))
		return False
	return 


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

mainwindow.configure(background=backgroundcolor)

verticalseparatorimage = get_path("hseparator.png")
verticalseparatorimagepath = PhotoImage(file = verticalseparatorimage)

separatorimage = get_path("separator.png")
separatorimagepath = PhotoImage(file = separatorimage)





#COLUMN A
cfwlabel = Label(mainwindow, height = 1, text = "Select Firmware Flavor:", font=(labelfont, 14, 'bold'))
cfwlabel.grid(column = COLA, row = gridrow, sticky = "w")
cfwlabel.configure(background=backgroundcolor)
gridrow += 1

cfwversion = StringVar()
cfwversion.set(CFWFLAVORS[0][FLAVOR])
for flavortext, filename, fileurl in CFWFLAVORS:
    b = Radiobutton(mainwindow, text=flavortext, variable=cfwversion, value=flavortext)
    b.grid(column=COLA, row=gridrow, sticky = "w")
    b.configure(background=backgroundcolor)
    gridrow += 1

titleinstallerlabel = Label(mainwindow, height = 1, text = "Select Title Installer", font=(labelfont, 14, 'bold'))
titleinstallerlabel.grid(column = COLA, row=gridrow,sticky = "w")
titleinstallerlabel.configure(background=backgroundcolor)
gridrow += 1


nspinstallerversion = StringVar()
nspinstallerversion.set(NSPINSTALLERS[0][FLAVOR])
for flavortext, filename, fileurl, subfolder in NSPINSTALLERS:
    b = Radiobutton(mainwindow, text=flavortext, variable=nspinstallerversion, value=flavortext)
    b.grid(column=COLA, row=gridrow, sticky = "w")
    b.configure(background=backgroundcolor)
    gridrow += 1

sigpatchlabel = Label(mainwindow, height = 1, text = "Other:", font=(labelfont, 14, 'bold'))
sigpatchlabel.grid(column = COLA, row=gridrow, sticky = "w")
sigpatchlabel.configure(background=backgroundcolor)
gridrow += 1

patchvar = IntVar()
patchbutton = Checkbutton(mainwindow, text="Install sigpatches? (recommended)", variable=patchvar)
patchbutton.grid(column = COLA, row=gridrow, sticky="w")
patchbutton.configure(background=backgroundcolor)
gridrow += 1

keepfiles = IntVar()
keepfilesbutton = Checkbutton(mainwindow, text="Keep files after installation? '/temp'", variable=keepfiles)
keepfilesbutton.grid(column = COLA, row=gridrow, sticky="w")
keepfilesbutton.configure(background=backgroundcolor)
gridrow += 1

# separatorimageline = Label(mainwindow, image = separatorimagepath,width=300)
# separatorimageline.grid(column = COLA, row = gridrow)
# gridrow += 1

pathvalue = StringVar()
pathvalue.set("Please select your sd card")
pathtext = Label(mainwindow, height=1, width = 40, textvariable=pathvalue)
pathtext.grid(column= COLA, row=gridrow)
pathtext.configure(background=backgroundcolor)
gridrow += 1

setpathbutton = Button(mainwindow,text="Select SD root", command=setSDpath, height = 1, width = 40)
setpathbutton.grid(column= COLA, row=gridrow)
setpathbutton.configure(background = "silver")
gridrow += 1

# separatorimageline2 = Label(mainwindow, image = separatorimagepath,width=300)
# separatorimageline2.grid(column= COLA, row = gridrow)
# gridrow += 1


if gridrow > MAXCOL:
	MAXCOL = gridrow

#COLUMN B
gridrow = 0

homebrewlabel = Label(mainwindow, height = 1, text = "Additional homebrew", font=(labelfont, 14, 'bold'))
homebrewlabel.grid(column = COLB, row = gridrow, padx=(10, 10))
homebrewlabel.configure(background=backgroundcolor)
gridrow += 1


hblistbox = Listbox(mainwindow,selectmode = MULTIPLE,exportselection=0)
hblistbox.grid(column = COLB, row = gridrow, rowspan = 6, sticky="nsew")
hblistbox.configure(background=backgroundcolor)
for flavortext, filename, fileurl, subfolder in HOMEBREW:
   	hblistbox.insert(END, flavortext)
gridrow += 6

# separatorimageline3 = Label(mainwindow, image = separatorimagepath,width=230)
# separatorimageline3.grid(column = COLB, row = gridrow,)
# gridrow += 1

emulabel = Label(mainwindow, height = 1, text = "Emulators", font=(labelfont, 14, 'bold'))
emulabel.grid(column = COLB, row = gridrow, padx=(10, 10))
emulabel.configure(background=backgroundcolor)
gridrow += 1


emulistbox = Listbox(mainwindow,selectmode = MULTIPLE,exportselection=0)
emulistbox.grid(column = COLB, row = gridrow, rowspan = 4, sticky="nsew")
emulistbox.configure(background=backgroundcolor)
for flavortext, filename, fileurl, subfolder in EMULATORS:
   	emulistbox.insert(END, flavortext)
gridrow += 4

textoutput = Text(mainwindow, height=10, width = 50, font=(labelfont, 8))
textoutput.grid(column= COLB, row=gridrow,rowspan = 4)
textoutput.configure({"background": "black"},)
textoutput.configure({"foreground": "white"},)
textoutput.configure(state=DISABLED)
gridrow += 3

#installbuttonimagepath = get_path("installbutton.png")
#installbuttonimage = PhotoImage(file = installbuttonimagepath)
installbutton = Button(mainwindow,text = "Install", command=installprocess, height=1, width=40)
installbutton.grid(column= COLB,row=gridrow)
installbutton.configure(background = "silver")
gridrow += 1
# separatorimageline4 = Label(mainwindow, image = separatorimagepath,width=230)
# separatorimageline4.grid(column = COLB, row = gridrow,)
# # gridrow += 1



# postinstallbuttonimagepath = get_path("postinstallbutton.png")
# postinstallbuttonimage = PhotoImage(file = postinstallbuttonimagepath)
# postinstallbutton = Button(mainwindow,image=postinstallbuttonimage, command=openhelp, height=30, width=290)
# postinstallbutton = Button(mainwindow,text="Click here for next steps after injecting your payload", command=openhelp, height=7, width=30)
# postinstallbutton.grid(column=COLB,row=gridrow,rowspan = 3)
# postinstallbutton.configure(background = "silver")
# gridrow += 3


#COLUMN C
gridrow = 0

payloadlabel = Label(mainwindow, height = 1, text = "Payload Injector", font=(labelfont, 14, 'bold'))
payloadlabel.grid(column = COLC, row = gridrow)
payloadlabel.configure(background=backgroundcolor)
gridrow += 1

payloadlistbox = Listbox(mainwindow,exportselection=0)
payloadlistbox.grid(column = COLC, row = gridrow, rowspan = 3, sticky="new")
payloadlistbox.configure(background=backgroundcolor)
for flavortext, filename, fileurl, in PAYLOADS:
   	payloadlistbox.insert(END, flavortext)
gridrow += 3

injectoroutput = Text(mainwindow, height=11, width = 40, font=(labelfont, 8))
injectoroutput.grid(column= COLC, row=gridrow,rowspan = 4,sticky="s")
injectoroutput.configure({"background": "black"},)
injectoroutput.configure({"foreground": "white"},)
injectoroutput.configure(state=DISABLED)
gridrow += 4

payloadbuttontext = StringVar()
payloadbuttontext.set("Inject using fusee")
payloadbutton = Button(mainwindow,textvariable=payloadbuttontext, command=injectpayload, height = 1, width = 30)
payloadbutton.grid(column= COLC, row=gridrow)
payloadbutton.configure(background = "silver")
gridrow += 1

separatorimageline4 = Label(mainwindow, image = separatorimagepath,width=230)
separatorimageline4.grid(column = COLC, row = gridrow,pady=(0,0),padx=(0,0))
separatorimageline4.configure(background = backgroundcolor)
gridrow += 1

thankyoulabel = Message(mainwindow, text = thankyoutext, font=(labelfont, 9, 'bold'))
thankyoulabel.grid(column = COLC, row = gridrow, rowspan = 4,padx=(0,0),sticky="n")
thankyoulabel.configure(background=backgroundcolor)
gridrow += 4


discordbutton = Button(mainwindow,text = "Developer Discord", command=openhelp, height=6, width=30)
discordbutton.grid(column= COLC,row=gridrow, sticky="n")
discordbutton.configure(background = "silver")
gridrow += 1


gbatempbutton = Button(mainwindow,text = "GBAtemp thread", command=OPENGBATEMP, height=1, width=30)
gbatempbutton.grid(column= COLC,row=gridrow)
gbatempbutton.configure(background = "silver")
gridrow += 1


# #VERTICAL SEPARATORS
# #AB SEPARATOR
# verticalseparatorA = Label(mainwindow, image = verticalseparatorimagepath,width=3, height = windowheight)
# verticalseparatorA.grid(row = 0,column = 0, sticky = "w", rowspan = MAXCOL)
# #BC Separator
# verticalseparatorAB = Label(mainwindow, image = verticalseparatorimagepath,width=3, height = 280)
# verticalseparatorAB.grid(row = 14,column = 1, sticky = "w", rowspan = MAXCOL, padx=(0,0))
# verticalseparatorAB.configure(background=backgroundcolor)

verticalseparatorBC = Label(mainwindow, image = verticalseparatorimagepath,width=3, height = windowheight)
verticalseparatorBC.grid(row = 0,column = 3, sticky = "nesw", rowspan = MAXCOL, padx=(0,0), pady=(0,0))
verticalseparatorBC.configure(background=backgroundcolor)
# #CD Separator
# verticalseparatorCD = Label(mainwindow, image = verticalseparatorimagepath,width=3, height = windowheight)
# verticalseparatorCD.grid(row = 0,column = 5, sticky = "w", rowspan = MAXCOL)








#main code
if not checkifpyusbinstalled():
	payloadbuttontext.set("PyUSB not installed, click to install")
	pyusbinstalled = False
	print("pyUSB installed")
else:
	pyusbinstalled = True

    


spewToTextOutput("Select your SD path to begin.")
mainwindow.mainloop()

