#homebrewexplorer.py

#file handling and fusee launching
import os, sys, subprocess
import shutil

#GUI imports (weird import format)
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter.font as tkFont

import webbrowser
#My modules
import webhandler 
from format import *

import urllib.request 
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)

def get_path(filename):
	return os.path.join(sys.path[0], filename)

def exists(filename):
	return os.path.isfile(filename)

downloadsfolder = get_path("downloads\\")
notfoundimage = get_path("notfound.png")
softwarechunknumber = 0 #variable to track where we are in the list of homebrew

def downloadFile(downloadas, filetodownload): #For downloading software art
	downloadlocation = get_path(os.path.join(downloadsfolder+downloadas))
	print("Downloading file {} from url {}".format(downloadas,filetodownload))
	# try: 
	urllib.request.urlretrieve(filetodownload, downloadlocation)

def openurl():
	webbrowser.open_new(projectpageurl)
def openurl():
	webbrowser.open_new(projectpageurl)

def pageup():
	global softwarechunknumber
	if softwarechunknumber < dictlen-1:
		softwarechunknumber += 1
		updatePage(softwarechunknumber)

def jumptopage(option):
	global softwarechunknumber
	softwarenumber = 0
	for softwarechunk in currentdict:
		if softwarechunk["software"] == option:
			softwarechunknumber = softwarenumber
		softwarenumber+= 1
	updatePage(softwarechunknumber)

def pagedown():
	global softwarechunknumber	
	if softwarechunknumber > 0:
		softwarechunknumber -= 1
		updatePage(softwarechunknumber)

#Make the globals needed for the browser
def startBrowserInternal(dicty, segment, window,columnstart):

	global browserwindow
	browserwindow = window

	global softwarechunknumber
	softwarechunknumber = 0 #variable to track where we are in the list of homebrew
	softwarechunknumber = segment

	global softwareauthorvar
	softwareauthorvar = StringVar()
	softwareauthorvar.set("author")

	global softwarenamelabelvar
	softwarenamelabelvar = StringVar()
	softwarenamelabelvar.set("software")

	global softwaredescription
	softwaredescription = Text(window, height=15, width = 25, wrap=WORD, font=softwaredescriptionfont)
	
	global projectpageurl
	projectpageurl = ""

	global popupchoices
	popupchoices = []

	global popupvar
	popupvar = StringVar(window)
	
	global currentdict
	currentdict = dicty

	global dictlen
	dictlen = len(dicty)

	global columnnum
	columnnum = columnstart

	build_browser(softwarechunknumber)

#Build base layout
def build_browser(softwarechunknumber):
	global softwareauthorvar
	global softwarenamelabelvar
	global browserwindow
	global softwaredescription
	global projectpageurl
	global popupvar
	global currentdict

	global invisiblespace
	invisiblespace = tkinter.Label(browserwindow,)
	invisiblespace.grid(row=0, column=columnnum)
	invisiblespace.configure(background=backgroundcolor)

	global invisiblespace2
	invisiblespace2 = tkinter.Label(browserwindow,)
	invisiblespace2.grid(row=0, column=columnnum+1)
	invisiblespace2.configure(background=backgroundcolor)

	global project_image_label
	project_image_label = tkinter.Label(browserwindow,)
	project_image_label.configure(background=backgroundcolor)
	project_image_label.grid(column=columnnum+2, columnspan=3, row=0,rowspan= 3,sticky="NSW")
	gridrow = 3

	global softwaredescription
	softwaredescription.grid(column=columnnum+2, columnspan =3,row=gridrow,rowspan=4,sticky="N")
	softwaredescription.configure(background=selectionboxcolor)
	softwaredescription.configure(foreground=bigbuttontextcolor)
	gridrow+=4

	for softwarechunk in currentdict:
		popupchoices.append(softwarechunk["software"])
	popupvar.set(popupchoices[softwarechunknumber])

	global softwarepopup
	softwarepopup = OptionMenu(browserwindow, popupvar, *popupchoices, command = jumptopage,)
	softwarepopup.grid(column=columnnum+2, columnspan=3, row=gridrow, rowspan=1,sticky="NSEW")
	softwarepopup.configure(background=selectionboxcolor)
	softwarepopup.configure(highlightthicknes=0)
	softwarepopup.configure(width="15")
	softwarepopup.configure(anchor="w")
	softwarepopup.configure(pady=4)
	softwarepopup.configure(font=largeboldtext)
	softwarepopup.configure(foreground=bigbuttontextcolor)
	gridrow+=1

	global softwareauthor
	softwareauthor = tkinter.Label(browserwindow, textvar = softwareauthorvar, font=boldtext)
	softwareauthor.configure(background=backgroundcolor)
	softwareauthor.configure(foreground=bigbuttontextcolor)
	softwareauthor.grid(column=columnnum+2, row=gridrow, columnspan = 3, sticky="NW")
	gridrow+=2

	global projectURLbutton
	projectURLbutton = tkinter.Button(browserwindow, text="Project Page", height=1,command=openurl)
	projectURLbutton.grid(column=columnnum+2, columnspan=3, row=gridrow, rowspan=2,sticky="SEW")
	projectURLbutton.configure(background=selectionboxcolor)
	projectURLbutton.configure(font=boldtext)
	projectURLbutton.configure(foreground=bigbuttontextcolor)

	gridrow+=2

	global backbutton
	backbutton = tkinter.Button(browserwindow, text="<- Back",width=9, command=pagedown,)
	backbutton.grid(column=columnnum+2, columnspan=1, row=gridrow, rowspan=1,sticky="NEW")
	backbutton.configure(font=boldtext)
	backbutton.configure(background=selectionboxcolor)
	backbutton.configure(foreground=bigbuttontextcolor)

	global nextbutton
	nextbutton = tkinter.Button(browserwindow, text="Next ->",width=9, command=pageup,)
	nextbutton.grid(column=columnnum+4, columnspan=1, row=gridrow, rowspan=1,sticky="NEW")
	nextbutton.configure(font=boldtext)
	nextbutton.configure(background=selectionboxcolor)
	nextbutton.configure(foreground=bigbuttontextcolor)

	updatePage(softwarechunknumber)

