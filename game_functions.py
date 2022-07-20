import pokemon as pkmn
import moves
import time
import sys
import random


# 1. Game Functions:
def initialize_blue_party():
    global blue_party
    blue_party = {}
    blue_movesets = {}

    # format: name, type, category, moveType, PP, power, accuracy, effect
    blue_movesets["Pidgeot"] = {
        1: moves.Moves("Aerial Ace", "flying", "physical", "damaging", 20, 60, None, "bypass accuracy"),
        2: moves.Moves("Sand-Attack", "ground", "status", "opponent", 15, -1, 1, "accuracy"),
        3: moves.Moves("Feather Dance", "flying", "status", "opponent", 15, -2, 1, "attack"),
        4: moves.Moves("Whirlwind", "normal", "status", "opponent switch", 20, 1, 1, "switchOut")}

    blue_movesets["Rhydon"] = {
        1: moves.Moves("Stone Edge", "rock", "physical", "damaging", 5, 80, 0.8, None),
        2: moves.Moves("Take Down", "normal", "physical", "damaging", 20, 90, 0.85, "recoil", None, 1 / 4),
        3: moves.Moves("Scary Face", "normal", "status", "opponent", 10, -2, 1, "speed"),
        4: moves.Moves("Earthquake", "ground", "physical", "damaging", 10, 100, 1, None)}

    blue_movesets["Arcanine"] = {
        1: moves.Moves("Flamethrower", "fire", "special", "damaging", 15, 95, 1, None),
        2: moves.Moves("ExtremeSpeed", "normal", "physical", "damaging", 5, 80, 1, "attack first"),
        3: moves.Moves("Bite", "dark", "physical", "damaging", 25, 60, 1, None),
        4: moves.Moves("Roar", "normal", "status", "opponent switch", 20, 1, 1, "switchOut")}

    blue_movesets["Blastoise"] = {
        1: moves.Moves("Ice Beam", "ice", "special", "damaging", 10, 95, 1, None),
        2: moves.Moves("Hydro Pump", "water", "special", "damaging", 5, 120, 0.8, None),
        3: moves.Moves("Bite", "dark", "physical", "damaging", 25, 60, 1, None),
        4: moves.Moves("Surf", "water", "special", "damaging", 15, 90, 1, None)}

    blue_movesets["Exeggutor"] = {
        1: moves.Moves("Giga Drain", "grass", "special", "damaging", 10, 60, 1, "lifesteal", None, 1 / 2),
        2: moves.Moves("Egg Bomb", "normal", "physical", "damaging", 10, 100, 0.75, None),
        3: moves.Moves("Psychic", "psychic", "special", "damaging", 10, 90, 1, None),
        4: moves.Moves("Double Team", "normal", "status", "self", 15, 1, None, "evasion")}

    blue_movesets["Alakazam"] = {
        1: moves.Moves("Psychic", "psychic", "special", "damaging", 10, 90, 1, None),
        2: moves.Moves("Calm Mind", "psychic", "status", "self", 20, 2, 1, "sp_atk"),
        3: moves.Moves("Shadow Ball", "ghost", "special", "damaging", 15, 80, 1, None),
        4: moves.Moves("Recover", "normal", "status", "self", 20, 0.5, 1, "heal")}

    # Format: name, hp, atk, defense, sp_atk, sp_def, speed, accuracy, moveSet, type1, type2
    blue_party[1] = pkmn.CreatePokemon("Pidgeot", 190, 145, 139, 134, 134, 157, blue_movesets["Pidgeot"], "normal",
                                       "flying")
    blue_party[2] = pkmn.CreatePokemon("Rhydon", 212, 200, 189, 106, 106, 101, blue_movesets["Rhydon"], "ground",
                                       "rock")
    blue_party[3] = pkmn.CreatePokemon("Arcanince", 197, 178, 145, 167, 145, 161, blue_movesets["Arcanine"], "fire",
                                       "fire")
    blue_party[4] = pkmn.CreatePokemon("Blastoise", 186, 148, 167, 150, 172, 130, blue_movesets["Blastoise"], "water",
                                       "water")
    blue_party[5] = pkmn.CreatePokemon("Exeggutor", 202, 161, 150, 194, 128, 117, blue_movesets["Exeggutor"], "grass",
                                       "psychic")
    blue_party[6] = pkmn.CreatePokemon("Alakazam", 162, 112, 106, 205, 150, 189, blue_movesets["Alakazam"], "psychic",
                                       "psychic")


