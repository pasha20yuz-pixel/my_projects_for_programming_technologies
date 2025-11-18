import requests

def analyze_sports_from_content(content):
    """
    Анализирует данные из содержимого файла (строка) и определяет
    три самых популярных вида спорта по количеству объектов.
    """
    sports_count = {}
    
    # Разбиваем содержимое на строки
    lines = content.split('\n')
    
    for line in lines:
        # Разделяем строку по табуляции
        parts = line.strip().split('\t')
        
        # Проверяем, что в строке достаточно столбцов
        if len(parts) >= 4:
            sports_column = parts[3]  # столбец с видами спорта
            
            # Разделяем виды спорта по запятой и очищаем от лишних пробелов
            sports_list = [sport.strip() for sport in sports_column.split(',')]
            
            # Увеличиваем счетчик для каждого вида спорта
            for sport in sports_list:
                if sport:  # проверяем, что строка не пустая
                    sports_count[sport] = sports_count.get(sport, 0) + 1

    # Сортируем словарь по значениям в порядке убывания
    sorted_sports = [(x, sports_count[x]) for x in sorted(sports_count, key=sports_count.get, reverse=True)]
    # sorted(sports_count.items(), key=lambda x: x[1], reverse=True)
    
    # Возвращаем топ-3
    top_3 = sorted_sports[:3]
    return top_3

# Использование функции
url = "https://dfedorov.spb.ru/python3/sport.txt"
response = requests.get(url)
response.encoding = 'cp1251'  # Устанавливаем кодировку
    
if response.status_code == 200:
    top_sports = analyze_sports_from_content(response.text)
    
    if top_sports:
        print("\n" + "=" * 50)
        print("ТРИ САМЫХ ПОПУЛЯРНЫХ ВИДА СПОРТА:")
        print("=" * 50)
        for i, (sport, count) in enumerate(top_sports, 1):
            print(f"{i} МЕСТО: {sport} - {count} объектов")
else:
    print("Ошибка при загрузке файла")