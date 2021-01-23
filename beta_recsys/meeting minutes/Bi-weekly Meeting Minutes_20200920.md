# Beta Project Notes  

> 2020.09.20
>
> By Zaiqiao Meng	Email: zaiqiao.meng@gmail.com
>
> Chair: Zaiqiao Meng
>
> Next Chair: Xi Wang

------
## 1. Process

### Format Issues

- [x] Check with flake8 failed in some files, which are all the previous version. 
- [x] Now we have update some package versions.
  - black==19.10b0 v.s. black==20.8b1(flake8-black==0.2.1 still not work well with the new black)
  - flake8-isort==4.0.0 and isort==5.5.2
  - ray==0.8.5 need to be fixed. This version need to be update.

New Features

- [ ] New interface for models
- [ ] Experiment part

## Discuss

- [ ] Version Update:
  - Version 1.x.x update frequency: When a milestone achieved.
  - Version x.x.1 update frequency: Each 1-2 poject meetings.Roughly 1 months.
  - Version x.1.x update frequency: Each 3-4 poject meetings .Roughly (2-3 x.x.1 updates) 2-3 months.
  - Version 1.0 Deadline: 2020.12.24.
- [ ] Rotating Chairing - meeting:
  - [ ] Each two weeks.
  - [ ] Issue hight priority will chair the next week.
  - [ ] Chair process:
    - [ ] Summarise issues
      - [ ] Issues Priority 
      - [ ] Bugs summary
    - [ ] Report features
    - [ ] Discuss issues
    - [ ] Make discussion notes
- [ ] Groups Partition:
  - [ ] Framework (Zaiqiao, Xi, Siwei, Yucheng, Junhua)
    - [ ] Experiment (Yucheng)
    - [ ] Ray
    - [ ] Eval-methods
    - [ ] Coresa
      - [ ] Model train
      - [ ] Model test
      - [ ] Dataloaders
  - [ ] Model (Siwei, Zaiqiao)
    - [ ] General Recommenders
    - [ ] Sequential Recommenders - temporal
    - [ ] Recommenders with Auxiliary Information
  - [ ] Datasets (Yucheng, Guangtao, Junhua)
    - [ ] Datasplit
    - [ ] Database
  - [ ] Documentation (Xi, Shangsong, Guangtao)
    - [ ] https://beta-recsys.readthedocs.io/en/latest/
    - [ ] README

## tODO

- [ ] Add amazon dataset.
- [ ] Update models with new interface.
- [ ] Check all the datasets.
- [ ] Check models and benchmarking.
- [ ] Docker image for the project and maintain it.
- [ ] Check the usage of the overall project.
- [ ] Experiment



------

## Appendix 1 Current Milestone (M 2)

### Data Span

**Start Data:** 2020-07-27

Middle Review:  2020-09-20 (Recsys2020, Sept 22-26, 2020)

**End Data:** 2020-11-20 

~110 Days

###  & Bug fixing

- New interface for each part
  - Load_Dataset 
    - Load_data(argkv**) 	
      - config
  - Data_Split 
    - Data_Split(argkv**)
  - Build DataLoader (Sequential Recommendation)
  - Model 
    - Train
    - Test
  - Example
    - MF(argkv**, config, json_config)
    - MF(argkv**)

### New features

- **Experiment part**
- Deploy Hyperparameter Tuning 
- Evaluation (Multi-model camparison)
- More Models
  - Sequential Recommendation
    - Models
    - Simulators
  - POI
  - CTR
  - Auxiliary (e.g. side information, social, knowledge graph)
  - Review RS

### Experiments & Papers

- Find sponsor

------
## Appendix 2. Models


- General Models

  - [x] GMF: Generalized Matrix Factorization, in [Neural Collaborative Filtering](https://arxiv.org/abs/1708.05031), WWW 2017
  - [x] MLP: Multi-Layer Perceptron, in [Neural Collaborative Filtering](https://arxiv.org/abs/1708.05031), WWW 2017
  - [x] NCF: [Neural Collaborative Filtering](https://arxiv.org/abs/1708.05031),  WWW 2017
  - [x] CMN: [Collaborative memory network for recommendation systems](https://dl.acm.org/doi/abs/10.1145/3209978.3209991),  SIGIR 2018
  - [ ] VAECF: [Variational autoencoders for collaborative filtering](https://dl.acm.org/doi/abs/10.1145/3178876.3186150), WWW 2018
  - [x] NGCF: [Neural graph collaborative filtering](https://dl.acm.org/doi/abs/10.1145/3331184.3331267), SIGIR 2019
  - [x] LightGCN: [**LightGCN**: Simplifying and Powering Graph Convolution Network for Recommendation](https://arxiv.org/abs/2002.02126), SIGIR 2020
  - [x] MF: [Neural Collaborative Filtering vs. Matrix Factorization Revisited](https://arxiv.org/abs/2005.09683), arXiv’ 2020

- Sequential Models?
  - [ ] GRU4Rec: [Session-based recommendations with recurrent neural networks](https://arxiv.org/abs/1511.06939), ICLR 2016

  - [x] NARM: [Neural Attentive Session-based Recommendation](https://arxiv.org/pdf/1711.04725.pdf), CIKM, 2017

  - [ ] SasRec:[**Self**-**attentive sequential recommendation**](https://ieeexplore.ieee.org/abstract/document/8594844/?casa_token=RINDZUuHnwoAAAAA:XBjSlh6-KqBjgCY1AWwgXyZqHtT_8zAPBMKjLIUJMlf6Ex9j55gG2UAsrRtG10roMUd6-_w3Jw). ICDM 2018

  - [ ] BERT4Rec: [BERT4Rec: **Sequential recommendation** with **bidirectional encoder representations** from **transformer**](https://dl.acm.org/doi/abs/10.1145/3357384.3357895), CIKM 2019

  - [ ] TiSASRec: [Time Interval Aware Self-Attention for **Sequential Recommendation**](https://dl.acm.org/doi/abs/10.1145/3336191.3371786). WWW 2020

- Grocery Recommendations
  - [x] Triple2vec: [Representing and recommending shopping baskets with complementarity, compatibility and loyalty](https://dl.acm.org/doi/abs/10.1145/3269206.3271786), CIKM 2018
  - [x] VBCAR: [Variational Bayesian Context-aware Representation for Grocery Recommendation](https://arxiv.org/abs/1909.07705),  arXiv’ 2019

- Recommendation Models with Auxiliary information?
  - Social

  - Item feature

  - User feature

  - Knowledge graph

  - [ ] KGAT: [Kgat: Knowledge graph attention network for recommendation](https://dl.acm.org/doi/abs/10.1145/3292500.3330989). SIGKDD 2019

  - Review

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

