# 主要类
---

***
## DatasetInfo
---
+ 文档数据集，包括其名称，版本和功能。


## Dataset
---
+ 基类datasets.Dataset实现由Apache Arrow表支持的数据集
+ http://arrow.apache.org/
+ https://github.com/apache/arrow
+ Apache Arrow为平面和分层数据定义了一种与语言无关的列式存储格式，该格式组织为在CPU和GPU等现代硬件上进行高效的分析操作而组织。Arrow存储器格式还支持零拷贝读取，以实现闪电般快速的数据访问，而无需序列化开销。

## DatasetDict
---
+ 以拆分名称作为键（例如“ train”，“ test”）和datasets.Dataset对象作为值的字典。

## Features
---

## MetricInfo
---
+ 有关指标的信息。

+ MetricInfo记录度量标准，包括其名称，版本和功能。有关完整列表，请参见构造函数的参数和属性。

+ 注意：并非所有字段在构造上都是已知的，以后可能会更新。

## Metric
---
+ 基类Metric实现由一个或几个支持的Metric datasets.Dataset。
+ 指标是所有指标的基类和通用API。

## Filesystems
---
+ 像访问文件系统一样访问S3。
+ datasets.filesystems.S3FileSystem是s3fs.S3FileSystem的子类
+ https://filesystem-spec.readthedocs.io/en/latest/?badge=latest

# 数据集构建过程中使用的类
---

***
+ datasets.DatasetBuilder
 - 所有数据集的抽象基类
+ datasets.GeneratorBasedBuilder
 - 具有基于字典生成器的数据生成的数据集的基类

# 表类
---

***
+ 每个datasets.Dataset对象都有一个pyarrow Table支持。可以从磁盘（映射到内存）或内存中加载表。有几种表类型可用，它们都继承自datasets.table.Table。
+ datasets.table.Table
  
# 记录方式
---

***
+ datasets.logging