#Populate layout
def updatePage(softwarechunknumber):
	global currentdict
	global softwareauthorvar
	global softwarenamelabelvar
	global browserwindow
	global softwaredescription
	global projectpageurl
	global popupchoices
	global popupvar
	global project_image_label

	softwarechunk = currentdict[softwarechunknumber]
	softwarename = softwarechunk["software"]
	projectpageurl = softwarechunk["projectpage"]
	photopath = get_path(os.path.join(downloadsfolder,(softwarename + ".png")))
	print(photopath)
	photoexists = exists(photopath)
	print("photoexists is {}".format(photoexists))
	
	project_image_label.destroy()

	if not photoexists:
		photourl = softwarechunk["image"]
		try:
			downloadFile(softwarename + ".png",photourl)
		except: 
			print("could not download icon image")
			photopath = get_path(notfoundimage)

	try:

		project_image = tkinter.PhotoImage(file=photopath,)
		project_image_label = tkinter.Label(browserwindow,width=200,height=120)

	except:
		photopath = get_path(notfoundimage)
		project_image = tkinter.PhotoImage(file=photopath,)
		project_image_label = tkinter.Label(browserwindow,width=200,height=120)

		print("used not-found image due to error")

	if project_image.width() > 400:
		project_image = project_image.subsample(3,3)

	elif project_image.width() > 300:
		project_image = project_image.subsample(2,2)

	elif project_image.width() < 100:
		project_image = project_image.zoom(2)

	project_image_label.configure(image=project_image)
	project_image_label.configure(background=backgroundcolor)
	project_image_label.image = project_image
	project_image_label.grid(column=columnnum+2, columnspan=3, row=0,rowspan= 3,sticky="NESW")

	softwarenamelabelvar.set(softwarename)
	popupvar.set(popupchoices[softwarechunknumber])

	softwareauthorvar.set("                ") #hacky cleaner
	softwareauthorvar.set("by {}".format(softwarechunk["author"]))
	
	softwaredescription.config(state=NORMAL)
	softwaredescription.delete('1.0', END)
	softwaredescription.insert(END, softwarechunk["description"])
	softwaredescription.config(state=DISABLED)

def destroyBrowserInternal():
	global project_image_label
	project_image_label.destroy()
	global softwaredescription
	softwaredescription.destroy()
	global softwarepopup
	softwarepopup.destroy()
	global softwareauthor
	softwareauthor.destroy()
	global projectURLbutton
	projectURLbutton.destroy()
	global backbutton
	backbutton.destroy()
	global nextbutton
	nextbutton.destroy()
	global invisiblespace
	invisiblespace.destroy()
	global invisiblespace2
	invisiblespace2.destroy()
