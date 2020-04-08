
file_name='NCT_ZF_20191208-221026.tsv'
delivered_date_segment = file_name.split('-')
delivered_date_string = delivered_date_segment[0].split('_')
delivered_date = delivered_date_string[-1]
print(delivered_date)