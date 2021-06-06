import csv
import pandas as pd
import math

# with open("weather_data.csv",mode="r") as raw_data:
#     data = csv.reader(raw_data)
#     temp=[]
#     for i in data:
#         if i[1]=="temp":
#             continue
#         temp.append(int(i[1]))
# print(temp)

# data=pd.read_csv("weather_data.csv")
# u=(data[data["temp"]==data.temp.max()])
# print(u["temp"])
#
#
# data_dic={
#     "std":{0:"a",1:"b"},
#     "boy":{0:"yea",1:"noo"}
# }
#
# d=pd.DataFrame(data_dic)
# print(d)


data=pd.read_csv("Squirrel_Data.csv")

blk=(len(data[data["Primary Fur Color"]=="Black"]))

cin=(len(data[data["Primary Fur Color"]=="Cinnamon"]))

grey=(len(data[data["Primary Fur Color"]=="Gray"]))


data_dict={
    "color":{0:"Cinnamon",1:"Black",2:"Gray"},
    "count":{0:cin,1:blk,2:grey}
}
our_data=pd.DataFrame(data_dict)
print(our_data)
