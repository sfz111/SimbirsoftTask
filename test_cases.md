## Тест-кейс: Создание клиента (Add Customer)

### TC-001:

**Предусловия**: Открыта страница: https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager

**Шаги**:

1) Нажать на кнопку "**Add Customer**"
2) Проверить, что открылась форма добавления клиента
2) Ввести в поле "**Post Code**" 10 цифр
3) Ввести в поле "**First Name**" данные на основе значения из "**Post Code**" согласно алгоритму:
    1) Разбить Post Code на 5 двузначных чисел (например, 12 34 56 78 90).
    2) Преобразовать каждое число в букву английского алфавита по правилу:
       0 → a, 1 → b, ..., 25 → z.
       Если число > 25, взять остаток от деления на 26
4) Ввести в поле "**Last Name**" любую строку
5) Нажать на кнопку "**Add Customer**"
6) Проверить, что на странице появился алерт с сообщением об успешном создании клиента

**Постусловия**: Удалить созданного клиента

## Тест-кейс: Сортировка клиентов по имени (First Name).

### TC-002:

**Предусловия**:

1) Открыта страница: https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager
2) В системе есть хотя бы два клиента (если нет, их необходимо создать)

**Шаги**:

1) Открыть список клиентов кликом по кнопке "**Customers**"
2) Проверить, что отображается таблица с клиентами
3) Кликнуть на заголовок колонки "**First Name**" для сортировки
4) Проверить, что отображается отсортированный по столбцу "**First Name**" список клиентов в алфавитном порядке по
   убыванию
5) Еще раз кликнуть на заголовок колонки "**First Name**" для сортировки
6) Проверить, что отображается отсортированный по столбцу "**First Name**" список клиентов в алфавитном порядке по
   возрастанию

## Тест-кейс: Удаление клиента по длине имени (First name).

### TC-003:

**Предусловия**:

1) Открыта страницу: https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager
2) В системе есть хотя бы один клиент (если нет, необходимо создать)

**Шаги**:

1) Открыть список клиентов кликом по кнопке "**Customers**"
2) Проверить, что отображается таблица с клиентами
3) Определить клиента для удаления по алгоритму:
    1) Вычислить длину каждого имени
    2) Найти среднее арифметическое длин всех имен
    3) Найти имя, длина которого ближе всего к среднему арифметическому
4) Нажать на кнопку "**Delete**" в строке найденного клиента
5) Проверить, что клиент с именем, длина которого ближе всего к среднему арифметическому, не отображается в таблице