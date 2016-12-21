def clustering(allTimeSeries, nClusters):
    import numpy as np
    from sklearn.cluster import KMeans

    allTimeSeries = np.array(allTimeSeries)

    kmeans_model = KMeans(n_clusters=nClusters, random_state=10).fit(allTimeSeries)
    labels = kmeans_model.labels_

    for label, feature in zip(labels, allTimeSeries):
        print(label, feature, feature.sum())
