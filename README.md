# clustering-api
POSTによって渡された二次元配列のクラスタリングを行うAPI。  
クラスタリングした結果をJSON形式で返す。

# URI
## K-meansを行うapi
POST: /api/v1/kmeans
- request
```  
  {  
    n_clusters : 1以上の整数  
    data : [[], [], ..., []] （二次元配列）  
  }
  ```

- resposense  
```
{  
  labels: [ ] (一次元配列)  
  average: [[], [], ..., []] (二次元配列)  
}  
```
labelsはクラスタリングした結果が一次元配列で格納される
averageはクラスタリング後の各クラスタの時系列データの平均値が格納される

- example

# Requirements
- SciPy
- sklearn
- [falcon](https://github.com/falconry/falcon)（Pythonサーバーフレームワーク）
