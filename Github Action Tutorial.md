# Github Action Tutorial

**Author: Yucheng Liang**

**Last Update Time: 2020-03-17**

This tutorial is used to help all team members to get to know how to set up a github action, as well as understand our CI workflow.

## Get Started

Let's use an example to get started.

```yaml
name: Python application

on: [push]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v1
    - name: Set up Python 3.6
      uses: actions/setup-python@v1
      with:
        python-version: 3.6
    - name: should it be skipped?
      run: |
        # Get Commit Message
        last_commit_log=$(git log -1 --pretty=format:"%s")
        echo "last commit log: $last_commit_log"
        feat="feat:[[:space:]].*$"
        fix="fix:[[:space:]].*$"
        test="test:[[:space:]].*$"
        chore="chore:[[:space:]].*$"
        merge="Merge pull request.*$"
        doc="doc:[[:space:]].*$"
        commit_msg_reg=(
          $feat
          $fix
          $test
          $chore
          $merge
          $doc
        )
        
        check_commit_msg() {
          for regex in ${commit_msg_reg[*]}
            do
              echo "last commit log: $last_commit_log"
              echo "$regex"
              if [[ lastcommitlog= regex ]]; then
                printf "do match \n\n  lastcommitlogregex"
                return 0
              else
                printf "does not match lastcommitlogregex"
              fi
            done
          return 1
        }
        
        check_commit_msg
        if [[ $? == 1 ]]
        then
          printf "\n\n $last_commit_log  commit message failed match"
          exit 1
        fi
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Lint with flake8
      run: |
        pip install flake8
        # stop the build if there are Python syntax errors or undefined names
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
    - name: Test with pytest
      run: |
        pip install pytest
        python -m pytest --cov-report=xml --cov=./tests/
        
    - name: Codecov
      uses: codecov/codecov-action@v1.0.5
      with:
        token: ${{secrets.CODECOV_TOKEN}}
        # Path to coverage file to upload
        file: ./coverage.xml
```

+ `name`: This is the name for this CI workflow
+ `on`: indicates which action event will trigger this workflow. Also it can specify the branch if needed.
+ `jobs`: defines the workflow
  + `runs-on`: the platform of CI
  + `steps`: each step of CI
  + `-uses`: use some scripts that provided by GitHub
  + `-name`: the name of a step
  + `with:`: attach some parameters in this step
  + `run`: can write bash script that is supposed to run

## Explanation

In this example, a push event should trigger this workflow. And the CI runs on ubuntu platform, with following steps:

1. Use `actions/checkout@v1` to get the latest code in the branch.
2. Set up Python environment
3. Check commit message format
4. Install dependencies of this project
5. Use flake8 to check code
6. Run pytest
7. Upload coverage report to Codecov.