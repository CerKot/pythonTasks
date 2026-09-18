from random import randint,seed
import time
from typing import Callable


def time_dec(func: Callable):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Время выполнения функции: {end-start} с')
        return result

    return wrapper



def battle_simulation(cloneCount: int,
                      droidCount: int,
                      droidAttackPower: int = 1,
                      killingCloneChance: int = 30,
                      verbose: bool = False) -> None:

    """This function simulates battle between drones and clones
    So, clones damage randomly and drones permanents

    Args:
        cloneCount (int): The number of clones
        droidCount (int): The number of drones
        droidAttackPower(int): How many drones can kill 1 clone
        killingCloneChance(int): the random number from 1 to 100
                                 must be more that may clone to kill droid
        verbose(bool): can function prints the result

    Returns:
        None
    """

    roundCounter = 1

    #Game loop:
    while cloneCount > 0 and droidCount > 0:
        if verbose:
            print(f"{'-'*8} {roundCounter} раунд {'-'*8}")
            print(f'Количество дроидов: {droidCount}')
            print(f'Количество клонов: {cloneCount}')

        droidCountInRound: int = droidCount

        #Атака клонов:
        for _ in range(cloneCount):
            if randint(1,100) >= killingCloneChance:
                droidCount -= 1
            if droidCount == 0:
                break


        #Атака дроидов
        cloneCount = max(0, cloneCount - droidCountInRound // droidAttackPower)

        if verbose:
            print(f'После битвы между дроидами и клонами осталось '
              f'{cloneCount} клонов и {droidCount} дроидов')

        roundCounter += 1

    if cloneCount == 0 and droidCount == 0:
        print('• Ничья! Все участники пали в бою!')
    elif cloneCount == 0:
        print(f'Победа за силами Торговой Федерации!\n'
              f'Осталось дроидов: {droidCount}')
    elif droidCount == 0:
        print(f'Победа за силами Галактической Республики!\n'
             f'Осталось клонов: {cloneCount}')
@time_dec
def manyCallings(N:int, cloneCount: int,
                 droidCount: int, droidAttackPower: int = 1,
                 killingCloneChance:int = 30, verbose: bool = False) -> None:
    """This function calls battle_simulation (function) N times"""

    for _ in range(N):
        battle_simulation(cloneCount=cloneCount,droidCount=droidCount,
                          droidAttackPower=droidAttackPower,
                          killingCloneChance=killingCloneChance,
                          verbose=verbose)

if __name__ == '__main__':
    seed(1)
    manyCallings(100,battle_simulation,cloneCount = 10, droidCount = 20)

