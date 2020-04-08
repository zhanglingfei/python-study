import pandas as pd
data_a={'state':[1,2,4,5,11],'pop':['x-','y-','z-','b-','r-'],'pop2':['ax','by','cr','rr','xr']}
data_b={'state':[1,2,3,5,6,9,9,11],'pop':['a','b','b','b','d','r','b','b'],'pop2':['a','b','r','r','d','r','b','r']}
diff_user_base=pd.DataFrame(data_a)
master_user=pd.DataFrame(data_b)
print(diff_user_base)
print(master_user)
# diff_user_base = diff_user_base.append(master_user)
#diff_user_base = diff_user_base.append(master_user)

#master_user.state.replace(dict(diff_user_base.values),inplace=True)
# diff_user_info = diff_user_base.drop_duplicates(keep=False)  # keep=false保留不相同的
# master_user_new = diff_user_base.merge(master_user,how='outer')
# master_user_new['state'] = master_user_new['state'].combine_first(master_user_new['state'] )
#master_user.drop('state',inplace=True,axis=1)
diff_user_base_list = diff_user_base['state'].tolist()
df_master_reduced = master_user[~master_user['state'].isin(diff_user_base_list)]
df_final_master=diff_user_base.append(df_master_reduced)
print(df_final_master)

