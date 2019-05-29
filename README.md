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

### There's gotta be an easier way.
Easier than putting one name per line in a plain text file?

Well, yes, actually. A utility has been included, called `add-list.py`, which will automatically format your name list and add it to the `lists` directory. If you want to use this tool, simply fill a text file with names that are separated by commas or new lines. Then, use `add-list.py` like so:

```
add-list.py [list.txt] [list name]
```

For example, let's say you've got the following list of names called `names.txt`:

```
susan, alana, julia, mallory,

ALEXANDRA,, , alexandra
blaise
,
janice, susan, alana,,

```

That's pretty sloppy, but `add-list.py` can handle it:

```
bash@localhost$ ./add-list.py names.txt names
7 names saved in lists/names.txt.
```

The script automatically detects duplicate names and fixes capitalization. Here's the contents of `lists/names.txt` after the script is run:

```
Alana
Alexandra
Blaise
Janice
Julia
Mallory
Susan
```

Then, to use that name list, simply call it by name:

```
bash@localhost$ ./name-gen.py names
[*] Name-Gen by CMSteffen (v0.0.1)
[*] Lists selected:
[-]   names
[*] Names generated:
[-]   Alaise
```


## How many names should be in a name list?
The more, the merrier. More names adds more potential variety to the names generated, while a shorter list will result in less diverse results.

## What name lists are currently included?
### Human Names from the United States
* female.txt: 4,098 female first names taken from U.S. Census data.
* male.txt: 1,147 male first names taken from U.S. Census data.
* last.txt: 1,118 surnames taken from U.S. Census data.
### Racial Names from The Elder Scrolls Games
* altmer_female.txt: 982 female Altmer first names.
* altmer_male.txt: 1,175 male Altmer first names.
* altmer_family.txt: 165 Altmer family surnames.
* argonian_female.txt: 928 female Argonian first names.
* argonian_male.txt: 984 male Argonian first names.
* argonian_family.txt: 169 Argonian family surnames.
* dunmer_female.txt: 1,471 female Dunmer first names.
* dunmer_male.txt: 1,729 male Dunmer first names.
* dunmer_family.txt: 1,344 Dunmer family surnames.
