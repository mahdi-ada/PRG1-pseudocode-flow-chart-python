print("=== Netflix Binge Calculator ===")
    
# Input
series_name = input("Enter the series name: ")
episodes_per_season = int(input("Enter episodes per season: "))
number_of_seasons = int(input("Enter number of seasons: "))
episode_length_minutes = int(input("Enter episode length in minutes: "))
# Calculations
total_episodes = episodes_per_season * number_of_seasons
total_minutes = total_episodes * episode_length_minutes
total_hours = total_minutes / 60
total_days = total_hours / 24
if total_days>7:
    print("Warning")
days_week=total_episodes/7

# Output
print(f"\nTo binge-watch {series_name} you need:")
print(f"{total_hours:.1f} hours")
print(f"That's {total_days:.1f} full days of your life!")
print(days_week,"Amount of ep per day"

print(f"Hellow" {\}