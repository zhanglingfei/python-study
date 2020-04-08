import pandas as pd

#check pandas verison
print(pd.__version__)
#from alternadb.crud_interface import crud_interface

import os
# create a list
# arr=[0,4,3,4,53]
# print(arr)
# series1=pd.Series(arr)
# print(series1)
# # create random array
# n=np.random.randn(5)
# index=['a',2,'a',5,6]
# series2=pd.Series(n,index=index)
# series2.index=['A','B','E','D','H']
# print('----------')
# print(series2)
#
# #create Series from dict
# # d={'a':1,'b':3,'ee':4,'d':8,'e':12}
# # print(d)
# # series3=pd.Series(d.items())
# # print(series3)
# delivered_date = pd.to_datetime('2019-12-21')
# print(delivered_date)
# df = pd.DataFrame({'id': [1, 2, 3], 'emp_no': ['a', 'b', 'c'],'name': ["A","B","C"]})
#
# # #print(df.loc[df.loc[:,'a']>2,:])
# # # print (df['name'])
# # print(df)
# # # print(list(df.loc[2]))
# # print (df.loc[1].size)
#
def return_step(rows, cpu_count):
    '''

    :param rows:
    :param cpu_count:
    :return:
    '''
    if rows % cpu_count == 0:
        step = int(rows / cpu_count)
        modified_rows=rows-step
        print(f"case 1: {step}|| {modified_rows}")

    else:
        diff = (rows % cpu_count)
        modified_rows = rows - diff
        step = int(modified_rows / cpu_count)
        print(f"case 2: {step}|| {modified_rows}")
    return step, modified_rows


def return_split_num_df_list(rows, cpu_count):
    '''

    :param rows:
    :param cpu_count:
    :return:
    '''
    split_num_list = []
    step, modified_rows = return_step(rows, cpu_count)
    for i in range(step, modified_rows+step, step):
        split_num_list.append(i)
    split_num_list.append(modified_rows)
    print(split_num_list)
    return split_num_list


def return_split_df_list(df2):
    number_cpu = os.cpu_count()
    print(number_cpu)
    if df2.shape[0] < number_cpu * 2:
        print('insert without split')
    else:
        print(f'insert with multiprocessing: {df2.shape[0]}')
        # 我们需要按照cpu数量划分df的个数
        split_num_list = return_split_num_df_list(101360,number_cpu)
        step, modified_rows = return_step(df2.shape[0], number_cpu)
        master_info_list = []
        counter = 0
        for split_num in split_num_list:
            if counter == 0:
                df = df2.iloc[:split_num, :]
                master_info_list.append(df)
            elif counter < len(split_num_list) - 1:
                df = df2.iloc[int(split_num - step):split_num, :]
                master_info_list.append(df)
            else:
                df = df2.iloc[split_num:, :]
                master_info_list.append(df)
            counter += 1
        return master_info_list

        # for master_user_info in master_info_list:
        #     print(master_user_info.shape[0])

if __name__ == '__main__':
    df2 = pd.DataFrame({'key1': (
    1, 2, {"ds", "sd"}, 'sd', 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2,
    1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2),
                        'key2': ['afdas', 'asd', 'afdas', 'asd', 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 1, 2, 1, 2, 1, 2,
                                 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1,
                                 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]})

    print(len(return_split_df_list(df2)))
