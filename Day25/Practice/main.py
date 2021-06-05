import csv
import pandas as pd

# with open("weather_data.csv",mode="r") as raw_data:
#     data = csv.reader(raw_data)
#     temp=[]
#     for i in data:
#         if i[1]=="temp":
#             continue
#         temp.append(int(i[1]))
# print(temp)

data=pd.read_csv("weather_data.csv")
print(data)