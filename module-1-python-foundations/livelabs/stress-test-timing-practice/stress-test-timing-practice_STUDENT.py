#!/usr/bin/env python3
"""Lab: Stress-Test Your Code: Timing & Efficiency
GitBook Quest 1.9: Lookups Matter

HOW TO RUN
    Open a terminal in this file's folder and run:
        python3 stress-test-timing-practice_STUDENT.py
    Or make it executable once:
        chmod +x stress-test-timing-practice_STUDENT.py
    and from then on run it directly:
        ./stress-test-timing-practice_STUDENT.py
    The first line, #!/usr/bin/env python3 (the "shebang"), is what
    makes ./ work. python3 <file> ignores it as a comment.

ANSWER EVERYTHING IN THIS FILE
    - Code goes under each step's banner.
    - Written answers go in # comments under each "# Your answer:"
      line.
    - Run the file after every change. It runs top to bottom, so a
      later step can use anything an earlier step made.

HINTS live in the worksheet (LiveLabOverview&Steps.md), collapsed
under each step. Open one only when you are stuck.

SUBMIT
    Commit this file (you may rename it stress-test-timing-practice.py) to your own data
    challenge repo, inside your Module 1 folder. Paste its direct GitHub URL
    into the LMS.
"""

# ===== Step 1: Generate Batches of Your Own Day 15 Class at Three Sizes (10, 1,000, and 100,000) =====
# Use your own class from Day 15's lab - your batch should be full of YOUR
# objects, not a shared template's.

# TODO: Generate Batches of Your Own Day 15 Class at Three Sizes (10, 1,000, and 100,000)
class number_work:
    def __init__(self, numbers_100, numbers_1000, numbers_1000000):
        self.numbers_100 = numbers_100
        self.numbers_1000 = numbers_1000
        self.numbers_1000000 = numbers_1000000


batches = [
    number_work(10, 1000, 100000),
    number_work(200, 2000, 2000000),
    number_work(300, 3000, 3000000)
    
]
    

# ===== Step 2: Write Two Searches Over That Batch - a Linear Scan and a Dict Lookup - and Confirm They Agree =====
# Same two functions Day 16's lecture wrote over SupplyItem - now over your
# own class and a much bigger batch.

# TODO: Write Two Searches Over That Batch - a Linear Scan and a Dict Lookup - and Confirm They Agree

def linear_scan(batches, numbers_100):
    for items in batches:
        if items.numbers_100 == numbers_100:
            return items
        
    return None

def dict_lookup(batches, numbers_100):
    for item in batches:
        if item.get(numbers_100) is not None:
            return item
    return None



Numeric_display = linear_scan(batches, 200)
print(Numeric_display.numbers_100,)
# ===== Step 3: Put a Stopwatch on Both Searches at All Three Sizes and Record the Numbers =====
# Predict the pattern before running: which column should grow as size
# grows, and which should stay roughly flat?

# TODO: Put a Stopwatch on Both Searches at All Three Sizes and Record the Numbers
import time

input("start time")
Start_time = time.perf_counter()
input("end time")
end_time = time.perf_counter()
total = end_time - Start_time
print(total, "seconds")
# ===== Step 4: Answer Your Manager's Question in One Sentence, in Big-O Terms =====

# Your answer:
#
#

# ===== Step 5: Optional Stretch: Ask an AI How to Speed Up Your Linear Scan, Then Make It Prove It =====
# Stretch work only - beyond the core lab budget. Take it if you finish
# Steps 1-4 early. Same 'verify before trusting' habit from Module 0's
# AI-literacy lesson, now applied to a code-optimization claim instead of a
# chatbot fact claim.

# Your answer:
#
#

# ----- Share Out -----
# Last 15 minutes, back together as a class. Bring:
#
# Bring your numbers, not a summary of them. Specifically:
# - Your timings at each batch size, for both searches. Everyone tested a
#   different class on a different laptop, so the raw numbers won't match -
#   put yours up anyway.
# - Which column changed as the batch grew, and which one didn't. - The
#   batch size where the difference stopped being something you had to
#   squint at.
# - Whether anything surprised you. A linear scan that looked suspiciously
#   flat is worth raising - say what you found out was going on.
# - If you tried the AI stretch: what it claimed, and whether your own
#   timings actually backed it up. "It was wrong" is a good answer if you
#   can show the number that proves it.
#
# Be ready for "why does that happen?" - the timings are evidence, and the
# explanation is what's being assessed.
#
# Be ready to answer "why did you do it that way?"

# Your notes for the share out:
#
#
