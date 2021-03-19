from classes import Dinosaurs, Robots, Game, Herd, Fleet, BotBattlefield, DinoBattlefield, Weapon

if __name__ == '__main__':

    the_game = Game()
    race_choice = the_game.start()
    if the_game.player_race == "Dinos":
        players_army = the_game.assemble_army(race_choice)
        enemies_army = the_game.assemble_enemies(race_choice)
        battlefield = DinoBattlefield()
    elif the_game.player_race == "Robots":
        players_army = the_game.assemble_army(race_choice)
        enemies_army = the_game.assemble_enemies(race_choice)
        battlefield = BotBattlefield()

        area = battlefield.area1
        area = battlefield.begin_journey(area, players_army)
        area = battlefield.begin_journey2(area, players_army)
        if area == battlefield.area1a:
            area = battlefield.begin_journey(area, players_army)
            area = battlefield.begin_journey2(area, players_army)
            area = battlefield.begin_journey3(area, players_army)
        else:
            area = battlefield.begin_journey3(area, players_army)
    rounds = the_game.rounds
    while not the_game.end:
        the_game.battle_start(rounds, players_army, enemies_army)

    print("WIN")




















