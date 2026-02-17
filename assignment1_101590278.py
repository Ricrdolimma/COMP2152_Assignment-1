"""
Author: <Ricardo Lima>
Assignment: #1
"""

# Step b: Create 4 variables
gym_member = "Alex Alliton"          # string
preferred_weight_kg = 20.5           # float
highest_reps = 25                    # int
membership_active = True             # boolean


# Step c: Create a dictionary named workout_stats
# Dictionary mapping friend names to tuples of workout minutes (yoga, running, weightlifting)
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (25, 60, 30),
    "Taylor": (40, 35, 50)
}


# Step d: Calculate total workout minutes using a loop and add to dictionary
for name in list(workout_stats.keys()):
    total_minutes = sum(workout_stats[name])
    workout_stats[name + "_Total"] = total_minutes


# Step e: Create a 2D nested list called workout_list
# (rows = friends, columns = activities)
workout_list = []

for name in workout_stats:
    if "_Total" not in name:
        workout_list.append(list(workout_stats[name]))


print(workout_stats)
print(workout_list)


# Step f: Slice the workout_list
# Yoga and running for all friends
yoga_running = [row[:2] for row in workout_list]
print("Yoga and running minutes for all friends:")
print(yoga_running)

# Weightlifting for last two friends
weightlifting_last_two = [row[2] for row in workout_list[-2:]]
print("Weightlifting minutes for last two friends:")
print(weightlifting_last_two)


# Step g: Check if any friend's total >= 120
for name in workout_stats:
    if "_Total" in name and workout_stats[name] >= 120:
        friend_name = name.replace("_Total", "")
        print(f"Great job staying active, {friend_name}!")


# Step h: User input to look up a friend
user_name = input("Enter a friend's name: ")

if user_name in workout_stats:
    print(f"{user_name}'s workout minutes (Yoga, Running, Weightlifting): {workout_stats[user_name]}")
    print(f"{user_name}'s total workout minutes: {workout_stats[user_name + '_Total']}")
else:
    print(f"Friend {user_name} not found in the records.")


# Step i: Friend with highest and lowest total workout minutes
totals = {
    name.replace("_Total", ""): workout_stats[name]
    for name in workout_stats if "_Total" in name
}

highest_friend = max(totals, key=totals.get)
lowest_friend = min(totals, key=totals.get)

print(f"Highest total workout minutes: {highest_friend} with {totals[highest_friend]} minutes.")
print(f"Lowest total workout minutes: {lowest_friend} with {totals[lowest_friend]} minutes.")