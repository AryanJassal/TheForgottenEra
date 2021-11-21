import os
import sys


def clear_screen():
    os.system('cls clear')


def pause_screen(prompt=''):
    print(prompt)
    if os.name == 'nt':
        import msvcrt as m
        result = m.getch()

    else:
        # That's a lot of code just to get a character from a linux terminal in python
        import termios
        fd = sys.stdin.fileno()

        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)

        try:
            result = sys.stdin.read(1)
        except IOError:
            pass
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)

    return
    # return result
