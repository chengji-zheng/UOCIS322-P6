# UOCIS322 - Project 6 #
Brevet time calculator with AJAX, MongoDB, and a RESTful API!

### Aurthor: Chengji Zheng      ### E-mail: chengjiz@uoregon.edu

#####   1. In this project, we will need to add code in api folder and website folder.

#####   2. In `api.py`, we will need to write code to handle parameters in different routes. Such like list data with filters `listAll`, `listOpenOnly` and `listCloseOnly`. 

#####   3. We will also write code to do more than that, like to specify whether display them in CSV or JSON.

#####   4. Will also let the user to specify how many lines of data to display by using top=k.

### Progress(es) with my second commit (May 31, 2021):
##### 1. Fixed configuration files (ie. `dockerfiles`, `docker-configure.yml`)
##### 2. Added database drop methods to `flask_brevets.py` to drop the db before each running(adding).
##### 3. Added website services (ie. `website.py` and `website.html`) under `website` folder

## Known Issue(s):
###### 1. There are two errors under `line 103` and `line 106` of `api.py` which needs to be fixed;
###### 2. Have not tested the web services under `website` folder
###### 3. Might have other issue(s)


## Credits

Michal Young, Ram Durairajan, Steven Walton, Joe Istas.
