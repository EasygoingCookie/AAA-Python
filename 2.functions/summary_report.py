# Реализация выгрузки сводного отчета по департаментам

def csv_to_list(filename: str) -> list:
    """Считывание данных из csv-файла в двумерный список"""
    result = []
    with open(filename, 'r', encoding='utf8') as file:
        lines = file.readlines()
    for element in lines:
        result.append(element.strip().split(';'))
    return result


def write_csv(report: list, filename: str):
    """Запись двумерного списка в табличном виде в csv-файл"""
    f = open(filename, 'w', encoding='utf8')
    for element in report:
        line = ';'.join(element)
        f.write(f'{line}\n')


def print_array_as_a_table(input_data: list,
                           distance: int = 10,
                           head_sep: str = '-',
                           column_sep: str = ''
                           ) -> None:
    """
    Печать в консоль думерного списка в читаемом виде
    -------------------------------------------------
    Параметры:
    ----------
    input_data - двумерный список данных, который выводим на экран
    distance - расстояние между столбами (10 по умолчанию)
    head_sep - разделитель "шапки" таблицы ('-' по умолчанию)
    column_sep - разделитель столбцов (по умолчанию без него)
    """
    lengths = []
    for column in zip(*input_data):
        lengths.append(max([len(str(word)) for word in column]))
    counter = 0
    for head in input_data[0]:
        print(f'{head}' +
              ' ' * (lengths[counter] - len(str(head)) + distance // 2) +
              column_sep + ' ' * (distance // 2),
              end=''
              )
        counter += 1
    print()
    print(f'{head_sep}' * (sum(lengths) + distance * len(lengths)))
    for column in input_data[1:]:
        counter = 0
        for word in column:
            print(f'{word}' +
                  ' ' * (lengths[counter] - len(str(word)) + distance // 2) +
                  column_sep + ' ' * (distance // 2),
                  end=''
                  )
            counter += 1
        print()


def print_dict_as_a_hierarchy(input_dict: dict) -> None:
    """Печать словаря в виде иерархий"""
    for key, value in input_dict.items():
        print('---'f'{key}')
        for team in value:
            print('     ---'f'{team}')


def transform_array_to_dict(array: list) -> dict:
    """
    Перевод думерного списка в словарь.
    Ключи - нулевые элементы каждого списка
    Значения - списки из элементов с 1 по n
    """
    result = {}
    for element in zip(*array):
        result[element[0]] = list(element[1:])
    return result


def transform_dict_to_array(input_dict: dict) -> list:
    """
    Перевод словаря (со списками в значениях) в двумерный список
    Каждый ключ становится нулевым элементом существющих списков
    """
    result = []
    for key, value in input_dict.items():
        result.append([key, *value])
    return result


def department_teams(departments: list, teams: list) -> dict:
    """Создание словаря Департамент -> Список команд, входящих в него"""
    result = {}
    for i in range(len(departments)):
        if departments[i] in result.keys():
            result[departments[i]].append(teams[i])
        else:
            result[departments[i]] = [teams[i]]
    for key, value in result.items():
        result[key] = list(set(value))
    return result


def department_salaries(departments: list, salaries: list) -> list:
    """
    Создание словаря
    Департамент -> [Численность, Вилка, Средняя зп]
    """
    header = [['Департамент', 'Численность', 'Вилка', 'Средняя зп']]
    salary_dict = {}
    for i in range(len(departments)):
        if departments[i] in salary_dict.keys():
            salary_dict[departments[i]].append(int(salaries[i]))
        else:
            salary_dict[departments[i]] = [int(salaries[i])]
    for key, value in salary_dict.items():
        salary_dict[key] = [str(len(value)),
                            str(min(value)) + ' - ' + str(max(value)),
                            str(round(sum(value) / len(value), 3))]
    result = transform_dict_to_array(salary_dict)
    return header + result


def main():
    """Главное меню. Реализация команд"""
    data = csv_to_list('Corp_Summary.csv')
    data_dict = transform_array_to_dict(data)
    option = ''
    options = [1, 2, 3]
    while option not in options:
        print('Выберите необходимую команду: {}, {} или {} \n'
              '1 - выводит департаменты со всеми входящими в него командами\n'
              '2 - выводит сводный отчет по департаментам с инфой по зп\n'
              '3 - сохраняет сводный отчет из п.2 в csv-файл'.format(*options))
        option = int(input())
    if option == 1:
        teams = department_teams(data_dict['Департамент'], data_dict['Отдел'])
        print_dict_as_a_hierarchy(teams)
    elif option == 2:
        dep = department_salaries(data_dict['Департамент'], data_dict['Оклад'])
        print_array_as_a_table(dep)
    else:
        print('Сводный отчет выгружен в файл Dep_summary.csv')
        dep = department_salaries(data_dict['Департамент'], data_dict['Оклад'])
        write_csv(dep, 'Dep_Summary.csv')


if __name__ == '__main__':
    main()
