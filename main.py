from classes import Game, BotBattlefield, DinoBattlefield

if __name__ == '__main__':

    the_game = Game()
    race_choice = the_game.start()
    if the_game.player_race == "Dinos":
        players_army = the_game.assemble_army(race_choice)
        enemies_army = the_game.assemble_enemies(race_choice)
        battlefield = DinoBattlefield()
        area = battlefield.area1
        battlefield.begin_dino_journey(area)
        rounds = the_game.rounds
        the_game.battle_start_for_dinosaurs(rounds, players_army, enemies_army)
        print("Good Game")

    elif the_game.player_race == "Robots":
        players_army = the_game.assemble_army(race_choice)
        enemies_army = the_game.assemble_enemies(race_choice)
        battlefield = BotBattlefield()

        area = battlefield.area1
        while area == battlefield.area1 or area == battlefield.area1a or area == battlefield.area2 or area == battlefield.area2a:
            if area == battlefield.area1:
                area = battlefield.begin_journey(area, players_army)

            if area == battlefield.area1a:
                area = battlefield.begin_journey(area, players_army)
            if area == battlefield.area2:
                area = battlefield.begin_journey2(area, players_army)
            if area == battlefield.area2a:
                area = battlefield.begin_journey2(area, players_army)
            if area == battlefield.area3:
                break
        area = battlefield.begin_journey3(area, players_army)

        rounds = the_game.rounds
        next_move = [False, battlefield.area3]
        while not the_game.end and players_army.race == "Robots":
            next_move = the_game.battle_start(rounds, players_army, enemies_army)
            if next_move == [False, battlefield.area2b]:
                area = battlefield.area2b
            if next_move == True:
                the_game.end = next_move
                break

            while area == battlefield.area1 or area == battlefield.area1a or area == battlefield.area2 or area == battlefield.area2a or next_move[1] == battlefield.area2b or area == battlefield.area_end:
                if area == battlefield.area1:
                    area = battlefield.begin_journey(area, players_army)

                if area == battlefield.area1a:
                    area = battlefield.begin_journey(area, players_army)
                if area == battlefield.area2:
                    area = battlefield.begin_journey2(area, players_army)
                if area == battlefield.area2a:
                    area = battlefield.begin_journey2(area, players_army)
                if area == battlefield.area2b:
                    area = battlefield.begin_journey2(area, players_army)
                if area == battlefield.area3:
                    area = battlefield.begin_journey3(area, players_army)
                if area == "battle":
                    break
                if area == battlefield.area_end:
                    the_game.end = True
                    break

        print("GOOD GAME")




















