# Datasets

> ### Public datasets
>

> If there is a **Standard Splitting** for the dataset?
>
> Which datasets are able to use the temporal splitting?
>s
>

|                         **Dataset**                          | **Interactions** | **Baskets** | **Temporal** | **Item Feature** | **User Feature** | **Store/Center** | **Standard Splitting** |
| :----------------------------------------------------------: | :--------------: | :---------: | :----------: | :--------------: | :--------------: | :--------------: | ------------------------------------------------------------ |
| [MovieLens-100K](https://grouplens.org/datasets/movielens/100k/) | $\surd$ | $\times$ | $\surd$ | $\surd$ | $\surd$ | $\times$ |5 fold cross validation (users) & Leave-(10 rating)-out|
| [MovieLens-1M](https://grouplens.org/datasets/movielens/1m/) | $\surd$ | $\times$ | $\surd$ | $\surd$ | $\surd$ | $\times$ |N/A|
| [MovieLens-25M](https://grouplens.org/datasets/movielens/25m/) | $\surd$ | $\times$ | $\surd$ | $\surd$ | $\times$ | $\times$ |N/A|
| [Last.FM](https://grouplens.org/datasets/hetrec-2011/) | $\surd$ | $\times$ | $\surd$ | $\times$ | social | $\times$ |N/A|
| [Epinions](http://www.trustlet.org/downloaded_epinions.html) | $\surd$ | $\times$ | $\times$ | $\times$ | social | $\times$ |N/A|
| [Tafeng](https://www.kaggle.com/chiranjivdas09/ta-feng-grocery-dataset)                           |     $\surd$      |   $\surd$   |   $\surd$    |     $\surd$      |     $\surd$      |     $\times$     |N/A|
| [Dunnhumby](https://www.kaggle.com/frtgnn/dunnhumby-the-complete-journey)                           |     $\surd$      |   $\surd$   |   $\surd$    |     $\surd$      |     $\surd$      |     $\surd$      |N/A|
| [Instacart](https://www.instacart.com/datasets/grocery-shopping-2017)                           |     $\surd$      |   $\surd$   |   $\surd$    |     $\surd$      |     $\times$     |     $\times$     |N/A|
| [citeulike-a](https://github.com/js05212/citeulike-a)                           |     $\surd$      |   $\surd$   |   $\surd$    |     $\surd$      |     $\times$     |     $\times$     |N/A|
| [Pinterest](https://data.mendeley.com/datasets/fs4k2zc5j5/3)                           |     $\surd$      |   $\surd$   |   $\surd$    |     $\surd$      |     $\times$     |     $\times$     |N/A|
| [citeulike-t](https://github.com/changun/CollMetric/tree/master/citeulike-t)                           |     $\surd$      |   $\surd$   |   $\surd$    |     $\surd$      |     $\times$     |     $\times$     |N/A|
| [HetRec](http://ir.ii.uam.es/hetrec2011/)                           |     $\surd$      |   $\surd$   |   $\surd$    |     $\surd$      |     $\times$     |     $\times$     |N/A|


### Two popular session-based recommendation datasets
| Datasets                        | Sessions | Items | Testing split|
| ------------------------------- | ------ | ----- | ----- |
| RecSys’15 Challenge (Yoochoose) | 7981580 | 37483 |subsequent day for testing|
| CIKM Cup 2016 (Diginetica)      | 204771 | 43097 |subsequent week for testing|

Out-of our scope

> All the session-based recommendation datasets are based on temporal spit.

Literature review on data splitting

|       Paper        | Leave-one (item)-out | Leave-one (basket/session)-out | Personalized Temporal Split | Global Temporal Split |User Split |
| :----------------: | :------------------: | :----------------------------: | :-------------------------: | :-------------------: | ------------------ |
|        BPR (UAI 2009)        |       $\surd$        |            $\times$            |          $\times$           |       $\times$        |$\times$|
|        FPMC (WWW 2010)        |       $\times$        |           $\surd$            |          $\times$           |       $\times$        |$\times$|
|   NCF (WWW 2017)   |       $\surd$        |            $\times$            |          $\times$           |       $\times$        |$\times$|
| CTRec (SIGIR 2019) |       $\surd$        |            $\surd$             |           $\surd$           |       $\times$        |$\times$|
| NGCF (SIGIR 2019)  |       $\times$       |            $\times$            |           $\surd$           |       $\times$        |$\times$|
| VAE_CF (WWW 2018) | $\times$ | $\times$ | $\times$ | $\times$ |$\surd$|
| SVAE (WSDM 2019) | $\times$ | $\times$ | $\surd$ | $\times$ |$\surd$|
| KGAT (KDD 2019) | $\times$ | $\times$ | $\surd$ | $\times$ |$\times$|
| HierTCN (CIKM 2019) | $\times$ | $\times$ | $\times$ | $\surd$ |$\surd$|
| JTM (NeurIPS 2019) | $\times$ | $\times$ | $\times$ | $\times$ |$\surd$|