def initialize_red_party():
    global red_party
    red_party = {}
    red_movesets = {}

    # format: name, type, category, moveType, PP, power, accuracy, effect
    red_movesets["Charizard"] = {
        1: moves.Moves("Flamethrower", "fire", "special", "damaging", 15, 95, 1, None),
        2: moves.Moves("Aerial Ace", "flying", "physical", "damaging", 20, 60, None, "bypass accuracy"),
        3: moves.Moves("Dragon Claw", "dragon", "physical", "damaging", 15, 80, 1, None),
        4: moves.Moves("Earthquake", "ground", "physical", "damaging", 10, 100, 1, None)}

    red_movesets["Lapras"] = {
        1: moves.Moves("Ice Beam", "ice", "special", "damaging", 10, 95, 1, None),
        2: moves.Moves("Surf", "water", "special", "damaging", 15, 90, 1, None),
        3: moves.Moves("Thunderbolt", "electric", "special", "damaging", 15, 95, 1, None),
        4: moves.Moves("Psychic", "psychic", "special", "damaging", 10, 90, 1, None)}

    red_movesets["Jolteon"] = {
        1: moves.Moves("Thunderbolt", "electric", "special", "damaging", 15, 95, 1, None),
        2: moves.Moves("Thunder", "electric", "special", "damaging", 5, 120, 0.7, None),
        3: moves.Moves("Flash", "normal", "status", "opponent", 20, -1, 1, "accuracy"),
        4: moves.Moves("Shadow Ball", "ghost", "special", "damaging", 15, 80, 1, None)}

    red_movesets["Primape"] = {
        1: moves.Moves("Cross Chop", "fighting", "physical", "damaging", 5, 100, 0.8, None),
        2: moves.Moves("Aerial Ace", "flying", "physical", "damaging", 20, 60, None, "bypass accuracy"),
        3: moves.Moves("Bulk Up", "fighting", "status", "self", 15, 1, None, "attack"),
        4: moves.Moves("Thunder Punch", "electric", "physical", "damaging", 15, 75, 1, None)}

    red_movesets["Nidoking"] = {
        1: moves.Moves("Megahorn", "bug", "physical", "damaging", 10, 120, 0.85, None),
        2: moves.Moves("Sludge Bomb", "poison", "special", "damaging", 10, 90, 1, None),
        3: moves.Moves("Earthquake", "ground", "physical", "damaging", 10, 100, 1, None),
        4: moves.Moves("Shadow Ball", "ghost", "special", "damaging", 15, 80, 1, None)}

    red_movesets["Dragonite"] = {
        1: moves.Moves("Dragon Claw", "dragon", "physical", "damaging", 15, 80, 1, None),
        2: moves.Moves("Double Team", "normal", "status", "self", 15, 1, None, "evasion"),
        3: moves.Moves("Fly", "flying", "physical", "damaging", 15, 90, 0.95, None),
        4: moves.Moves("Dragon Rush", "dragon", "physical", "damaging", 5, 110, 0.75, None)}

    # Format: name, hp, atk, defense, sp_atk, sp_def, speed, accuracy, moveSet, type1, type2
    red_party[3] = pkmn.CreatePokemon("Charizard", 162, 115, 109, 140, 116, 131, red_movesets["Charizard"], "fire",
                                      "flying")
    red_party[2] = pkmn.CreatePokemon("Lapras", 214, 116, 111, 116, 126, 91, red_movesets["Lapras"], "water", "ice")
    red_party[1] = pkmn.CreatePokemon("Jolteon", 200, 96, 91, 141, 126, 162, red_movesets["Jolteon"], "electric",
                                      "electric")
    red_party[4] = pkmn.CreatePokemon("Primape", 149, 136, 91, 91, 101, 126, red_movesets["Primape"], "fighting",
                                      "fighting")
    red_party[5] = pkmn.CreatePokemon("Nidoking", 165, 123, 107, 116, 106, 116, red_movesets["Nidoking"], "poison",
                                      "ground")
    red_party[6] = pkmn.CreatePokemon("Dragonite", 175, 165, 126, 131, 131, 111, red_movesets["Dragonite"], "dragon",
                                      "flying")


def initialize_battle():
    print("*Input (-1) to return to previous menu during the game*")
    initialize_blue_party()
    initialize_red_party()
    global red_active_pokemon
    global blue_active_pokemon
    global red_active_pokemon_directory
    global blue_active_pokemon_directory
    red_active_pokemon = red_party[1]
    blue_active_pokemon = blue_party[1]
    red_active_pokemon_directory = 1
    blue_active_pokemon_directory = 1
    intro_dialogue()


def red_turn():
    while True:
        action = red_action()
        if action.upper() == "FIGHT":
            selected_move = red_fight()
            if selected_move != -1:
                return [action.upper(), selected_move]

        elif action.upper() == "POKEMON":
            swap_choice = red_swap()
            if swap_choice in red_party.keys():
                return [action.upper(), swap_choice]

        elif action.upper() == "RUN":
            write(0.03, "There's no running from a Trainer battle!")


