# code-challenge-jpc-345

This is a program that parses a sentence and replaces each word with the following: first letter,
number of distinct characters between first and last character, and last letter.
Words are separated by spaces or non-alphabetic characters and
these separators should be maintained in their original form and location in the answer.

Examples:

1. “Smooth” becomes “S3h”
2. “Space separated” becomes “S3e s5d”
3. “Dash-separated” becomes “D2h-s5d”
4. “Number2separated” becomes “N4r2s5d”

Made for JPC 345 code challenge

## Author

Martin Carmona Diaz

## Last update

28/03/2023

## Basic Usage

Requirements should be installed with pip:

`pip install -r requirements`

The program can be run from the command line in the repository location using the following command:

`python3 -m app --sentence "Hello world! This is an example sentence"`

To run tests in the command line use the following command:

`python3 -m unittest tests/test_main.py`

## Docker Usage

You should have Docker installed in your machine and build the image with

`docker build -t code-challenge-jpc-345 .`

The program can be run from Docker int the command line in the repository location using the following command:

`docker run --rm code-challenge-jpc-345 --sentence "Hello world! This is an example sentence"`

## Repository Layout

This repo uses the monorepo format, to contain all of the things for the project.

```
.
├── README.md
├── .gitignore
├── app                     <== Main project code
│   ├── __init__.py
│   ├── utils               <== Functions made to parse sentences
│   └── main
└── test                    <== Tests module
    ├── __init__.py
    └── test.py             <== Project tests script
```

## Notes

    - The program only works with alphabetical characters.
    - The separators are maintained in their original form and location in the answer.
    - The program is case-sensitive.
    - If the input sentence contains any non-alphabetic character without space, it will consider each word between separately.
    - As the project doesn't give any information about the behaviour of the functions with non string variables, all of those cases will be considered returning None.
