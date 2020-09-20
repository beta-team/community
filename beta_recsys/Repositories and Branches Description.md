# Repository  and Branches Description

> By Zaiqiao	Email: Zaiqiao.Meng@gmail.com
------
## 1. Repositories 

### [beta-recsys](https://github.com/beta-team/beta-recsys)

Main code repository.

 We are going to use the [**Git Flow**](https://www.youtube.com/watch?v=w2r0oLFtXAw)  as our branching workflows.

- `master` — this branch contains production code. All development code is merged into `master` in sometime. (For release new version)
- `develop` — this branch contains pre-production code. When the features are finished then they are merged into develop. (Always fork this branches for developing)
- During the development cycle, a variety of supporting branches are used:
  - `feature-*` — feature branches are used to develop new features for the upcoming releases. May branch off from `develop` and must merge into `develop`.
  - `hotfix-*` — hotfix branches are necessary to act immediately upon an undesired status of `master`. May branch off from `master` and must merge into `master` and`develop`.
  - `release-*` — release branches support preparation of a new production release. They allow many minor bug to be fixed and preparation of meta-data for a release. May branch off from `develop` and must merge into `master` and`develop`. (In this branch, we will use for generating docs, and pull request to **master**)

### [![Image result for github flow](https://tva1.sinaimg.cn/large/00831rSTgy1gcyx5guo6aj30zk0k0dgr.jpg)community](https://github.com/beta-team/community) (only master branch)

Stores documents used by the Beta developer community

### [docs](https://github.com/beta-team/docs) (only master branch, but all the review and check work will be done in the `release-*` branch of the code repository)

**Beta-recsys** documentation





How to Forks and Pull Requests, watch [here](https://www.youtube.com/watch?v=_NrSWLQsDL4)