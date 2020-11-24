
# Collaboration through TeraLab Marketplace: setup

## Pre-requisites

* Familiarity with TeraLab Marketplace, read the workflow [Getting Started with TeraLab Marketplace]()

## Context

This workflow component describes more explicitly how the details of the workflow.

Here is sequence :
* Team B creates an App (A1)
* Team B published the App on TeraLab Marketplace as a workshop item (in SAS mode, i.e. running the app container on Teralab) as well as a resource (downloadable and deployable in any environment). _A note explaining the difference between a workshop item and a resource is specified below._
* Team A first tests the App in workshop mode and is satified
* Then team A downloads the App from resource catalog in order to deploy it in a constrained environment (i.e because of legal of technical bindings let us say it is better to have the app brought to Team A's secure environment rather than sending sesitive data outside of the secure / allowed perimeter) 
* Once deployed, Team A runs the App on their own data (D1), which in turn produces new data (D2) 

_**Note**: a workshop item is a container based deployment orchestrated on TeraLab Merketplace to render a given service, whereas a resource is a shareable data of any given type (notebook, dataset (such as .csv .sql ...), dockerfile / docker-compose file ... ) other Marketplace users can download and exploit in their own environment. This is relevant in the current context, since using the former (workshop item) means possibly sending data to the TeraLab Marketplace to be processed while the later means downloading the processing and apply it in the workflow user's own [secure] environment where he can exrcise control over the constraints (i.e. prevent any possibility to of data leakage). Clearly, the workshop item is more "demonstrative" whereas the resource is more "operative"._

### App, Script & Data

_**/!\Note**: several notes are provided for those who are unfamiliar with TeraLab marketplace_

The App (container) team B creates aims to provide a scikit learn-ready evironment to all users.

The app is called "algorun" (app available [here](https://ws67-af-portal.tl.teralab-datascience.fr/workshop/items/5fb633ea4f5aa7013ddae944), an instance is running [here](https://ws67-af-portal.tl.teralab-datascience.fr/workshop/items/5fbd1a6d4f5aa7013ddae94a)), is essentially a [scikit learn]() environment with some basic [pip]() modules installed. It takes in a **python script**, runs it, and informs via websocket whenever new logging data (stdout and stderr) ara available. 

Since the main goal is still to describe a case of collaboration between teams, to keep things simple, we decided to that the script provided by Team A will exhibit a "KMeans" training on "IRIS" datasets and produce a model.
This means that A1 is represented by "Algorun", D1 (c.f [Context](#context)) is represented by the IRIS dataset, and D2 is represented by the KMeans model obtained.

Futhermore, since the Algorun App is a bit free-style (just provides an evironment for you to run your scripts in), it also provide the opportunity to specify a workshop storage at path <code>/data</code> in case users want to bring out the results of their scripts.

The script that will be used by Team A is in [example-kmeans.py](./example-kmeans.py), and as you can see, the sucessfull execution of it will save the model at <code>/data/models/kmeans-model.pickle</code> and plots at <code>/data/models/kmeans-model.pickle</code>. Everything is saved in <code>/data</code> because, as stated previously the App give the possibility to mount a storage there. As a result we created an instance of Algorun while specifying a Marketplace volume at /data, which then, bu nature (Merketplace Volumes are designed that way) exposed an SFTP interface by which we can explore the Volume.

_**Note 1**: As of today (November 2020), Workshop items can be of two main types (the second can further be divided in two kinds as discussed in note 2 below): a marketplace storage or an App. A marketplace storage is a shareable volume created by and for a user allowing him to persist data when deploying Apps. It also have an SFTP interface allowing the user to either upload or donload data into or from it. As for an App, it is, for the sake of simplicity for now, a docker deployment orchestrated on TeraLab Marketplace. Further info on that in the following note._

_**Note 2** : an App is a template referencing a docker image to be deployed. The templating allows a contributor (when a user creates a resource or a workshop item, he is called the contributor in regards to the created resource/workshop item) to specify a context defined by : the ports to expose, the volume mountpoints if any, and settings (envrinment variables) if any. An App Instance on the hand, is a deployment based on the template described by the App. It allows other users to provide a context to an App template (i.e. provide a custom volume (such as a Marketplace Storage) for each mountpoint, or provide a value for each setting)_


## Outcome

* Understanding the setup and steps of the workflow to come in particular the deployment of the Algorun App and its instance

## Instructions

The following video explains how a storage is created

[VIDEO]

The next workflow components contain videos showcasing the creation of a workflow item and that of a resource. 