def red_action():
    write(0.03, "What will " + red_active_pokemon.getName() + " do? (FIGHT, POKéMON, RUN) ")
    action = input()
    return action


def red_swap():
    while True:
        write(0.03, "Which Pokémon would you like to switch with?")
        for i in range(1, len(red_party) + 1):
            if red_party[i].getStatus() == "(fainted)":
                if red_party[i].getType1() == red_party[i].getType2():
                    print("[" + str(i) + "]. " + red_party[i].getName() + " (Type: " + red_party[
                        i].getType1().capitalize() + ")(Fainted)")
                else:
                    print("[" + str(i) + "]. " + red_party[i].getName() + " (Type: " + red_party[
                        i].getType1().capitalize() + ", " +
                          red_party[i].getType2().capitalize() + ")(Fainted)")
            else:
                if red_party[i].getType1() == red_party[i].getType2():
                    print("[" + str(i) + "]. " + red_party[i].getName() + " (HP: " + str(
                        red_party[i].getHP_percentage()) + "%, Type: " + red_party[i].getType1().capitalize() + ")")
                else:
                    print("[" + str(i) + "]. " + red_party[i].getName() + " (HP: " + str(
                        red_party[i].getHP_percentage()) + "%, Type: " + red_party[i].getType1().capitalize() + ", " +
                          red_party[i].getType2().capitalize() + ")")

        swap_choice = int(input())
        if swap_choice == -1:
            return swap_choice
        elif swap_choice == red_active_pokemon_directory:
            write(0.03, "This Pokémon is already in battle.")
        elif red_party[swap_choice].getStatus() == "(fainted)":
            write(0.03, "This pokemon has fainted and can no longer battle!")
        else:
            return swap_choice


def red_fight():
    moveData()
    selected_move_num = int(input())
    if selected_move_num == -1:
        return selected_move_num
    selected_move = red_active_pokemon.getMoveSet()[selected_move_num]
    red_active_pokemon.getMoveSet()[selected_move_num].changePP(-1)
    return selected_move


def blue_turn():
    damaging_moves = []
    non_damaging_moves = []
    for i in range(1, 5):
        if blue_active_pokemon.getMoveSet()[i].getMoveType() == "damaging":
            damaging_moves.append(blue_active_pokemon.getMoveSet()[i])
        else:
            non_damaging_moves.append(blue_active_pokemon.getMoveSet()[i])
    if damaging_moves == []:
        moveType = "non damaging"
    elif non_damaging_moves == []:
        moveType = "damaging"
    else:
        moveType_random = random.randint(1, 100)
        if moveType_random <= 70:
            moveType = "damaging"
        elif moveType_random > 70:
            moveType = "non damaging"

    if moveType == "damaging":
        moveChoice = random.randint(0, len(damaging_moves) - 1)
        selected_move = damaging_moves[moveChoice]
    else:
        moveChoice = random.randint(0, len(non_damaging_moves) - 1)
        selected_move = non_damaging_moves[moveChoice]

    return selected_move


def first_move_order(red_choice, blue_choice):
    red_speed = red_active_pokemon.getSpeed() * general_stage_multiplier(red_active_pokemon.getSpeedStage())
    blue_speed = blue_active_pokemon.getSpeed() * general_stage_multiplier(blue_active_pokemon.getSpeedStage())
    if red_choice[0] == "POKEMON":
        return "red"
    elif red_choice[0] == "FIGHT":
        if red_choice[1].getEffect() == "attack first" and blue_choice.getEffect() == "attack first":
            if red_speed > blue_speed:
                return "red"
            elif blue_speed > red_speed:
                return "blue"
            elif red_speed == blue_speed:
                return random.choice(["red", "blue"])

        elif red_choice[1].getEffect() == "attack first":
            return "red"

        elif blue_choice.getEffect() == "attack first":
            return "blue"

        elif red_speed > blue_speed:
            return "red"

        elif blue_speed > red_speed:
            return "blue"

        elif red_speed == blue_speed:
            return random.choice(["red", "blue"])


def second_move_order(first_move_order):
    if first_move_order == "red":
        return "blue"
    elif first_move_order == "blue":
        return "red"


def switchPokemon(team, active_pokemon_directory, active_pokemon, switch_target_directory, skip_call_back=False):
    if team == "red":
        global red_active_pokemon
        global red_active_pokemon_directory
        if skip_call_back is False:
            write(0.03, active_pokemon.getName() + ", come back!")
        red_party[active_pokemon_directory].resetStages()
        red_active_pokemon = red_party[switch_target_directory]
        red_active_pokemon_directory = switch_target_directory
        write(0.03, "Go! " + red_active_pokemon.getName() + "!\n")

    elif team == "blue":
        global blue_active_pokemon
        global blue_active_pokemon_directory
        blue_party[active_pokemon_directory].resetStages()
        blue_active_pokemon = blue_party[switch_target_directory]
        blue_active_pokemon_directory = switch_target_directory
        write(0.03, "CHAMPION Blue sent out " + blue_active_pokemon.getName() + ".")


