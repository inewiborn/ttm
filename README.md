### Структура приложения

#### исполняемые файлы
1. ttm - ядро приложения представляет собой сетевое приложение
1. ttmcli - утилита для консоли
1. ttmdb - работа с БД
1. ttmw - графическая оболочка приложения
2. ttmweb - веб интерфейс построенный на Flask

#### Директория с модулями

Директори lib делится на пакеты(слои(layer) приложеия)

1. model - базовые классы модели приложения
1. orm - работа с базой
1. cli - работа с консолью
1. view - визуальный интерфейс
1. network - слой для сети

#### Структура БД

###### Project
id
name
dir
time

###### Task
id
id_project
description
time

###### Files
id
id_task
path
name
description

###### Notes
id
id_task
text

###### Time
id
id_poject
id_task
id_file
id_note
start
end
time


##### Зависимости
beautifulsoup4
lxml
Flask
