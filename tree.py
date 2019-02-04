import os

dir = input('Введите директорию: ')
if dir[-1] != '/': dir = dir + '/'
if dir is not None:
    for item in os.listdir(dir):
        if os.path.isfile(dir + str(item)):
            print('{0:<50} {1:^5}'.format(item, 'file'))
        elif os.path.isdir(dir + str(item)):
            print('{0:<50} {1:^5}'.format(item, 'dir'))
        elif os.path.islink(dir + str(item)):
            print('{0:<50} {1:^5} '.format(item, 'link'))
        else:
            print('{0:<50} {1:^5} '.format(item, 'IDK'))
# print( os.listdir('/home/ant') )