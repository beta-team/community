# Beta-Recsys Project Bi-weekly Meeting Minutes

>When：Saturday (1:30 – 2:30pm **[UTC +0](https://24timezones.com/time-zone/utc#gref)**/9:30 – 10:30pm **[UTC +8](https://24timezones.com/time-zone/utc+8#gref)**), (start from 7 November 2020)**⋅** [![Add Event](https://img.shields.io/badge/Add-Event-blue)](https://github.com/beta-team/community/releases/download/meeting/bi-weekly.meeting.ics)
>Where:[Microsoft Team](http://tiny.cc/82t1tz)
>This note link: https://hackmd.io/@betarecsys/SJNw1m4tP

## 2020.11.07
> Notes Taken by: Zaiqiao Meng (zaiqiao.meng@gmail.com)

### Attendees:
- Siwei Liu
- Guangtao Zeng
- Shuqi Mo
- Zaiqiao Meng
- Langning Liang

### Current Issues

- [ ] #43 Add additional information for recommendation.  ![progress](https://progress-bar.dev/50)
- [x] #166 Add Amazon book dataset.
- [x] #167 Add new feature for experiments.
- [x] #171 allow to generate validation and testing sets with all the negative items
  > Pass parameters n_negative = -1
  > Documentation need to be update
- [x] #172 Add more dataset mappings in data_load.py 
  > New data api will no long need this feature
- [ ] #186 Enable the model to train on train dataset only or (train + validation) datasets
  > Cannot remember what is this.
- [ ] #205 detach dataloader from train_engine
  > Already  detached the load_dataset() function, need to be check once all the recommenders are finished.
- [ ] #248 Check all the datasets ![progress](https://progress-bar.dev/0)
- [ ] #250  Benchmarking![progress](https://progress-bar.dev/0)
- [ ] #251 Code refactoring
- [ ] #253 Idle thread under Monitor
- [ ] #254 create a docker image for the framework 
- [x] #259 Add amazon datasets
- [ ] #279 update ray with the latest version
- [x] #289 figures in the documentation page cannot be shown normally
- [ ] #290 Add documentation of recommender new API 
- [ ] #291 Add documentation of experiment
- [x] #292 New API for dataset process
  > https://beta-recsys.readthedocs.io/en/latest/notes/datasets.html
- [ ] #300 regenerate all the data split
- [x] #303 add changing logs to community repository
- [ ] #304 Add the documentation of evaluation with negative sampling
- [ ] #305 Add the documentation for the new experiment feature (reduplicated)
- [ ] #311 upload the project to conda 


### Documentation

- Readme: Updated
- [Installation](https://beta-recsys.readthedocs.io/en/develop/notes/installation.html): 
  - pip and conda. 
  - Additional information for development?
- [Introduction](https://beta-recsys.readthedocs.io/en/develop/notes/introduction.html)
  - New dataset api
  - New recommendation API
  - New experiment feature
- [Overview](https://beta-recsys.readthedocs.io/en/develop/notes/framework.html): 
  - Add more feature?

### Models

The following is a list of recommender models currently available in the repository, or to be implemented soon.

#### General Models

  - [x] GMF: Generalized Matrix Factorization, in [Neural Collaborative Filtering](https://arxiv.org/abs/1708.05031), WWW 2017
  - [x] MLP: Multi-Layer Perceptron, in [Neural Collaborative Filtering](https://arxiv.org/abs/1708.05031), WWW 2017
  - [x] NCF: [Neural Collaborative Filtering](https://arxiv.org/abs/1708.05031),  WWW 2017
  - [x] CMN: [Collaborative memory network for recommendation systems](https://dl.acm.org/doi/abs/10.1145/3209978.3209991),  SIGIR 2018
  - [ ] VAECF: [Variational autoencoders for collaborative filtering](https://dl.acm.org/doi/abs/10.1145/3178876.3186150), WWW 2018
  - [x] NGCF: [Neural graph collaborative filtering](https://dl.acm.org/doi/abs/10.1145/3331184.3331267), SIGIR 2019
  - [x] LightGCN: [**LightGCN**: Simplifying and Powering Graph Convolution Network for Recommendation](https://arxiv.org/abs/2002.02126), SIGIR 2020
  - [x] MF: [Neural Collaborative Filtering vs. Matrix Factorization Revisited](https://arxiv.org/abs/2005.09683), arXiv’ 2020

#### Sequential Models
  - [x] NARM: [Neural Attentive Session-based Recommendation](https://arxiv.org/abs/1711.04725), CIKM 2017
  - [ ] GRU4Rec: [Session-based recommendations with recurrent neural networks](https://arxiv.org/abs/1511.06939), ICLR 2016
  - [ ] SasRec:[**Self**-**attentive sequential recommendation**](https://ieeexplore.ieee.org/abstract/document/8594844/?casa_token=RINDZUuHnwoAAAAA:XBjSlh6-KqBjgCY1AWwgXyZqHtT_8zAPBMKjLIUJMlf6Ex9j55gG2UAsrRtG10roMUd6-_w3Jw). ICDM 2018
  - [ ] BERT4Rec: [BERT4Rec: **Sequential recommendation** with **bidirectional encoder representations** from **transformer**](https://dl.acm.org/doi/abs/10.1145/3357384.3357895), CIKM 2019
  - [ ] TiSASRec: [Time Interval Aware Self-Attention for **Sequential Recommendation**](https://dl.acm.org/doi/abs/10.1145/3336191.3371786). WWW 2020

#### Recommendation Models with Auxiliary Information
  ##### Baskets/Sessions
  - [x] Triple2vec: [Representing and recommending shopping baskets with complementarity, compatibility and loyalty](https://dl.acm.org/doi/abs/10.1145/3269206.3271786), CIKM 2018
  - [x] VBCAR: [Variational Bayesian Context-aware Representation for Grocery Recommendation](https://arxiv.org/abs/1909.07705),  arXiv’ 2019
  ##### Knowledge Graph
  - [ ] KGAT: [Kgat: Knowledge graph attention network for recommendation](https://dl.acm.org/doi/abs/10.1145/3292500.3330989). SIGKDD 2019
  ##### Social




### About [RecBole](https://github.com/RUCAIBox/RecBole)
- More Models and More datasets

  ![](https://tva1.sinaimg.cn/large/0081Kckwgy1gkgw9t1o98j30u010tdnr.jpg)

- GPU evaluation

  - perform the full ranking over the entire item set 

  ![](https://tva1.sinaimg.cn/large/0081Kckwgy1gkgw3o1wu5j31ms0r2n61.jpg)

### Dicsussion

### TODOs

- [ ] Merge the current develop branch to the master branch and release another version of Beta-RecSys.(Zaiqiao)
- [ ] Update models with new interface. (LightGCN and NCF) (**Siwei**)
- [ ] Check models and benchmarking. (Shuqi)
- [ ] Docker image for the project and maintain it. (**Bingchang**)
- [ ] Add pip description (**Xi**)
- [ ] Add our project to conda (**Xi**)
- [ ] Try all available models and check ambigous descriptions 
- [ ] Update Ray along with the issue page (**Zaiqiao, Siwei**)
- [ ] Add requirement install readme.
- [ ] Link [model](https://beta-recsys.readthedocs.io/en/develop/notes/models.html) to [reference](https://beta-recsys.readthedocs.io/en/develop/modules/models.html#beta_rec.models.cmn.CollaborativeMemoryNetwork) 
- [ ] Add a new [model](https://arxiv.org/pdf/2006.15516.pdf), Low-pass Collaborative Filter (LCF).(This year ICML)

