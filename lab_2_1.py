import os  # для работы с файловой системой

class MyFile:
    def __init__(self, filename, mode):
        self.filename = filename  # сохраняем имя файла
        self.mode = mode          # сохраняем режим работы
        self.content = ""         # здесь будем хранить содержимое файла
        
        # Проверяем, что режим корректен
        if mode not in ['read', 'write', 'append']:
            raise ValueError(f"Неправильный режим: {mode}. Допустимо: read, write, append")
    
    def read(self):
        # Проверяем режим
        if self.mode != 'read':
            raise ValueError(f"Для чтения используйте режим 'read', а не '{self.mode}'")
        
        # Проверяем существует ли файл
        if not os.path.exists(self.filename):
            raise FileNotFoundError(f"Файл {self.filename} не найден")
        
        # Открываем файл для чтения
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                self.content = file.read()  # читаем все содержимое
                return self.content         # возвращаем содержимое
        except Exception as e:
            raise Exception(f"Ошибка при чтении файла: {e}")
    
    def write(self, text):
        # Проверяем режим
        if self.mode not in ['write', 'append']:
            raise ValueError(f"Для записи используйте режим 'write' или 'append', а не '{self.mode}'")
        
        # Определяем как открывать файл
        # 'w' - перезаписать (write), 'a' - добавить в конец (append)
        file_mode = 'w' if self.mode == 'write' else 'a'
        
        # Открываем и записываем
        try:
            with open(self.filename, file_mode, encoding='utf-8') as file:
                file.write(text)  # записываем текст
            return f"Текст записан в файл {self.filename}"
        except Exception as e:
            raise Exception(f"Ошибка при записи в файл: {e}")
    
    def __str__(self):
        return f"MyFile: файл='{self.filename}', режим='{self.mode}'"


def main():
    print("\n1. Создаю тестовый файл...")
    with open("test.txt", "w", encoding="utf-8") as f:
        f.write("Первая строка\n")
        f.write("Вторая строка\n")
    print("Файл test.txt создан")
    
    print("\n2. Читаю файл...")
    try:
        # Создаем объект для чтения
        file1 = MyFile("test.txt", "read")
        
        # Читаем содержимое
        content = file1.read()
        
        # Выводим результат
        print(f"Прочитано из файла:\n{content}")
        print(f"Объект: {file1}")
        
    except Exception as e:
        print(f"Ошибка: {e}")
    
    print("\n3. Записываю в файл (перезапись)...")
    try:
        # Создаем объект для записи (перезаписи)
        file2 = MyFile("output.txt", "write")
        
        # Записываем текст
        result = file2.write("Это новый текст\nОн заменит всё содержимое файла")
        
        # Выводим результат
        print(f"{result}")
        print(f"Объект: {file2}")
        
    except Exception as e:
        print(f"Ошибка: {e}")
    
    print("\n4. Добавляю текст в конец файла...")
    try:
        # Создаем объект для добавления
        file3 = MyFile("output.txt", "append")
        
        # Добавляем текст
        result = file3.write("\nЭтот текст добавился в конец")
        
        # Выводим результат
        print(f"{result}")
        print(f"Объект: {file3}")
        
    except Exception as e:
        print(f"Ошибка: {e}")
    
    print("\n5. Показываю что получилось в output.txt...")
    if os.path.exists("output.txt"):
        with open("output.txt", "r", encoding="utf-8") as f:
            print(f"   Содержимое:\n{f.read()}")
    
    print("\n6. Демонстрация обработки ошибок...")
    
    # Неправильный режим
    print("a) Неправильный режим:")
    try:
        file_error = MyFile("test.txt", "wrong_mode")
    except ValueError as e:
        print(f"Поймана ошибка: {e}")
    
    # Чтение несуществующего файла
    print("b) Чтение несуществующего файла:")
    try:
        file_error = MyFile("не_существует.txt", "read")
        content = file_error.read()
    except FileNotFoundError as e:
        print(f"Поймана ошибка: {e}")
    
    # Попытка записать в режиме чтения
    print("c) Попытка записать в режиме чтения:")
    try:
        file_error = MyFile("test.txt", "read")
        file_error.write("Текст")
    except ValueError as e:
        print(f"Поймана ошибка: {e}")
    
    print("\n7. Удаляю тестовые файлы...")
    for filename in ["test.txt", "output.txt"]:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"   Файл {filename} удален")


if __name__ == "__main__":
    main()