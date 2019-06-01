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
  ./name-gen.py r/us/mas
      generate one name based on lists/r/us/mas
  ./name-gen.py -n 5 r/us/fem
      generate five names based on lists/r/us/fem
  ./name-gen.py -n 5 r/us/mas,r/us/fem
      generate five names based on both lists combined
  ./name-gen.py -o names.txt -n 5 f/dun/sur
      generate five names based on lists/f/dun/sur and store
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
7 names saved in lists/names.
```

The script automatically detects duplicate names and fixes capitalization. Here's the contents of `lists/names` after the script is run:

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

*Note: `add-list.py` does not automatically assume taxonomy for the name lists you create. They will be stored in the `lists` directory, unsorted, until you choose to sort them.*

## How many names should be in a name list?
The more, the merrier. More names adds more potential variety to the names generated, while a shorter list will result in less diverse results.

## What name lists are currently included?
The name lists are sorted into subfolders within the `lists/` directory, dependent upon their taxonomy. Here is how they are organized:

```
lists           Included Name-Lists:
├── f             Fiction: Names from books, games, and other media.
│   ├── alt         Altmer -- The Elder Scrolls
│   │   ├── fem       Feminine Altmer names.
│   │   ├── mas       Masculine Altmer names.
│   │   └── sur       Altmer surnames.
│   ├── arg         Argonian -- The Elder Scrolls
│   │   ├── fem       Feminine Argonian names.
│   │   ├── mas       Masculine Argonian names.
│   │   └── sur       Argonian surnames.
│   ├── bos         Bosmer -- The Elder Scrolls
│   │   ├── fem       Feminine Bosmer names.
│   │   ├── mas       Masculine Bosmer names.
│   │   └── sur       Bosmer surnames.
│   ├── bre         Breton -- The Elder Scrolls
│   │   ├── fem       Feminine Breton names.
│   │   ├── mas       Masculine Breton names.
│   │   └── sur       Breton surnames.
│   ├── dun         Dunmer -- The Elder Scrolls
│   │   ├── fem       Feminine Dunmer names.
│   │   ├── mas       Masculine Dunmer names.
│   │   └── sur       Dunmer surnames.
│   ├── dwe         Dwemer -- The Elder Scrolls
│   │   └── rui       Dwemer ruins.
│   ├── imp         Imperial -- The Elder Scrolls
│   │   ├── fem       Feminine Imperial names.
│   │   ├── mas       Masculine Imperial names.
│   │   └── sur       Imperial surnames.
│   ├── kha         Khajiit -- The Elder Scrolls
│   │   ├── fem       Feminine Khajiit names.
│   │   ├── mas       Masculine Khajiit names.
│   │   └── sur       Khajiit surnames.
│   ├── nor         Nord -- The Elder Scrolls
│   │   ├── fem       Feminine Nord names.
│   │   ├── mas       Masculine Nord names.
│   │   └── sur       Nord surnames.
│   ├── orc         Orc -- The Elder Scrolls
│   │   ├── fem       Feminine Orc names.
│   │   ├── mas       Masculine Orc names.
│   │   └── sur       Orc surnames.
│   └── red         Redguard -- The Elder Scrolls
│       ├── fem       Feminine Redguard names.
│       ├── mas       Masculine Redguard names.
│       └── sur       Redguard surnames.
└── r             Reality: Names from real people, places and things.
    └── usa         USA -- The United States
        ├── fem       Feminine American names.
        ├── mas       Masculine American names.
        └── sur       American surnames.

13 directories, 33 files
```

**Note:** The Altmer, Argonian, Bosmer, Breton, Dunmer, Imperial, Khajiit, Nord, Orc and Redguard races and names belong to The Elder Scrolls games and their creators, and no claim is made by the author of this software of ownership of these names. The creator of this software included these names as an homage, not as a claim of any kind.
