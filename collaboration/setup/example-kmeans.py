#!/usr/bin/env python3

from sklearn import cluster, datasets
import matplotlib.pyplot as plt
import pickle
import os


DATASET_MOUNTPOINT = '/data'
MODEL_DIR = DATASET_MOUNTPOINT+'/models'
PLOTS_DIR = DATASET_MOUNTPOINT+'/plots'

os.makedirs(MODEL_DIR, exist_ok=True)
os.makedirs(PLOTS_DIR, exist_ok=True)

n_clusters = 2
random_state = 0
data = datasets.load_iris()

model = cluster.KMeans(n_clusters=n_clusters, random_state=random_state)
print("Training KMeans classifier with : n_clusters of %d, random_state of %f on IRIS database" % (n_clusters, random_state))
model.fit(data.data)

pickle.dump(model, open(MODEL_DIR+'/kmeans-model.pickle', 'wb'))
print('Model recorded at : %s' % (MODEL_DIR+'/model.pickle'))

centers = model.cluster_centers_.tolist()
labels = model.labels_.tolist()

for i in range(4):
    for j in range(i, 4):
        x = data.data[:, i]
        y = data.data[:, j]
        
        # Plotting Data
        plt.scatter(x, y, c=model.labels_, s=50, cmap="viridis")
        
        # Adding centroids
        plt.scatter(model.cluster_centers_[:, i], model.cluster_centers_[:, j], c='black', s=200, alpha=0.5)

        # Saving figure
        plt.savefig( PLOTS_DIR +'/plot_%dx%d.png'% (i,j))
        plt.close()

print('Plots recorded at : %s' % PLOTS_DIR)
