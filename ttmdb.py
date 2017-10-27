import os
import sys
import sqlite3
#Директория приложения
#print(sys.path[0])
'''
Сейчас база создается в текущей директории приложения,
но в будующем нужно перенести в директорию пользователя
'''
#con = sqlite3.connect(sys.path[0] + '/ttm.db')
#con = sqlite3.connect(os.path.expanduser('ttm.db'))
db_file_path = os.path.expanduser('~/.ttm/ttm.db')
print(db_file_path)
if(os.path.exists(db_file_path)):
    print('db_yes');
else:
    db_dir_path = os.path.expanduser('~/.ttm/')
    os.mkdir(db_dir_path)
    print('create');
    con = sqlite3.connect(db_file_path)
    con.close()