def faint_switch(team):
    if team == "red":
        swap_target = red_swap()
        switchPokemon("red", red_active_pokemon_directory, red_active_pokemon, swap_target, True)

    if team == "blue":
        swap_target = blue_faint_switch_choice(blue_party)
        write(0.03, "CHAMPION Blue is about to use " + blue_party[
            swap_target].getName() + ". Will Red change Pokémon? (YES/NO)")
        red_change = input()
        if red_change.upper() == "YES" or red_change.upper() == "Y":
            red_swap_target = red_swap()
            if red_swap_target in red_party.keys():
                switchPokemon("red", red_active_pokemon_directory, red_active_pokemon, red_swap_target, True)
        switchPokemon("blue", blue_active_pokemon_directory, blue_active_pokemon, swap_target)


def blue_faint_switch_choice(party):
    active_party = party.copy()
    for i in range(1, len(active_party) + 1):
        if active_party[i].getStatus() == "(fainted)":
            del active_party[i]

    while True:
        switch_target_directory = random.choice(list(active_party.keys()))
        if switch_target_directory != blue_active_pokemon_directory:
            return switch_target_directory


def checkFaint(target):
    if target == "red":
        if red_active_pokemon.getHP() <= 0:
            write(0.05, red_active_pokemon.getName() + " fainted!")
            return True
    elif target == "blue":
        if blue_active_pokemon.getHP() <= 0:
            write(0.05, "Foe " + blue_active_pokemon.getName().upper() + " fainted!")
            return True


def wipeout_check(party):
    faint_count = 0
    for i in range(1, len(party) + 1):
        if party[i].getStatus() == "(fainted)":
            faint_count += 1

    if faint_count == len(party):
        if party == blue_party:
            win_message()
        elif party == red_party:
            lose_message()
        return True

    else:
        return False


def final_pokemon_check(party):
    faint_count = 0
    for i in range(1, len(party) + 1):
        if party[i].getStatus() == "(fainted)":
            faint_count += 1

    if faint_count == len(party) - 1:
        return True
    else:
        return False


def general_stage_multiplier(stage_mult):
    if stage_mult > 0:
        return (2 + stage_mult) / 2
    elif stage_mult < 0:
        return 2 / (2 - stage_mult)
    elif stage_mult == 0:
        return 1


def accuracy_stage_multiplier(self_accuracy_stage, target_evasion_stage):
    if (self_accuracy_stage - target_evasion_stage) > 0:
        return (3 + (self_accuracy_stage - target_evasion_stage)) / 3
    elif (self_accuracy_stage - target_evasion_stage) < 0:
        return 3 / (3 - (self_accuracy_stage - target_evasion_stage))
    elif (self_accuracy_stage - target_evasion_stage) == 0:
        return 1


def hit_check(attack, attacker, target):
    if attack.getEffect() == "bypass accuracy":
        return True
    else:
        attack_accuracy = attack.getAccuracy()
        attacker_accuracy_stage = attacker.getAccuracyStage()
        target_evasion_stage = target.getEvasionStage()
        accuracy_multiplier = accuracy_stage_multiplier(attacker_accuracy_stage, target_evasion_stage)
        total_accuracy = int(attack_accuracy * accuracy_multiplier * 100)
        rand_int = random.randint(1, 100)
        if rand_int <= total_accuracy:
            return True
        else:
            write(0.03, attacker.getName() + "'s attack missed!")
            return False


