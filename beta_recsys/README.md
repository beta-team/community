# Beta-recsys community resources

## Community meeting

- Meeting time: Saturday (1:30 – 2:30pm **[UTC +0](https://24timezones.com/time-zone/utc#gref)**/9:30 – 10:30pm **[UTC +8](https://24timezones.com/time-zone/utc+8#gref)**), (start from 7 November 2020)**⋅** <a target="_blank" href="https://calendar.google.com/event?action=TEMPLATE&amp;tmeid=XzYwcTMwYzFnNjBvMzBlMWk2MG80YWMxZzYwcmo4Z3BsODhyajJjMWg4NHMzNGg5ZzYwczMwYzFnNjBvMzBjMWc2OTIzY2dxMjg4cDQ0Z2hnODUxazhkaGc2NG8zMGMxZzYwbzMwYzFnNjBvMzBjMWc2MG8zMmMxZzYwbzMwYzFnOGwyMzhkaHA2MHFqY2UyNDg1MTM0ZzlrNnQwamFkMWw2OTMzaWNobThjcjRhZTluOGwxZ18yMDIwMTEwN1QxNDAwMDBaIHphaXFpYW8ubWVuZ0Bt&amp;tmsrc=zaiqiao.meng%40gmail.com&amp;scp=ALL"><img border="0" src="https://www.google.com/calendar/images/ext/gc_button1_en-GB.gif"></a>
- Meeting minutes: [notes](https://github.com/beta-team/community/tree/master/beta_recsys/meeting%20minutes)
- Meeting recordings: [recording links]: Can be found in each [meeting note](https://github.com/beta-team/community/tree/master/beta_recsys/meeting%20minutes) (since Nov.7, 2020).

## Discussion channels

- Slack: [join](https://join.slack.com/t/beta-recsys/shared_invite/zt-iwmlfb0g-yxeyzb0U9pZfFN~A4mrKpA)
- Mailing list: TBC

## Version release

- Version x.x.n update frequency: Four weeks
- Version x.n.x update frequency: Eight weeks
- Version n.x.x update frequency: TBC

## Contribution guidelines

### Did you write a patch that fixes a bug?

Open a new GitHub pull request with the patch.

Ensure the PR description clearly describes the problem and solution. Include the relevant issue number if applicable.

### Do you intend to add a new feature or change an existing one?

Suggest your change in the [Beta-recsys mailing list](beta_recsys) or [slack](https://join.slack.com/t/beta-recsys/shared_invite/zt-iwmlfb0g-yxeyzb0U9pZfFN~A4mrKpA), where you can collect feedbacks about the change. Then open an issue on GitHub, assign it to youself or related members,  and start writing code.

Before submitting, please read the [Contributing to Beta-recsys guide](https://beta-recsys.readthedocs.io/en/latest/contribute/standardization-of-code-format-and-documentation.html) to know more about coding conventions and benchmarks.

### Code of Conduct

We use the automatic style formatter Black. See the installation guide for VSCode and PyCharm. Black supersets the well-known style guide PEP 8, defined by Guido van Rossum and collaborators. PEP 8 defines everything from naming conventions, indentation guidelines, block vs inline comments, how to use trailing commas and so on.

We use Google style for formatting the docstrings.

Black formatting on Python files.
Black formatting on Notebooks.
Docstring with Google style.
Isort to sort imports alphabetically, and automatically separated into sections.
If you are using Pycharm, it will be convenient to deploy black and isort commands as External Tools.

**Use the following args to make it compatible with black. **

isort --multi-line=3 --trailing-comma --force-grid-wrap=0 --use-parentheses --line-width=88 [ file.py ]
Or directly apply the default config file in our project root folder.

```shell
[settings]
line_length=88
indent='    '
multi_line_output=3
include_trailing_comma=true
use_parentheses=true
force_grid_wrap=0
```

The following examples are part of demo.py. For complete usages, please refer to demo.py.

## Git Setup

### Configure remotes

When a repository is cloned, it has a default remote called `origin` that points to your fork on GitHub, not the original repository it was forked from. To keep track of the original repository, you should add another remote named `upstream`:<br />

1. Get the path where you have your git repository on your machine. Go to that path in Terminal using cd. Alternatively, Right click on project in Github Desktop and hit ‘Open in Terminal’.<br />
2. Run `git remote -v`  to check the status you should see something like the following:<br />

> origin    https://github.com/YOUR_USERNAME/beta-recsys.git (fetch)<br />
> origin    https://github.com/YOUR_USERNAME/beta-recsys.git (push)<br />

3. Set the `upstream`:<br />
   `git remote add upstream https://github.com/beta-team/beta-recsys.git`<br />
4. Run `git remote -v`  again to check the status, you should see something like the following:<br />

> origin    https://github.com/YOUR_USERNAME/beta-recsys.git (fetch)<br />
> origin    https://github.com/YOUR_USERNAME/beta-recsys.git (push)<br />
> upstream https://github.com/beta-team/beta-recsys.git  (fetch)<br />
> upstream  https://github.com/beta-team/beta-recsys.git (push)<br />

5. To update your local copy with remote changes, run the following:<br />
   `git fetch upstream master`<br />
    `git rebase  upstream/master`<br />
   This will give you an exact copy of the current remote, make sure you don't have any local changes.<br />
6. Project set-up is complete.


### Contributing and developing a feature

1. Make sure you are in the develop branch `git checkout develop`.<br />
2. Sync your copy with the upstream.<br />
3. Create a new branch with a meaningful name `git checkout -b branch_name`.<br />
4. Add the files you changed `git add file_name` (avoid using `git add .`).<br />
5. Commit your changes `git commit -m "feat: Message briefly explaining the feature"`.<br />
6. Keep one commit per issue. If you forgot to add changes, you can edit the previous commit `git commit --amend`.<br />
7. Push to your repo `git push origin branch-name`.<br />
8. Go into [the Github repo](https://github.com/beta-team/beta-recsys.git) and create a pull request explaining your changes.<br />
9. If you are requested to make changes, edit your commit using `git commit --amend`, push again and the pull request will edit automatically.<br />
10. If you have more than one commit try squashing them into single commit by following command:<br />
     `git rebase -i origin/master~n master`(having n number of commits).<br />
11. Once you've run a git rebase -i command, text editor will open with a file that lists all the commits in current branch, and in front of each commit is the word "pick". For every line except the first, replace the word "pick" with the word "squash".<br />
12. Save and close the file, and a moment later a new file should pop up in  editor, combining all the commit messages of all the commits. Reword this commit message into meaningful one briefly explaining all the features, and then save and close that file as well. This commit message will be the commit message for the one, big commit that you are squashing all of your larger commits into. Once you've saved and closed that file, your commits of current branch have been squashed together.<br />
13. Force push to update your pull request with command `git push origin branchname --force`.<br/>


#### Commit guidelines

- Make sure that you only have one commit for each PR. To merge commits, please refer to [link](https://stackoverflow.com/questions/5189560/squash-my-last-x-commits-together-using-git).

- The commit message should strictly be start with the following six strings, otherwise, the PR cannot be passed by our CI.

  - | String                  | Issue                                                        |
    | ----------------------- | ------------------------------------------------------------ |
    | "feat:[[:space:]].*$"   | New feature                                                  |
    | "fix:[[:space:]].*$"    | Fixing a bug                                                 |
    | "test:[[:space:]].*$"   | Adding test codes                                            |
    | "chore:[[:space:]].*$"  | Others  chore operation such as rearranging folders or renaming files. |
    | "Merge pull request.*$" | Automatic merge                                              |
    | "doc:[[:space:]].*$"    | Improving documentation                                      |

## Active members (based on [Github contributors](https://github.com/beta-team/beta-recsys/graphs/contributors))

- Zaiqiao Meng, University of Cambridge, United Kingdom, zaiqiao.meng@gmail.com
- Siwei Liu, University of Glasgow, United Kingdom, s.liu.4@research.gla.ac.uk
- Xi Wang, University of Glasgow, United Kingdom, x.wang.6@research.gla.ac.uk
- Yucheng Liang, Sun Yat-sen Univeristy, China, liangych28@mail2.sysu.edu.cn
- Guangtao Zeng, Sun Yat-sen Univeristy, China, zengguangtao98@gmail.com
- Qiang Zhang, University College, London, qiang.zhang.16@ucl.ac.uk
- Junhua Liang, Sun Yat-sen Univeristy, China, liangjh45@mail2.sysu.edu.cn


