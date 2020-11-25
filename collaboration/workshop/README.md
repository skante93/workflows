
# Collaboration through TeraLab Marketplace: testing app

## Context

The App is "Algorun" and as of now (Nov 2020), the App is available [here]() and one its instances is running [here]().

We are going to cover how you can use it in workshop mode with a video showing the whole process. 

## Outcome

* Test the Algorun in Workshop mode

## Instructions

* Go to the [page of the instance of Algorun](https://ws67-af-portal.tl.teralab-datascience.fr/workshop/items/5fb633ea4f5aa7013ddae944) or create your own instance of Algorun then visit its page (an instance is available [here]())
* Locate the "Request" section and upload the example-kmeans.py script 
* Click on submit and wait for the execution to end. You should have the following output:
<pre>
</pre>
* Now you can log in via the Marketplace Storage SFTP interface (you should visit the page of the Marketplace Storage to see the command in particular the Port number and the user@host informations), and download the model 
<pre>
</pre>

You should now have a <code>kmeans-model.pickle</code> which is the kmeans model dumped in pickle format. You can load this model now in your own environment using the pickle library on python and use it make further predictions / classifications.

[VIDEO]