def change_status_stage(attacker, move):
    if (attacker == "blue" and move.getMoveType() == "opponent") or (
            attacker == "red" and move.getMoveType() == "self"):
        if move.getEffect() == "accuracy":
            red_active_pokemon.changeAccuracyStage(move.getPower())
        elif move.getEffect() == "attack":
            red_active_pokemon.changeAtkStage(move.getPower())
        elif move.getEffect() == "defense":
            red_active_pokemon.changeDefenseStage(move.getPower())
        elif move.getEffect() == "sp_atk":
            red_active_pokemon.changeSp_atkStage(move.getPower())
        elif move.getEffect() == "sp_def":
            red_active_pokemon.changeSp_defStage(move.getPower())
        elif move.getEffect() == "speed":
            red_active_pokemon.changeSpeedStage(move.getPower())
        elif move.getEffect() == "evasion":
            red_active_pokemon.changeEvasionStage(move.getPower())

        write(0.03,
              red_active_pokemon.getName() + "'s " + move.getEffect().capitalize() + " has been changed by " + str(
                  move.getPower()) + " stage(s)!\n")


    elif (attacker == "red" and move.getMoveType() == "opponent") or (
            attacker == "blue" and move.getMoveType() == "self"):
        if move.getEffect() == "accuracy":
            blue_active_pokemon.changeAccuracyStage(move.getPower())
        elif move.getEffect() == "attack":
            blue_active_pokemon.changeAtkStage(move.getPower())
        elif move.getEffect() == "defense":
            blue_active_pokemon.changeDefenseStage(move.getPower())
        elif move.getEffect() == "sp_atk":
            blue_active_pokemon.changeSp_atkStage(move.getPower())
        elif move.getEffect() == "sp_def":
            blue_active_pokemon.changeSp_defStage(move.getPower())
        elif move.getEffect() == "speed":
            blue_active_pokemon.changeSpeedStage(move.getPower())
        elif move.getEffect() == "evasion":
            blue_active_pokemon.changeEvasionStage(move.getPower())

        write(0.03,
              "Foe " + blue_active_pokemon.getName().upper() + "'s " + move.getEffect().capitalize() + " has been changed by " + str(
                  move.getPower()) + " stage(s)!\n")


# Damage:
def base_damage(A, D, power):
    # Original formula:
    # (((((2 x Level)/5) + 2) x Power x A/D)/50) + 2
    # However, all pokemon in this game has been set to level 50. Thus, (((2 x Level)/5) + 2) has
    # been set into a constant, which is 22
    constant = 22
    base_damage_value = ((constant * power * A / D) / 50) + 2
    return int(base_damage_value)


def damage_calculation(attacker, target, attack, team):
    hitCheck = hit_check(attack, attacker, target)
    if hitCheck is True:
        attack_type = attack.getType()
        attacker_type1 = attacker.getType1()
        attacker_type2 = attacker.getType2()
        first_defense_type = target.getType1()
        second_defense_type = target.getType2()
        power = attack.getPower()
        if attack.getCategory() == "physical":
            A = attacker.getAtk() * general_stage_multiplier(attacker.getAtkStage())
            D = target.getDefense() * general_stage_multiplier(target.getDefenseStage())
            base_dmg = base_damage(A, D, power)
            critical = critical_hit()
            random_multiplier = random_damage()
            same_type_attack_bonus = STAB(attack_type, attacker_type1, attacker_type2)
            type_effectiveness = dual_type_effectiveness(attack_type, first_defense_type, second_defense_type)
            modifier = critical * random_multiplier * same_type_attack_bonus * type_effectiveness
            # Original formula:
            # Modifier = Targets x Weather x Badge x Critical x random x STAB x Type x Burn x other
            total_damage = base_dmg * modifier
            damageInfo(attacker, target, attack, team, type_effectiveness, critical)
            return int(total_damage)

        elif attack.getCategory() == "special":
            A = attacker.getSp_atk() * general_stage_multiplier(attacker.getSp_atkStage())
            D = target.getSp_def() * general_stage_multiplier(target.getSp_defStage())
            base_dmg = base_damage(A, D, power)
            critical = critical_hit()
            random_multiplier = random_damage()
            same_type_attack_bonus = STAB(attack_type, attacker_type1, attacker_type2)
            type_effectiveness = dual_type_effectiveness(attack_type, first_defense_type, second_defense_type)
            modifier = critical * random_multiplier * same_type_attack_bonus * type_effectiveness
            # Original formula:
            # Modifier = Targets x Weather x Badge x Critical x random x STAB x Type x Burn x other
            total_damage = base_dmg * modifier
            damageInfo(attacker, target, attack, team, type_effectiveness, critical)
            return int(total_damage)
    else:
        return 0


def updateHP(damage, target):
    if target == "red":
        red_active_pokemon.changeHP(-damage)
        if red_active_pokemon.getHP() > 0:
            write(0.03,
                  red_active_pokemon.getName() + "'s HP is now " + str(red_active_pokemon.getHP_percentage()) + "%\n")
        else:
            red_active_pokemon.setStatus("(fainted)")

    elif target == "blue":
        blue_active_pokemon.changeHP(-damage)
        if blue_active_pokemon.getHP() > blue_active_pokemon.getMax_HP():
            blue_active_pokemon.setHP(blue_active_pokemon.getMax_HP())
        if blue_active_pokemon.getHP() > 0:
            write(0.03, "Foe " + blue_active_pokemon.getName().upper() + "'s HP is now " + str(
                blue_active_pokemon.getHP_percentage()) + "%\n")
        else:
            blue_active_pokemon.setStatus("(fainted)")


