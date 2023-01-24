import pandas as pd
from pandas_profiling import ProfileReport
df=pd.read_csv(r"C:\Users\UMAPRIYA\Desktop\Project ineuron\Amazon Sales Analysis\New folder\Amazon Cleaned Sales Data.csv")
print(df.head())

profile = ProfileReport(df,title='Amazon Cleaned Sales Data')
profile.to_file('Amazon Cleaned Sales Datas.html')
