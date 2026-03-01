import time


class PLAYER:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name


all_players = []
test_player1 = PLAYER(1, "ty_die")
test_player2 = PLAYER(2, "vosky")
test_player3 = PLAYER(3, "ram")


all_players.append(test_player1)
all_players.append(test_player2)
all_players.append(test_player3)


"""

ШАБЛОНЫ 

print()
print(f"{' ' * 8}  {' ' * 8}")

"""


print()
print(f"{' ' * 8} Тест поиска игроков {' ' * 8}")
time.sleep(1)
print()
print(f"{' ' * 8} Создание нового пользователя {' ' * 8}")
print()
print(f"{' ' * 8} Ведите имя пользователя {' ' * 8}")


print()
print(f"{' ' * 8} Пользователь записан в базу {' ' * 8}")

#   КВЕСТЫ
#
# Реализовать запись в базу данных в генерацией id на сервере
# Сделать проверку пользователя на уникальность по имени
