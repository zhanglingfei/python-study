
import os

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import FuncFormatter  ### 今天的主角
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()
#from scipy.interpolate import spline
# フォントパスを指定 .ttf 形式でないと駄目な模様, 関連：https://github.com/matplotlib/matplotlib/pull/3912
# fp = FontProperties(fname='/Library/Fonts/Osaka.ttf', size=14)
#
# # get_name() で 'Osaka' が返ってきています。メソッドの代わりに = 'Osaka' としてもOK
# rcParams['font.family'] = fp.get_name()
plt.rcParams.update({'figure.max_open_warning': 0})
x=[]
y=[]
# athena_list=['6040','7561','7581','7823',
# '8005','9438','9704','9792','2910','6027','8202','9633','7554','2729','9671','7816','9945','2211','7844','9850','9990','9846','8200','7840','2331','3034','3659','4337','3349','2193','6076','9993','2371','9424',
# '9697','2931','3385','3660','8153','2686','7636','6630','9039','8022','2798','8163','2742','7603','3087','3397','3635','8167','2930','9035','8114','6071','7604','3091','2753','7829','8207','7621','2792','7806','7937','6097','5261','7630','7421','4344','4680','7475','3046','8168','8011','3341','9842',
# '7445','7936','2764','3319','3765','3395','8008','3415','2694','9979','7455','7564','8190','9713','7952','3097','2484','2138','3632','7951','3053','2726','9605','3193','3178','9627','9919','9873','7416','9900','9948','8111','7605','9416','9733','2780','2305','4924','8218','8217','2695','2674','9735','9206','9601','7520','8160','8174','4751','4704','3387','2659','8278','9419','9278',
# '8185','7860','3064','9994','8289','8276','9997','3549','7494','7974','3539','9722','9823','2157','9684','8179','9708','8255','7545','3665','4921','8237','9861','3333','2928','8244','3938','3050','8273','2790','7780','3098','3182','7616','3191','8227','2685','3148',
# '4927','9956','8165','7606','7550','9766','3197','9882','9974','2681','7649','2678','2670','7516','9603','8182','9989','8252','3088','2432','8016','9412','4839','6030','6191','3028','8281','8184','8214','7618','2730','3391','8203','9832','8219','8173','8194','8279','9783','3222','7513','9726',
# '6098','4661','7419','2752','7453','7532','8028','4385','8282','3099','3092','9201','9843','2651','8242','3048','9983','9202','9831','8267','3382','4755','9432','4689','9433','AMZN','9984']

athena_list=[6040,7561,7581,7823,
8005,9438,9704,9792,2910,6027,8202,9633,7554,2729,9671,7816,9945,2211,7844,9850,9990,9846,8200,7840,2331,3034,3659,4337,3349,2193,6076,9993,2371,9424,
9697,2931,3385,3660,8153,2686,7636,6630,9039,8022,2798,8163,2742,7603,3087,3397,3635,8167,2930,9035,8114,6071,7604,3091,2753,7829,8207,7621,2792,7806,7937,6097,5261,7630,7421,4344,4680,7475,3046,8168,8011,3341,9842,
7445,7936,2764,3319,3765,3395,8008,3415,2694,9979,7455,7564,8190,9713,7952,3097,2484,2138,3632,7951,3053,2726,9605,3193,3178,9627,9919,9873,7416,9900,9948,8111,7605,9416,9733,2780,2305,4924,8218,8217,2695,2674,9735,9206,9601,7520,8160,8174,4751,4704,3387,2659,8278,9419,9278,
8185,7860,3064,9994,8289,8276,9997,3549,7494,7974,3539,9722,9823,2157,9684,8179,9708,8255,7545,3665,4921,8237,9861,3333,2928,8244,3938,3050,8273,2790,7780,3098,3182,7616,3191,8227,2685,3148,
4927,9956,8165,7606,7550,9766,3197,9882,9974,2681,7649,2678,2670,7516,9603,8182,9989,8252,3088,2432,8016,9412,4839,6030,6191,3028,8281,8184,8214,7618,2730,3391,8203,9832,8219,8173,8194,8279,9783,3222,7513,9726,
6098,4661,7419,2752,7453,7532,8028,4385,8282,3099,3092,9201,9843,2651,8242,3048,9983,9202,9831,8267,3382,4755,9432,4689,9433,9984]
athena_list.sort()
#print(athena_list)
def formatnum(x, pos):
    return '$%.1f$x$10^{6}$' % (x / 10000000)

athena_list2=[]
#first we need read csv from dir
#dir=f'/Users/stevenzhang/Downloads/ticker_fixed_raw_monthly_sales/'
dir=f'/Users/stevenzhang/Downloads/ticker_daily_split_raw_monthly_sales_flash/'

file_list=[]
for i in os.walk(dir):
    #print(i[2])
    file_list.append(i[2])

