#!skills-py-venv/Scripts/python.exe

# This script is used to update the categories of the skills in the database from the categories md file in the skills repo
# source/skills/public/Categories Kanban.md

# The script is run from the skills-py-venv/Scripts directory

if __name__ == __main__: 
    print("Updating the categories of the skills in the database from the categories md file in the skills repo")
    
def importSkillsCategories():
    import os
    import sys
    import re

    # Add the parent directory to the path
    sys.path.append(os.getcwd() + "/..")

    # Open the categories md file
    with open("../../../skills/public/Categories Kanban.md", "r") as f:
        lines = f.readlines()

    # Create the skills db
    db = SkillsDB()

    # Iterate through the lines in the file
    for line in lines:

        # Get the skill category from the line add it to an array
        skill_category = line.split("|")[1].strip()

        # Get the skills from the line and add them to an array
        skills = line.split("|")[2].strip().split(",")

        # Iterate through the skills
        for skill in skills:
            # Remove the whitespace from the skill
            skill = skill.strip()

            # Get the skill from the db
            skill = db.getSkill(skill)

            # Update the skill category
            skill.category = skill_category

            # Update the skill in the db
            db.updateSkill(skill)
