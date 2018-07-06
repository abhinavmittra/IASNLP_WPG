'''
Script for Kmeans clustering

Authors: Aditya, Abhinav

'''
import json
import numpy as np
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
from sklearn.externals import joblib


with open("sentencesword2vec", mode='r', encoding='utf-8', errors='ignore') as f:
	x = f.read().splitlines()

qnList = x


vectorizer = TfidfVectorizer(stop_words='english')
vector = vectorizer.fit_transform(qnList)

kmeans3 = KMeans(n_clusters=3, random_state=0).fit(vector)
clusters = 3

#### Print top words in cluster #############

# print("Cluster-wise most frequent terms:")
# num_wor = 15 #Define number of words per cluster
# order_centroids = kmeans3.cluster_centers_.argsort()[:, ::-1]
# terms = vectorizer.get_feature_names()
# for i in range(clusters):
#     print("Cluster %d:" % i),
#     for i in order_centroids[i, :num_wor]:
#         print(' %s' % terms[i]),
#     print("\n")

#############################################

result = zip(vector , kmeans3.labels_)

# sortedR = sorted(result, key=lambda x: x[1])

sentence_class = []

vec1 = vector.todense()
emb = TSNE(n_components=2)
Y = emb.fit_transform(vec1)

#### Kmeans graph visualize #############
# plt.scatter(Y[:,0], Y[:,1],c=kmeans3.labels_.astype(float), cmap = plt.cm.get_cmap('Dark2'))
# plt.show(block=True)
#########################################

