"""
[REDACTED]
[REDACTED]
25/11/2023
CSPC31
Greedy Algorithm - Activity Selection Problem
"""

def choose_activities(activities):
    sorted_activities = sorted(activities, key=lambda x: x[2])
    selected_activities = [sorted_activities[0]]

    for i in range(1, len(sorted_activities)):
        current_activity = sorted_activities[i]
        last_selected_activity = selected_activities[-1]

        if current_activity[1] >= last_selected_activity[2]:
            selected_activities.append(current_activity)

    return selected_activities

activities_list =\
[
    ("a1", 1, 4),
    ("a2", 2, 9),
    ("a3", 7, 15),
    ("a4", 5, 8),
    ("a5", 10, 18),
    ("a6", 16, 17),
    ("a7", 21, 27),
    ("a8", 23, 30),
]

selected_activities = choose_activities(activities_list)

for activity in selected_activities:
    print(f"Activity {activity[0]}: Start Time - {activity[1]}, End Time - {activity[2]}", end=' ')
