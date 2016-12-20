import scipy.spatial.distance

def clustering(allTimeSeries):
    from  scipy.spatial.distance  import pdist
    from scipy.cluster.hierarchy import linkage, dendrogram
    from matplotlib.pyplot import show

    pdist = pdist(([[1,1,1], [2,3,4], [5,3,1]]))
    result = linkage(pdist)
    dendrogram(result)
    show()
    # pDistance = scipy.spatial.distance.pdist(allTimeSeries)
    # for timeSeries in allTimeSeries:
    #
    #     print(timeSeries)
