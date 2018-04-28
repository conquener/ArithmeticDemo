# -*- coding: utf-8 -*-
datas = [22,15,21,54,76,15,12,56,45,38]

#data 是数据集 index 是排序位置
def selectionSort(paramDatas):
    result = [];#接收数据的结果集

    for i in range(len(paramDatas)):
        index = 0;  # 数组索引
        max_data = paramDatas[0];
        #通过循环,选出最大的元素
        for j in range(len(paramDatas)):
            if paramDatas[j] > max_data:
               index = j;
               max_data = paramDatas[j];
        #在新数组中添加最大的元素,再从以前的数组中移除最大的元素
        result.append(paramDatas.pop(index));

    return  result;

#调用方法
print(selectionSort(datas));





