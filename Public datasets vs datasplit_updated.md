# Datasets

> ### Public datasets
>

> If there is a **Standard Splitting** for the dataset?
>
> Which datasets are able to use the temporal splitting?
> s
>

|                         **Dataset**                          | **Interactions** | **Baskets** | **Temporal** | **Item Feature** | **User Feature** | **Store/Center** | **Standard Splitting**                                  |
| :----------------------------------------------------------: | :--------------: | :---------: | :----------: | :--------------: | :--------------: | :--------------: | ------------------------------------------------------- |
| [MovieLens-100K](https://grouplens.org/datasets/movielens/100k/) |     :heavy_check_mark:      |  :heavy_multiplication_x:   |   :heavy_check_mark:    |     :heavy_check_mark:      |     :heavy_check_mark:      |     :heavy_multiplication_x:     | 5 fold cross validation (users) & Leave-(10 rating)-out |
| [MovieLens-1M](https://grouplens.org/datasets/movielens/1m/) |     :heavy_check_mark:      |  :heavy_multiplication_x:   |   :heavy_check_mark:    |     :heavy_check_mark:      |     :heavy_check_mark:      |     :heavy_multiplication_x:     | N/A                                                     |
| [MovieLens-25M](https://grouplens.org/datasets/movielens/25m/) |     :heavy_check_mark:      |  :heavy_multiplication_x:   |   :heavy_check_mark:    |     :heavy_check_mark:      |     :heavy_multiplication_x:     |     :heavy_multiplication_x:     | N/A                                                     |
|    [Last.FM](https://grouplens.org/datasets/hetrec-2011/)    |     :heavy_check_mark:      |  :heavy_multiplication_x:   |   :heavy_check_mark:    |     :heavy_multiplication_x:     |      social      |     :heavy_multiplication_x:     | N/A                                                     |
| [Epinions](http://www.trustlet.org/downloaded_epinions.html) |     :heavy_check_mark:      |  :heavy_multiplication_x:   |   :heavy_multiplication_x:   |     :heavy_multiplication_x:     |      social      |     :heavy_multiplication_x:     | N/A                                                     |
| [Tafeng](https://www.kaggle.com/chiranjivdas09/ta-feng-grocery-dataset) |     :heavy_check_mark:      |   :heavy_check_mark:   |   :heavy_check_mark:    |     :heavy_check_mark:      |     :heavy_check_mark:      |     :heavy_multiplication_x:     | N/A                                                     |
| [Dunnhumby](https://www.kaggle.com/frtgnn/dunnhumby-the-complete-journey) |     :heavy_check_mark:      |   :heavy_check_mark:   |   :heavy_check_mark:    |     :heavy_check_mark:      |     :heavy_check_mark:      |     :heavy_check_mark:      | N/A                                                     |
| [Instacart](https://www.instacart.com/datasets/grocery-shopping-2017) |     :heavy_check_mark:      |   :heavy_check_mark:   |   :heavy_check_mark:    |     :heavy_check_mark:      |     :heavy_multiplication_x:     |     :heavy_multiplication_x:     | N/A                                                     |
|    [citeulike-a](https://github.com/js05212/citeulike-a)     |     :heavy_check_mark:      |   :heavy_check_mark:   |   :heavy_check_mark:    |     :heavy_check_mark:      |     :heavy_multiplication_x:     |     :heavy_multiplication_x:     | N/A                                                     |
| [Pinterest](https://data.mendeley.com/datasets/fs4k2zc5j5/3) |     :heavy_check_mark:      |   :heavy_check_mark:   |   :heavy_check_mark:    |     :heavy_check_mark:      |     :heavy_multiplication_x:     |     :heavy_multiplication_x:     | N/A                                                     |
| [citeulike-t](https://github.com/changun/CollMetric/tree/master/citeulike-t) |     :heavy_check_mark:      |   :heavy_check_mark:   |   :heavy_check_mark:    |     :heavy_check_mark:      |     :heavy_multiplication_x:     |     :heavy_multiplication_x:     | N/A                                                     |
|          [HetRec](http://ir.ii.uam.es/hetrec2011/)           |     :heavy_check_mark:      |   :heavy_check_mark:   |   :heavy_check_mark:    |     :heavy_check_mark:      |     :heavy_multiplication_x:     |     :heavy_multiplication_x:     | N/A                                                     |
|          [Yelp](https://www.yelp.com/dataset)           |     :heavy_check_mark:      |    :heavy_multiplication_x:  |   :heavy_check_mark:    |     :heavy_check_mark:      |     :heavy_check_mark:      |     :heavy_multiplication_x:     | N/A  
|          [Gowalla](https://snap.stanford.edu/data/loc-Gowalla.html)           |     :heavy_check_mark:      |    :heavy_multiplication_x:  |   :heavy_check_mark:    |     :heavy_multiplication_x:      |     social      |     :heavy_multiplication_x:     | N/A 

### Two popular session-based recommendation datasets
| Datasets                        | Sessions | Items | Testing split               |
| ------------------------------- | -------- | ----- | --------------------------- |
| RecSys’15 Challenge (Yoochoose) | 7981580  | 37483 | subsequent day for testing  |
| CIKM Cup 2016 (Diginetica)      | 204771   | 43097 | subsequent week for testing |

Out-of our scope

> All the session-based recommendation datasets are based on temporal spit.

Literature review on data splitting

|        Paper        | Leave-one (item)-out | Leave-one (basket/session)-out | Personalized Temporal Split | Global Temporal Split | User Split |
| :-----------------: | :------------------: | :----------------------------: | :-------------------------: | :-------------------: | ---------- |
|   BPR (UAI 2009)    |       :heavy_check_mark:        |            :heavy_multiplication_x:            |          :heavy_multiplication_x:           |       :heavy_multiplication_x:        | :heavy_multiplication_x:   |
|   FPMC (WWW 2010)   |       :heavy_multiplication_x:       |            :heavy_check_mark:             |          :heavy_multiplication_x:           |       :heavy_multiplication_x:        | :heavy_multiplication_x:   |
|   NCF (WWW 2017)    |       :heavy_check_mark:        |            :heavy_multiplication_x:            |          :heavy_multiplication_x:           |       :heavy_multiplication_x:        | :heavy_multiplication_x:   |
| CTRec (SIGIR 2019)  |       :heavy_check_mark:        |            :heavy_check_mark:             |           :heavy_check_mark:           |       :heavy_multiplication_x:        | :heavy_multiplication_x:   |
|  NGCF (SIGIR 2019)  |       :heavy_multiplication_x:       |            :heavy_multiplication_x:            |           :heavy_check_mark:           |       :heavy_multiplication_x:        | :heavy_multiplication_x:   |
|  VAE_CF (WWW 2018)  |       :heavy_multiplication_x:       |            :heavy_multiplication_x:            |          :heavy_multiplication_x:           |       :heavy_multiplication_x:        | :heavy_check_mark:    |
|  SVAE (WSDM 2019)   |       :heavy_multiplication_x:       |            :heavy_multiplication_x:            |           :heavy_check_mark:           |       :heavy_multiplication_x:        | :heavy_check_mark:    |
|   KGAT (KDD 2019)   |       :heavy_multiplication_x:       |            :heavy_multiplication_x:            |           :heavy_check_mark:           |       :heavy_multiplication_x:        | :heavy_multiplication_x:   |
| HierTCN (CIKM 2019) |       :heavy_multiplication_x:       |            :heavy_multiplication_x:            |          :heavy_multiplication_x:           |        :heavy_check_mark:        | :heavy_check_mark:    |
| JTM (NeurIPS 2019)  |       :heavy_multiplication_x:       |            :heavy_multiplication_x:            |          :heavy_multiplication_x:           |       :heavy_multiplication_x:        | :heavy_check_mark:    |
