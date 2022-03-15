import os

#初始化要计算的文件夹大小
SUM = 0

'''
计算文件夹大小的函数
1、遍历文件夹下的文件夹和文件
2、如果是文件，计算文件大小并加入文件夹大小中
3、如果是文件夹，继续遍历其下的文件夹和文件
'''
def calc_dir_size(path):
    global SUM
    for name in os.listdir(path):
        subpath = path+'/'+name
        if os.path.isfile(subpath):
            SUM += os.path.getsize(subpath)
        elif os.path.isdir(subpath):
            calc_dir_size(subpath)
        else:
            print('warning:%s不是文件也不是文件夹，程序无法处理' %subpath)
            continue


'''
格式化字节数
'''
def reduce_unit(value):
    units = ["B", "KB", "MB", "GB", "TB", "PB"]
    size = 1024
    for unit in units:
        if (value / size) < 1:
            return "%.2f%s" % (value, unit)
        value = value / size


'''
输入一个文件夹路径，得到其文件夹大小的函数
'''
def get_dir_size():
    while True:
        dirpath = input('请输入文件夹的绝对路径,按回车结束；您也可以直接按回车退出\n').strip()
        if os.path.isdir(dirpath):
            calc_dir_size(dirpath)
            print("文件夹大小为{0}({1:,}字节)".format(reduce_unit(SUM),SUM))
            break
        elif dirpath == '':
            print('程序结束')
            return
        else:
            print('您输入的不是文件夹，请输入正确路径')



get_dir_size()