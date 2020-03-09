
# -*- coding: utf-8 -*-

import MySQLdb
import numpy as np
import pandas as pd
from pandas import DataFrame

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'mxonline3',
#         'USER': 'root',
#         'PASSWORD': 'edit',
#         'HOST':'127.0.0.1'
#
#     }
# }



db = MySQLdb.connect(db= 'mxonline3',user= 'root',password= 'edit',host='127.0.0.1',charset='utf8')

# sql_s = """SELECT name, f1, f2, f3 FROM swap_radas;"""
# columns_s = ['name', 'f1', 'f2', 'f3']
# index_col_s  = "f1"
# df = pd.read_sql(sql_s, db, index_col = index_col_s, columns = columns_s)
# # print('-----', df8, df8.dtypes)

sql_s = "select typen, count(*) f1, sum(order_m) as f2, sum(status) f3, max(order_m) f4, avg(order_m) f5 from myechart_ewsales group by typen"
columns_s = ["typen", "f1", "f2", "f3", "f4", "f5"]
# index_col_s = "f1"
df = pd.read_sql(sql_s, db, columns=columns_s)

df = df.sort_values(by='f1', ascending=False)
# f1 数量, f2 金额, f2  成功率, f4  最大金额, F5   平均金额

df1 = list(df['typen'])
print(df1)
df2 = df[['f1', 'f2', 'f3', 'f4', 'f5']]

print(df1[1])
print(df2)

# print(df1[0:1])
# print(df1.ix[[0]].values[0][0])
print(df1[1], df2[0:1].values.tolist())
print(df1[2], df2[1:2].values.tolist())

# cursor = db.cursor()
# # cursor.execute("select name, f1, f2 from swap_radas  order by f2 desc limit 0,5")
#
# # query_sql = "select count(*) 数量, sum(order_m) as 金额, sum(status) 成功率, max(order_m) 最大金额, avg(order_m) 平均金额, typen from myechart_ewsales group by typen"
#
# query_sql = "select typen, count(*) f1, sum(order_m) as f2, sum(status) f3, max(order_m) f4, avg(order_m) f5 from myechart_ewsales group by typen"
#
#
#
# cursor.execute(query_sql)
# data = cursor.fetchall()
#
# data = list(data)
# data = [list(i) for i in data]
#
# df = DataFrame(data, columns=["typen", "f1", "f2", "f3", "f4","f5"])
#
# df[["f1", "f2", "f3", "f4", "f5"]] = df[["f1", "f2", "f3", "f4", "f5"]].astype(float)
#
# df5 = df.copy()
# df = df.sort_values(by='f1', ascending=False)
# print(df)
#
# df1 = df['typen']
# df2 = df[['f1', 'f2', 'f3', 'f4', 'f5']]
#
# print(df1)
# print(df2)
#
# print(df1[0:1].values, df2[0:1].values.tolist())
# print(df1[1:2], df2[1:2].values.tolist())
# print(df1[2:3], df2[2:3].values.tolist())
# print(df1[3:4], df2[3:4].values.tolist())
# print(df1[4:5], df2[4:5].values.tolist())
#
# # 加一列 平均每单金额
# # df.m_per_order = df.f2/df.f1
#
# # df = DataFrame(data)
# #
# df[["f1", "f2", "f3", "f4","f5"]] = df[["f1", "f2", "f3", "f4","f5"]].astype(float)
# # print(df)
# # print(df.dtypes)
#
# #
# print(df.index)
#
# # 转置
# print(df.T)
#
#
# # # # 读取列
# print(df['f2'])
# print(df.typen, df.m_per_order)

# df2 = df[['f1','f2']]
# print(df2)
#
# 读取行
# print(df.loc[df.typen == '二供'])

# print(df.loc[df.f1 > 5 ] )

# 读取物理行，列
# print(df[:1] )

# 3行4列
# print(df.ix[:3, :'f4'])

# 求列最大值
# print(df['f1'].max())
#
# # 按f1排序
# df = df.sort_values(by='f1',ascending=False )
# # print( df.sort_values(by='f1',ascending=False ) )
# print(df)

# df1 = df['typen']
# df2 = df[['f1','f2','f3','f4','f5']]
# 
# print(df2[:1])
# d3 = df2[:1].values.tolist()
# print(d3)

# print(df1[:1] )
# print(df2[:1] )
# print(df2 )
# print(d3 )

# d1 = [[0.79, 0.90, 0.46, 0.57, -0.50]]
# print(d1)
# -----------------------------------------------------------------------------------
# data_list = cursor.exc_sql(query_sql)
#
# print(data_list)
# data = cursor.fetchall()

# 这里必须把fetch回来的data转换为list的格式，否则DataFrame会在初始化的时候报错。

# data = list(data)
# data = [list(i) for i in data]
#
# df = DataFrame(data, columns=["name", "f1", "f2"])
# # df_stack = df.stack()
# # print(df_stack)
# # print(df_stack[1])
#
# n = list(df["name"])
# d1 = [list(df["f1"])]
# d2 = list(df["f2"])
#
# print(list(df["name"]))
# print(d1)
# print(df["f1"])
# value2 = [[0.11, 0.34, 0.31, -0.11, 0.21]]
# print(value2)
#
# d1 = [1,2,3,4,5,6]
# print(d1)