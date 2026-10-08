import random
from Task2.main import table_create

def battle_simulation(clone_counter: int,
                      droid_counter: int,
                      droid_attack_power: int = 1,
                      killing_clone_chance: int = 10,
                      verbose: bool = False) -> dict:

    """This function simulates battle between drones and clones
    So, clones damage randomly and drones permanents

    Args:
        clone_counter (int): The number of clones
        droid_counter (int): The number of drones
        droid_attack_power(int): How many drones can kill 1 clone
        killing_clone_chance(int): the random number from 1 to 100
                                 must be more that may clone to kill droid
        verbose(bool): can function prints the result

    Returns:
        dict
    """

    round_counter = 0

    while clone_counter > 0 and droid_counter > 0:
        round_counter += 1

        if verbose:
            print(f"{'-'*8} {round_counter} раунд {'-'*8}")
            print(f'Количество дроидов: {droid_counter}')
            print(f'Количество клонов: {clone_counter}')


        # Атака дроидов
        clone_counter = max(0, clone_counter - droid_counter // droid_attack_power)

        #Атака клонов:
        for _ in range(clone_counter):
            if random.randint(1,100) >= killing_clone_chance:
                droid_counter -= 1

            if droid_counter == 0:
                break
                
        if verbose:
            print(f'После битвы между дроидами и клонами осталось '
              f'{clone_counter} клонов и {droid_counter} дроидов')

    winner = None
    if clone_counter == 0 and droid_counter == 0:
        if verbose:
            print('• Ничья! Все участники пали в бою!')
    elif clone_counter == 0:
        winner = "Дроиды"
        if verbose:
            print(f'Победа за силами Торговой Федерации!\n'
                f'Осталось дроидов: {droid_counter}')
    elif droid_counter == 0:
        winner = "Клоны"
        if verbose:
            print(f'Победа за силами Галактической Республики!\n'
                 f'Осталось клонов: {clone_counter}')

    return {
        "clone_counter" : clone_counter,
            "droid_counter" : droid_counter,
            "winner" : winner,
            "rounds" : round_counter
    }

def many_battle_simulation_call(clone_counter: int,
                 droid_counter: int,
                 n:int = 1000,
                 droid_attack_power: int = 1,
                 killing_clone_chance:int = 10,
                 verbose: bool = False) -> dict:

    """This function calls battle_simulation (function) n times"""

    round_counter: int = 0
    droid_win_counter: int = 0
    clone_win_counter: int = 0
    alive_counter: int = 0
    for _ in range(n):
        results = battle_simulation(clone_counter=clone_counter,droid_counter=droid_counter,
                          droid_attack_power=droid_attack_power,
                          killing_clone_chance=killing_clone_chance,
                          verbose=verbose)
        alive_counter += results["clone_counter"] + results["droid_counter"]

        if results['clone_counter'] == 0:
            droid_win_counter += 1
        elif  results['droid_counter'] == 0 :
            clone_win_counter += 1
        round_counter += results["rounds"]
    return {
            "meanAliveNumber": alive_counter // n,
            "meanDroidWinCounter": droid_win_counter // n,
            "meanCloneWinCounter": clone_win_counter // n,
            "meanround_counter": round_counter // n
            }

if __name__ == '__main__':
    seedKey = input('Напиши что-нибудь для ключа\n')
    random.seed(seedKey)
    details = many_battle_simulation_call(clone_counter = 10, droid_counter = 1,droid_attack_power=1,
                                          killing_clone_chance = 0)
    data = []
    table_create(title="Статистика", header=[name for name in details],
                  data=[[value for value in details.values()]],place_to_value=20)

