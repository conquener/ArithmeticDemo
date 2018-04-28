# -*- coding: utf-8 -*-

data_arry = [15,2,12,84,51,9,52,41];

def quicksort(arry):
    #如果数组长度小于2  说明已经不需要再进行拆分了
    if len(arry) < 2:
        return arry;
    else:
        #选定基准值
        pivot = arry[0];
        #获得大于privot 的数组
        maxarry = [data for data in arry[1:] if data > pivot];
        #获得 小于等于privot 的数组
        minarry = [data for data in arry[1:] if data <= pivot];

        #继续将分开的数组进行拆分,直到数组长度小于2结束
        result = quicksort(minarry) + [pivot] + quicksort(maxarry);

        return result;

print(quicksort(data_arry));




