#!/usr/bin/env python3

"""Properly format name lists and add them to the `lists` directory."""

import sys

if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} [names.txt] [one-word name for list]")
    print(f"Example: {sys.argv[0]} demo.txt demo_names")
    print("  This would format the names in demo.txt and store them")
    print("  in lists/demo_names.")
    sys.exit(0)

with open(sys.argv[1]) as f:
    names = sorted(
        set(
            [
                name.strip().capitalize()
                for name
                in ",".join(
                    [
                        line.strip()
                        for line
                        in f.readlines()
                    ]
                ).split(",")
                if name.strip() != ""
            ]
        )
    )
output = "\n".join(names)
with open(f"lists/{sys.argv[2]}", "w") as f:
    f.write(output)
print(f"{len(names)} names saved in lists/{sys.argv[2]}.")
