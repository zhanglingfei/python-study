import matplotlib.pyplot as plt
import pandas as pd

def hot_Time1():#统计上网高峰时段
    #根据数据使用折线图
    pr = pd.read_csv("hydata_swjl_0.csv")
    pr1 = pd.read_csv("hydata_swjl_1.csv", low_memory=False)
    print('用折线图统计上网高峰时段：')

#绘制上机统计图
    #plt.title('Peak Hours_1',fontsize=15)
    plt.xlabel('Up and down time_1',color='blue')
    plt.ylabel('Number of time periods_1',color='blue')
    #plt.bar(index+bw, values1_on, bw, alpha=0.7)
    x=['0~6','6~8','8~10','10~12','12~14','14~16','16~18','18~20','20~24']
    plt.plot(x,values1_on,label='Onlinetime',color='y',linewidth=3.0)
    plt.plot(x,values1_off,label='Offtime',color='b',linewidth=2.0)
    plt.plot(0,0)
    plt.plot(0, 0)
    plt.plot(0, 0)
    plt.plot(0, 0)
    plt.plot(0, 0)
    plt.plot(0,0)
    plt.plot(0, 0)
    plt.plot(0, 0)
    plt.plot(0, 0)
    plt.grid(alpha=0.3,linestyle=':')
    #plt.xticks()
   # plt.legend(['0~6','6~8','8~10','10~12','12~14','14~16','16~18','18~20','20~24'],
    #           loc=2,edgecolor='b')
    plt.legend(loc='best')
    plt.show()
    print('可以看出，折线图可以更好地反映上网的高峰时期。')
    print('早晨上网人数较少，而到了下午，上网人数陡增')
    print()
if __name__=="__main__":
    hot_Time1()