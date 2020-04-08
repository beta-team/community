# How to use our datasets?

**Author: Yucheng Liang**

**Last Updated Time: 2020-04-08**

This document illustrates the usage of our dataset from the view of client.

## Glossary

+ split data: data split by our methods(leave one item, leave one basket, ...)
+ raw data: original raw data of the dataset.
+ processed data: data that is reformatted but not split.
+ Onedrive: our team's remote drive.
+ local: client's computer

## Methods

1. `download()`: download raw data with a URL.
2. `make_xxx()`: generate split data and store them locally.
3. `load_xxx()`: load split data from local disk or from Onedrive.

## Senario

1. For those datasets that can be download with a URL:

   a. download raw data and store in local.

   b. load_xxx: if the data is not existed locally, download from Onedrive.

   c. make_xxx: split data based on processed data and store them locally.

2. For those datasets that must be download by client manurally:

   a. download manurally from website and move to the specified folder.

   b-c: the same as the 1.

## Difference between load and make

load:

+ pros:
  + this method do not need any computational resource of local machine. Client can access split data easily by downloading from our Onedrive.
  + For those who want to run on PC, this is faster.
+ cons:
  + The split data is split by us in advanced with specified parameters(e.g, test_rate, random), the user cannot specify parameters when using this methods. But it sometimes could be a pros because novice can use the default data easily.
  + Occupy some storage locally.

make:

+ pros: 
  + Allow client to specify some parameters when spliting data, more flexible for experienced users.
  + Client can specify whether to store the result locally. If not, this method can save a huge amount of storage.
+ cons:
  + It may use client's computational resource.