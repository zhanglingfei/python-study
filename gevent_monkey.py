import gevent
from gevent import monkey
monkey.patch_all()
import requests
from time import time




# 下载图片的任务
def download_img(img_url, img_name):
    try:
        # 获取当前协程
        print("download_img:", gevent.getcurrent())
        # 根据图片地址打开网络资源文件
        #file = urllib.request.urlopen(img_url)
        file = requests.get(img_url,stream=True)
        # 打开下载的文件，写入网络文件数据
        with open(img_name, "wb") as img_file:
            while True:
                # 获取网络资源文件数据
                img_data = file.read(1024)
                if img_data:
                    # 把网络资源文件的数据写入到指定下载文件里面
                    img_file.write(img_data)
                else:
                    # 代码执行到此，说明文网络中的文件数据读取完成
                    break
    except Exception as e:
        print("网络异常，下载失败:", e)
    else:
        print("下载成功:", img_name)

def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)

if __name__ == '__main__':
    # 准备下载图片的地址
    img_url1 = "https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1293860636,1088191402&fm=27&gp=0.jpg"
    img_url2 = "https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=2086972466,4153089489&fm=27&gp=0.jpg"
    img_url3 = "https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=4115825325,3478781251&fm=27&gp=0.jpg"
    img_url4 = "https://media.defense.gov/2015/Dec/15/2001326108/-1/-1/0/151215-F-DW547-001.JPG"
    img_url5 = "https://media.defense.gov/2005/Dec/26/2000574555/780/780/0/050317-F-1234P-008.JPG"

    img_list=[]
    img_list.append(img_url1)
    img_list.append(img_url2)
    img_list.append(img_url3)
    img_list.append(img_url4)
    img_list.append(img_url5)

    start_time_non=time()
    download_file(img_url1)
    download_file(img_url2)
    download_file(img_url3)
    download_file(img_url4)
    download_file(img_url5)
    end_time_non=time()
    print(f"the non-couroutine download takes : {end_time_non-start_time_non} seconds")





    # 创建协程  参数不是元组的形式，而是位置参数
    # g1 = gevent.spawn(download_img, img_url1, "1.jpg")
    # g2 = gevent.spawn(download_img, img_url2, "2.jpg")
    # g3 = gevent.spawn(download_img, img_url3, "3.jpg")
    #print(g1, g2, g3)
    g_list=[]
    start_time = time()
    for img in img_list:
        g = gevent.spawn(download_file, img)
        g_list.append(g)

    for g in g_list:
        g.join()
    end_time = time()
    print(f"the couroutine download takes : {end_time - start_time} seconds")

    print( f": the gain factor is {end_time_non-start_time_non}/{end_time - start_time}")

    #gevent.joinall([g1, g2, g3])

print