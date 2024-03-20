import socket
import time

# Задайте IP-адрес и порт удаленного сервера
server_ip = '127.0.0.1'
server_port = 80

# Создайте сокет
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключитесь к удаленному серверу
s.connect((server_ip, server_port))

# Отправьте данные на сервер
s.send(b'Hello, server!')

# Засеките время
start = time.time()

# Ждите ответа от сервера
data = s.recv(1024)

# Засеките время окончания
end = time.time()

# Вычислите время ожидания
time_waiting = end - start

# Если время ожидания превышает порог, считайте, что произошла потеря пакета
if time_waiting > 5:
    print('Потеря пакета')
else:
    print('Пакет получен')

# Закройте сокет
s.close()

# Запустите цикл для отправки и получения нескольких пакетов
for i in range(10):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))
    s.send(b'Hello, server!')
    data = s.recv(1024)
    s.close()

# Подсчитайте количество потерянных пакетов
lost_packets = 10 - i

# Подсчитайте процент потерянных пакетов
percent_lost = lost_packets / 10 * 100

print(f'Процент потерянных пакетов: {percent_lost:.2f}%')
