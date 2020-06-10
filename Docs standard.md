# Documentation for Code Format Standard 代码格式规范

**Author:** Junhua Liang, Yucheng Liang

**Last Updated:** 2020-06-10

## Goal

As we expect to become a efficient and useful generalized framework regarding recommendation system for a wide range of researchers, our code readability is extremly critical. We hope building a powerful framework with concise codes, which allows others to understand our code in an easy way even contribute to our project.

In addition, we try to maintain an informative documentation, which requires a formatted comment style in codes. Stacking everything into a documentation is quite easy, but a clear, formatted documentation will be more helpful, and that's what we want to achieve.

Consequently, in this documentation, some rules are listed in order to keep developers writting codes properly. And we hope every contributor is supposed to observe these standards.

------

## Overview

In general, all our codes follow the [Google Python Style Guide](http://google.github.io/styleguide/pyguide.html), and we use PEP8 to check all the code which is ready to merge into master in Github Action. Your pull request will not be approved before all your codes are formatted according to the guide.

### Method

### Class

------

## Special Cases

### 1. Indention 缩进问题

There should be **no space** between the first letter and the `"""` in the first line of comment. And the first character should **use uppercase**.

注释应该要顶着`"""`来写。同时首字母需要大写。

| 代码编写格式                          | 文档显示                              |
| ------------------------------------- | ------------------------------------- |
| ![1591513795011](./img/docs/img1.png) | ![1591514054954](./img/docs/img2.png) |
| ![1591513943295](./img/docs/img3.png) | ![1591514086911](./img/docs/img4.png) |

### 2. 注释规范

正确例子：

| 代码编写                              | 显示                                  |
| ------------------------------------- | ------------------------------------- |
| ![1591516041880](./img/docs/img5.png) | ![1591516056191](./img/docs/img6.png) |

错误例子：

| 代码编写                              | 显示                                  |
| ------------------------------------- | ------------------------------------- |
| ![1591516682450](./img/docs/img7.png) | ![1591516692503](./img/docs/img8.png) |

### 3. 注释换行问题

| 代码编写                              | 显示                                   |
| ------------------------------------- | -------------------------------------- |
| ![1591516116811](./img/docs/img9.png) | ![1591515840206](./img/docs/img10.png) |

### 4. 小问题

| 代码                                   | 显示                                   |
| -------------------------------------- | -------------------------------------- |
| ![1591516496649](./img/docs/img11.png) | ![1591516510170](./img/docs/img12.png) |

### 5. 跳转到某个类的注释写法

![1591520192198](./img/docs/img13.png)

Return type的指定:

![1591520240907](./img/docs/img14.png)

![1591520255156](./img/docs/img15.png)

![1591520271277](./img/docs/img16.png)

### 6. 添加数学公式的方法

![1591520769559](./img/docs/img17.png)

### 7. 添加例子说明

| 代码                                   | 显示结果                               |
| -------------------------------------- | -------------------------------------- |
| ![1591520811620](./img/docs/img18.png) | ![1591520829207](./img/docs/img19.png) |

### 8. 建议

![1591522096569](./img/docs/img20.png)
