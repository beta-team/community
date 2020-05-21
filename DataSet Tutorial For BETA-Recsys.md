# DataSet Tutorial For BETA-Recsys

**Author: **Yucheng Liang

**Last Update Time: **2020-05-09

## Introduction

BETA-Recsys provides users a wide range of datasets for recommendation system training. For convenience, we preprocess a number of datasets for you to train, getting you rid of splitting them on you local machine. Also this framework provides users a set of useful interfaces for data split.

---

## Dataset Statistics

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

## Data Split

For users who are willing to split some datasets that is not covered by our framework, we still provide various methods to make it easy to split huge data, without caring the details. There are 6 main methods for users to split data.

#### random_split

#### random_basket_split

#### leave_one_out

#### leave_one_basket

#### temporal_split

#### temporal_basket_split

## More

For any quesitons, please tell us by **creating an issue**. We will try to respond it as soon as possible.