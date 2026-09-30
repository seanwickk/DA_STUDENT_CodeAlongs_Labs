# Dev Environment & Data Fundamentals

**Module 0: Foundations** food feelgi

**Learning Objectives:**
- Have a working terminal, git, and VS Code setup on your own machine
- Define variable, data type, and data structure in your own words
- Correctly label 5 everyday examples by data type

## Scenario

You're starting your first week as a data analyst, and IT just handed you a blank laptop. Before you can look at a single spreadsheet, you need a real terminal, git, and VS Code set up the way working analysts actually use them - and a shared vocabulary (variable, data type, data structure) for describing what you're looking at once you do.

> **How to use this worksheet:** each shaded block below (the ones starting with three backtick marks and the word "bash") contains real commands - type them into your own terminal, one line at a time. The backtick fence marks themselves aren't something you type, they just tell this file "this is code." A `# TODO:` line means: replace it with the real command.

## Check Your Environment

*Context: code --version only works once VS Code's 'code' command is installed to your PATH — the setup guide covers this. If the two git config lines print nothing, set them now: git config --global user.name "Your Name" and git config --global user.email "you@example.com" — without this, the first real commit in the git lecture will fail with a real, confusing error.*

**AI Mode:** Try Without AI, Then Tutor If Stuck

*Complete the TODOs below as you work through this step.*

```bash
# TODO: check which shell you're using
# TODO: confirm git is installed and see its version
# TODO: confirm VS Code's command-line tool is installed
# TODO: confirm git knows your name
# TODO: confirm git knows your email
```

## Look Before You Type

*Context: This file is real energy-consumption data from Our World in Data (OWID) — not the dataset you'll use for your own project, just a safe one to practice on today.*

```bash
# open a real data file in a plain text view BEFORE
# running any inspection command on it
$ head -n 3 data/energy_sample.csv
```

## Find Your Way Around

*Context: pwd prints your current folder; ls lists what's in it; cd moves into another folder.*

**AI Mode:** Try Without AI, Then Tutor If Stuck

*Complete the TODOs below as you work through this step.*

```bash
# TODO: print your current directory
# TODO: list what's in it
# TODO: move into the modules folder
# TODO: list what's in there
```

## A Typo Looks Like This

*Note: this command is expected to fail/raise `command not found` - that's the teaching point, not a bug.*

*Context: gti is a real, extremely common typo of git - this fails reliably on every system, no exceptions.*

```bash
# a genuine typo - not a real command anywhere
$ gti status
```
