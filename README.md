# Name-Gen
A Markov chain random name generator.

## A what now?
This application generates random names using math and large lists of extant names.

## How do I use it?
```
usage: name-gen.py [-h] [-n NUM] [-o OUT] lists

Generate random names with Markov chains. Names are generated
based on seed names read from text files located in the lists
directory.

positional arguments:
  lists              comma-separated list selections

optional arguments:
  -h, --help         show this help message and exit
  -n NUM, --num NUM  how many names to generate
  -o OUT, --out OUT  output file name

examples:
  ./name-gen.py male
      generate one name based on lists/male.txt
  ./name-gen.py -n 5 female
      generate five names based on lists/female.txt
  ./name-gen.py -n 5 male,female
      generate five names based on both lists combined
  ./name-gen.py -o names.txt -n 5 last
      generate five names based on lists/last.txt and store
      them in names.txt
```

## Where can I find these name lists?
Name lists are stored in the 'lists' directory. Name-Gen allows you to select one or more name lists from which to derive new names. You can even add your own lists!

## I can create my own lists?
It's not hard. The lists are simply text files with one name per line. To create a new name list, simply add your names to a .txt file and give it a unique one-word name.

## How many names should be in a name list?
The more, the merrier. More names adds more potential variety to the names generated, while a shorter list will result in less diverse results. The included name lists each have at least 500 names.

## What name lists are currently included?
* female.txt: 4,098 female first names taken from U.S. Census data.
* male.txt: 1,147 male first names taken from U.S. Census data.
* last.txt: 1,118 surnames taken from U.S. Census data.