# Damage Modifier:
def single_type_effectiveness(attack_type, defense_type):
    if attack_type == "normal":
        if defense_type == "rock":
            return 1 / 2
        elif defense_type == "steel":
            return 1 / 2
        elif defense_type == "ghost":
            return 0
        else:
            return 1

    elif attack_type == "fighting":
        if defense_type == "normal":
            return 2
        elif defense_type == "flying":
            return 1 / 2
        elif defense_type == "poison":
            return 1 / 2
        elif defense_type == "rock":
            return 2
        elif defense_type == "bug":
            return 1 / 2
        elif defense_type == "ghost":
            return 1
        elif defense_type == "steel":
            return 2
        elif defense_type == "psychic":
            return 1 / 2
        elif defense_type == "ice":
            return 2
        elif defense_type == "dark":
            return 2
        else:
            return 1

    elif attack_type == "flying":
        if defense_type == "fighting":
            return 2
        elif defense_type == "rock":
            return 1 / 2
        elif defense_type == "bug":
            return 2
        elif defense_type == "steel":
            return 1 / 2
        elif defense_type == "electric":
            return 1 / 2
        elif defense_type == "grass":
            return 2
        else:
            return 1

    elif attack_type == "poison":
        if defense_type == "poison":
            return 1 / 2
        elif defense_type == "ground":
            return 1 / 2
        elif defense_type == "rock":
            return 1 / 2
        elif defense_type == "ghost":
            return 1 / 2
        elif defense_type == "steel":
            return 0
        elif defense_type == "grass":
            return 2
        else:
            return 1

    elif attack_type == "ground":
        if defense_type == "flying":
            return 0
        elif defense_type == "poison":
            return 2
        elif defense_type == "rock":
            return 2
        elif defense_type == "bug":
            return 1 / 2
        elif defense_type == "steel":
            return 2
        elif defense_type == "fire":
            return 2
        elif defense_type == "grass":
            return 1 / 2
        elif defense_type == "electric":
            return 2
        else:
            return 1

    elif attack_type == "rock":
        if defense_type == "fighting":
            return 1 / 2
        elif defense_type == "flying":
            return 2
        elif defense_type == "ground":
            return 1 / 2
        elif defense_type == "bug":
            return 2
        elif defense_type == "steel":
            return 1 / 2
        elif defense_type == "fire":
            return 2
        elif defense_type == "ice":
            return 2
        else:
            return 1

    elif attack_type == "bug":
        if defense_type == "fighting":
            return 1 / 2
        elif defense_type == "flying":
            return 1 / 2
        elif defense_type == "poison":
            return 1 / 2
        elif defense_type == "ghost":
            return 1 / 2
        elif defense_type == "steel":
            return 1 / 2
        elif defense_type == "fire":
            return 1 / 2
        elif defense_type == "grass":
            return 2
        elif defense_type == "psychic":
            return 2
        elif defense_type == "dark":
            return 2
        else:
            return 1

    elif attack_type == "ghost":
        if defense_type == "normal":
            return 0
        elif defense_type == "ghost":
            return 2
        elif defense_type == "steel":
            return 1 / 2
        elif defense_type == "psychic":
            return 2
        elif defense_type == "dark":
            return 1 / 2
        else:
            return 1

    elif attack_type == "steel":
        if defense_type == "rock":
            return 2
        elif defense_type == "steel":
            return 1 / 2
        elif defense_type == "fire":
            return 1 / 2
        elif defense_type == "water":
            return 1 / 2
        elif defense_type == "electric":
            return 1 / 2
        elif defense_type == "ice":
            return 2
        else:
            return 1

    elif attack_type == "fire":
        if defense_type == "rock":
            return 1 / 2
        elif defense_type == "bug":
            return 2
        elif defense_type == "steel":
            return 2
        elif defense_type == "fire":
            return 1 / 2
        elif defense_type == "water":
            return 1 / 2
        elif defense_type == "grass":
            return 2
        elif defense_type == "ice":
            return 2
        elif defense_type == "dragon":
            return 1 / 2
        else:
            return 1

    elif attack_type == "water":
        if defense_type == "ground":
            return 2
        elif defense_type == "rock":
            return 2
        elif defense_type == "fire":
            return 2
        elif defense_type == "water":
            return 1 / 2
        elif defense_type == "grass":
            return 1 / 2
        elif defense_type == "dragon":
            return 1 / 2
        else:
            return 1

    elif attack_type == "grass":
        if defense_type == "flying":
            return 1 / 2
        elif defense_type == "poison":
            return 1 / 2
        elif defense_type == "ground":
            return 2
        elif defense_type == "rock":
            return 2
        elif defense_type == "bug":
            return 1 / 2
        elif defense_type == "steel":
            return 1 / 2
        elif defense_type == "fire":
            return 1 / 2
        elif defense_type == "water":
            return 2
        elif defense_type == "grass":
            return 1 / 2
        elif defense_type == "dragon":
            return 1 / 2
        else:
            return 1

    elif attack_type == "electric":
        if defense_type == "flying":
            return 2
        elif defense_type == "ground":
            return 0
        elif defense_type == "water":
            return 2
        elif defense_type == "grass":
            return 1 / 2
        elif defense_type == "electric":
            return 1 / 2
        elif defense_type == "dragon":
            return 1 / 2
        else:
            return 1

    elif attack_type == "psychic":
        if defense_type == "fighting":
            return 2
        elif defense_type == "poison":
            return 2
        elif defense_type == "steel":
            return 1 / 2
        elif defense_type == "psychic":
            return 1 / 2
        elif defense_type == "dark":
            return 0
        else:
            return 1

    elif attack_type == "ice":
        if defense_type == "flying":
            return 2
        elif defense_type == "ground":
            return 2
        elif defense_type == "steel":
            return 1 / 2
        elif defense_type == "dragon":
            return 2
        elif defense_type == "fire":
            return 1 / 2
        elif defense_type == "water":
            return 1 / 2
        elif defense_type == "grass":
            return 2
        elif defense_type == "ice":
            return 1 / 2
        else:
            return 1

    elif attack_type == "dragon":
        if defense_type == "steel":
            return 1 / 2
        elif defense_type == "dragon":
            return 2
        else:
            return 1

    elif attack_type == "dark":
        if defense_type == "fighting":
            return 1 / 2
        elif defense_type == "bug":
            return 2
        elif defense_type == "steel":
            return 1 / 2
        elif defense_type == "psychic":
            return 2
        elif defense_type == "dark":
            return 1 / 2
        else:
            return 1


