# Coding Guidelines


## Python Coding and Docstrings Style

We use the automatic style formatter [Black](https://github.com/ambv/black). See the installation guide for [VSCode](https://github.com/ambv/black#visual-studio-code) and [PyCharm](https://github.com/ambv/black#pycharm). Black supersets the well-known style guide [PEP 8](https://www.python.org/dev/peps/pep-0008/), defined by Guido van Rossum and collaborators. PEP 8 defines everything from naming conventions, indentation guidelines, block vs inline comments, how to use trailing commas and so on.

We use [Google style](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) for formatting the docstrings.

- [Black formatting on Python files](https://github.com/ambv/black#the-black-code-style).
- [Black formatting on Notebooks](https://github.com/csurfer/blackcellmagic).
- [Docstring with Google style](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).
- [Isort to sort imports alphabetically, and automatically separated into sections.](https://pypi.org/project/isort/)

***** If you are using Pycharm, it will be convenient to deploy **black** and **isort** commands as [External Tools](https://www.jetbrains.com/help/pycharm/configuring-third-party-tools.html).
***** Use the following args to make it [compatible](https://github.com/timothycrosley/isort/issues/694#issuecomment-564261886) with black. 
```shell
isort --multi-line=3 --trailing-comma --force-grid-wrap=0 --use-parentheses --line-width=88 [ file.py ]
``` 



