def do_stuff():
    i : int = 0
    for b in [False, True]:
        if b:
            print("yes")
        else:
            print("no")
    for s in ["a","b","c"]:
        print(s)
    while i < 10:
        print(i)
        i = i + 1

class Student (object):
    name: str
    points: int
    passing: bool
    def __init__(self, name: str, points: int, passing: bool):
        self.name = name
        self.points = points
        self.passing = passing
    def print(self):
        print(self.name)
        print(self.points)
        print(self.passing)


def main():
    do_stuff()
    s: "Student" = Student("Peter Anteater", 99, True)
    s.print()
    print("\n")

main()
