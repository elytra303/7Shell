import platform
import os
import sys
import ctypes
import subprocess
from colorama import init, Fore

init(autoreset=True, convert=True)


def get_pc_info():
    username = os.getlogin()
    hostname = platform.node()
    C = Fore.LIGHTCYAN_EX
    W = Fore.WHITE
    R = Fore.RESET

    return [
        f"{C}{username}{W}@{C}{hostname}",
        f"{C}OS{R}: Windows {platform.release()}",
        f"{C}Host{R}: {hostname}",
        f"{C}Kernel{R}: {platform.version()}",
        f"{C}Arch{R}: {platform.machine()}",
        f"{C}Python{R}: {platform.python_version()}",
    ]


def show_neofetch():
    C = Fore.LIGHTCYAN_EX
    line_part = "=========================  "
    logo = [line_part + "========================="] * 12 + [" " * 52] + [line_part + "========================="] * 10

    sys_info = get_pc_info()
    print("\n")
    max_rows = max(len(logo), len(sys_info))
    for i in range(max_rows):
        l_row = f"{C}{logo[i]}{Fore.RESET}" if i < len(logo) else " " * 52
        i_txt = sys_info[i] if i < len(sys_info) else ""
        print(f" {l_row}   {i_txt}")
    print("\n")


def start_terminal():
    try:
        ctypes.windll.kernel32.SetConsoleTitleW("7Shell")
    except:
        pass

    os.system('cls')
    show_neofetch()

    username = os.getlogin()
    hostname = platform.node()

    while True:
        C = Fore.LIGHTCYAN_EX
        W = Fore.WHITE
        R = Fore.RESET

        prompt = f"{C}{username}{W}@{C}{hostname}{W}:{C}~{W}$ {R}"

        sys.stdout.write(prompt)
        sys.stdout.flush()
        user_input = sys.stdin.readline().strip()

        if not user_input:
            continue

        cmd_parts = user_input.split()
        main_cmd = cmd_parts[0].lower()
        if main_cmd == "fetch":
            show_neofetch()

        elif main_cmd == "pip":
            pip_args = cmd_parts[1:]
            if not pip_args:
                print(f"{Fore.RED}Использование: pip install <package>")
            else:
                print(f"{Fore.YELLOW}Запуск: python -m pip {' '.join(pip_args)}...{R}")
                try:
                    subprocess.run([sys.executable, "-m", "pip"] + pip_args, shell=True)
                except Exception as e:
                    print(f"{Fore.RED}Ошибка выполнения pip: {e}")

        elif main_cmd == "clear":
            os.system('cls')
            show_neofetch()

        elif main_cmd == "help":
            print(f"\n{C}СПИСОК КОМАНД:{W}")
            print(" fetch  - показать лого и инфо")
            print(" pip    - управление пакетами (pip install colorama)")
            print(" clear  - очистить экран")
            print(" exit   - выйти\n")

        elif main_cmd == "exit":
            print(f"{C}BB!{R}")
            break

        else:
            print(f"{Fore.RED}Команда '{main_cmd}' не распознана. Введи 'help'.")

        print("")


if __name__ == "__main__":
    start_terminal()