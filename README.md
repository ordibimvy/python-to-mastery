# Mad Libs Program

A small Python command-line game. It asks you a few questions about yourself, then has you fill in random words to build a short, ridiculous story.

## What it does

**Part 1 — Intro**
Asks for your name, age, bank balance, and relationship status, and reacts to each answer. Includes some (very unserious) divorce math.

**Part 2 — Mad Libs**
Collects 13 words — adjectives, nouns, a celebrity, a body part, and so on — without telling you what they're for. Then it drops them into a pre-written story and prints the result.

## Requirements

- Python 3.6 or newer (the story uses f-strings)
- No external libraries

## How to run

```bash
python madlibs.py
```

Then just answer the prompts. Type whatever you want — the weirder the words, the better the story.

## Example

```
An adjective: soggy
A plural noun: traffic cones
A verb ending in -ing: sprinting
...

========================================
   THE SOGGY DAY OF ORDI
========================================

It was a soggy morning when Ordi woke up surrounded by
traffic cones. Nobody knew how they got there...
```

## Python concepts used

- Variables and assignment
- `input()` for user input
- `if` / `else` conditionals and nesting
- Type casting with `int()`
- String concatenation and f-strings
- Multi-line strings with triple quotes
- Arithmetic (division)

## Notes

Answers are not saved anywhere — everything disappears when the program ends.
