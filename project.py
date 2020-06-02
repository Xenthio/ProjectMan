#!/usr/bin/env python3
import sys
import json
import os
from pathlib import Path


Error = "\033[1;31mError\033[1;37m: "
Changing = "Changing into \'%s\'..."
NotFound = Error + "\'%s\' not found in projects root.\nCheck if it exists or the config (~/.projectcfg) is setup correctly."
FirstTime = "This is your first time using Project,\nplease specify a directory to use as a project root...\n(e.g. /home/xen/projects/)"
PreferedShell = "Please specify your prefered shell. (e.g. /bin/bash)"
FirstPromptDir = "Directory: "
FirstPromptShell = "Path: "
SetupNotFound = Error + "Cannot open \'%s\', the specified directory is invalid."
ConfigFile = str(Path.home()) + "/.projectcfg"

if os.path.exists(ConfigFile) != True:
	file1 = open(ConfigFile,"w")
	file1.write("{\n")
	file1.write("\"ProjectsRoot\": \"")
	print(FirstTime)
	Prompt = True
	while Prompt == True:
		x = input(FirstPromptDir)
		if os.path.exists(x) != True:
			print(SetupNotFound % x)
		else:
			Prompt = False
	file1.write(x)
	file1.write("\"\n")
	file1.write("}\n")
	file1.close()
	exit()

def help():
	print("help")

def changeDir(arg):
	path = "error"
	if sys.platform == "darwin":
		path = arg.replace(" ", "\\ ")
	elif sys.platform == "linux":
		path = "\"" + arg + "\""
	elif sys.platform == "win32":
		path = "\"" + arg + "\""
	#os.chdir(path)
	os.system('cd ' + path)
	print(path)

with open(ConfigFile, 'r') as config:
    data=config.read()

settings = json.loads(data)
ProjectsRoot = settings['ProjectsRoot']


if len(sys.argv) == 1:
	help() #no command
else:
	Dirs = list(os.walk(ProjectsRoot))
	Dirs.pop(0)
	found = 0
	for x in Dirs:
		#print(x[0] + "/projectfile")
		try:
			with open(x[0] + "/projectfile", 'r') as checkPass:
				data2=checkPass.read()
			projectfile = json.loads(data2)
			if sys.argv[1].upper() in map(str.upper,projectfile['Aliases']):
				print(Changing % projectfile['FolderName'])
				os.chdir(ProjectsRoot + projectfile['FolderName'])
				print(ProjectsRoot + projectfile['FolderName'])
				os.system(os.environ['SHELL'])
				found = 1
		except:
			pass
	if found == 0:
		print(NotFound % sys.argv[1])
