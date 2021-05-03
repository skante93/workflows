
# Collaboration through TeraLab Marketplace: download and run the project

## Pre-requisites

* Install Docker and Docker-Compose

## Instructions

### Variables

### Manual

* Go to the [page of the Algorun resource](https://ws67-af-portal.tl.teralab-datascience.fr/store/items/5fbd1c254f5aa7013ddae94b) 
* Scroll to the bottom of the page then Open the collapsed "Download" section
* Click on the "Donwload" button and wait for the download to be complete
<!-- * Extract the zip file, you should have an executable named setup.sh, run it 
* setup.sh will clone a git repository named "algorun", move inside and start the compose file "docker-compose.yaml" file -->
* Extract the zip file, you should have a folder inside of which there is a "algorun-compose.yaml" file
* Move inside the folder and run :
```bash
$ docker-compose -f algorun-compose.yaml up
```
* In your browser access <code>http://localhost:3000</code>
* The project is represented by a simple script: [example-kmeans.py](./example-kmeans.py). Upload it through the Algorun interface and run it.
* You can see stdout and stderr, thus you can see if there is an error and what kind
* If eveything went without a mishap, you should see a <code>pickle</code> file in <code>data/models/kmeans-model.pickle</code> 

The following video illustrates the whole process :
* [Downloading App](https://www.youtube.com/watch?v=AIMqpV4kgYw)


## Outcome

* Download resources A1 and D1
* Run the project