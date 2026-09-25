coachType = input("Enter your coach type (sleeper | ac | general | luxury): ").lower()


def get_coach_price(coach_type):
    match coach_type:
        case "sleeper":
            return f"Your ticket in {coach_type} coach is confirmed. Please wait for 10 minutes."

        case "ac":
            return f"Your ticket in {coach_type} coach is confirmed. Please wait for 10 minutes."

        case "general":
            return f"Your ticket in {coach_type} coach is confirmed. Please wait for 10 minutes."

        case "luxury":
            return f"Your ticket in {coach_type} coach is confirmed. Please wait for 10 minutes."

        case _:
            return "Invalid coach type. Please choose from sleeper, ac, general, or luxury."


print(get_coach_price(coachType))


# 2 nd way to do this in switch case in python 

coachType = input(
    "Enter your coach type (sleeper | ac | general | luxury): "
).lower()

match coachType:
    case "sleeper":
        print(f"Your ticket in {coachType} coach is confirmed. Please wait for 10 minutes.")

    case "ac":
        print(f"Your ticket in {coachType} coach is confirmed. Please wait for 10 minutes.")

    case "general":
        print(f"Your ticket in {coachType} coach is confirmed. Please wait for 10 minutes.")

    case "luxury":
        print(f"Your ticket in {coachType} coach is confirmed. Please wait for 10 minutes.")

    case _:
        print("Invalid coach type. Please choose from sleeper, ac, general, or luxury.")