import random

#Gamer
#Используем словарь для хранения информации о игроке
player = {
    "name": "Player",
    "health": 100,
    "attack": 10,
    "inventory": ["sword", "potion"]
}

#events in dungeon
EVENTS = ["monster","chest","empty"]

def handle_event(event: str) -> None:
    ##Обработка событий в подземелье
    if event == "monster":
        damage = random.randint(5, 20)
        player["health"] -= damage
        print(f"You hangout with monster and lost {damage} health")
    
    elif event == "chest":
        loot = random.choice(["gold", "sword", "magical shield"])
        player["inventory"].append(loot)
        print(f"You found {loot} in the chest! Now you have {', '.join(player['inventory'])}")

    else:
        print("You found nothing.")

def game_loop() -> None:
    """Основной цикл игры"""
    print("Welcome to the dungeon, {player['name']}! ")
    print(f"Your mission - come to the end,avoid monsters.\n")

    steps = 0
    while player["health"] > 0 and steps < 10:
        input("\nPress Enter to move...")
        event = random.choice(EVENTS)
        handle_event(event)
        steps += 1
        print(f"<3 HP: {player['health']} | step: {steps}/10")

#Finish of the game
    if player["health"] <= 0:
        print("\nYou died in the dungeon. Game over.")
    else:
        print("\nCongratulations! You've reached the end of the dungeon.")

if __name__ == "__main__":
    game_loop()