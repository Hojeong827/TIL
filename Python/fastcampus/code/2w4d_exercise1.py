#딕셔너리 데이터를 데이터 프레임에 하나씩 추가하기
import numpy as np
import pandas as pd

money_df = pd.DataFrame(columns=["ID", "Money"])
# np.random.randint(1,9)
for _ in range(15):
    money_df.loc[len(money_df)]={
        "ID": np.random.randint(1,9),
        "Money": np.random.randint(1,21)*1000,
    }

# 컬럼데이터에서 Unique 값 확인
ids = money_df["ID"].unique()
ids.sort()
print(ids)
print(money_df)
                                 