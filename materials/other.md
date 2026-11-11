Просмотр расположения файлов стандартной библиотеки

```Python
import sys, os, json

print(json.__file__)  # C:\Python314\Lib\json\__init__.py
print(os.__file__)  # C:\Python314\Lib\os.py
```

Директории хранения модулей (при установке python -m)

```Python
import sys

print(sys.path) 
#  ['C:\\Python314\\python314.zip', 'C:\\Python314\\DLLs', 'C:\\Python314\\Lib', 'C:\\Python314', 'D:\\Applications\\modern\\venv', 'D:\\Applications\\modern\\venv\\Lib\\site-packages']
```

`os.environ` - словарь переменных окружения процесса (PATH, USERNAME)
