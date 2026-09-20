from random import randint,seed
import time
from typing import Callable
from Task2.main import tableCreating

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
                      verbose: bool = False) -> dict:

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
    winner = None
    if cloneCount == 0 and droidCount == 0:
        if verbose:
            print('• Ничья! Все участники пали в бою!')
    elif cloneCount == 0:
        winner = "Дроиды"
        if verbose:
            print(f'Победа за силами Торговой Федерации!\n'
                f'Осталось дроидов: {droidCount}')
    elif droidCount == 0:
        winner = "Клоны"
        if verbose:
            print(f'Победа за силами Галактической Республики!\n'
                 f'Осталось клонов: {cloneCount}')
    return {"cloneCount" : cloneCount,
            "droidCount" : droidCount,
            "winner" : winner,
            "rounds" : roundCounter
            }

@time_dec
def manyCallings(cloneCount: int,
                 droidCount: int,
                 N:int = 1000,
                 droidAttackPower: int = 1,

                 killingCloneChance:int = 30, verbose: bool = False) -> dict:
    """This function calls battle_simulation (function) N times"""
    roundCounter: int = 0
    droidWinCounter: int = 0
    cloneWinCounter: int = 0
    aliveCounter: int = 0
    for _ in range(N):
        results = battle_simulation(cloneCount=cloneCount,droidCount=droidCount,
                          droidAttackPower=droidAttackPower,
                          killingCloneChance=killingCloneChance,
                          verbose=verbose)
        aliveCounter += results["cloneCount"] + results["droidCount"]

        if results["winner"] == "Дроиды":
            droidWinCounter += 1
        elif results["winner"] == "Клоны":
            cloneWinCounter += 1
        roundCounter += results["rounds"]
    return {"meanAliveNumber": aliveCounter // N,
            "meanDroidWinCounter": droidWinCounter // N,
            "meanCloneWinCounter": cloneWinCounter // N,
            "meanRoundCounter": roundCounter // N
            }
if __name__ == '__main__':
    seed(1)
    details = manyCallings(cloneCount = 10, droidCount = 20)
    data = []
    ...
    #Как должна выглядить таблица? ....