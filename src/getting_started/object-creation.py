import numpy as np
import pandas as pd

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
