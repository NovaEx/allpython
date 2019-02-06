import psutil
import platform

# задача 4  - вывести диагностическую информацию рабочей
# машины  - ЦПУ, оперативная память свободная/занятая,
# диски - свободно/занято, сетевые интерфейсы, тип и версия ОС


print('CPU: {0}  CORES: {1} THREADS: {2} LOAD: {3} % FREQ_CUR: {4} MHz FREQ_MAX: {5} MHz FREQ_MIN: {6} MHz'.format(
    platform.processor(),                           # Тип проца
    psutil.cpu_count(logical=False),                # Количество ядер
    psutil.cpu_count(),                             # Ядра(логические)
    psutil.cpu_percent(interval=None),              # Нагрузка в данный момент
    int(psutil.cpu_freq()[0]),                      # Частота в данный момент
    int(psutil.cpu_freq()[2]),                      # Максимальная частота
    int(psutil.cpu_freq()[1]))                      # Минимальная
)
print('MEMORY ALL: {0} MB IN_USE: {1} MB FREE: {2} MB AVAILABLE: {3} MB'.format(
    int(psutil.virtual_memory().total/1024/1024),           # Память вся
    int(psutil.virtual_memory().used/1024/1024),            # Использованная
    int(psutil.virtual_memory().free/1024/1024),            # Свободная
    int(psutil.virtual_memory().available/1024/1024))       # Всего доступно памяти
)
print('DISKS: ')
for part in psutil.disk_partitions():
    print('     DEV :{0:<15} MOUNT: {1:<30} fstype: {2:<10} USED: {3:<10}  FREE: {4:<10} MB ALL: {5} MB'.format(
        part.device, part.mountpoint, part.fstype,                              # Устройство, точка монтирования и тип фс
        str(int(psutil.disk_usage(part.mountpoint).used/1024/1024)) + ' MB',    # Занято на разделе
        str(int(psutil.disk_usage(part.mountpoint).free/1024/1024)) + ' MB',    # Свободное место на разделе
        int(psutil.disk_usage(part.mountpoint).total/1024/1024))                # Всего памяти
    )

