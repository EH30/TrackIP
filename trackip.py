import os
import sys


def check_system():
    if sys.platform == "linux" or sys.platform == "linux2":
        os.system("clear")
        return "linux"
    elif sys.platform == "win32":
        os.system("cls")
        return "win32"



def run_server():
    os.chdir("djserver")
    print("[+] wait for the server to start on this window")
    print("[+] Send the https link that should open in a new termnal/cmd")
    print("[+] make sure your sending the https link not http\n")
    os.system("manage.py runserver 127.0.0.1:80")


if __name__ == "__main__":
    if check_system() == "linux":
        output = os.system("xterm -e ngrok_linux http 80")

        if output >= 1:
            print("[-}Error You may need to install xterm")
        else:
            run_server()

    elif check_system() == "win32":
        output = os.system("start call ngrok_win32.exe http 80")

        if output >= 1:
            print("[-]Error")
        else:
            run_server()
