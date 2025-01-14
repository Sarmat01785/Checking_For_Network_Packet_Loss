# Проверка Потери Сетевых Пакетов

Простая программа на Python для проверки потери сетевых пакетов путем подключения к удаленному серверу через TCP/IP сокеты.

## Описание

Эта программа создает TCP соединение с указанным сервером и портом, отправляет простое сообщение, ожидает ответ и измеряет время ожидания ответа. Если время ожидания превышает определенный порог, программа интерпретирует это как потерю пакета.

## Как использовать

1. Установите Python 3 на вашем компьютере, если он еще не установлен.
2. Измените переменные `server_ip` и `server_port` в коде, чтобы указать IP-адрес и порт сервера, с которым вы хотите установить соединение.
3. Запустите программу. Программа отправит 10 TCP пакетов на сервер и сообщит о потерях пакетов.

## Настройка

Замените следующие значения в коде программы:

- `server_ip`: IP-адрес удаленного сервера, к которому вы хотите подключиться.
- `server_port`: Порт удаленного сервера.

## Пример использования


Запустите скрипт после внесения изменений:

```bash
Python Internet_Packet_Loss_Test.py
```


## Ожидаемые результаты

Программа выведет сообщение о получении каждого пакета и в конце предоставит общий процент потерянных пакетов.


