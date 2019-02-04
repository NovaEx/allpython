import os

dir = input('Введите директорию: ')
if dir[-1] != '/': dir = dir + '/'
if dir is not None:
    for item in os.listdir(dir):
        if os.path.isfile(dir + str(item)):
            print('{0:<50} {1:^5} {2:^50} '.format(item, 'file', os.path.getsize(dir + item)))
        elif os.path.islink(dir + str(item)):
            print('{0:<50} {1:^5} '.format(item, 'link'))
        elif os.path.isdir(dir + str(item)):
            dirsize = 0
            for dirpath, dirnames, filenames in os.walk(dir + item):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    dirsize += os.path.getsize(fp)
            print('{0:<50} {1:^5} {2:^50} '.format(item, 'dir', dirsize))
        else:
            print('{0:<50} {1:^5} '.format(item, 'IDK'))
# print( os.listdir('/home/ant') )