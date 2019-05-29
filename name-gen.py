#!/usr/bin/env python3

usage = """Name-Gen Frontend."""

import argparse, sys, textwrap

from libs.markov import NameGenerator


def pnr(obj):
    print(f"[-]   {obj}")
    return obj

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
              {sys.argv[0]} -o names.txt -n 5 female
                  generate five names based on lists/female.txt and store
                  them in names.txt
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
    parser.add_argument(
        "-o",
        "--out",
        default=None,
        help="output file name",
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

if args.out:
    with open(args.out, "w") as f:
        f.write("\n".join(names))
    print(f"[*] Names saved to {args.out}.")
