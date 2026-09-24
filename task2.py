class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = set(can_teach_subjects)
        self.assigned_subjects = set()  # Предмети, які буде закріплено за викладачем

def create_schedule(subjects, teachers):
    """
    Жадібний алгоритм для складання розкладу занять.
    """
    uncovered_subjects = set(subjects)
    schedule = []

    # Поки є непокриті предмети
    while uncovered_subjects:
        best_teacher = None
        best_cover = set()

        for teacher in teachers:
            # З'ясовуємо, скільки ще непокритих предметів може взяти цей викладач
            potential_cover = teacher.can_teach_subjects & uncovered_subjects
            
            # Якщо викладач не може взяти жодного нового предмета — пропускаємо
            if not potential_cover:
                continue
            
            # Критерії жадібного вибору
            if best_teacher is None:
                best_teacher = teacher
                best_cover = potential_cover
            else:
                # 1. Пріоритет: найбільша кількість непокритих предметів
                if len(potential_cover) > len(best_cover):
                    best_teacher = teacher
                    best_cover = potential_cover
                # 2. Пріоритет (при однаковій кількості предметів): наймолодший викладач
                elif len(potential_cover) == len(best_cover):
                    if teacher.age < best_teacher.age:
                        best_teacher = teacher
                        best_cover = potential_cover

        # Якщо ми пройшли всіх викладачів, але так і не знайшли кандидата
        # для покриття предметів, що залишились
        if best_teacher is None:
            return None

        # Призначаємо знайдені предмети обраному викладачу
        best_teacher.assigned_subjects = best_cover
        schedule.append(best_teacher)
        
        # Видаляємо покриті предмети з пулу непокритих
        uncovered_subjects -= best_cover

    return schedule

if __name__ == '__main__':
    # Множина предметів
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}
    
    # Створення списку викладачів
    teachers = [
        Teacher('Олександр', 'Іваненко', 45, 'o.ivanenko@example.com', {'Математика', 'Фізика'}),
        Teacher('Марія', 'Петренко', 38, 'm.petrenko@example.com', {'Хімія'}),
        Teacher('Сергій', 'Коваленко', 50, 's.kovalenko@example.com', {'Інформатика', 'Математика'}),
        Teacher('Наталія', 'Шевченко', 29, 'n.shevchenko@example.com', {'Біологія', 'Хімія'}),
        Teacher('Дмитро', 'Бондаренко', 35, 'd.bondarenko@example.com', {'Фізика', 'Інформатика'}),
        Teacher('Олена', 'Гриценко', 42, 'o.grytsenko@example.com', {'Біологія'})
    ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")