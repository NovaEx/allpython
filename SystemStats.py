import psutil
import platform

# задача 4  - вывести диагностическую информацию рабочей
# машины  - ЦПУ, оперативная память свободная/занятая,
# диски - свободно/занято, сетевые интерфейсы, тип и версия ОС


print('CPU: {0}  CORES: {1} THREADS: {2} LOAD: {3} FREQ_CUR: {4} MHz FREQ_MAX: {5} MHz FREQ_MIN: {6} MHz'.format(platform.processor(), psutil.cpu_count(logical=False), psutil.cpu_count(), '', int(psutil.cpu_freq()[0]), int(psutil.cpu_freq()[2]), int(psutil.cpu_freq()[1])))
print('MEMORY ALL: {0} MB IN_USE: {1} MB FREE: {2} MB AVAILABLE: {3} MB'.format(int(psutil.virtual_memory().total/1024/1024), int(psutil.virtual_memory().used/1024/1024), int(psutil.virtual_memory().free/1024/1024), int(psutil.virtual_memory().available/1024/1024)))
print('DISKS: ')
for part in psutil.disk_partitions():
    print('     DEV :{0:<15} MOUNT: {1:<30} fstype: {2} USAGE: {3}'.format(part.device ,part.mountpoint, part.fstype, psutil.disk_usage()))

