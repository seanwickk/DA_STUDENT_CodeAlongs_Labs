#!/usr/bin/env python3
"""Lookups Matter: see DataChallengeOverview&Steps.md for the steps."""

import csv

DATA_FILE = "member_directory.csv"  # edit the filepath with the data
CHECKINS_FILE = "door_checkins.txt"  # edit the filepath with the data

with open(DATA_FILE, newline="") as f:
    members = list(csv.DictReader(f))

# One row represents one single person 
# Joined_on_home is a numeric field
# The same name popping up with different last name
# Step 1: Write `find_linear()` to Return the Member and Its Comparisons
def find_linear(members, member_id):
    comparison = 0
    for row in members:
        comparison +=1

    # TODO: assign `comparisons` to 0
    # TODO: loop over `members`; add 1 to `comparisons` for every row
        if row["member_id"] == member_id:
            return row, comparison
    # TODO: inside the loop, return row, comparisons on a member_id match
    # TODO: after the loop, return None, comparisons
    return None, comparison


row, count = find_linear(members, "M1150")
print("members in the directory:", len(members))
print("found:", row["name"], "at", row["home_branch"])
print("comparisons:", count)

# Step 1, answer 1:
# my predication is thomas member address will show up


# Step 2: Total the Comparisons for All 20 Swipes in `door_checkins.txt`
with open (CHECKINS_FILE) as f:
    swipes = f.read().splitlines()
linear_total = 0
not_members = 0
for member_id in swipes:
    row, comparison = find_linear(members, member_id)
    if row is None:                    # not found
        name = "NOT A MEMBER"
        not_members += 1
    else:
        name = row["name"]
    print(member_id, name, comparison)
    linear_total += comparison

    



# TODO: open CHECKINS_FILE in a with block as `f`
# TODO: inside it, assign `swipes` to f.read().splitlines()
# TODO: assign `linear_total` and `not_members` to 0
# TODO: loop over `swipes`; call find_linear(members, member_id)
# TODO: print the ID, the name or "NOT A MEMBER", and the comparisons
# TODO: add each count to `linear_total`
# TODO: add 1 to `not_members` for every swipe with no row

print("swipes:", len(swipes), "| not members:", not_members)
print("linear total comparisons:", linear_total)

# Step 2, answer 1:
#3 seconds i would say and each not member would be a second as well
# Step 2, answer 2:
# i would say the last code would take the longest since they must run through everything else


# Step 3: Build `members_by_id` and Find the Swipe Where It Pays Off
members_by_id = {}
build_steps = 0
for row in members:
    members_by_id[row["member_id"]] = row
    build_steps +=1
def find_dict(members_by_id, member_id):
    return members_by_id.get(member_id), 1
# TODO: assign `members_by_id` to an empty dict and `build_steps` to 0
# TODO: loop over `members`; store each row under row["member_id"]
# TODO: add 1 to `build_steps` for every row
# TODO: write find_dict(members_by_id, member_id)
# TODO: make find_dict() return members_by_id.get(member_id), 1

print("build cost:", build_steps, "| keys in the dict:", len(members_by_id))

# TODO: assign `linear_running` to 0 and `dict_running` to build_steps
linear_running = 0
dict_running = build_steps
pays_off_at = None
swipe_number = 0
# TODO: assign `pays_off_at` to None and `swipe_number` to 0
for member_id in swipes:
    swipe_number +=1
    # TODO: add 1 to `swipe_number`
    _, linear_count = find_linear(members, member_id)
    _, dict_count = find_dict(members_by_id, member_id)
    linear_running += linear_count
    dict_running += dict_count
    print (swipe_number, "the id", member_id, "linear", linear_count, "dict", dict_running)
    # TODO: add each search's count to its running total
    # TODO: print swipe_number, the ID and both running totals
    if pays_off_at is None and dict_running < linear_running:
        pays_off_at = swipe_number
        
    # TODO: the first time dict_running < linear_running, set `pays_off_at`

print("dict pays off at swipe:", pays_off_at)
print("morning totals | linear:", linear_running, "| dict:", dict_running)

# Step 3, answer 1:
# 
# Step 3, answer 2:
# The door does the same job over and over: take an ID and find that member.
# Step 3, answer 3:
#332 mornings


# Step 4: Test an AI Speed Claim Against Your Totals and Write a Verdict
# TODO: replace the text below with your AI's claim, word for word
ai_claim = "For 20 lookups across 312 rows, a pre-built dictionary lookup is roughly 100x to 150x faster than a linear search "
print("AI CLAIM:", ai_claim)

_, front_count = find_linear(members, swipes[0])
_, absent_count = find_linear(members, "M1313")
ratio = round(linear_running / dict_running, 1)
# TODO: unpack find_linear() for swipes[0] into `_, front_count`
# TODO: unpack find_linear() for "M1313" into `_, absent_count`
# TODO: assign `ratio` to round(linear_running / dict_running, 1)

print("one front-of-file swipe | linear:", front_count, "| dict: 1")
print("one non-member swipe | linear:", absent_count, "| dict: 1")
print("whole morning | linear:", linear_running, "| dict:", dict_running,
      "| ratio:", ratio)

# TODO: replace the text below with your own verdict
verdict = "inear search ties a dict when an item is right at the start of the list"
print("VERDICT:", verdict)

# Step 4, answer 1:
# 
# Step 4, answer 2:
#No
