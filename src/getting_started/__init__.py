import numpy as np
import pandas as pd

# object-creation

# 用值列表生成 Series (opens new window)时，Pandas 默认自动生成整数索引：
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

# 用含日期时间索引与标签的 NumPy 数组生成 DataFrame (opens new window)：
dates = pd.date_range('20211212', periods=6)
print(dates)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)

# 用 Series 字典对象生成 DataFrame:
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
print(df2)

# DataFrame 的列有不同数据类型 (opens new window)。
print(df2.dtypes)

# viewing-data
# 查看 DataFrame 头部和尾部数据：
print(df.head)
print(df.tail(3))
# 显示索引与列名：
print(df.index)
print(df.columns)
# DataFrame.to_numpy() (opens new window)输出底层数据的 NumPy 对象。
# DataFrame.to_numpy() (opens new window)的输出不包含行索引和列标签。

# df 这个 DataFrame (opens new window)里的值都是浮点数，DataFrame.to_numpy() (opens new window)的操作会很快，而且不复制数据。
print(df.to_numpy())
# df2 这个 DataFrame (opens new window)包含了多种类型，DataFrame.to_numpy() (opens new window)操作就会耗费较多资源。
print(df2.to_numpy())
# describe() (opens new window)可以快速查看数据的统计摘要：
print(df.describe())
# 转置数据：
print(df.T)
# 按轴排序：
print(df.sort_index(axis=1, ascending=False))
# 按值排序：
print(df.sort_values(by='B'))
