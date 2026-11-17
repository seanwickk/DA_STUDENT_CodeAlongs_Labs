#!/usr/bin/env python3
"""Lab: Solo Class Design Rep
GitBook Quest 1.8: Meet the Objects

HOW TO RUN
    Open a terminal in this file's folder and run:
        python3 solo-class-design-practice_STUDENT.py
    Or make it executable once:
        chmod +x solo-class-design-practice_STUDENT.py
    and from then on run it directly:
        ./solo-class-design-practice_STUDENT.py
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
    Commit this file (you may rename it solo-class-design-practice.py) to your own data
    challenge repo, inside your Module 1 folder. Paste its direct GitHub URL
    into the LMS.
"""

# ===== Step 1: Read the Stakeholder Need =====
# A new stakeholder need. Not the board-game or office-supply domain from
# lecture, and not one of the project's own 4 scenarios.

    
       
               

 


        


# Your answer:
# Tools_keeper has become the name for my classification since it aligns with my job
#

# ===== Step 2: Decide Your Attributes, Each With a Reason From the Scenario =====
     

# Your answer:
# I have chosen those atributes since it helps me idenify a specific tool, given their name, avability, and if a repaiir is needed.

# ===== Step 3: Write __init__ and a Method, From Scratch =====
class Tools_keeper:
    def __init__(self, Power_tool, Status_for_use, Status_for_maintenance):
        self.Power_tool = Power_tool
        self.status_for_use = Status_for_use
        self.status_for_maintenance = Status_for_maintenance
        return

    def Mantain(self):
        if self.status_for_maintenance == True:
            return "yes needed repair"
        else:
            return "all good"
# There is no single correct design here. Your class name, your attribute
# names and your method can all differ from everyone else's and still be
# right. The test is whether each one traces back to the stakeholder
# paragraph.

# TODO: Write __init__ and a Method, From Scratch

# ===== Step 4: Instantiate 2+ Objects, Confirm Independent Storage =====
# The same proof Day 13's lecture asked for, now on a class you designed
# yourself. Predict what each print() will show before you run it.

# TODO: Instantiate 2+ Objects, Confirm Independent Storage
drill = Tools_keeper("Drill", 3, True)
ladders = Tools_keeper("Ladders", 2, False,)
pressure_washer = Tools_keeper("Pressure Washer", 7, True,)
Tools = [drill, ladders, pressure_washer]
# ===== Step 5: Justify Your Design Choice in 2-3 Sentences =====
print("DRILL", drill.Mantain()) # It will print needed repair since the boolen is true statement
# Your answer:
# I picked to create a list instead of a JSON file since it was simpler to map out and identify what I want from the list. JSON kept giving me errors and I was running in circles. I also wanted each value for my power tools to be easily analyzed as well, that's why I've chosen 3 attributes for each power tool.
#

# ----- Share Out -----
# Last 15 minutes, back together as a class. Bring:
#
# Come ready to show your class and defend it. Specifically:
# - The attribute list you chose, and for each one, the phrase in the
#   coordinator's request it came from. If you can't point at a phrase for
#   an attribute, say so - that's a real finding, not a failure.
# - One attribute you considered and rejected, and why. - Your method: what
#   question does it answer, and why would the coordinator reach for it
#   first?
# - Anything you got stuck on. Designing from a paragraph with nobody to
#   check against is genuinely hard, and naming where it was hard is worth
#   more to the room than a tidy answer.
#
# Expect to be asked "why that attribute and not another?" - there is no
# single right list here, so the reasoning IS the answer.
#
# Be ready to answer "why did you do it that way?"

# Your notes for the share out:
## One attribute I did consider was an ID field for each individual tool, but that felt like it would require
# about 10x the coding since I’d have to define one for every different tool. The method I went with instead
# lets the user quickly see whether maintenance is required for that category of power tools. That check
# should be one of the first things that happens, since they shouldn’t be handing out power tools if they
# aren’t cleaned it’s a real hazard.
#
# I definitely got stuck early on deciding how to format the data. At first I thought JSON would be easier
# to manage, but I was completely wrong. I had a much simpler time working with a plain list.
#
