"""
 Author: [Your First and Last Name]
 Assignment: #1 python
"""
gym_member = "Alex Alliton" # str
preferred_weight_kg = 20.5 # float
highest_reps = 25 # int
membership_active = True # bool

# Dictionary with friend names (keys) and workout minutes as tuples (values)
workout_stats = {
    "Alex": (30, 60, 75),
    "Jamie": (25,50,15), 
    "Taylor": (40,30,15)
}
for friend,minutes in list(workout_stats.items()):
    total=sum(minutes)
    workout_stats[friend+"_Total"]=total
    
print(workout_stats)

# 2D list (nested list) containing workout minutes for each friend
workout_list= []
for friend,minutes in list(workout_stats.items()):
    if not friend.endswith("_Total"):
        workout_list.append(list(minutes))
print(workout_list)

#f.	Slice the workout_list to:
yoga_and_running = []
for friend in workout_list:
    yoga_and_running.append(friend[:2]) 
print("Yoga and running minutes for all friends:")
print(yoga_and_running)

weightlifting_last_two = []
for friend in workout_list[-2:]:
    weightlifting_last_two.append(friend[2])

print("Weightlifting minutes for last two friends:")
print(weightlifting_last_two)

# Check if any friend's total workout minutes >= 120
for friend, value in workout_stats.items():
    if friend.endswith("_Total") and value >= 120:
        friend_name = friend.replace("_Total", "")
        print(f"Great job staying active, {friend_name}!")    

#h.	Add a feature to allow the user to input a friend’s name. Check if the name exists in the dictionary:
# Get user input for friend's name
user_input = input("Enter a friend's name: ")
if user_input in workout_stats:

    minutes = workout_stats[user_input]
    total = workout_stats[user_input + "_Total"]
    
    print(f"\n{user_input}'s workout minutes:")
    print(f"  Yoga: {minutes[0]} minutes")
    print(f"  Running: {minutes[1]} minutes")
    print(f"  Weightlifting: {minutes[2]} minutes")
    print(f"  Total: {total} minutes")
else:
    print(f"Friend {user_input} not found in the records.")

# Find friend with highest and lowest total workout minutes
highest_total = 0
lowest_total = float('inf')  # Start with infinity
highest_friend = ""
lowest_friend = ""
for friend, value in workout_stats.items():
    if friend.endswith("_Total"):
        friend_name=friend.replace("_Total", "")


        if value>highest_total:
            highest_total=value
            highest_friend=friend_name
            
        if value<lowest_total:
            lowest_total=value
            lowest_friend= friend_name
print("\n" + "="*50)
print("WORKOUT SUMMARY")
print("="*50)
print(f"Friend with highest total:  {highest_friend}({highest_total} minutes)")
print(f"Friend with lowest total: {lowest_friend} ({lowest_total} minutes)")
print("="*50)