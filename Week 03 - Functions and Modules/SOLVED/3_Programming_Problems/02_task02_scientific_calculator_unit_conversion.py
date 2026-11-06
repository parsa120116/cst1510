# All factors below are copied from the Unit Conversion Chart (Fig. 1).
FT_PER_M = 3.3
CM_PER_IN = 2.43        # chart value (the exact value is 2.54)
KM_PER_MI = 1.61
LB_PER_KG = 2.2
G_PER_OZ = 28.35
CHART_M3_PER_FT3 = 0.028   # chart prints "1 ft = 0.028 m" in the Mass box
CC_PER_ML = 1
ML_PER_CUP = 237
CUPS_PER_GAL = 16
FT3_PER_M3 = 35.31
KPA_PER_ATM = 101.3
MMHG_PER_ATM = 760
PA_PER_BAR = 10 ** 5
MBAR_PER_PSI = 68.948
KCAL_PER_J = 2.39e-4
J_PER_EV = 1.602e-19    # chart prints "K"; the unit should be J


# ---------- Length ----------
def m_to_ft(value):
    """Convert metres to feet."""
    return value * FT_PER_M

def ft_to_m(value):
    """Convert feet to metres."""
    return value / FT_PER_M

def in_to_cm(value):
    """Convert inches to centimetres."""
    return value * CM_PER_IN

def cm_to_in(value):
    """Convert centimetres to inches."""
    return value / CM_PER_IN

def mi_to_km(value):
    """Convert miles to kilometres."""
    return value * KM_PER_MI

def km_to_mi(value):
    """Convert kilometres to miles."""
    return value / KM_PER_MI


# ---------- Temperature ----------
def c_to_f(value):
    """Convert Celsius to Fahrenheit: F = 9/5 C + 32."""
    return 9 / 5 * value + 32

def f_to_c(value):
    """Convert Fahrenheit to Celsius: C = 5/9 (F - 32)."""
    return 5 / 9 * (value - 32)

def c_to_k(value):
    """Convert Celsius to Kelvin: K = C + 273.15."""
    return value + 273.15

def k_to_c(value):
    """Convert Kelvin to Celsius: C = K - 273.15."""
    return value - 273.15

def f_to_k(value):
    """Convert Fahrenheit to Kelvin: K = 5/9 (F - 32) + 273."""
    return 5 / 9 * (value - 32) + 273

def k_to_f(value):
    """Convert Kelvin to Fahrenheit (the chart formula turned around)."""
    return 9 / 5 * (value - 273) + 32


# ---------- Mass ----------
def kg_to_lb(value):
    """Convert kilograms to pounds."""
    return value * LB_PER_KG

def lb_to_kg(value):
    """Convert pounds to kilograms."""
    return value / LB_PER_KG

def oz_to_g(value):
    """Convert ounces to grams."""
    return value * G_PER_OZ

def g_to_oz(value):
    """Convert grams to ounces."""
    return value / G_PER_OZ

def cubic_ft_to_cubic_m(value):
    """Convert cubic feet to cubic metres (Mass box of the chart)."""
    return value * CHART_M3_PER_FT3

def cubic_m_to_cubic_ft(value):
    """Convert cubic metres to cubic feet (Mass box of the chart)."""
    return value / CHART_M3_PER_FT3


# ---------- Volume ----------
def ml_to_cc(value):
    """Convert millilitres to cubic centimetres."""
    return value * CC_PER_ML

def cc_to_ml(value):
    """Convert cubic centimetres to millilitres."""
    return value / CC_PER_ML

def cup_to_ml(value):
    """Convert cups to millilitres."""
    return value * ML_PER_CUP

def ml_to_cup(value):
    """Convert millilitres to cups."""
    return value / ML_PER_CUP

def gal_to_cup(value):
    """Convert gallons to cups."""
    return value * CUPS_PER_GAL

def cup_to_gal(value):
    """Convert cups to gallons."""
    return value / CUPS_PER_GAL

def m3_to_ft3(value):
    """Convert cubic metres to cubic feet."""
    return value * FT3_PER_M3

def ft3_to_m3(value):
    """Convert cubic feet to cubic metres."""
    return value / FT3_PER_M3


