"""Markov Chain Name Generator.

This module includes a random name generator which uses Markov chains to create
semirealistic character names, based on lists of real names taken from 1990s
census data. New names can be requested based on gender, specified as 'male',
'female', or 'agender'.

This module is based on public-domain code created by Peter Corbett, used in
the Mines of Elderlore game. The original code can be found here:

http://www.roguebasin.com/index.php?title=Markov_chains_name_generator_in_Python

author: CMSteffen - cmsteffen@protonmail.com
"""

import random


class Mdict(object):
    """Mdict Class by Peter Corbett."""

    def __init__(self):
        """Initialize Mdict."""
        self.d = {}

    def __getitem__(self, key):
        """Get an item."""
        if key in self.d:
            return self.d[key]
        else:
            raise KeyError(key)

    def add_key(self, prefix, suffix):
        """Add a key."""
        if prefix in self.d:
            self.d[prefix].append(suffix)
        else:
            self.d[prefix] = [suffix]

    def get_suffix(self, prefix):
        """Get a suffix."""
        suffix_list = self[prefix]
        return random.choice(suffix_list)


class MName(object):
    """MName Class by Peter Corbett.

    Create a name from a Markov chain.
    """

    def __init__(self, source_list, chainlen=2):
        """Build the dictionary."""
        if chainlen > 10 or chainlen < 1:
            print("Chain length must be between 1 and 10, inclusive")
            sys.exit(0)

        self.mcd = Mdict()
        oldnames = []
        self.chainlen = chainlen

        for list_item in source_list:
            list_item = list_item.strip()
            oldnames.append(list_item)
            s = " " * chainlen + list_item
            for n in range(0, len(list_item)):
                self.mcd.add_key(s[n : n + chainlen], s[n + chainlen])
            self.mcd.add_key(
                s[len(list_item) : len(list_item) + chainlen], "\n"
            )

    def New(self):
        """Create a new name from the Markov chain."""
        prefix = " " * self.chainlen
        name = ""
        suffix = ""
        while True:
            suffix = self.mcd.get_suffix(prefix)
            if suffix == "\n" or len(name) > 9:
                break
            else:
                name = name + suffix
                prefix = prefix[1:] + suffix
        return name.capitalize()


class NameGenerator(object):
    """NameGenerator Class by CMSteffen.

    A Markov-Chain Random Name Generator.
    """

    # ---[ PRIVATE METHODS ]--- #

    def __init__(self):
        """Initialize the Name Generator."""
        self.Male_List = self.__load_list("libs/namelists/male.txt")
        self.Female_List = self.__load_list("libs/namelists/female.txt")

    def __load_list(self, filename):
        """Load a list of names from the specified text file."""
        return [item.strip() for item in open(filename, "r").readlines()]

    def __pull_random(self, source_list, count):
        """Pull [count] random elements from [source_list]."""
        source_list = list(source_list)
        new_list = []
        for x in range(count):
            new_list.append(
                source_list.pop(random.choice(range(len(source_list))))
            )
        return new_list

    def __pick_names(self, gender):
        """Pick 1000 random names from the specified gendered list."""
        names = []
        if gender == "male":
            names = self.__pull_random(self.Male_List, 1000)
        elif gender == "female":
            names = self.__pull_random(self.Female_List, 1000)
        elif gender == "agender":
            names = self.__pull_random(self.Male_List, 500)
            names += self.__pull_random(self.Female_List, 500)
        else:
            raise ValueError("Invalid gender specified: {}".format(gender))
        return names

    # ---[ PUBLIC METHODS ]--- #

    def get_name(self, gender):
        """Generate a new name for the specified gender."""
        return MName(self.__pick_names(gender)).New()
