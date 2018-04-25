import fun as fun
import traceback

a = [];
i = 1;
while i<=100:
    a.append(i);
    i = i+1;
#以上就构建了一个1-100 的有序数组
data = 30;

#递归法
def bisectionMethod1(arry,low,high,index):
    #首先判断 两个位置关系
    if low > high :
        print("未找到查找的数据!");
        return -1;

    try:
        # 首先获取到最大值最小值,
        middle = int((low + high) / 2);
        guess = arry[middle];
        print(guess,middle)
        if guess == index:
            #如果相等 那么middle就是要找的值
            return middle;
        elif guess > index :
            #如果middle的值比需要找的值大,说明 要找的值应该在 low 和middle-1(不包括middle)之间
            middle = bisectionMethod1(arry,low,middle-1, index);
        else:
            # 如果middle的值比需要找的值小,说明 要找的值应该在 high 和middle+1(不包括middle)之间
            middle = bisectionMethod1(arry, middle+1,high, index);
    except Exception:
        print(low,high,middle)
        traceback.print_exc();
    return middle;

#利用while 也能实现此方法 和递归实现也是类似
def bisectionMethod2(arry,low,high,index):
    #判断条件为最小的位置 等于最大位置为止
    while low <=high:
        middle =  int((low + high)/2);
        try:
            guess = arry[middle];
            if guess == index:
                return middle;
            elif guess > index:
                high =  middle -1;
            else:
                low = middle +1;
        except Exception:
            print(low, high, middle)
            traceback.print_exc();
    print("未找到查找的数据!");
    return -1;



# 二分法求函数的零值 y = x^2 + 3x -2    x∈[0,1] y的值域为 y∈[-2,2] 这个区间存在0解  近似解0.001
#首先设定 x 的取值范围
def fun_cal(x):
    y = x**2 + 3*x -2;
    return y;

def fun_bisection_method_y():
    xlow = 0;
    xhigh = 1;

    #同样 low > high 结束循环
    while xlow <= xhigh:
        middle = (xlow+xhigh)/2;
        print(middle,xlow,xhigh)
        y = fun_cal(middle);
        if (y-0)<= 0.001 and y >=-0.001:
            return middle;
        elif y>0.001 :
            #函数在区间是单调递增 该区间只有一个零点时能这么用
            xhigh = middle;
        else:
            xlow = middle;

    print("未在该区间找到函数零点!");
    return -1;



# 初始化位置
# low = 0;
# high = len(a);
#print(bisectionMethod1(a,low,high,data));
print("--------------分界线----------------")
#print(bisectionMethod1(a,low,high,data));
print(fun_bisection_method_y());










