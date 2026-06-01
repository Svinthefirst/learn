class Alchemist:
    def __init__(self):
        self.elements = ["вода", "огонь", "земля", "ветер"]

        self.recipes = {
            ("вода", "огонь"): "чай",
            ("земля", "вода"): "болото",
            ("огонь", "земля"): "кирпич",
            ("ветер", "огонь"): "дым",
            ("дым", "вода"): "дождь",
            ("болото", "жизнь"): "лягушка",
            ("чай", "вода"): "жизнь",
            ("кирпич", "кирпич"): "дом",
            ("дом", "жизнь"): "человек",
            ("человек", "огонь"): "кузнец",
            ("кузнец", "кирпич"): "мастерская",
            ("человек", "дом"): "семья"
        }

    def show_elements(self):
        print("\nОткрытые элементы:")
        for item in self.elements:
            print("-", item)

    def show_recipes(self):
        print("\nИзвестные рецепты:")
        for (a, b), c in self.recipes.items():
            print(f"{a} + {b} = {c}")

    def combine(self, a, b):
        result = self.recipes.get((a, b))

        if result is None:
            result = self.recipes.get((b, a))

        if result is None:
            print("Ничего не получилось.")
            return

        if result in self.elements:
            print("Этот элемент уже открыт.")
            return

        self.elements.append(result)
        print(f"Получен новый элемент: {result}")

    def reset(self):
        self.elements = ["вода", "огонь", "земля", "ветер"]
        print("Прогресс очищен.")

    def play(self):
        print("=== АЛХИМИК ===")
        print("Команды: список, рецепты, сброс, выход")
        print("Для смешивания введите два элемента через пробел.")

        while True:
            command = input("\n> ").lower().strip()

            if command == "выход":
                print("Игра завершена.")
                break

            if command == "список":
                self.show_elements()
                continue

            if command == "рецепты":
                self.show_recipes()
                continue

            if command == "сброс":
                self.reset()
                continue

            parts = command.split()

            if len(parts) != 2:
                print("Неверная команда.")
                continue

            self.combine(parts[0], parts[1])

            if len(self.elements) >= 12:
                print("\nПоздравляем! Вы стали великим алхимиком!")
                break


if __name__ == "__main__":
    game = Alchemist()
    game.play()