# ---------- Pressure ----------
def atm_to_kpa(value):
    """Convert atmospheres to kilopascals."""
    return value * KPA_PER_ATM

def kpa_to_atm(value):
    """Convert kilopascals to atmospheres."""
    return value / KPA_PER_ATM

def atm_to_mmhg(value):
    """Convert atmospheres to millimetres of mercury."""
    return value * MMHG_PER_ATM

def mmhg_to_atm(value):
    """Convert millimetres of mercury to atmospheres."""
    return value / MMHG_PER_ATM

def bar_to_pa(value):
    """Convert bar to pascals."""
    return value * PA_PER_BAR

def pa_to_bar(value):
    """Convert pascals to bar."""
    return value / PA_PER_BAR

def psi_to_mbar(value):
    """Convert psi to millibar."""
    return value * MBAR_PER_PSI

def mbar_to_psi(value):
    """Convert millibar to psi."""
    return value / MBAR_PER_PSI


# ---------- Energy ----------
def j_to_kcal(value):
    """Convert joules to kilocalories."""
    return value * KCAL_PER_J

def kcal_to_j(value):
    """Convert kilocalories to joules."""
    return value / KCAL_PER_J

def ev_to_j(value):
    """Convert electronvolts to joules."""
    return value * J_PER_EV

def j_to_ev(value):
    """Convert joules to electronvolts."""
    return value / J_PER_EV


# ---------- Helpers for the menus ----------
def is_number(text):
    """Return True if text is a number such as 7, -3 or 2.5."""
    if text.startswith("-"):
        text = text[1:]
    return text.replace(".", "", 1).isdigit()


def read_value():
    """Ask until the user types a number; return it as a float."""
    while True:
        text = input("Enter the value to convert: ").strip()
        if is_number(text):
            return float(text)
        print("That is not a number, please try again.")


def ask_choice(highest, lowest=1):
    """Ask until the user picks a whole number from lowest to highest; return it."""
    while True:
        text = input(f"Choose {lowest}-{highest}: ").strip()
        if text.isdigit() and lowest <= int(text) <= highest:
            return int(text)
        print("Not on the menu, please try again.")


def show_result(value, from_unit, result, to_unit):
    """Print one conversion, e.g. 10 m = 33 ft."""
    print(f"{value:g} {from_unit} = {result:.6g} {to_unit}")


# ---------- One menu per unit type ----------
def length_menu():
    """Let the user pick a length conversion and print the result."""
    print("1) m -> ft     2) ft -> m")
    print("3) in -> cm    4) cm -> in")
    print("5) mi -> km    6) km -> mi")
    choice = ask_choice(6)
    value = read_value()
    if choice == 1:
        show_result(value, "m", m_to_ft(value), "ft")
    elif choice == 2:
        show_result(value, "ft", ft_to_m(value), "m")
    elif choice == 3:
        show_result(value, "in", in_to_cm(value), "cm")
    elif choice == 4:
        show_result(value, "cm", cm_to_in(value), "in")
    elif choice == 5:
        show_result(value, "mi", mi_to_km(value), "km")
    else:
        show_result(value, "km", km_to_mi(value), "mi")


def temperature_menu():
    """Let the user pick a temperature conversion and print the result."""
    print("1) °C -> °F    2) °F -> °C")
    print("3) °C -> K     4) K -> °C")
    print("5) °F -> K     6) K -> °F")
    choice = ask_choice(6)
    value = read_value()
    if choice == 1:
        show_result(value, "°C", c_to_f(value), "°F")
    elif choice == 2:
        show_result(value, "°F", f_to_c(value), "°C")
    elif choice == 3:
        show_result(value, "°C", c_to_k(value), "K")
    elif choice == 4:
        show_result(value, "K", k_to_c(value), "°C")
    elif choice == 5:
        show_result(value, "°F", f_to_k(value), "K")
    else:
        show_result(value, "K", k_to_f(value), "°F")


