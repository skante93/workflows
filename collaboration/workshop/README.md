
# Collaboration through TeraLab Marketplace: testing app

## Context

The App is "Algorun" and as of now (Nov 2020), the App is available [here]() and one its instances is running [here]().

We are going to cover how you can use it in workshop mode with a video showing the whole process. 

## Outcome

* Test the Algorun in Workshop mode

## Instructions

* Go to the [page of the instance of Algorun](https://ws67-af-portal.tl.teralab-datascience.fr/workshop/items/5fb633ea4f5aa7013ddae944) or create your own instance of Algorun then visit its page (an instance is available [here](https://ws67-af-portal.tl.teralab-datascience.fr/workshop/items/5fbd1a6d4f5aa7013ddae94a))
* Locate the "Request" section and upload the example-kmeans.py script 
* Click on submit and wait for the execution to end. You should have the following output:
<pre>
Training KMeans classifier with : n_clusters of 2, random_state of 0.000000 on IRIS database
Model recorded at : /data/models/model.pickle
Plots recorded at : /data/plots
</pre>
* Now you can log in via the Marketplace Storage SFTP interface (you should visit the page of the Marketplace Storage to see the command in particular the Port number and the user@host informations), and download the model 

You should now have a <code>kmeans-model.pickle</code> which is the kmeans model dumped in pickle format. You can load this model now in your own environment using the pickle library on python and use it make further predictions / classifications.

[App Instance creation](https://www.youtube.com/watch?v=8fi63e6hXL8)

[App instance Demo](https://www.youtube.com/watch?v=bD5q_OMLkEs)



