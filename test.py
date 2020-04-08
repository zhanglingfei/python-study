current_download_list=['NCT_RKUF_20200113-110230.tsv', 'NCT_RKUF_20200114-110230.tsv','NCT_RMF_20191122-123101.tsv','NCT_ZF_20191208-221026.tsv']

keyword='NCT_RKUF'
keyword2='NCT_RMF'
keyword3='NCT_ZF'
data_type_list_flash=[]
data_type_list_fixed=[]
data_type_list_user=[]
for item in current_download_list:
    if keyword in item :
        #print ("true")
        data_type_list_flash.append(item)
    elif keyword2 in item:
        #print ("false")
        #print(item)
        data_type_list_fixed.append(item)
    else:
        data_type_list_user.append(item)

if len(data_type_list_flash)>0:
    print("we loaded flash data")
if len(data_type_list_fixed)>0:
    print("we loaded fixed data")
if len(data_type_list_user)>0:
    print("we loaded user info data")