def dual_type_effectiveness(attack_type, first_defense_type, second_defense_type):
    if first_defense_type == second_defense_type:
        return single_type_effectiveness(attack_type, first_defense_type)

    elif first_defense_type != second_defense_type:
        first_multiplier = single_type_effectiveness(attack_type, first_defense_type)
        second_multiplier = single_type_effectiveness(attack_type, second_defense_type)
        final_multiplier = first_multiplier * second_multiplier
        return final_multiplier


def random_damage():
    rand_int = random.randint(85, 100)
    random_multiplier = rand_int / 100
    return random_multiplier


def STAB(attack_type, attacker_type1, attacker_type2):  # (Same Type Attack Bonus)
    if attack_type == attacker_type1 or attack_type == attacker_type2:
        return 1.5
    else:
        return 1


def critical_hit():
    critical_chance = random.randint(1, 16)
    if critical_chance == 1:
        return 2
    else:
        return 1


# 2. Text Functions:
def intro_dialogue():
    write(0.05, "Blue: Hey! I was looking forward to seeing you, Red! My rival should be strong to keep me sharp!")
    write(0.05,
          "Blue: While working on my Pokédex, I looked all over for pokémon! Not only that, I assembled teams that would beat")
    write(0.05,
          "any pokémon type! And now... I am the Pokémon League Champion! Red! Do you know what that means? I'll tell you!")
    write(0.05, "Blue: I am the most powerful Trainer in the world!")
    for i in range(5):
        write(0.5, ".")
    for i in range(10):
        write(0.03, " ")
    write(0.05, "CHAMPION Blue would like to battle!")
    write(0.05, "CHAMPION Blue sent out " + blue_active_pokemon.getName().upper() + "!")
    write(0.05, "Go! " + red_active_pokemon.getName() + "!")


