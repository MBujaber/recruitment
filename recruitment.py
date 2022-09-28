# This function returns a list of skills.
# This is the list that the user will choose from
# Add at least 3 random skills for the user to select from
from operator import truediv


def get_skills():
    skills = ["Python","C++","Javascript","Juggling","Running","Eating"]
    return skills
# print(get_skills())    

# This function pretty prints the skills to the user
# It takes the list of skills as an argument and prints them numbered
# This function doesn't return anything
skills = get_skills()
def show_skills(skills):
    print("Skills: ")
    # skills = get_skills()
    for number, letter in enumerate(skills, 1):
        print(f"{number}, {letter}")



# Shows the available skills and have user pick from them two skills
# HINT: Use previous built functions to show the skills
# For example, if the user enters 1, the first skill in your list of skills will be added to the list
# Return a list of the two skills that the user inputted


def get_user_skills(skills):
    # skills = get_skills()
    print(show_skills(get_skills()))
    skill_1 = int(input(f"Choose a skill from above by entering its number: "))
    skill_2 = int(input(f"Choose another skill from above by entering its number: "))
    lst = [skills[skill_1 -1], skills[skill_2 -1]]
    # selected_skills = [skill_1, skill_2]
    return lst

# print(get_user_skills(skills))

# This function will get the user's cv from their inputs
# HINT: Use previous built functions to get the skills from the user
def get_user_cv(skills):
    cv = {}
    name = input("What's your name: ")
    age = int(input("How old are you? "))
    experience = int(input("How many years of experience do you have? "))
    cv= {
        "name": name, 
        "age": age,
        "experience": experience,
        "skills": get_user_skills(skills),
    }
    return cv
# print(get_user_cv(skills))
# This functions checks if the cv is acceptable or not, by checking the age, experience and skills and return a boolean (True or False) based on that
def check_acceptance(cv, desired_skill):
    if 25 <= cv["age"] <= 40 and cv["experience"] > 3 and desired_skill in cv["skills"]:
        return True 
    else:
        return False
    

# print(check_acceptance(get_user_cv(skills), "Javascript"))

def main():
    # Write your main logic here by combining the functions above into the
    # desired outcome
    print("Welcome to the special recruitment program, please answer the following questions:")
    skills = get_skills()
    user_cv = get_user_cv(skills)
    is_accepted = check_acceptance(user_cv, "Python")
    # print(check_acceptance(get_user_cv(skills), "Javascript"))
    if is_accepted:
        print(f"You have been accepted, {user_cv['name']}!")
    else:
        print("You have been Rejected")
#still not finish
if __name__ == "__main__":
    main()
