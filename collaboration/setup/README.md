
# Collaboration through TeraLab Marketplace: setup

## Prre-requisites

* Familiarity with TeraLab Marketplace, read the workflow [Getting Started with TeraLab Marketplace]()

## Context

This workflow component describes more explicitly how the details of the workflow.

Here is sequence :
* Team B creates an App (A1)
* Team B published the App on TeraLab Marketplace as a workshop item (in SAS mode, i.e. running the app container on Teralab) as well as a resource (downloadable and deployable in any environment )
* Team A first tests the App in workshop mode and is satified
* Then team A downloads the App from resource catalog in order to deploy it in a constrained environment (i.e because of legal of technical bindings let us say it is better to have the app brought to Team A's secure environment rather than sending sesitive data outside of the secure / allowed perimeter) 
* Once deployed, Team A runs the app on their own data (D1), which in turn produces new data (D2) 

### App, Script & Data

The app (container) team B creates aims to provide a scikit learn-ready evironment to all users.

The app is called "algorun" (app available [here](), an instance is running [here]()), is essentially a [scikit learn]() environment with some basic [pip]() modules installed. It takes in a **python script**, runs it, and informs via websocket whenever logging data (stdout and stderr) ara available. 

Since the main goal is still to describe a case of collaboration between teams, to keep things simple, we decided to that the script provided by Team A will exhibit a "KMeans" training on "IRIS" datasets and produce a model.
This means that A1 is represented by "Algorun", D1 (c.f [Context]()) is represented by the IRIS dataset, and D2 is represented by the KMeans model obtained.

Futhermore, since the Algorun App is a bit free-style (just provides an evironment for you to run your scripts in), it also provide the opportunity to specify a workshop storage at path <pre>/data</pre> in case users want to bring out the results of their scripts.

The script that will be used by Team A is in [example-kmeans.py](./example-kmeans.py), and as you can see, the sucessfull execution of it will save the model at <pre>/data/models/kmeans-model.pickle</pre> and plots at <pre>/data/models/kmeans-model.pickle</pre>. Everything is saved in <pre>/data</pre> because, as stated previously the App give the possibility to mount a storage there. As a result we created an instance of Algorun while specifying a Marketplace volume at /data, which then, bu nature (Merketplace Volumes are designed that way) exposed an SFTP interface by which we can explore the Volume.

THe following video show how the whole process works.

[VIDEO]

## Outcome

* Understanding the setup and steps of the workflow to come in particular the deployment of the Algorun App and its instance
