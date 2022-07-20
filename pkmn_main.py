import game_functions as gf


def red_sequence(red_choice):
    if red_choice[0] == "FIGHT":
        gf.used_move_info("red", gf.red_active_pokemon, red_choice[1])
        if red_choice[1].getMoveType() == "damaging":
            damage = gf.damage_calculation(gf.red_active_pokemon, gf.blue_active_pokemon, red_choice[1], "red")
            gf.updateHP(damage, "blue")
            if red_choice[1].getEffect() == "recoil":
                gf.write(0.03, gf.red_active_pokemon.getName() + " was hit by the recoil.")
                gf.updateHP(damage * red_choice[1].getSecondary_power(), "red")

            elif red_choice[1].getEffect() == "lifesteal":
                gf.write(0.03, "Foe " + gf.blue_active_pokemon.getName().upper() + " had its energy drained.")
                gf.updateHP(-damage * red_choice[1].getSecondary_power(), "red")

        elif red_choice[1].getCategory() == "status":
            if red_choice[1].getMoveType() == "opponent":
                gf.hit_check(red_choice, gf.red_active_pokemon, gf.blue_active_pokemon)
                gf.change_status_stage("red", red_choice[1])
            elif red_choice[1].getMoveType() == "self":
                if red_choice[1].getEffect() == "heal":
                    gf.write(0.03, gf.red_active_pokemon.getName().upper() + " regained health!")
                    gf.updateHP(-gf.red_active_pokemon.getMax_HP() * red_choice[1].getPower())
                else:
                    gf.change_status_stage("red", red_choice[1])

    elif red_choice[0] == "POKEMON":
        gf.switchPokemon("red", gf.red_active_pokemon_directory, gf.red_active_pokemon, red_choice[1])


def blue_sequence(blue_choice):
    global premature_swap
    premature_swap = False
    gf.used_move_info("blue", gf.blue_active_pokemon, blue_choice)
    if blue_choice.getMoveType() == "damaging":
        damage = gf.damage_calculation(gf.blue_active_pokemon, gf.red_active_pokemon, blue_choice, "blue")
        gf.updateHP(damage, "red")
        if blue_choice.getEffect() == "recoil":
            gf.write(0.03, "Foe " + gf.blue_active_pokemon.getName().upper() + " was hit by the recoil.")
            gf.updateHP(damage * blue_choice.getSecondary_power(), "blue")
        elif blue_choice.getEffect() == "lifesteal":
            gf.write(0.03, gf.red_active_pokemon.getName() + " had its energy drained.")
            gf.updateHP(-damage * blue_choice.getSecondary_power(), "blue")

    elif blue_choice.getMoveType() == "opponent switch":
        if gf.final_pokemon_check(gf.red_party) is True:
            gf.write(0.03, "But it failed!")
        else:
            if blue_choice.getName() == "Whirlwind":
                gf.write(0.05, gf.red_active_pokemon.getName() + " was blown away! You are forced to switch Pokémon.")
            elif blue_choice.getName() == "Roar":
                gf.write(0.05, gf.red_active_pokemon.getName() + " was scared away! You are forced to switch Pokémon.")
            swap_target = gf.red_swap()
            gf.switchPokemon("red", gf.red_active_pokemon_directory, gf.red_active_pokemon, swap_target, True)
            premature_swap = True

    elif blue_choice.getCategory() == "status":
        if blue_choice.getMoveType() == "opponent":
            gf.hit_check(blue_choice, gf.blue_active_pokemon, gf.red_active_pokemon)
            gf.change_status_stage("blue", blue_choice)
        elif blue_choice.getMoveType() == "self":
            if blue_choice.getEffect() == "heal":
                gf.write(0.03, "Foe " + gf.blue_active_pokemon.getName().upper() + " regained health!")
                gf.updateHP(-gf.blue_active_pokemon.getMax_HP() * blue_choice.getPower(), "blue")
            else:
                gf.change_status_stage("blue", blue_choice)


def complete_faint_check():
    global battle
    global cont
    faint_check = gf.checkFaint("blue")
    if faint_check is True:
        wipeout = gf.wipeout_check(gf.blue_party)
        if wipeout is False:
            gf.faint_switch("blue")
            cont = False
        else:
            cont = False
            battle = False
    else:
        pass

    faint_check = gf.checkFaint("red")
    if faint_check is True:
        wipeout = gf.wipeout_check(gf.red_party)
        if wipeout is False:
            gf.faint_switch("red")
            cont = False
        else:
            cont = False
            battle = False
    elif premature_swap is True:
        cont = False


def run_game():
    while True:
        gf.main_menu()
        if gf.main == "PLAY":
            gf.initialize_battle()
            global battle
            battle = True
            while battle is True:
                global cont
                global premature_swap
                cont = True
                premature_swap = False
                gf.battle_info()
                red_choice = gf.red_turn()
                blue_choice = gf.blue_turn()
                first_move_order = gf.first_move_order(red_choice, blue_choice)
                if first_move_order == "red":
                    red_sequence(red_choice)
                    complete_faint_check()
                    if cont is True:
                        blue_sequence(blue_choice)
                        complete_faint_check()

                elif first_move_order == "blue":
                    blue_sequence(blue_choice)
                    complete_faint_check()
                    if cont is True:
                        red_sequence(red_choice)
                        complete_faint_check()

                print("\n\n")

            retry = input("Would you like to play again? (YES/NO) ")
            if retry.upper() == "YES" or retry.upper() == "Y":
                pass
            elif retry.upper() == "NO" or retry.upper() == "N":
                break
        elif gf.main == "EXIT":
            break


run_game()

"""
References:
1. All credits of Pokémon gameplay, names, and asssets goes to Nintendo 
2. Delayed text printing: https://stackoverflow.com/questions/4627033/printing-a-string-with-a-little-delay-between-the-chars
3. Pokemon stats and move data: https://bulbapedia.bulbagarden.net/wiki/Main_Page
4. Damage calculation: https://bulbapedia.bulbagarden.net/wiki/Damage
"""
