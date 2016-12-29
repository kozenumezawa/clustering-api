# clustering-api
POSTによって渡された二次元配列のクラスタリングを行うAPI。  
クラスタリングした結果をJSON形式で返す。

# URI
## K-meansを行うapi
### POST: /api/v1/kmeans
labelsはクラスタリングした結果が一次元配列で格納される
averageはクラスタリング後の各クラスタの時系列データの平均値が格納される

- request
```  
  {  
    n_clusters : 1以上の整数  
    data : [[], [], ..., []] （二次元配列）  
  }
  ```

- response
```
{  
  labels: [ ] (一次元配列)  
  average: [[], [], ..., []] (二次元配列)  
}  
```


### GET: /api/v1/kmeans
POSTした後に、GETパラメータにn_clustersを与えることで、
その分割されたクラスタが返ってくる
- request
```
{
  n_clusters : n
}
```

- response
```
{  
  labels: [ ] (一次元配列)  
  average: [[], [], ..., []] (二次元配列)  
}  
```


# Requirements
- SciPy
- sklearn
- [falcon](https://github.com/falconry/falcon)（Pythonサーバーフレームワーク）
