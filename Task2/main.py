#Пусть будет 1-ый вариант...
import math

def vattTodBm(power: float) -> float:
    """This function translates power from vatt to dBm
        Args:
            power(float): not negative value of power in Vatt
        Returns:
            float: value of power in dBm
        Raises:
            ValueError: if power <= 0
    """

    if power <= 0:
        raise ValueError("We can't translate this power value")
    return 10 * math.log10(power) + 30


def dBmToVatt(power: float) -> float:
    """This function translates power from dBm to vatt
           Args:
               power(float): value of power in dBm
           Returns:
               float: value of power in Vat
       """
    return 10 ** (power/10 - 3)


def dBVToVolt(voltage: float) -> float:
    """This function translates voltage from dBV to Volt
               Args:
                   voltage(float): value of voltage in dBV
               Returns:
                   float: value of Voltage in Vat
           """
    return 10 ** (voltage / 20)


def voltTodBV(voltage: float) -> float:
    """This function translates voltage from Volt to dBV
               Args:
                   voltage(float): value of voltage in Volt
               Returns:
                   float: value of voltage in dBV
               Raises:
                   ValueError: if voltage <= 0
           """
    if voltage <= 0:
        raise ValueError("We can't translate negative"
                         "voltage to dBV ")

    return 20 * math.log10(voltage)


def tableCreating(title: str, header: list[str],data: list[ list[float] ],
                  precision: int = 3,
                  placeToValue:int = 10) -> None:
    valuesLength = len(header)
    if not all(len(i) == valuesLength for i in data):
        raise TypeError("We can not create table, because of number of translations "
                        "is not equal number of translation functions ")
    print(f'{title:*^{valuesLength * placeToValue + valuesLength + 1}}')

    #roof
    roof: str = (valuesLength * placeToValue + valuesLength + 1) * "-"

    print(roof)
    [print(f"|{i:^{placeToValue}}", end = '') for i in header]
    print("|")
    print(roof)

    for row in data:

        [print(f"|{i:^{placeToValue}.{precision}f}", end = '') for i in row]
        print("|")
        print(roof)


def IsStrToFloat(value : str,

               ) -> bool:
    """"This function show if this string number can be translated  into the float
        Args:
            value(str): input string value
        Returns:
            bool: if this value translated in float
       """

    try:
        float(value)
    except ValueError:
        return False
    else:
        return True


def getFloatInputValue(queryToUser: str,
                        errorMessage: str =
                            "You can not translate it,"
                            "it's not a float number"
                       ) -> float:
    """This function make user to input float value
    Args:
        queryToUser(str): it's what will user has to input
        errorMessage(str): error what user will see if input value is not number
    Returns:
        float: user's input value in float
    """

    while True:
        userInput = input(queryToUser)
        if IsStrToFloat(userInput):
            return float(userInput)
        print(errorMessage)

if __name__ == "__main__":

    voltage = getFloatInputValue("Введите напряжение в Вольтах\n")
    # power = getFloatInputValue("Введите мощность в Ваттах\n")
    # dBVVoltage = getFloatInputValue("Введите напряжение в дБВ\n")
    # dBMPower = getFloatInputValue("Введите мощность в дБМ\n")

    data = []
    for i in range(10):
        data.append([i+voltage,voltTodBV(i+voltage)])
    print(data)
    tableCreating("Таблица",['В','дБВ'],data=data)

