# MAIN SCRIPT



RUN = True
PROMPT = "Enter your command: "


# This seems to be a main loop:

while RUN:
    user_input = input(PROMPT)

    if user_input == "exit":
        RUN = False
