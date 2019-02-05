import os


def dirsize(path):
    size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            if not os.path.exists(os.path.join(dirpath, f)): continue
            fp = os.path.join(dirpath, f)
            size += os.path.getsize(fp)
    return size


dir = input('Введите директорию: ')
if dir[-1] != '/': dir = dir + '/'
if dir is not None:
    for item in os.listdir(dir):
        itempath = dir + str(item)
        if os.path.isfile(itempath):
            print('{0:<50} {1:^5} {2:^50} '.format(item, 'file', os.path.getsize(itempath)))
        elif os.path.islink(itempath):
            print('{0:<50} {1:^5} '.format(item, 'link'))
        elif os.path.isdir(itempath):
            print('{0:<50} {1:^5} {2:^50} '.format(item, 'dir', dirsize(itempath)))
        else:
            print('{0:<50} {1:^5} '.format(item, 'IDK'))
# print( os.listdir('/home/ant') )
