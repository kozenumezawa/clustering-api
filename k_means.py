def clustering(allTimeSeries, nClusters):
    import numpy as np
    from sklearn.cluster import KMeans

    allTimeSeries = np.array(allTimeSeries)

    kmeans_model = KMeans(n_clusters=nClusters, random_state=10).fit(allTimeSeries)
    kmeansLabels = kmeans_model.labels_

    responseMsg = {
        "labels": kmeansLabels.tolist()
    }
    return responseMsg
