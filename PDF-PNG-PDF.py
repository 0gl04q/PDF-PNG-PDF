import os
import shutil
import threading
from PIL import Image
from pathlib import Path
from pdf2image import convert_from_path
from reportlab.lib.pagesizes import landscape, A4
from reportlab.pdfgen import canvas

PATH_MAIN = os.path.join(os.getcwd(), 'PDF-ATM')
PATH_PNG = os.path.join(os.getcwd(), 'PNG')
PATH_PDF = os.path.join(os.getcwd(), 'SCAN-PDF-АТМ')


class FilePPP:
    """
        FilePPP - File PDF -> PNG -> PDF
    """

    def __init__(self, pdf_path, save_path, name):
        self.pdf_path = pdf_path
        self.save_path = save_path
        self.png_path = os.path.join(PATH_PNG, name + '.png')

    def convert_pdf_to_png(self):
        """
            Функция создания PNG на основе PDF файла
        """

        images = convert_from_path(f'{self.pdf_path}', dpi=300)
        images[0].save(self.png_path, 'PNG')

    def convert_png_to_pdf(self):
        """
            Функция создания PDF на основе PNG файла
        """

        # Вызываем создание PNG
        self.convert_pdf_to_png()

        # Выставляем размеры страницы A4
        width, height = landscape(A4)

        # Получаем размеры PNG из файла
        with Image.open(self.png_path) as img:
            image_width, image_height = img.size

        # Находим масштаб
        scale_x = image_width / width
        scale_y = image_height / height

        # Выбор минимального масштаба
        scale = min(scale_x, scale_y)

        # Создаем и сохраняем файл
        c = canvas.Canvas(self.save_path, pagesize=landscape(A4))
        c.drawImage(self.png_path, 0, 0, width * scale, height * scale)
        c.showPage()
        c.save()

        # Удаляем исходник
        os.remove(self.pdf_path)


def convert_file(pdf_file_obj):
    semaphore.acquire()  # Приобретаем семафор
    try:
        # Задаем путь к файлу и путь сохранения файл
        pdf_file_path = str(pdf_file_obj)
        pdf_file_save_path = os.path.join(PATH_PDF, str(pdf_file_obj).replace(PATH_MAIN, '').strip('\\'))

        # Проверка на существование файла
        if not os.path.exists(pdf_file_save_path):
            # Выполняем преобразование с экземпляром
            file = FilePPP(pdf_file_path, pdf_file_save_path, pdf_file_obj.name)
            try:
                file.convert_png_to_pdf()
                print(f'Файл создан: {pdf_file_save_path}')
            finally:
                # Удаляем временный файл
                os.remove(file.png_path)

    finally:
        semaphore.release()


def make_dir():
    """
        Функция создания необходимых и временных папок при включении программы
    """
    if not os.path.exists(PATH_PNG):
        os.mkdir(PATH_PNG)
    if not os.path.exists(PATH_PDF):
        os.mkdir(PATH_PDF)

    # Перебираем папки создания структуры
    for directory in filter(lambda d: d.is_dir(), Path(PATH_MAIN).rglob("*")):
        dir_in_tree = os.path.join(PATH_PDF, str(directory).replace(PATH_MAIN, '').strip('\\'))
        if not os.path.exists(dir_in_tree):
            os.mkdir(dir_in_tree)
            print(f'Папка создана: {dir_in_tree}')


if __name__ == '__main__':

    """
        Программа для преобразования PDF в "Невыделяемый" PDF файл на основе картинки страницы.
    """

    print('-' * 100)
    print('Запуск программы'.rjust(55))
    print('-' * 100)

    # Все объекты
    all_obj = Path(PATH_MAIN).rglob("*")

    # Создаем необходимые папки
    make_dir()

    max_threads = 5  # Выставляем количество потоков 5
    semaphore = threading.Semaphore(max_threads)
    threads = []

    try:
        # Перебираем файлы
        for pdf_file in filter(lambda f: f.is_file(), Path(PATH_MAIN).rglob("*")):
            # Создаем поток работы программы
            t = threading.Thread(target=convert_file, args=(pdf_file,))
            threads.append(t)
            t.start()

        # Ожидаем окончания всех потоков
        [thread.join() for thread in threads]

    finally:
        # Очистка папок временных файлов
        shutil.rmtree(PATH_PNG)

        print('-' * 100)
        print('Завершение работы программы'.rjust(60))
        print('-' * 100)
