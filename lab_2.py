
import requests  
import csv      
import matplotlib.pyplot as plt

def main():
    print("Начинаю загрузку данных о пенсиях...")
    url = "https://raw.githubusercontent.com/dm-fedorov/python_basic/master/data/opendata.stat"
    
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Ошибка! Не удалось скачать данные. Код ошибки: {response.status_code}")
            return
        text = response.text
        print("Данные успешно загружены")

    except Exception as e:
        print(f"Ошибка при загрузке данных: {e}")
        return
    
    months = []      
    pensions = []    
    
    reader = csv.reader(text.splitlines())
    next(reader)
    
    for row in reader:
        if len(row) < 4:
            continue 
            
        name = row[0]       # название показателя
        region = row[1]     # регион
        date = row[2]       # дата
        value = row[3]      # значение
        
        if "Средняя пенсия" not in name:
            continue

        if "Забайкальский" not in region:
            continue  
            
        if "2018" not in date:
            continue  

        try:
            pension_value = float(value)
        except:
            continue  
            
    
        month_str = date.split('-')[1]  # разделяем по "-" и берем вторую часть
        month = int(month_str)  # преобразуем в число
        
        # Добавляем данные в списки
        months.append(month)
        pensions.append(pension_value)
        
        # Выводим информацию о найденных данных
        print(f"  Найдено: {date} - {pension_value} руб.")
    

    if len(pensions) == 0:
        print("Не найдено данных о пенсиях в Забайкальском крае за 2018 год")
        return
    
    total = sum(pensions)
    average = total / len(pensions)
    

    print(f"Регион: Забайкальский край")
    print(f"Год: 2018")
    print(f"Количество записей: {len(pensions)}")
    print(f"Средняя пенсия: {average:.2f} руб.")
    
    # 6. СОРТИРУЕМ ДАННЫЕ ДЛЯ ГРАФИКА
    # Объединяем месяцы и пенсии в пары
    data_pairs = list(zip(months, pensions))
    
    # Сортируем по месяцам (от января к декабрю)
    data_pairs.sort(key=lambda x: x[0])
    
    # Разделяем обратно на списки
    sorted_months = [pair[0] for pair in data_pairs]
    sorted_pensions = [pair[1] for pair in data_pairs]
    
    print("\nСтрою график...")
    
    # Создаем новое окно для графика
    plt.figure(figsize=(10, 5))
    
    # Рисуем линию графика
    plt.plot(sorted_months, sorted_pensions, 'b-', linewidth=2, marker='o')
    
    # Добавляем заголовок и подписи осей
    plt.title('Изменение пенсии в Забайкальском крае в 2018 году', fontsize=14)
    plt.xlabel('Месяц')
    plt.ylabel('Размер пенсии, руб.')
    
    # Добавляем сетку для удобства чтения
    plt.grid(True, alpha=0.3)
    
    # Настраиваем деления на оси X (номера месяцев)
    plt.xticks(sorted_months)
    
    # Добавляем подписи значений над точками
    for month, pension in zip(sorted_months, sorted_pensions):
        plt.text(month, pension, f'{pension:.0f}', ha='center', va='bottom')
    
    # Добавляем горизонтальную линию средней пенсии
    plt.axhline(y=average, color='r', linestyle='--', 
                label=f'Средняя: {average:.2f} руб.')
    plt.legend()  # показываем легенду
    
    # Показываем график
    plt.tight_layout()
    plt.show()
    
    print("\nГрафик построен успешно!")
    print("Программа завершена.")

# Запускаем программу
if __name__ == "__main__":
    main()