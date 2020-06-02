# ProjectMan
ProjectMan is a simple project manager for easily managing and CD'ing to your
projects.

## Install

### On (superior) UNIX based operating systems
```
git clone https://github.com/Xenthio/ProjectMan.git
cd ./ProjectMan-master
./installproject.sh
```

### On Windows 7/8/10
###### (I feel bad for you)

**NOTE: First install [git!](https://gitforwindows.org/)**
```
git clone https://github.com/Xenthio/ProjectMan.git
cd ./ProjectMan-master
./installproject.bat
```

## Usage
```
project [-cdDghv] [project]

Usage:
  project [-g|--goto] <project>
  project -l | --list
  project -h | --help
  project -v | --version

Options:
  -h --help         Show this screen.
  -v --version      Show version.
  -g --goto         Default: Goto project folder.
  -c --create       Create project file.
  -d --delete       Delete project file.
  -D --deleteAll    Delete entire project folder.
  -l --list         List all projects.
  ```
