
# Collaboration through TeraLab Marketplace: Objectives & Setup

## Pre-requisites

* Familiarity with TeraLab Marketplace, read the workflow [Getting Started with TeraLab Marketplace]()

## Context

### Scenario

This is a workflow component (WFC1) of the [Collaboration through TeraLab Marketplace](../) worfklow.

This workflow component describes more explicitly the objectives of the workflow through a scenario, as well as introduces some fundamental Markeplace concepts required to fully understand the application of the scenario whenever the Marketplace is involved.

Here is sequence :
* Team B creates an App (A1)
* Team B published the App on TeraLab Marketplace as a workshop item (in SAS mode, i.e. running the app container on Teralab) as well as a resource (downloadable and deployable in any environment). _A note explaining the difference between a workshop item and a resource is specified below._
* Team A first tests the App in workshop mode (workshop mode explained later) and is satified
* Then team A downloads the App from resource catalog in order to deploy it in a constrained environment (i.e because of legal of technical bindings. Let us say it is better to have the app brought to Team A's secure environment rather than them sending their sensitive data outside of their secure infrasctructure) 
* Once deployed, Team A runs the App on their own data (D1), which in turn produces new data (D2) 
* Team A publishes the new Data (D2) so other interested users (let's consider D2 as the output of a scientific experiment) can access it.

_**Note**: a workshop item is a container based deployment orchestrated on TeraLab Merketplace to render a given service, whereas a resource is a shareable data of any given type (notebook, dataset (such as .csv .sql ...), dockerfile / docker-compose file ... ) other Marketplace users can download and exploit in their own environment. This is relevant in the current context, since using the former (workshop item) means possibly sending data to the TeraLab Marketplace to be processed while the later means downloading the processing and apply it in the workflow user's own [secure] environment where he can exrcise control over the constraints (i.e. prevent any possibility to of data leakage). Clearly, the workshop item is more "demonstrative" whereas the resource is more "operative"._

### Scenario adaptation (defining A1, the Script & D1)

_**/!\Note**: several notes are provided for those who are unfamiliar with TeraLab marketplace_

#### App: Algorun

The App (container) team B creates aims to provide a scikit learn-ready evironment to all users.

The app is called "algorun" (app available [here](https://ws67-af-portal.tl.teralab-datascience.fr/workshop/items/5fb633ea4f5aa7013ddae944), an instance is running [here](https://ws67-af-portal.tl.teralab-datascience.fr/workshop/items/5fbd1a6d4f5aa7013ddae94a)), is essentially a [scikit learn]() environment with some basic [pip]() modules installed. It takes in a **python script**, runs it, and informs via websocket whenever new logging data (stdout and stderr) ara available. 

Futhermore, since the Algorun App is a bit free-style (just provides an evironment for you to run your python scripts in), it also provide the opportunity to specify a workshop storage at path <code>/data</code> in case users want to bring out the results (IO operations) of their scripts. To put it differently, by giving the opportunity of mount a volume at <code>/data</code>, any script can write output files (trained models, generated data ...) in a subpath of <code>/data</code>, this will record said output files in the mounted volume (i.e a Marketplace Storage) and thus persist them beyond the container own life-cycle. Of course any file recorded in a Marketplace storage can be accessed via an SFTP interface, the command can be found on the page of the Marketplace storage on the portal.

### Data D1: IRIS dataset

Since the main goal is still to describe a case of collaboration between teams, to keep things simple, we decided to that the script provided by Team A will exhibit a "KMeans" training on "IRIS" datasets and produce a model.
This means that A1 is represented by "Algorun", D1 (c.f [Context](#context)) is represented by the IRIS dataset, and D2 is represented by the KMeans model obtained.

### Script 

The script that will be used by Team A is in [example-kmeans.py](./example-kmeans.py), and as you can see, the sucessfull execution of it will save the model at <code>/data/models/kmeans-model.pickle</code> and plots at <code>/data/models/kmeans-model.pickle</code>. Everything is saved in <code>/data</code> because, as stated previously the Algorun App gives the possibility to mount a storage there. As a result we created an instance of Algorun while specifying a Marketplace storage at /data, which then, by nature (Merketplace storages are designed that way) exposed an SFTP interface by which we can explore the Volume.




## Outcome

* Understanding the setup and steps of the workflow to come in particular the deployment of the Algorun App and its instance

## Instructions

The following video explains how a storage is created

<!-- [![Storage creation](https://www.youtube.com/vi/TwB0Ay51R_w/0.jpg)](https://www.youtube.com/watch?v=TwB0Ay51R_w) -->

[Storage creation](https://www.youtube.com/watch?v=TwB0Ay51R_w)

The next workflow components contain videos showcasing the creation of a workflow item and that of a resource. 
