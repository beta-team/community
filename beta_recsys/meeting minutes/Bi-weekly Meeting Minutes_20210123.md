# Beta-Recsys Project Bi-weekly Meeting Minutes

>When：Saturday (1:30 – 2:30pm **[UTC +0](https://24timezones.com/time-zone/utc#gref)**/9:30 – 10:30pm **[UTC +8](https://24timezones.com/time-zone/utc+8#gref)**)⋅** [![Add Event](https://img.shields.io/badge/Add-Event-blue)](https://github.com/beta-team/community/releases/download/meeting/bi-weekly.meeting.ics)
>Where:[Microsoft Team](http://tiny.cc/82t1tz)

## 2021.1.23

### Charing

> Notes Taken by: Siwei Liu (siweiliu525@gmail.com)
>
> Next Chair: Yingxu Wang (Active Learning)

#### Checklist

- [x] Review Past Issues/Actions

- [x] Review Documentation

- [x] Review Milestone (See Appendix A)

- [x] Discuss New Issues/Actions for the Next Step

- [x] Confirm the chair of next meeting

- [x] Fill attendees list

- [x] Merge all the changes into master

- [ ] New version release

  - Release to github

  - Update to pip
  - Update to conda

#### Attendees

- Zaiqiao Meng
- Siwei Liu
- Wu Xiangkun
- Langning Liang
- Shuqi Mo
- Yingxu Wang

---



### Past actions/issues

#### Bugs

- [ ] [dependency check](https://github.com/beta-team/beta-recsys/issues/360) 
- [ ] [Cuda valueError](https://github.com/beta-team/beta-recsys/issues/343)

#### New Features

- [ ] [Implementation of BERT4Rec](https://github.com/beta-team/beta-recsys/issues/342)
- [x] Implementation of SASRec
- [ ] [detach dataload from train_engine](https://github.com/beta-team/beta-recsys/issues/205) 
- [ ] [Add additional information for recommendation (side information, social)](https://github.com/beta-team/beta-recsys/issues/43)

#### Chore Issues

- [ ] [create a quick Quickstart notebook for each model under Colab](https://github.com/beta-team/beta-recsys/issues/322) 
- [ ] [Add the documentation of evaluation with negative sampling](https://github.com/beta-team/beta-recsys/issues/304) 

#### Others

- [ ]  [Check all the datasets](https://github.com/beta-team/beta-recsys/issues/248)
- [ ]  [Check all the models](https://github.com/beta-team/beta-recsys/issues/249) 
- [ ]  [regenerate all the data split](https://github.com/beta-team/beta-recsys/issues/300) 
- [ ]  [Benchmarking](https://github.com/beta-team/beta-recsys/issues/250)

### Discussions

- What to do this year?
  - New Milestone (2021-4-1)
    - Benchmarking
    - **Negative Sampling+contrastive learning**
    - **Text-Image-**
    - Add new models (TiSASRec, VAECF)
    - A novel dataset module offering users an interface to upload their own dataset.

### Actions

- [ ] Check epinions dataset
- [ ] Check VBCAR and Trip2Vec
- [ ] Review SASRec
- [ ] Add dataset module so that users can upload their own datasets according to provided format. Example: Huggingface dataset.

- [ ] Check all models (Shuqi Mo)

- [ ] Check all datasets (Xiangkun Wu)

- [ ] Implement VAECF model (Siwei Liu, Shuqi Mo)

- [ ] Implement TiSASRec model (Zaiqiao Meng)

- [ ] Add some SOTA model with review text (Xi Wang)

- [ ] Investigate "Negative Sampling+contrastive learning" (Siwei Liu, Zaiqiao Meng)

- [ ] Investigate "Recommendation+Image" (Siwei Liu, Zaiqiao Meng)

  




------

## Appendix 1 Milestone (M 2)

### Period

**Start Data:** 2021-01-01

Middle Review:  2020-03-01

**End Data:** 2020-04-01

### Key Actions (To be expended)

- Benchmark
- **Negative Sampling+contrastive learning**
- **Recommendation+Image**
- Add new models

------
## Appendix 2. Models
The following is a list of recommender models currently available in the repository, or to be implemented soon.

### General Models
  - [x] MF[![Example In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1tJX4ZTtNp6tdGer-jUQ_ZZSIf9J2MB7G?usp=sharing): [Neural Collaborative Filtering vs. Matrix Factorization Revisited](https://arxiv.org/abs/2005.09683), arXiv’ 2020 
  - [x] GMF: Generalized Matrix Factorization, in [Neural Collaborative Filtering](https://arxiv.org/abs/1708.05031), WWW 2017
  - [x] MLP: Multi-Layer Perceptron, in [Neural Collaborative Filtering](https://arxiv.org/abs/1708.05031), WWW 2017
  - [x] NCF[![Example In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1-3zfUNEexpB5eoTIwDfIqgMNFLQet2vV?usp=sharing): [Neural Collaborative Filtering](https://arxiv.org/abs/1708.05031),  WWW 2017
  - [x] CMN: [Collaborative memory network for recommendation systems](https://dl.acm.org/doi/abs/10.1145/3209978.3209991),  SIGIR 2018
  - [x] NGCF: [Neural graph collaborative filtering](https://dl.acm.org/doi/abs/10.1145/3331184.3331267), SIGIR 2019
  - [x] LightGCN: [**LightGCN**: Simplifying and Powering Graph Convolution Network for Recommendation](https://arxiv.org/abs/2002.02126), SIGIR 2020
  - [x] LCF: [Graph Convolutional Network for Recommendation with Low-pass Collaborative Filters](https://arxiv.org/abs/2006.15516)
  - [ ] VAECF: [Variational autoencoders for collaborative filtering](https://dl.acm.org/doi/abs/10.1145/3178876.3186150), WWW 2018 (Siwei)

### Sequential Models
  - [x] NARM: [Neural Attentive Session-based Recommendation](https://arxiv.org/abs/1711.04725), CIKM 2017
  - [ ] Caser: [Personalized Top-N Sequential Recommendation via Convolutional Sequence Embedding](https://dl.acm.org/doi/abs/10.1145/3159652.3159656), WSDM 2018
  - [ ] GRU4Rec: [Session-based recommendations with recurrent neural networks](https://arxiv.org/abs/1511.06939), ICLR 2016
  - [ ] SasRec:[**Self**-**attentive sequential recommendation**](https://ieeexplore.ieee.org/abstract/document/8594844/?casa_token=RINDZUuHnwoAAAAA:XBjSlh6-KqBjgCY1AWwgXyZqHtT_8zAPBMKjLIUJMlf6Ex9j55gG2UAsrRtG10roMUd6-_w3Jw). ICDM 2018
  - [ ] **MARank: [Multi-Order Attentive Ranking Model for Sequential Recommendation](https://ojs.aaai.org//index.php/AAAI/article/view/4516), AAAI 2019**
  - [ ] NextItnet: [A Simple Convolutional Generative Network for Next Item Recommendation](https://dl.acm.org/doi/abs/10.1145/3289600.3290975), WSDM 2019
  - [ ] BERT4Rec: [BERT4Rec: **Sequential recommendation** with **bidirectional encoder representations** from **transformer**](https://dl.acm.org/doi/abs/10.1145/3357384.3357895), CIKM 2019 (Yingting)
  - [ ] TiSASRec: [Time Interval Aware Self-Attention for **Sequential Recommendation**](https://dl.acm.org/doi/abs/10.1145/3336191.3371786). WWW 2020 (Zaiqiao)

### Recommendation Models with Auxiliary Information
  ### Baskets/Sessions
  - [x] Triple2vec: [Representing and recommending shopping baskets with complementarity, compatibility and loyalty](https://dl.acm.org/doi/abs/10.1145/3269206.3271786), CIKM 2018
  - [x] VBCAR: [Variational Bayesian Context-aware Representation for Grocery Recommendation](https://arxiv.org/abs/1909.07705),  arXiv’ 2019
  ### Knowledge Graph
  - [ ] KGAT: [Kgat: Knowledge graph attention network for recommendation](https://dl.acm.org/doi/abs/10.1145/3292500.3330989). SIGKDD 2019

### Review
- [ ] 

### Social

### Image

- [ ] Text image


******

## Appendix 3. Datasets


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
| [Yoochoose](https://2015.recsyschallenge.com/challenge.html) |        ✔️         |      ✖️      |      ✔️       |
|    [Diginetica](https://cikm2016.cs.iupui.edu/cikm-cup/)     |        ✔️         |      ✖️      |      ✔️       |
| [Taobao](https://tianchi.aliyun.com/dataset/dataDetail?dataId=649) |        ✔️         |      ✖️      |      ✔️       |
| [Ali-mobile](https://tianchi.aliyun.com/dataset/dataDetail?dataId=46) |        ✔️         |      ✖️      |      ✔️       |
| [Retailrocket](https://www.kaggle.com/retailrocket/ecommerce-dataset#events.csv) |        ✔️         |      ✖️      |      ✔️       |
