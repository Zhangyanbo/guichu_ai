# AI鬼畜大师

## 核心功能

### 一、典故搜索

首先导入模型和嵌入：
```python
import guichu_ai
import numpy as np
import pandas as pd


with open('openai.key', 'r') as f:
    key = f.read().strip()

data = pd.read_csv('./data/master_ma.csv')
embs = np.load('./data/master_ma_embs.npy') # 如果没有，则会使用OpenAI的API自动计算

master_ma = guichu_ai.GuichuMaster(data, key, embedding=embs)
```

然后就可以根据语义搜索名言：

```python
master_ma.search(query='愤怒，生气', top_k=5)

'''
Output:
    start_time  end_time content  \
37      38.075    40.539    他不服气   
75     100.043   101.006       哎   
43      47.054    48.005   这是化劲儿   
90     118.013   118.079  对不起对不起   
83     110.015   110.057     捂着眼   

                                          source  similarity  
37  https://www.bilibili.com/video/BV1584y1N7cR/    0.845329  
75  https://www.bilibili.com/video/BV1584y1N7cR/    0.823142  
43  https://www.bilibili.com/video/BV1584y1N7cR/    0.821372  
90  https://www.bilibili.com/video/BV1584y1N7cR/    0.819167  
83  https://www.bilibili.com/video/BV1584y1N7cR/    0.818789  
'''
```

### 二、自动接句

使用数据库中的语句自动接下句

> 这个功能目前不是很完善。原理是调用GPT-3的句子补全，然后用补全的句子搜索名言。所以存在一定的随机性，同时速度会比较慢。

```python
master_ma.search_next(query='你们啊，', top_k=5)

'''
Output:
    start_time  end_time content  \
55      68.003    69.015   防出去了啊   
50      60.022    61.024     很快啊   
75     100.043   101.006       哎   
48      57.001    58.066   我说可以诶   
53      66.032    67.016   一个左刺拳   

                                          source  similarity  
55  https://www.bilibili.com/video/BV1584y1N7cR/    0.817576  
50  https://www.bilibili.com/video/BV1584y1N7cR/    0.812839  
75  https://www.bilibili.com/video/BV1584y1N7cR/    0.810418  
48  https://www.bilibili.com/video/BV1584y1N7cR/    0.810311  
53  https://www.bilibili.com/video/BV1584y1N7cR/    0.808796  
'''
```