Задание №1
Разработать эмулятор для языка оболочки ОС. Необходимо сделать работу
эмулятора как можно более похожей на сеанс shell в UNIX-подобной ОС.
Эмулятор должен запускаться из реальной командной строки, а файл с
виртуальной файловой системой не нужно распаковывать у пользователя.
Эмулятор принимает образ виртуальной файловой системы в виде файла формата
zip. Эмулятор должен работать в режиме CLI.
Конфигурационный файл имеет формат csv и содержит:
• Путь к архиву виртуальной файловой системы.
• Путь к лог-файлу.
• Путь к стартовому скрипту.
Лог-файл имеет формат csv и содержит все действия во время последнего
сеанса работы с эмулятором.
Стартовый скрипт служит для начального выполнения заданного списка
команд из файла.
Необходимо поддержать в эмуляторе команды ls, cd и exit, а также
следующие команды:
1. find.
2. touch.
3. cat.
Все функции эмулятора должны быть покрыты тестами, а для каждой из
поддерживаемых команд необходимо написать 3 теста.

Реализация программы
![image](https://github.com/user-attachments/assets/bc29b2ed-1c0c-4a9d-8098-e64e79236883)

Тестирование программы
![image](https://github.com/user-attachments/assets/e4b293fc-320b-4ee2-a1cc-aab0cc5aca89)

