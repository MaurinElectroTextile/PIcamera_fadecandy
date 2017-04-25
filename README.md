
# PIcamera_fadecandy
 - Stream video to multiple screens made out of LED streeps
 - Credit: Maurin Donneaud maurin@datapaulette.org

### Hardware
 - [Raspbeary-PI 3](https://www.raspberrypi.org)
 - [Fadecandy](https://github.com/scanlime/fadecandy)

### Clone this repository
 - git clone git@github.com:MaurinElectroTextile/PIcamera_fadecandy.git
 - git submodule init
 - git submodule update

### Compiling/installing fadecandy serveur
 - cd fadecandy/server
 - make submodules
 - make
 - The compiled binary will be created in the same server directory
 - cd /usr/local/bin/
 - sudo ln -s /home/pi/PIcamera_fadecandy/fadecandy/server/fcserver ./fcserver
 - sudo ln -s /home/pi/PIcamera_fadecandy/fcserver.json ./fcserver.json

### Fadecandy IDs :
 - Channel 0  TZXTQOUKWKVZDDUN
 - Channel 1  UEICYSNDBXIHAJEV
 - Channel 2  TXTXWEYKYITTRRYF
 - Channel 3  TNFLPPXLBXELMHMT

~~~~
	-------------------------
	|           |           |
	| Channel 0 | Channel 1 |
	|           |           |
	|           |           |
	-------------------------
	|           |           |
	| Channel 2 | Channel 3 |
	|           |           |
	|           |           |
	-------------------------
~~~~

### TODO :
 - BugFix : https://groups.google.com/forum/#!topic/fadecandy/-xz-Ij6x0Wo
