CATEGORIES = [
    "Работа",
    "Здоровье",
    "Путешествия",
    "Образование",
    "Недвижимость (дом, квартира)",
    "Развлечения",
]


class Goal:
    def __init__(self, name, target_amount, category):
        self.name = name
        self.target_amount = target_amount
        self.current_balance = 0
        self.category = category
        self.status = "в работе"

    def add_amount(self, amount):
        if self.current_balance + amount <= self.target_amount:
            self.current_balance += amount
            print(
                f"Успешно пополнено. Баланс: {self.current_balance} из {self.target_amount}"
            )
            # <-- Проверка статуса ПОСЛЕ успешного пополнения
            if self.current_balance >= self.target_amount:
                self.status = "выполнена"
        else:
            print("Ошибка: пополнение превысит итоговую сумму цели!")

    def subtract_amount(self, amount):
        if self.current_balance >= amount:
            self.current_balance -= amount
            print(f"Успешно снято. Баланс: {self.current_balance}")
            # <-- При снятии статус может снова стать «активна»
            if self.current_balance < self.target_amount:
                self.status = "активна"
        else:
            print("Ошибка: недостаточно средств на балансе цели!")

    def get_progress_percent(self):
        if self.target_amount == 0:
            return 0
        return (self.current_balance / self.target_amount) * 100


goals = []


def add_goal():
    name = input("Название цели: ")
    target_amount = float(input("Итоговая сумма: "))
    print("Доступные категории:")
    for i, category in enumerate(CATEGORIES, 1):
        print(f"{i}. {category}")
    while True:
        category_choice = input(
            "Выберите номер категории (1-{}): ".format(len(CATEGORIES))
        )
        if category_choice.isdigit() and 1 <= int(category_choice) <= len(CATEGORIES):
            category = CATEGORIES[int(category_choice) - 1]
            break
        else:
            print(f"Ошибка: введите число от 1 до {len(CATEGORIES)}")
    goal = Goal(name, target_amount, category)
    goals.append(goal)
    print(f"Цель '{name}' добавлена в категорию '{category}'!")


while True:
    print("\n--- МЕНЮ КОПИЛКИ ---")
    print("1. Добавить новую цель")
    print("2. Посмотреть все цели")
    print("3. Выйти")
    print("4. Пополнить баланс цели")
    print("5. Снять средства с цели")
    print("6. Посмотреть цели по категории")
    print("7. Удалить цель")  # <-- Новый пункт меню

    choice = input("\nВыберите действие (1-7): ")  # <-- Изменено на 1-7

    if choice == "1":
        add_goal()
    elif choice == "2":
        if goals:
            for goal in goals:
                progress = goal.get_progress_percent()
                print(
                    f"Цель: {goal.name} | Категория: {goal.category} | Баланс: {goal.current_balance}/{goal.target_amount} | Прогресс: {progress:.1f}% | Статус: {goal.status}"
                )
        else:
            print("Список целей пуст.")
    elif choice == "3":
        print("До свидания!")
        break
    elif choice == "4":
        goal_name = input("Введите название цели для пополнения: ").strip()
        goal_found = False
        for goal in goals:
            if goal.name.lower() == goal_name.lower():
                amount = float(input("Введите сумму для пополнения: "))
                goal.add_amount(amount)
                goal_found = True
                break
        if not goal_found:
            print("Цель не найдена.")
    elif choice == "5":
        goal_name = input("Введите название цели для снятия: ").strip()
        goal_found = False
        for goal in goals:
            if goal.name.lower() == goal_name.lower():
                amount = float(input("Введите сумму для снятия: "))
                goal.subtract_amount(amount)
                goal_found = True
                break
        if not goal_found:
            print("Цель не найдена.")
    elif choice == "6":
        print("Доступные категории:")
        for i, category in enumerate(CATEGORIES, 1):
            print(f"{i}. {category}")
        category_choice = input(
            "Выберите номер категории для просмотра (1-{}): ".format(len(CATEGORIES))
        )
        if category_choice.isdigit() and 1 <= int(category_choice) <= len(CATEGORIES):
            selected_category = CATEGORIES[int(category_choice) - 1]
            print(f"\n--- ЦЕЛИ В КАТЕГОРИИ '{selected_category}' ---")
            found = False
            for goal in goals:
                if goal.category == selected_category:
                    progress = goal.get_progress_percent()
                    print(
                        f"Цель: {goal.name} | Баланс: {goal.current_balance}/{goal.target_amount} | Прогресс: {progress:.1f}% | Статус: {goal.status}"
                    )
                    found = True
            if not found:
                print("В этой категории целей нет.")
        else:
            print(f"Ошибка: введите число от 1 до {len(CATEGORIES)}")
    elif choice == "7":  # <-- НОВЫЙ БЛОК ДЛЯ УДАЛЕНИЯ ЦЕЛИ
        if not goals:
            print("Список целей пуст. Удалять нечего.")
            continue

        print("\n--- СПИСОК ЦЕЛЕЙ ДЛЯ УДАЛЕНИЯ ---")
        for i, goal in enumerate(goals, 1):
            progress = goal.get_progress_percent()
            print(
                f"{i}. {goal.name} | Категория: {goal.category} | Прогресс: {progress:.1f}%"
            )

        # <-- ВАЖНО: while True должен быть на том же уровне отступа, что и elif
        while True:
            try:
                choice_num = int(
                    input("\nВведите номер цели для удаления (0 — отмена): ")
                )

                if choice_num == 0:
                    print("Удаление отменено.")
                    break

                # Проверяем, что номер в пределах списка целей
                if 1 <= choice_num <= len(goals):
                    removed_goal = goals.pop(choice_num - 1)
                    print(f"Цель '{removed_goal.name}' успешно удалена!")
                    break
                else:
                    # Если число не 0 и не попадает в диапазон целей
                    print(
                        f"Ошибка: введите число от 1 до {len(goals)} или 0 для отмены."
                    )

            except ValueError:
                print("Ошибка: пожалуйста, введите число!")
