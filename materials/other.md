Регистрация

```Python
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout
from django.shortcuts import redirect

def login_user(request):
    if request.method == "POST":
        form = LoginUserForm(request.POST)
  
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd["username"], password=cd["password"])
    
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("home"))
  
    else:
        form = LoginUserForm()
  
    return HttpResponseRedirect(request, "users/login.html", {"form": form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("users:login"))
```

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

## CSRF

`{% csrf_token %}` - защита от CSRF-атак - шаблонный тег Django, который вставляет в HTML скрытое поле с токеном для защиты от межсайтовой подделки запроса (Cross-Site Request Forgery, CSRF).

Если у пользователя есть активная сессия на сайте, злоумышленник может заманить его на свой сайт, где будет форма, отправляющая POST-запрос на текущий домен (удалить аккаунт или перевести деньги). Браузер отправит куки сессии автоматически - и сервер подумает, что запрос сделал пользователь.

Схема работы:

1. Сервер генерирует уникальный токен для сессии пользователя (хранится в сессии/куке, зависит от настроек);
2. Тег `{% csrf_token %}` в шаблоне рендерит: `<input type="hidden" name="csrfmiddlewaretoken" value="...long-string...">`
3. При POST-запросе Django middleware (CsrfViewMiddleware) проверяет:
   1. Есть ли токен в данных формы;
   2. Совпадает ли он с тем, что хранится в сессии;
   3. Корректен ли источник запроса (Referer/Origin при необходимости)
4. Если проверка не пройдена - возвращается ошибка 403 (Forbidden)