def mass_menu():
    """Let the user pick a mass conversion and print the result."""
    print("1) kg -> lb    2) lb -> kg")
    print("3) oz -> g     4) g -> oz")
    print("5) ft³ -> m³   6) m³ -> ft³   (the chart's '1 ft = 0.028 m')")
    choice = ask_choice(6)
    value = read_value()
    if choice == 1:
        show_result(value, "kg", kg_to_lb(value), "lb")
    elif choice == 2:
        show_result(value, "lb", lb_to_kg(value), "kg")
    elif choice == 3:
        show_result(value, "oz", oz_to_g(value), "g")
    elif choice == 4:
        show_result(value, "g", g_to_oz(value), "oz")
    elif choice == 5:
        show_result(value, "ft³", cubic_ft_to_cubic_m(value), "m³")
    else:
        show_result(value, "m³", cubic_m_to_cubic_ft(value), "ft³")


def volume_menu():
    """Let the user pick a volume conversion and print the result."""
    print("1) ml -> cc     2) cc -> ml")
    print("3) cup -> ml    4) ml -> cup")
    print("5) gal -> cup   6) cup -> gal")
    print("7) m³ -> ft³    8) ft³ -> m³")
    choice = ask_choice(8)
    value = read_value()
    if choice == 1:
        show_result(value, "ml", ml_to_cc(value), "cc")
    elif choice == 2:
        show_result(value, "cc", cc_to_ml(value), "ml")
    elif choice == 3:
        show_result(value, "cup", cup_to_ml(value), "ml")
    elif choice == 4:
        show_result(value, "ml", ml_to_cup(value), "cup")
    elif choice == 5:
        show_result(value, "gal", gal_to_cup(value), "cup")
    elif choice == 6:
        show_result(value, "cup", cup_to_gal(value), "gal")
    elif choice == 7:
        show_result(value, "m³", m3_to_ft3(value), "ft³")
    else:
        show_result(value, "ft³", ft3_to_m3(value), "m³")


def pressure_menu():
    """Let the user pick a pressure conversion and print the result."""
    print("1) atm -> kPa     2) kPa -> atm")
    print("3) atm -> mm Hg   4) mm Hg -> atm")
    print("5) bar -> Pa      6) Pa -> bar")
    print("7) psi -> mbar    8) mbar -> psi")
    choice = ask_choice(8)
    value = read_value()
    if choice == 1:
        show_result(value, "atm", atm_to_kpa(value), "kPa")
    elif choice == 2:
        show_result(value, "kPa", kpa_to_atm(value), "atm")
    elif choice == 3:
        show_result(value, "atm", atm_to_mmhg(value), "mm Hg")
    elif choice == 4:
        show_result(value, "mm Hg", mmhg_to_atm(value), "atm")
    elif choice == 5:
        show_result(value, "bar", bar_to_pa(value), "Pa")
    elif choice == 6:
        show_result(value, "Pa", pa_to_bar(value), "bar")
    elif choice == 7:
        show_result(value, "psi", psi_to_mbar(value), "mbar")
    else:
        show_result(value, "mbar", mbar_to_psi(value), "psi")


def energy_menu():
    """Let the user pick an energy conversion and print the result."""
    print("1) J -> kcal    2) kcal -> J")
    print("3) eV -> J      4) J -> eV")
    choice = ask_choice(4)
    value = read_value()
    if choice == 1:
        show_result(value, "J", j_to_kcal(value), "kcal")
    elif choice == 2:
        show_result(value, "kcal", kcal_to_j(value), "J")
    elif choice == 3:
        show_result(value, "eV", ev_to_j(value), "J")
    else:
        show_result(value, "J", j_to_ev(value), "eV")


def main():
    """Show the main menu until the user chooses 0 to quit."""
    while True:
        print()
        print("===== Unit Conversion Calculator =====")
        print("1) Length    2) Temperature   3) Mass")
        print("4) Volume    5) Pressure      6) Energy")
        print("0) Quit")
        unit_type = ask_choice(6, 0)
        if unit_type == 0:
            break
        elif unit_type == 1:
            length_menu()
        elif unit_type == 2:
            temperature_menu()
        elif unit_type == 3:
            mass_menu()
        elif unit_type == 4:
            volume_menu()
        elif unit_type == 5:
            pressure_menu()
        else:
            energy_menu()
    print("Goodbye!")


if __name__ == "__main__":
    main()
