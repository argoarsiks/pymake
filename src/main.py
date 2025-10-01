import ctypes
from pathlib import Path
import sys
import winreg
from utils.show_version import show_version
import subprocess


def add_path():
    try:
        if getattr(sys, "frozen", False):
            path_to_add = Path(sys.executable).parent
        else:
            path_to_add = Path(__file__).parent

        with winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            "Environment",
            0,
            winreg.KEY_READ | winreg.KEY_SET_VALUE,
        ) as key:
            current_path, _ = winreg.QueryValueEx(key, "Path")

            if "pymake" not in current_path:
                new_path = current_path + ";" + str(path_to_add)
                winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, new_path)
                ctypes.windll.user32.SendMessageW(0xFFFF, 0x1A, 0, "Environment")

    except Exception as e:
        print(e)


def parse_makefile(target_command: str):
    current_dir = Path.cwd()
    makefile_path = current_dir / "Makefile"

    if makefile_path.exists():
        found_target = False
        commands_to_execute = []

        with open(makefile_path, "r", encoding="utf-8") as f:
            lines = f.read()

            for line in lines.split("\n"):
                line = line.rstrip()

                if not line or line.startswith("#"):
                    continue
                if ":" in line:
                    target = line.split(":")[0].strip()
                    if target == target_command:
                        found_target = True
                elif found_target and line.startswith("\t"):
                    command = line.strip()
                    if command:
                        commands_to_execute.append(command)

            if found_target and commands_to_execute:
                execute_commands(commands_to_execute)
            elif target_command and not found_target:
                print(f"{target_command} is not found")

    else:
        print("Makefile is not found")


def execute_commands(commands: list):
    for command in commands:
        subprocess.run(command, shell=True, cwd=Path.cwd())


def main():
    add_path()
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == "--version" or arg == "-v":
            show_version()
        else:
            parse_makefile(arg)


if __name__ == "__main__":
    main()
