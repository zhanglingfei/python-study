import pandas as pd
user_info_dir=f"/Users/stevenzhang/Downloads/-221013_copy.tsv"
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('max_colwidth', 10000)
dtype = {
        'sid': str,
        'pid': str,
        'gender_cls': str,
        'age_range_cls': str,
        'international_brand_cls': str,
        'card_product_rank_cls': str,
        'card_system': str,
        'card_system_cls': str,
        'contract_dt': str,
        'family_cd': str,
        'income_cls': str,
        'address_cd': str,
        'termination_contract_dt': str,
        'delivered_date': str
    }
master_userinfo_df = pd.read_csv(user_info_dir,
                          sep='\t',
                          header=0,
                          dtype=dtype)
# master_userinfo_df.fillna('', inplace=True)
master_userinfo_df_2 = master_userinfo_df[master_userinfo_df['family_cd']!='1']
master_userinfo_df_3 = master_userinfo_df_2[master_userinfo_df_2['family_cd']!='2']
master_userinfo_df_4 = master_userinfo_df_3[master_userinfo_df_3['family_cd']!='3']
master_userinfo_df_5 = master_userinfo_df_4[master_userinfo_df_4['family_cd']!='4']
print(f"master_userinfo_df rows: {master_userinfo_df.shape[0]}, master_userinfo_df_2 rows: {master_userinfo_df_5.shape[0] }")

master_userinfo_df_5.to_csv('NCT_ZF_20200308-221013.tsv',sep='\t',index=False)