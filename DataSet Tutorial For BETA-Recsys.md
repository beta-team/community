# DataSet Tutorial For BETA-Recsys

**Author: **Yucheng Liang

**Last Update Time: **2020-05-29

## Introduction

BETA-Recsys provides users a wide range of datasets for recommendation system training. For convenience, we preprocess a number of datasets for you to train, getting you rid of splitting them on you local machine. Also this framework provides users a set of useful interfaces for data split.

---

## Dataset Statistics

Here we present some basic staticstics for the datasets in our framework.

|                         **Dataset**                          | **Interactions** | **Baskets** | **Temporal** |
| :----------------------------------------------------------: | :--------------: | :---------: | :----------: |
| [MovieLens-100K](https://grouplens.org/datasets/movielens/100k/) |        ✔️         |      ✖️      |      ✔️       |
| [MovieLens-1M](https://grouplens.org/datasets/movielens/1m/) |        ✔️         |      ✖️      |      ✔️       |
| [MovieLens-25M](https://grouplens.org/datasets/movielens/25m/) |        ✔️         |      ✖️      |      ✔️       |
|    [Last.FM](https://grouplens.org/datasets/hetrec-2011/)    |        ✔️         |      ✖️      |      ✖️       |
| [Epinions](http://www.trustlet.org/downloaded_epinions.html) |        ✔️         |      ✖️      |      ✖️       |
| [Tafeng](https://www.kaggle.com/chiranjivdas09/ta-feng-grocery-dataset/) |        ✔️         |      ✖️      |      ✔️       |
| [Dunnhumby](https://www.kaggle.com/frtgnn/dunnhumby-the-complete-journey) |        ✔️         |      ✔️      |      ✔️       |
| [Instacart](https://www.instacart.com/datasets/grocery-shopping-2017) |        ✔️         |      ✖️      |      ✔️       |
|    [citeulike-a](https://github.com/js05212/citeulike-a)     |        ✔️         |      ✖️      |      ✖️       |
| [citeulike-t](https://github.com/changun/CollMetric/tree/master/citeulike-t) |        ✔️         |      ✖️      |      ✖️       |
|     [HetRec](http://ir.ii.uam.es/hetrec2011/) MoiveLens      |        ✔️         |      ✖️      |      ✔️       |
|     [HetRec](http://ir.ii.uam.es/hetrec2011/) Delicious      |        ✔️         |      ✔️      |      ✖️       |
|       [HetRec](http://ir.ii.uam.es/hetrec2011/) LastFM       |        ✔️         |      ✔️      |      ✔️       |
|             [Yelp](https://www.yelp.com/dataset)             |        ✔️         |      ✖️      |      ✔️       |
|  [Gowalla](https://snap.stanford.edu/data/loc-Gowalla.html)  |        ✔️         |      ✖️      |      ✔️       |
| [Yoochoose](https://2015.recsyschallenge.com/challenge.html) |                  |             |              |
|    [Diginetica](https://cikm2016.cs.iupui.edu/cikm-cup/)     |                  |             |              |
| [Taobao](https://tianchi.aliyun.com/dataset/dataDetail?dataId=649) |                  |             |              |
| [Ali-mobile](https://tianchi.aliyun.com/dataset/dataDetail?dataId=46) |                  |             |              |
| [Retailrocket](https://www.kaggle.com/retailrocket/ecommerce-dataset#events.csv) |                  |             |              |

Because some split methods require a specific features, like `random_basket` expect the dataset has a **Basket** column. Here we list all the split methods for each dataset.

The prerequisite for each split methods are:

+ `leave_one_out`: none
+ `leave_one_basket`: require a **Basket** column in dataset
+ `random`: none
+ `random_basket`: require a **Basket** column in dataset
+ `temporal`: require a **Timestamp(Temporal)** column in dataset
+ `temporal_basket`: require a **Timestamp(Temporal)** and a **Basket** column in dataset

|                         **Dataset**                          | **leave_one_out** | **leave_one_basket** | **random** | **random_basket** | **temporal** | temporal_basket |
| :----------------------------------------------------------: | :---------------: | :------------------: | :--------: | :---------------: | :----------: | :-------------: |
| [MovieLens-100K](https://grouplens.org/datasets/movielens/100k/) |         ✔️         |          ✖️           |     ✔️      |         ✖️         |      ✔️       |        ✖️        |
| [MovieLens-1M](https://grouplens.org/datasets/movielens/1m/) |         ✔️         |          ✖️           |     ✔️      |         ✖️         |      ✔️       |        ✖️        |
| [MovieLens-25M](https://grouplens.org/datasets/movielens/25m/) |         ✔️         |          ✖️           |     ✔️      |                   |              |                 |
|    [Last.FM](https://grouplens.org/datasets/hetrec-2011/)    |         ✔️         |          ✖️           |     ✔️      |         ✖️         |      ✖️       |        ✖️        |
| [Epinions](http://www.trustlet.org/downloaded_epinions.html) |         ✔️         |          ✖️           |     ✔️      |         ✖️         |      ✖️       |        ✖️        |
| [Tafeng](https://www.kaggle.com/chiranjivdas09/ta-feng-grocery-dataset/) |         ✔️         |          ✖️           |     ✔️      |         ✖️         |      ✔️       |        ✖️        |
| [Dunnhumby](https://www.kaggle.com/frtgnn/dunnhumby-the-complete-journey) |         ✔️         |          ✔️           |     ✔️      |         ✔️         |      ✔️       |        ✔️        |
| [Instacart](https://www.instacart.com/datasets/grocery-shopping-2017) |         ✔️         |          ✖️           |     ✔️      |         ✖️         |      ✔️       |        ✖️        |
|    [citeulike-a](https://github.com/js05212/citeulike-a)     |         ✔️         |          ✖️           |     ✔️      |         ✖️         |      ✖️       |        ✖️        |
| [citeulike-t](https://github.com/changun/CollMetric/tree/master/citeulike-t) |         ✔️         |          ✖️           |     ✔️      |         ✖️         |      ✖️       |        ✖️        |
|     [HetRec](http://ir.ii.uam.es/hetrec2011/) MoiveLens      |         ✔️         |          ✖️           |     ✔️      |         ✖️         |      ✔️       |        ✖️        |
|     [HetRec](http://ir.ii.uam.es/hetrec2011/) Delicious      |         ✔️         |          ✔️           |     ✔️      |         ✖️         |      ✖️       |        ✖️        |
|       [HetRec](http://ir.ii.uam.es/hetrec2011/) LastFM       |         ✔️         |          ✔️           |     ✔️      |         ✔️         |      ✔️       |        ✔️        |
|             [Yelp](https://www.yelp.com/dataset)             |         ✔️         |          ✖️           |     ✔️      |                   |              |                 |
|  [Gowalla](https://snap.stanford.edu/data/loc-Gowalla.html)  |         ✔️         |          ✖️           |     ✔️      |         ✖️         |      ✖️       |        ✖️        |
| [Yoochoose](https://2015.recsyschallenge.com/challenge.html) |         ✔️         |                      |     ✔️      |                   |              |                 |
|    [Diginetica](https://cikm2016.cs.iupui.edu/cikm-cup/)     |         ✔️         |                      |     ✔️      |                   |              |                 |
| [Taobao](https://tianchi.aliyun.com/dataset/dataDetail?dataId=649) |         ✔️         |                      |     ✔️      |                   |              |                 |
| [Ali-mobile](https://tianchi.aliyun.com/dataset/dataDetail?dataId=46) |         ✔️         |                      |     ✔️      |                   |              |                 |
| [Retailrocket](https://www.kaggle.com/retailrocket/ecommerce-dataset#events.csv) |         ✔️         |                      |     ✔️      |                   |              |                 |

Also, we provide some information about the dataset content such as the number of items, users and so on. This may give you a brief view of the dataset.

|                         **Dataset**                          |   User/unique   | **Item/unique**  | Rating/unique | **Timestamp**/unique |
| :----------------------------------------------------------: | :-------------: | :--------------: | :-----------: | -------------------- |
| [MovieLens-100K](https://grouplens.org/datasets/movielens/100k/) |   100000/943    |   100000/1682    |   100000/5    | 100000/49282         |
| [MovieLens-1M](https://grouplens.org/datasets/movielens/1m/) |  1000209/6040   |   1000209/3706   |   1000209/5   | 1000209/458455       |
| [MovieLens-25M](https://grouplens.org/datasets/movielens/25m/) | 25000095/162541 |  25000095/59047  |  25000095/10  | 25000095/20115267    |
|    [Last.FM](https://grouplens.org/datasets/hetrec-2011/)    |   92834/1892    |   92834/17632    |  92834/5436   | 92834/1              |
| [Epinions](http://www.trustlet.org/downloaded_epinions.html) |  664825/40163   |  664825/139738   |   664825/5    | 664825/1             |
| [Tafeng](https://www.kaggle.com/chiranjivdas09/ta-feng-grocery-dataset/) |                 |                  |               |                      |
| [Dunnhumby](https://www.kaggle.com/frtgnn/dunnhumby-the-complete-journey) |     500/28      |     500/463      |     500/1     | N/A                  |
| [Instacart](https://www.instacart.com/datasets/grocery-shopping-2017) | 33819106/206209 |  33819106/49685  |  33819106/1   | 33819106/3346083     |
|    [citeulike-a](https://github.com/js05212/citeulike-a)     |   204986/240    |   204986/16980   |   204986/1    | 204986/1             |
| [citeulike-t](https://github.com/changun/CollMetric/tree/master/citeulike-t) |   134860/216    |   134860/25584   |   134860/1    | 134860/1             |
|     [HetRec](http://ir.ii.uam.es/hetrec2011/) MoiveLens      |   855598/2113   |   855598/10109   |   855598/10   | 855598/809328        |
|     [HetRec](http://ir.ii.uam.es/hetrec2011/) Delicious      |   437593/1867   |   437593/69223   |   437593/1    | 437593/104093        |
|       [HetRec](http://ir.ii.uam.es/hetrec2011/) LastFM       |   186479/1892   |   186479/12523   |   186479/1    | 186479/9749          |
|             [Yelp](https://www.yelp.com/dataset)             | 8021122/1968703 |  8021122/209393  |   8021122/5   | 8021122/7853102      |
|  [Gowalla](https://snap.stanford.edu/data/loc-Gowalla.html)  | 6442892/107092  | 6442892/1280969  |   6442892/1   | 6442892/5561957      |
| [Yoochoose](https://2015.recsyschallenge.com/challenge.html) | 1150753/509696  |   1150753/735    |   1150753/1   | 1150753/19949        |
|    [Diginetica](https://cikm2016.cs.iupui.edu/cikm-cup/)     | 1235380/310324  |  1235380/122993  |   1235380/1   | 1235380/152          |
| [Taobao](https://tianchi.aliyun.com/dataset/dataDetail?dataId=649) |  3835331/37376  |  3835331/930607  |   3835331/1   | 3835331/698889       |
| [Ali-mobile](https://tianchi.aliyun.com/dataset/dataDetail?dataId=46) | 12256906/10000  | 12256906/2876947 |  12256906/1   | 12256906/1           |
| [Retailrocket](https://www.kaggle.com/retailrocket/ecommerce-dataset#events.csv) | 2756101/1407580 |  2756101/235061  |   2756101/1   | 2756101/2749921      |

---

## Dataset Usage

### Download Data

BETA-Recsys provides download interface for users to download different dataset. Here is an example:

```python
import sys
import os
sys.path.append(os.path.abspath('.'))
from beta_rec.datasets.movielens import Movielens_1m

movielens_1m = Movielens_1m()
movielens_1m.download()
```

However, not every dataset could be downloaded directly with our framework. **For some datasets, you will still have to download them manually. You are supposed to follow our tips to download and put the dataset in the correct folder in order to be detected by our framework.** 

### Load Data

Downloading and preprocessing giant datasets may be a disturbing things, and in order to deal with this issue, we have preprocessed a wide range of datasets and stored the processed data in our remote server. Users can access them easily by using our `load` function.

```python
import sys
import os
sys.path.append(os.path.abspath('.'))
from beta_rec.datasets.movielens import Movielens_1m

movielens_1m = Movielens_1m()
movielens_1m.load_leave_one_out()
movielens_1m.load_random_split()
```

Due to storage limitation, we only store a copy of split data with default parameters. If you want a custom split, you'll still have to split them on you local machine.

### Make Data

Users can simply ignore these functions because when you use custom parameters in `load` functions, it will automatically call `make` functions. So you don't need to care about this functions. **We strongly recommend you to use `load` function directly in most of you time.**

---

## Data Split

For users who are willing to split some datasets that is not covered by our framework, we still provide various methods to make it easy to split huge data, without caring the details. There are 6 main methods for users to split data.

### random_split

This method will select a portion of records based on the given `test_rate` randomly.

### random_basket_split

This method will select a portion of baskets(one basket may cover more than one record) based on the given `test_rate` randomly.

### leave_one_out

This method will first rank all the records by time (if a timestamp column is provided), and then select the last record.

### leave_one_basket

This method will first rank all the records by time (if a timestamp column is provided), and then select the last basket.

### temporal_split

This method will first rank all the records by time (if a timestamp column is provided), and then select the last portion of records.

### temporal_basket_split

This method will first rank all the records by time (if a timestamp column is provided), and then select the last portion of baskets.

## More

For any quesitons, please tell us by **creating an issue** or contact us by sending an email to recsys.beta@gmail.com. We will try to respond it as soon as possible.