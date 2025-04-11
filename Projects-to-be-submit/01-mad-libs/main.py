def main():

    adjective: str = input("Adjective: ")
    name: str = input("Person name: ")
    noun: str = input("Noun: ")
    verb1: str = input("Verb: ")
    verb2: str = input("Another verb: ")
    number: str = input("Number: ")
    symbol: str = input("Symbol: ")

    madlib: str = f"""
    I was writing a {adjective} Python script when suddenly, {name} yelled 😱,
    "Why is this {noun} not working?! 😩"

    Turns out, they forgot to {verb1} the {noun} before running it. 🤦‍♂️
    After {number} hours of debugging ⏰, the solution was just adding a {symbol} ⚡️.

    Moral of the story: Always {verb1} before you {verb2}! 😅💡
    """

    print(madlib)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass