import chapter1 as ch1
import chapter2 as ch2
import chapter3 as ch3

from addon_code.console import screen_clear as clear


def first():
    ch1.Chapter1_Menu()

def second():
    ch2.Chapter2_Menu()


options = { 1: first,
            2: second,

    }


if __name__ == "__main__":

    print("Select a Chapter")
    print("1. Chapter 1")
    print("2. Chapter 2")

    num = int(input())
    clear()
    options[num]()

    




