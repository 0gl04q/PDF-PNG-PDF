# Конвертер PDF в "Невыделяемый" PDF

Этот Python-скрипт предназначен для преобразования обычных PDF-файлов в PDF-файлы, в которых текст нельзя выделять или копировать. Скрипт достигает этой цели, конвертируя PDF в изображение в формате PNG, а затем создавая PDF-файл на основе этого изображения.

## Особенности

- Конвертирует PDF-файлы в "невыделяемые" PDF-файлы.
- Поддерживает сохранение макета и внешнего вида исходного PDF.
- Позволяет обрабатывать несколько PDF-файлов одновременно.
- Создает структуру папок для организации конвертированных файлов.

## Установка

1. Установите необходимые библиотеки с помощью `pip`:

   ```bash
   pip install pdf2image Pillow reportlab

2. Клонируйте этот репозиторий на свой компьютер:

   ```bash
   git clone https://github.com/0gl04q/PDF-PNG-PDF.git
   cd PDF-PNG-PDF

## Использование

1. Поместите ваши исходные PDF-файлы в папку PDF-ATM в корне проекта.
2. Запустите скрипт:
   
   ```bash
   python script_name.py
   
3. Скрипт создаст новую структуру папок в директории SCAN-PDF-АТМ, которая будет отражать структуру папок в PDF-ATM. В этой новой структуре будут храниться "невыделяемые" версии ваших PDF-файлов.

## Пример

Предположим, у вас есть следующая структура в папке PDF-ATM:

  ```bash
  PDF-ATM/
      ├── Папка1/
      │   ├── Документ1.pdf
      │   └── Документ2.pdf
      ├── Папка2/
      │   ├── Документ3.pdf
      └── Документ4.pdf
```
После выполнения скрипта, структура в папке SCAN-PDF-АТМ будет выглядеть так:

```bash
SCAN-PDF-АТМ/
    ├── Папка1/
    │   ├── Документ1.pdf
    │   └── Документ2.pdf
    ├── Папка2/
    │   ├── Документ3.pdf
    └── Документ4.pdf
```

Каждый PDF-файл в папке SCAN-PDF-АТМ будет "невыделяемой" версией оригинала.

## Примечание

Скрипт временно сохраняет изображения в формате PNG в папке PNG во время процесса конвертации. Эти временные файлы удаляются после завершения работы скрипта.

Пожалуйста, не стесняйтесь вносить свой вклад в этот проект или сообщать о любых обнаруженных проблемах. Наслаждайтесь использованием Конвертера PDF в "Невыделяемый" PDF!
