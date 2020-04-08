from typing import Dict


# Default network configuration used for now
def get_vpc_config(assignPublicIp=True,
                   security_group=['sg-61ec1b19'],
                   subnets=['subnet-ae7dd1d8', 'subnet-6d1aea35']) -> Dict:
    result = {'awsvpcConfiguration': {}}
    if assignPublicIp:
        result['awsvpcConfiguration']['assignPublicIp'] = 'ENABLED'
    else:
        result['awsvpcConfiguration']['assignPublicIp'] = 'DISABLED'
    result['awsvpcConfiguration']['securityGroups'] = security_group
    result['awsvpcConfiguration']['subnets'] = subnets
    return result











def main():
    # str_1 = '12*&^345,12345%%'
    # nPos = str_1.find('*&^')
    # print(nPos)
    # # try:
    # #     str_2=multi_sub(str_1,[11,12],['88','##','但是'])
    # #     print((str_2))
    # # except IndexError:
    # #     print('out of index error')
    # # print('after exception cotinue to run')
    # # for i in range(10):
    # #     i+=1
    # #     print(i)
    # npos_list=[]
    # for i in range(10):
    #     i += 1
    #     npos_list.append(11 + i)
    #
    # print(npos_list)
    vpc.get_vpc_config()








if __name__ == '__main__':
    main()
