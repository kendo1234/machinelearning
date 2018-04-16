import pandas as pd
import quandl

#df = data frame
df = quandl.get("WIKI/GOOGL", authtoken="NyE5gCTW3yxWWVeHfC7y")

df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]

#Create high low percentage equal to average high minus average close, divided by average close and times 100
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
#Percentage change equal to adusted closed minus adjusted open divided by open and times 100
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
#New data frame consisting of 'features' we care about
df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

print(df.head())
