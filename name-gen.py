#!/usr/bin/env python3

usage = """
Name-Gen Frontend.

This application generates random names from predefined lists. It allows for
combining lists or adding your own. The lists are defined in the "lists"
directory, as text files with one name per line. To create a new name list,
simply give it a unique one-word name and write one name per line within the
list. The bigger, the better. At least 1,000 names is preferred, but if there
are less, that's okay.

Usage:
name-gen.py [options] [name lists]

Options:
-n [#]      The number of names to be generated.

Examples:
name-gen.py male              Generate one name based on lists/male.txt
name-gen.py -n 5 female       Generate five names based on lists/female.txt
name-gen.py -n 5 male,female  Generate five names based on both lists combined
"""

import argparse, sys, textwrap

from libs.markov import NameGenerator


def pnr(object):
    print(f"[-]   {object}")
    return object

def read_args():
    parser = argparse.ArgumentParser(
        description=textwrap.dedent("""\
            Generate random names with Markov chains. Names are generated
            based on seed names read from text files located in the lists
            directory.
        """),
        epilog=textwrap.dedent(
            f"""\
            examples:
              {sys.argv[0]} male
                  generate one name based on lists/male.txt
              {sys.argv[0]} -n 5 female
                  generate five names based on lists/female.txt
              {sys.argv[0]} -n 5 male,female
                  generate five names based on both lists combined
            """
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "-n",
        "--num",
        type=int,
        default=1,
        help="how many names to generate"
    )
    parser.add_argument("lists", help="comma-separated list selections")
    return parser.parse_args()


args = read_args()

print("[*] Name-Gen by CMSteffen (v0.0.0)")
print("[*] Lists selected:")
lists = [
    pnr(list)
    for list
    in args.lists.split(",")
]

NameGen = NameGenerator(lists)
print("[*] Names generated:")
names = [
    pnr(name)
    for name
    in NameGen.generate(args.num)
]
