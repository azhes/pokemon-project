import pygame
import pygame.locals
import random
from views import BattleView

class BattleController:
    """ Controls a pokemon battle. """

    FPS = 60

    def __init__(self, view, window, trainer_pokemon, rival_pokemon):
        self.view = view
        self.window = window
        self.view = view
        self.battle_run = True
        self.state = 'moves'
        self.trainer_pokemon = trainer_pokemon
        self.rival_pokemon = rival_pokemon
        self.from_pokemon = None
        self.to_pokemon = None
        self.first_effectiveness = None
        self.second_effectiveness = None

    def type_effectiveness(self, mv_type, def_type):
        """ Method for determining type effectiveness """
        effectiveness = {
            'fire': {
                'weakness': ['water'],
                'strength': ['grass', 'fire']
            },
            'water': {
                'weakness': ['grass', 'electric'],
                'strength': ['fire', 'water']
            },
            'grass': {
                'weakness': ['fire'],
                'strength': ['grass', 'electric', 'water']
            },
            'electric': {
                'weakness': ['water'],
                'strength': ['electric']
            },
            'ghost': {
                'weakness': ['ghost'],
                'strength': ['ghost']
            },
            'poison': {
                'weakness': ['psychic'],
                'strength': ['grass'],
            }
        }

        if mv_type in effectiveness[def_type]['weakness']:
            multiplier = 2
        elif mv_type in effectiveness[def_type]['strength']:
            multiplier = 0.5
        else:
            multiplier = 1

        return multiplier

    def calculate_damage(self, direction, mv_index):
        """ Calculates damage """
        if direction:
            from_pokemon = self.trainer_pokemon
            to_pokemon = self.rival_pokemon
        else:
            from_pokemon = self.rival_pokemon
            to_pokemon = self.trainer_pokemon
        move = from_pokemon.moves_list[mv_index]
        mv_type = move.type
        def_type = to_pokemon.type1
        power = move.power
        atk_type = self.trainer_pokemon.type1
        attack = self.trainer_pokemon.attack
        defense = self.trainer_pokemon.defense

        # 10% chance of a critical hit (double damage)
        critical_chance = random.randint(0, 9)
        if critical_chance == 9:
            critical = 2
        else: 
            critical = 1

        # determine type effectiveness
        effectiveness = self.type_effectiveness(mv_type, def_type)
        
        # STAB (Same Type Attack Bonus) If the pokemon's type is the same as the
        # type of the move it's using, then it deals 1.5x damage.
        if atk_type == mv_type:
            stab = 1.5
        else:
            stab = 1
        
        # calculate damage (adapted from https://bulbapedia.bulbagarden.net/wiki/Damage)
        damage = int((((((10 / 5) + 2) * power * (attack/defense))/50)+2) * stab * effectiveness * critical)

        return damage, effectiveness, critical

    def run(self):

        running = True
        start = pygame.time.get_ticks()
        clock = pygame.time.Clock()

        while self.trainer_pokemon.current_hp > 0 and self.rival_pokemon.current_hp > 0:
            clock.tick(self.FPS)
            
            # Show move selection
            while self.state == 'moves':
                self.view.show_moves()
                self.view.draw()
                self.view.update()
                for event in pygame.event.get():
                    if event.type == pygame.locals.QUIT:
                        pygame.quit()
                    elif event.type == pygame.locals.KEYDOWN:
                        if event.key == pygame.locals.K_ESCAPE:
                            pygame.quit()
                        if event.key == pygame.locals.K_1:
                            # If first move is selected
                            player_mv_index = 0
                            opponent_mv_index = random.randint(0, 1)    # Randomly select AI opponent's move
                            # Determine speed
                            if self.trainer_pokemon.speed > self.rival_pokemon.speed:
                                # If player's pokemon is faster
                                direction = True
                                self.from_pokemon = self.trainer_pokemon
                                self.to_pokemon = self.rival_pokemon
                                first_move = player_mv_index
                                second_move = opponent_mv_index
                            elif self.trainer_pokemon.speed < self.rival_pokemon.speed:
                                # If opponent's pokemon is faster
                                direction = False
                                self.from_pokemon = self.rival_pokemon
                                self.to_pokemon = self.trainer_pokemon
                                first_move = opponent_mv_index
                                second_move = player_mv_index
                            else:
                                # If both pokemon have equal speed
                                direction = random.choice([True, False])
                                self.from_pokemon = random.choice([self.trainer_pokemon, self.rival_pokemon])
                                if self.from_pokemon == self.trainer_pokemon:
                                    self.to_pokemon = self.rival_pokemon
                                    first_move = player_mv_index
                                    second_move = opponent_mv_index
                                else:
                                    self.to_pokemon = self.trainer_pokemon
                                    first_move = opponent_mv_index
                                    second_move = player_mv_index

                            # Faster pokemon attacks
                            if self.from_pokemon.current_hp > 0:
                                damage, self.first_effectiveness, first_critical = self.calculate_damage(direction, first_move)
                                self.to_pokemon.current_hp -= damage
                                if self.to_pokemon.current_hp <= 0:
                                    self.state = 'faint'

                                if self.to_pokemon == self.trainer_pokemon:
                                    self.view.update_player_HP()
                                    self.to_pokemon = self.rival_pokemon
                                    self.from_pokemon = self.trainer_pokemon
                                else:
                                    self.view.update_opponent_HP()
                                    self.to_pokemon = self.trainer_pokemon
                                    self.from_pokemon = self.rival_pokemon
                                    print(self.rival_pokemon.current_hp)

                            # Slower pokemon attacks
                            if self.from_pokemon.current_hp > 0:
                                damage, self.second_effectiveness, second_critical = self.calculate_damage(not direction, second_move)
                                
                                self.to_pokemon.current_hp -= damage
                                if self.to_pokemon.current_hp <= 0:
                                    self.state = 'faint'
                                if self.to_pokemon == self.trainer_pokemon:
                                    self.view.update_player_HP()
                                else:
                                    self.view.update_opponent_HP()
                                # Change game state and show the attacks in the textbox
                                self.state = 'first_attack'

                        elif event.key == pygame.locals.K_2:
                            # If the first move is selected
                            player_mv_index = 1
                            opponent_mv_index = random.randint(0, 1)    # Randomly choose the AI opponent's move
                            # Determine speed
                            if self.trainer_pokemon.speed > self.rival_pokemon.speed:
                                # If player's pokemon is faster
                                direction = True
                                self.from_pokemon = self.trainer_pokemon
                                self.to_pokemon = self.rival_pokemon
                                first_move = player_mv_index
                                second_move = opponent_mv_index
                            elif self.trainer_pokemon.speed < self.rival_pokemon.speed:
                                # If opponent's pokemon is faster
                                direction = False
                                self.from_pokemon = self.rival_pokemon
                                self.to_pokemon = self.trainer_pokemon
                                first_move = opponent_mv_index
                                second_move = player_mv_index
                            else:
                                # If both pokemon have the same speed
                                direction = random.choice([True, False])
                                self.from_pokemon = random.choice([self.trainer_pokemon, self.rival_pokemon])
                                if self.from_pokemon == self.trainer_pokemon:
                                    self.to_pokemon = self.rival_pokemon
                                    first_move = player_mv_index
                                    second_move = opponent_mv_index
                                else:
                                    self.to_pokemon = self.trainer_pokemon
                                    first_move = opponent_mv_index
                                    second_move = player_mv_index

                            # Faster pokemon attacks
                            if self.from_pokemon.current_hp > 0:
                                damage, self.first_effectiveness, first_critical = self.calculate_damage(direction, first_move)
                                self.to_pokemon.current_hp -= damage
                                if self.to_pokemon.current_hp <= 0:
                                    self.state = 'faint'
                                
                                if self.to_pokemon == self.trainer_pokemon:
                                    self.view.update_player_HP()
                                    self.to_pokemon = self.rival_pokemon
                                    self.from_pokemon = self.trainer_pokemon
                                else:
                                    self.view.update_opponent_HP()
                                    self.to_pokemon = self.trainer_pokemon
                                    self.from_pokemon = self.rival_pokemon
                            
                            # Slower pokemon attacks
                            if self.from_pokemon.current_hp > 0:
                                damage, self.second_effectiveness, second_critical = self.calculate_damage(not direction, second_move)
                                self.to_pokemon.current_hp -= damage
                                if self.to_pokemon.current_hp <= 0:
                                    self.state = 'faint'
                                
                                if self.to_pokemon == self.trainer_pokemon:
                                    self.view.update_player_HP()
                                else:
                                    self.view.update_opponent_HP()

                                self.state = 'first_attack'

                self.view.draw()
                self.view.update()
            
            while self.state == 'first_attack':
                # show the first attack
                self.view.show_attack(self.to_pokemon.nickname, self.to_pokemon.moves_list[first_move].name, self.first_effectiveness, first_critical)
                for event in pygame.event.get():
                    if event.type == pygame.locals.QUIT:
                        pygame.quit()
                    elif event.type == pygame.locals.KEYDOWN:
                        if event.key == pygame.locals.K_ESCAPE:
                            pygame.quit()
                        if event.key == pygame.locals.K_RETURN:
                            self.state = 'second_attack'

                self.view.draw()
                self.view.update()

            while self.state == 'second_attack':
                # show the second attack
                self.view.show_attack(self.from_pokemon.nickname, self.from_pokemon.moves_list[second_move].name, self.second_effectiveness, second_critical)
                for event in pygame.event.get():
                    if event.type == pygame.locals.QUIT:
                        pygame.quit()
                    elif event.type == pygame.locals.KEYDOWN:
                        if event.key == pygame.locals.K_ESCAPE:
                            pygame.quit()
                        if event.key == pygame.locals.K_RETURN:
                            self.state = 'moves'

                self.view.draw()
                self.view.update()
        
        # Determines if a pokemon has fainted
        if self.trainer_pokemon.current_hp <= 0:
            fainted_pokemon = self.trainer_pokemon
            result = 0
        if self.rival_pokemon.current_hp <= 0:
            fainted_pokemon = self.rival_pokemon
            result = 1

        while running:
            # Shows the fainted pokemon
            self.state = 'faint'
            while self.state == 'faint':
                self.view.show_faint(fainted_pokemon.nickname)
                for event in pygame.event.get():
                        if event.type == pygame.locals.QUIT:
                            pygame.quit()
                        elif event.type == pygame.locals.KEYDOWN:
                            if event.key == pygame.locals.K_ESCAPE:
                                pygame.quit()
                            if event.key == pygame.locals.K_RETURN:
                                self.state = 'result'
                self.view.draw()
                self.view.update()
            
            while self.state == 'result':
                # Shows whether the player won or lost
                self.view.show_result(result)
                for event in pygame.event.get():
                        if event.type == pygame.locals.QUIT:
                            pygame.quit()
                        elif event.type == pygame.locals.KEYDOWN:
                            if event.key == pygame.locals.K_ESCAPE:
                                pygame.quit()
                
                self.view.draw()
                self.view.update()
