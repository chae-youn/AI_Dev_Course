## Mission 1. Netflix and Code
import numpy as np
import pandas as pd

data = pd.read_csv('/content/netflix_titles.csv')

## Mandatory Part
# 한국 작품은 총 얼마나 있는가?
data[data.country == 'South Korea'].shape[0]

## Bonus Part
# 가장 많은 작품이 올라간 국가는 어디이고, 얼마나 많은 작품이 있는가?

# country에 ","가 있는 행이 여러 국가를 포함한 행이므로 제거
data_single = data[data['country'].str.contains(',', na = False)==False]

# groupby하기 위해 null 없는 행인지 확인
data_single['show_id'].info()

# 국가로 groupby하고, 영화 수 상위 20개 확인
data_country = data_single['show_id'].groupby(by = data_single['country']).count()
data_country.sort_values(ascending = False).head(1)


## Mission 2: 가즈아!
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('/content/BitCoin.csv')

## Mandatory Part
# 2016.6~2017.6 기간의 5-MA 비트코인 가격 그래프 그리기

data = data.sort_values(by = 'Date')
data = data[('2016-05-31' < data['Date']) & (data['Date'] < '2017-07-01')]
sma5 = data['Open'].rolling(window=5).mean()

# plot
plt.figure(figsize = (10, 4))  
plt.plot(data['Date'],sma5, color = '#f2a900')                      
plt.xlabel("Date")
plt.ylabel("5-MA")
plt.xticks(rotation=45, ticks=[i for i in range(1,377,29)], labels=['2016-06', '2016-07', '2016-08', '2016-09', '2016-10','2016-11', 
                                                                    '2016-12', '2017-01', '2017-02', '2017-03', '2017-04', '2017-05', '2017-06'])
plt.title("5-MA of Bitcoin Price")
plt.show()

## Bonus part
# 이더리움과 비트코인 그래프 그리기

data2 = pd.read_csv('/content/ETH_day.csv')
data2 = data2.sort_values(by = 'Date')
data2 = data2[('2016-05-31' < data2['Date']) & (data2['Date'] < '2017-07-01')]

sma5_eth = data2['Open'].rolling(window=5).mean()

# plot
plt.figure(figsize = (10, 4))
plt.plot(data['Date'], sma5, label='Bitcoin', color='#f2a900')
plt.plot(data2['Date'], sma5_eth, label='Ethereum', color='#3c3c3d')

plt.xlabel("Date")
plt.ylabel("5-MA")
plt.xticks(rotation=45, ticks=[i for i in range(1,377,29)], labels=['2016-06', '2016-07', '2016-08', '2016-09', '2016-10','2016-11',
                                                                    '2016-12', '2017-01', '2017-02', '2017-03', '2017-04', '2017-05', '2017-06'])
plt.legend()
plt.title("5-MA of Bitcoin and Ethereum Price")
plt.show()
