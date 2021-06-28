game_level = 3

enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]

# Since there is no block scope, I can use new_enemies even though new_enemy is defined inside if block.
print(new_enemy)

level = 1
if level < 2:
    n = 1
print(n)
