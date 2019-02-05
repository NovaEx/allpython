import zipfile
import os
import threading


class Zip(threading.Thread):

    def __init__(self, file):
        self.file = file
        threading.Thread.__init__(self)

    def run(self):
        if not os.path.exists('{0}/zips'.format(dir)):
            os.makedirs('{0}/zips'.format(dir))
        with zipfile.ZipFile('{1}/zips/{0}.zip'.format(self.file, dir), 'w') as myzip:
            myzip.write(self.file)



if __name__ == '__main__':
    dir = input('Введите директорию для zip: ')
    os.chdir(dir)
    for file in filter(os.path.isfile, os.listdir(dir)):
        t = Zip(file)
        t.start()
    print('Все файлы в {0}'.format(dir + '/zips/'))
