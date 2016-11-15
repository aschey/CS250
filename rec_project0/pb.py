import sys
from contact import Contact

class Phonebook:

    # Special Method (**Constructor**)
    def __init__(self):
        self._entries = [] # private field named entries

    # Method (Mutator)
    def add_entry(self, name, number):
        newContact = Contact(name, number)
        self._entries.append(newContact)

    # Method (Accessor/Query)
    def lookup(self, name):
        for entry in self._entries:
            if entry.get_name() == name:
                return entry.get_number()
        return "Private Number"

    # Method (Accessor/Query)
    def reverse_lookup(self, number):
        for entry in self._entries:
            if entry.get_number() == number:
                return entry.get_name()
        return "Unknown"

    # Method (Accessor/Query)
    def size(self):
        return len(self._entries)

    def load(self, filename):
        f = open(filename, "r")
        lines = f.readlines()
        for l in lines:
            contacts = l.split()
            for c in contacts:
                c = c.split(":")
                self.add_entry(c[0], c[1])

    # Special Method
    def __str__(self):
        s = ''
        for entry in self._entries:
            s += entry.get_name() + ' ' + entry.get_number() + '\n'
        return s


def main(argv):
    pb = Phonebook() # calls Phonebook.__init__
    pb.add_entry("Nicholas Kraft", "205-555-5555")
    pb.add_entry("Elizabeth Williams", "256-555-5555")
    pb.load("data.txt")
    #print(pb, end='') # calls Phonebook.__str__
    print(pb) # equivalent to line 43
    print(pb.lookup("Nicholas Kraft"))
    print(pb.lookup("Jonathan Corley"))
    print(pb.reverse_lookup("256-555-5555"))
    print(pb.reverse_lookup("812-555-5555"))
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
