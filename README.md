# Тестирование API

В этой части проекта будет производиться тестирование API:

 - https://travelpayouts.github.io/slate/ поиск авиабилетов по параметрам.

У данного сервиса есть 2 версии API, в тестах используются обе.

Для получения ответа от сервиса необходима регистрация и отправка токена в каждом запросе.

### Что умеет:
Реализована отправка запросов на разные "ручки", проверка кода ответа со статусом 200 и проверка ответа соответствию json схеме предполагаемого ответа.

Так же были написаны негативные тесты под маркером xfail