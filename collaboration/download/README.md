
# Collaboration through TeraLab Marketplace: download app

## Pre-requisites

* Install Docker and Docker-Compose

## Context

The Resource is "Algorun" and as of now (Nov 2020), the App is available [here]()
We are going to show how can download the resource

## Outcome

* Download a resource

## Instructions

* Go to the [page of the Algorun resource]() 
* Scroll to the bottom of the page then Open the collapsed "Download" section
* Click on the "Donwload" button and wait for the download to be complete
<!-- * Extract the zip file, you should have an executable named setup.sh, run it 
* setup.sh will clone a git repository named "algorun", move inside and start the compose file "docker-compose.yaml" file -->
* Extract the zip file, you should have a folder (let's call it the docker context) inside of which there is a "docker-compose.yaml" file
* Move inside the docker context folder and run <pre>docker-compose up</pre>
* In your browser access localhost:3000

Now you can see the familiar web interface used when testing you Algorun in workshop mode. The only difference is that you no longer need an SFTP interface to access the generated data, you can directly see it inside the data folder of the docker context folder.

The following video illustrates the process

[VIDEO]



