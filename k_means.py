def clustering(all_time_series, n_clusters):
    import numpy as np
    from sklearn.cluster import KMeans

    all_time_series = np.array(all_time_series)

    kmeans_model = KMeans(n_clusters=n_clusters, random_state=10).fit(all_time_series)
    kmeans_labels = kmeans_model.labels_

    # calculate each average

    responseMsg = {
        "labels": kmeans_labels.tolist()
    }
    return responseMsg
