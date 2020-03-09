__author__ = 'ROOT'
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pymongo import MongoClient
#  macOS 下 matplotlib 正常显示汉字， 其他系统请自行google
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

#  连接mongo数据库
client = MongoClient(host="localhost", port=27017)
db = client.scrapy
col = db.gitee_redis
# 获取原始数据
data = list(col.find())

# 将数据转为pandas数据
df = pd.DataFrame(data)
# df1 = pd.group(by='category')
# print(df1)
# 根据'lang' 进行分组统计数量
c = df.groupby('lang').count()
#  根据_id 列升序排列去最后20个数据
d = c.sort_values('_id').tail(20)
# 通过matplotlib进行绘图，展示
x = d.index
y = d['_id']
# 设置图片大小与dpi
fig = plt.figure(figsize=(16, 5), dpi=80)
# 绘制横向条形图，分别配色
a = plt.barh(x, y, color=['#0072BD','#D95319','#EDB120','#7E2F8E','#77AC30','#4DBEEE','#A2142F'])
# 设置表名称
plt.title('开源项目分布')

# 为每个条形图数据添加具体数值
for rect in a:
    w = rect.get_width()
    plt.text(w, rect.get_y()+rect.get_height()/2, '%d' %
            int(w), ha='left', va='center')

# for a, b in zip(x, y):
#     plt.text(a, int(b)+0.05, '%.0f' % b, ha='center', va='bottom', fontsize=7)
# 保存条形图为svg
plt.savefig('test.svg')
# 展示条形图
plt.show()