def write(delay, text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")


def main_menu():
    print("_____________________________________")
    print(" ")
    print("Pokémon: Versus Champion Blue VER 1.0")
    print("_____________________________________")
    print(" ")
    print(" ")
    global main
    main = input("What would you like to do? (PLAY/EXIT) ")
    main = main.upper()
    return main.upper()


def battle_info():
    if red_active_pokemon.getType1() == red_active_pokemon.getType2():
        print("Red's Pokémon: " + red_active_pokemon.getName() + " (HP: " + str(
            red_active_pokemon.getHP_percentage()) + "%, Type: " + red_active_pokemon.getType1().capitalize() + ")")
    else:
        print("Red's Pokémon: " + red_active_pokemon.getName() + " (HP: " + str(
            red_active_pokemon.getHP_percentage()) + "%, Type: " + red_active_pokemon.getType1().capitalize() + ", " + red_active_pokemon.getType2().capitalize() + ")")
    stage_multiplier_info(red_active_pokemon)

    if blue_active_pokemon.getType1() == blue_active_pokemon.getType2():
        print("Blue's Pokémon: " + blue_active_pokemon.getName() + " (HP: " + str(
            blue_active_pokemon.getHP_percentage()) + "%, Type: " + blue_active_pokemon.getType1().capitalize() + ")" + "\n")
    else:
        print("Blue's Pokémon: " + blue_active_pokemon.getName() + " (HP: " + str(
            blue_active_pokemon.getHP_percentage()) + "%, Type: " + blue_active_pokemon.getType1().capitalize() + ", " + blue_active_pokemon.getType2().capitalize() + ")" + "\n")
    stage_multiplier_info(blue_active_pokemon)


def stage_multiplier_info(active_pokemon):
    sentinel = False
    if active_pokemon.getAtkStage() != 0:
        print("Attack Stage: " + str(active_pokemon.getAtkStage()))
        sentinel = True
    if active_pokemon.getDefenseStage() != 0:
        print("Defense Stage: " + str(active_pokemon.getDefenseStage()))
        sentinel = True
    if active_pokemon.getSp_atkStage() != 0:
        print("Special Attack Stage: " + str(active_pokemon.getSp_atkStage()))
        sentinel = True
    if active_pokemon.getSp_defStage() != 0:
        print("Special Defense Stage: " + str(active_pokemon.getSp_defStage()))
        sentinel = True
    if active_pokemon.getSpeedStage() != 0:
        print("Speed Stage: " + str(active_pokemon.getSpeedStage()))
        sentinel = True
    if active_pokemon.getAccuracyStage() != 0:
        print("Accuracy Stage: " + str(active_pokemon.getAccuracyStage()))
        sentinel = True
    if active_pokemon.getEvasionStage() != 0:
        print("Evasion Stage: " + str(active_pokemon.getEvasionStage()))
        sentinel = True

    if sentinel == True:
        print("")


def damageInfo(attacker, target, attack, team, type_effectiveness, critical):
    if type_effectiveness > 1:
        write(0.03, "It's super effective!")
    elif type_effectiveness < 1 and type_effectiveness != 0:
        write(0.03, "It's not very effective...")
    elif type_effectiveness == 0:
        write(0.03, "It doesn't affect " + target.getName() + "...")

    if critical > 1:
        write(0.03, "It's a critical hit!")


def used_move_info(team, attacker, attack):
    if team == "red":
        write(0.03, attacker.getName() + " used " + attack.getName() + "!")
    elif team == "blue":
        write(0.03, "Foe " + attacker.getName().upper() + " used " + attack.getName() + "!")


def moveData():
    print("Moves:")
    for i in range(1, 5):
        if red_active_pokemon.getMoveSet()[i].getAccuracy() is None:
            print("[" + str(i) + "]. " + red_active_pokemon.getMoveSet()[i].getName() + " (Type: " +
                  red_active_pokemon.getMoveSet()[
                      i].getType().capitalize() + ", Category: " + str(
                red_active_pokemon.getMoveSet()[i].getCategory()) + ", Power: " + str(
                red_active_pokemon.getMoveSet()[i].getPower()) + ", Accuracy: ~~~), Special Effect: " + str(
                red_active_pokemon.getMoveSet()[i].getEffect().capitalize()) + ")")

        else:
            print("[" + str(i) + "]. " + red_active_pokemon.getMoveSet()[i].getName() + " (Type: " +
                  red_active_pokemon.getMoveSet()[
                      i].getType().capitalize() + ", Category: " + str(
                red_active_pokemon.getMoveSet()[i].getCategory()) + ", Power: " + str(
                red_active_pokemon.getMoveSet()[i].getPower()) + ", Accuracy: " + str(
                int(red_active_pokemon.getMoveSet()[i].getAccuracy() * 100)) + "%, Special Effect: " + str(
                red_active_pokemon.getMoveSet()[i].getEffect()).capitalize() + ")")


def win_message():
    write(0.05,
          "Blue: NO! That can't be! You beat me at my best! After all that work to become the League Champ? My reign is over already? It's not fair!")
    write(0.05,
          "Blue: Why? Why did I lose? I never made any mistakes raising my Pokémon… Darn it! You're the new Pokémon League Champion! Although I don't like to admit it…\n")
    print("Congratulations! You've won the game!")


def lose_message():
    write(0.05, "Red is out of usable Pokémon!")
    for i in range(6):
        write(0.3, ".")
    write(0.02, "Red blacked out!\n")
    write(0.5, "YOU LOST")


# 3. Test Functions:
def initialize_battle_no_text():
    print("*Input (-1) to return to previous menu during the game*")
    initialize_blue_party()
    initialize_red_party()
    global red_active_pokemon
    global blue_active_pokemon
    global red_active_pokemon_directory
    global blue_active_pokemon_directory
    red_active_pokemon = red_party[1]
    blue_active_pokemon = blue_party[1]
    red_active_pokemon_directory = 1
    blue_active_pokemon_directory = 1
