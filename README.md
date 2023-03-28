# code-challenge-jpc-345

This is a public repo for a code that replaces each word in a sentence with a specific format. Made for JPC 345 code challenge

# Usage

The program can be run from the command line in the repository location using the following command:

`python3 app/main.py`

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

# Notes

    - The program only works with alphabetical characters.
    - The separators are maintained in their original form and location in the answer.
    - The program is case-sensitive.
    - If the input sentence contains any non-alphabetic character without space, it will consider each word between separately.
