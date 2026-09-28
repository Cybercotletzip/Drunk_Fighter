import random

fighter_Denis = 100
fighter_Egor = 100

print(f"Пьянный бой начинается! {fighter_Denis}  Денис против {fighter_Egor} Егора \n")


def make_hit():
    hit = random.randint(1,5)
    return hit 


while fighter_Denis > 0 and fighter_Egor > 0:
  # 1. Ход Дениса
  denis_damage = make_hit()  # Сначала получаем урон и сохраняем в переменную
  fighter_Egor -= denis_damage
  print(
      f" Денис наносит {denis_damage} урона. У Егора осталось {max(0, fighter_Egor)} HP."
  )

  if fighter_Egor <= 0:
    break

  # 2. Ход Егора
  egor_damage = make_hit()  # Получаем урон для второго удара
  fighter_Denis -= egor_damage
  print(
      f" Егор отвечает и наносит {egor_damage} урона. У Дениса осталось {max(0, fighter_Denis)} HP."
  )
  print("-" * 40)

print("\n💀 БОЙ ЗАВЕРШЕН 💀")
if fighter_Denis > 0:
    print(f"🎉 Победил {fighter_Denis}!")
else:
    print(f"🎉 Победил {fighter_Egor}!")

    

    