#print(file_list[0])
#before plot first delete all older files
# for item in file_list[0]:
#     os.remove(os.path.join(dir,item))

counter=1
for item in file_list[0]:
    if item =='.DS_Store' :
        #print (item)
        pass
    else:
        print(counter)
        # x_list_name=f'x_{counter}'
        # x_list_name=[]
        # y_list_name = f'y_{counter}'
        # y_list_name=[]
        csv_data = pd.read_csv(os.path.join(dir,item))
        #newDf = pd.DataFrame(csv_data, columns=['sales', 'ticker_code'])
        csv_data['year'] = csv_data['year'].map(lambda x: str(x))
        csv_data['month'] = csv_data['month'].map(lambda x: str(x))
        csv_data['year'].str.cat(csv_data['month'], sep='-')
        csv_data['date'] = csv_data['year'] + '-' + csv_data['month']
        csv_data['date'] = pd.to_datetime(csv_data['date'], format='%Y-%m')
        #print(csv_data.dtypes)
        newDf = pd.DataFrame(csv_data, columns=['billion','date'])
        #csv_data.to_csv(ticker_code[0].csv)

        #print(csv_data['sales'])
        # smooth_iter=f'df_{counter}'
        # smooth_iter=interp1d(csv_data.index,csv_data['sales'])
        ticker_code=csv_data['ticker_code']

        # if ticker_code[0]!= 'AMZN':
        athena_list2.append(ticker_code[0])
        #print(ticker_code[0])
        # x_list_name.append(counter)
        # y_list_name.append(csv_data['sales'])
        # data = pd.Series(x, y)

        # xnew = np.linspace(300)
        # power_smooth=interp1d(newDf,xnew)
        if counter==1000:
            break
        else:
            #plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
            #plt.rcParams['font.family'] = 'SimHei'
            ax = plt.gca()
            #ax.margins(2)
            #ax = plt.axes([0.2, 0.8, .2, .8])
            plt.plot(newDf['date'], newDf['billion'],'g+-')
            plt.xticks(rotation=15,fontsize=8)  # 这里是调节横坐标的倾斜度，rotation是度数
            plt.yticks(rotation=30, fontsize=9)  # 这里是调节横坐标的倾斜度，rotation是度数
            plt.title(f"monthly sales of ticker_{ticker_code[0]}")
            plt.xlabel('Date (2017-11 to 2019-10)')
            plt.ylabel('SALES unit: billion JPY')
            #plt.Rectangle((100, 100), 300, 500)plt

            formatter = FuncFormatter(formatnum)
            #ax.yaxis.set_major_formatter(formatter)


            #plt.gcf().set_facecolor(np.ones(3) * 200 / 285)  # 生成画布的大小
            plt.grid(True, linestyle='-.')  # 生成网格

            #plt.margins(0.5)


            # ax = newDf.plot(newDf['date'],newDf['sales'], title=f'fixed raw data Monthly sales_{ticker_code[0]}')
            # ax.legend([f"monthly sales of ticker_{ticker_code[0]}"])
            # xlabel="number of month (2017-11 to 2019-10)"
            # ylabel="SALES unit: billion JPY"
            # xmajorLocator= MultipleLocator(2) # 将x主刻度标签设置为20的倍数  
            # xmajorFormatter = FormatStrFormatter('%1.0f') # 设置x轴标签文本的格式  
            # xminorLocator = MultipleLocator(1) # 将x轴次刻度标签设置为5的倍数 
            # # 设置主刻度标签的位置,标签文本的格式  
            # ax.xaxis.set_major_locator(xmajorLocator)
            # ax.xaxis.set_major_formatter(xmajorFormatter)
            #
            #
            #
            # ax.set_xlabel(xlabel)
            # ax.set_ylabel(ylabel)
            # ax.grid(True, which='major', c='gray', ls='-', lw=1, alpha=0.2)
            # # # plt.show()
            # # for i in range(10):
            # fig_handle=f'fig_{counter}'
            # fig_handle = ax.get_figure()
            plt.savefig(f'/Users/stevenzhang/Downloads/png_flash/fig{counter}_flash_raw_{ticker_code[0]}.png')
            #plt.show()
            plt.close()
            # #fig_handle.clf() # to avoid warning of opening too many figures
            csv_data.to_csv(f'/Users/stevenzhang/Downloads/data_flash/{ticker_code[0]}.csv', index=0)
            # print(counter)
            counter+=1
print ('-----'+str(len(athena_list2)))


# for i in range(10):
#     x.append(i)
#     y.append(i+1)
#     # data = pd.Series(np.random.randn(1000),index=np.arange(1000))
# data = pd.Series(x, y)
# data = data.cumsum()
# ax = data.plot()
# # plt.show()
# for i in range(10):
#     fig_handle=f'fig_{i}'
#     fig_handle = ax.get_figure()
#     fig_handle.savefig(f'fig_{i}.png')

