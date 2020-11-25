
# Collaboration through TeraLab Marketplace: download app

## Pre-requisites

* Install Docker and Docker-Compose

## Context

The Resource is "Algorun" and as of now (Nov 2020), the resource is available [here](https://ws67-af-portal.tl.teralab-datascience.fr/store/items/5fbd1c254f5aa7013ddae94b)
We are going to show how can download the resource

## Outcome

* Download a resource

## Instructions

* Go to the [page of the Algorun resource](https://ws67-af-portal.tl.teralab-datascience.fr/store/items/5fbd1c254f5aa7013ddae94b) 
* Scroll to the bottom of the page then Open the collapsed "Download" section
* Click on the "Donwload" button and wait for the download to be complete
<!-- * Extract the zip file, you should have an executable named setup.sh, run it 
* setup.sh will clone a git repository named "algorun", move inside and start the compose file "docker-compose.yaml" file -->
* Extract the zip file, you should have a folder (let's call it the docker context) inside of which there is a "algorun-compose.yaml" file
* Move inside the docker context folder and run <code>docker-compose -f algorun-compose.yaml up</code>
* In your browser access <code>http://localhost:3000</code>

Now you can see the familiar web interface used when testing you Algorun in workshop mode. The only differences are :
* the algorun App is no longer ran remotely but locally
* you no longer have an SFTP interface to access the generated data, but you can directly access them from inside the data folder of the docker context folder.

The following video illustrates the process :

[Downloading App](https://www.youtube.com/watch?v=AIMqpV4kgYw)



