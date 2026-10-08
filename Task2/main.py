import math
def vat_to_dbm(power: float) -> float:
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


def dbm_to_vat(power: float) -> float:
    """This function translates power from dBm to vatt
           Args:
               power(float): value of power in dBm
           Returns:
               float: value of power in Vat
       """
    return 10 ** (power/10 - 3)


def dbv_to_volt(voltage: float) -> float:
    """This function translates voltage from dBV to Volt
               Args:
                   voltage(float): value of voltage in dBV
               Returns:
                   float: value of Voltage in Vat
           """
    return 10 ** (voltage / 20)


def volt_to_dbv(voltage: float) -> float:
    """This function translates voltage from Volt to dBV
               Args:
                   voltage(float): value of voltage in Volt
               Returns:
                   float: value of voltage in dBV
               Raises:
                   ValueError: if voltage <= 0
           """
    if voltage <= 0:
        raise ValueError("We can't translate negative "
                         "voltage to dBV ")

    return 20 * math.log10(voltage)




def is_str_to_float(value : str) -> bool:
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


def get_float_input_value(query_to_user: str,
                       error_message: str =
                            "You can not translate it,"
                            "it's not a float number"
                       ) -> float:
    """This function make user to input float value
    Args:
        query_to_user(str): it's what will user has to input
        error_message(str): error what user will see if input value is not number
    Returns:
        float: user's input value in float

    """

    while True:
        userInput = input(query_to_user)
        if is_str_to_float(userInput):
            return float(userInput)
        print(error_message)

def table_create(title: str, header: list[str],data: list[ list[float] ],
                  precision: int = 3,
                  place_to_value:int = 10) -> None:
    eps = 1e-6
    values_length = len(header)
    if not all(len(i) == values_length for i in data):
        raise TypeError("We can not create table, because of number of translations "
                        "is not equal number of translation functions ")
    print(f'{title:*^{values_length * place_to_value + values_length + 1}}')

    #roof
    roof: str = (values_length * place_to_value + values_length + 1) * "-"

    print(roof)
    for row in header:
        print(f"|{row:^{place_to_value}}", end='')

    print("|")
    print(roof)

    for row in data:
        for number in row:
            if 0 < abs(number) - abs(int(number)) < eps:
                number_format = 'e'
                number_precision = 1
            else:
                number_precision = precision
                number_format = 'f'
            print(f"|{number:^{place_to_value}.{number_precision}{number_format}}", end = '')

        print("|")
        print(roof)


if __name__ == "__main__":

    voltage = get_float_input_value("Введите напряжение в Вольтах\n")
    power = get_float_input_value("Введите мощность в Ваттах\n")
    dBVVoltage = get_float_input_value("Введите напряжение в дБВ\n")
    dBMPower = get_float_input_value("Введите мощность в дБМ\n")

    data = []
    for i in range(10):
        data.append([i+voltage,volt_to_dbv(i+voltage)])
    print(data)
    table_create("Таблица",['В','дБВ'],data=data)
