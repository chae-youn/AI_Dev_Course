import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# dataset: https://www.kaggle.com/datasets/jawadawan/global-warming-trends-1961-2022
long_df = pd.read_csv('./long.csv')
wide_df = pd.read_csv('./wide.csv')

## 1961년과 비교하여 2022년에 가장 표면 온도가 많이 증가한 나라는 어디일까?
wide_df['Change'] = wide_df['F2022'] - wide_df['F1961']
wide_df = wide_df.sort_values('Change',ascending=False)
wide_df.head(1) # New Caledonia

# 전처리
long_df['Year'] = long_df['Year'].apply(lambda x:x.replace('F','')).astype(int)

## 가설 - 전세계의 평균 표면 온도는 상승해왔을 것이다.
## 표면 온도가 가장 많이 상승한 뉴칼레도니아와 전세계 표면 온도 평균에 비해 한국은 어느 정도 상승했을까?

# 뉴칼레도니아, 한국, 전세계 평균의 온도 변화 추이 시각화
NC_df = long_df.loc[long_df['Country'] == 'New Caledonia']
KR_df = long_df.loc[long_df['Country'] == 'Korea, Rep. of']

plt.figure(figsize = (10, 4))
plt.plot(NC_df.groupby('Year')['Temperature'].mean(), label='New Caledonia', color='#f2a900')
plt.plot(KR_df.groupby('Year')['Temperature'].mean(), label='Korea', color='#3c3c3d')
plt.plot(long_df.groupby('Year')['Temperature'].mean(), label='Global mean', color='#228b22')

plt.xlabel("Year")
plt.ylabel("Surface Temperature")

plt.legend()
plt.title("Surface Temperature Fluctuation Trend")
plt.show()

# 전세계적으로 표면온도가 상승해왔음을 알 수 있었으며 뉴칼레도니아에서의 표면온도가 가장 많이 상승한 것을 확인했다.
# 한국의 경우 표면온도의 변동 폭이 큰 편이었으며 2010년 이후 급격히 상승하였다.
# 뉴칼레도니아와 한국 모두 2022년 세계 평균보다 표면 온도가 높았다.
