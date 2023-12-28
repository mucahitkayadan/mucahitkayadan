# update_counter.py
import re

duolingo_streak = None

try:
    with open("README.md", "r", encoding="utf-8") as readme_file:
        readme_content = readme_file.read()

    match = re.search(r'My_Current_Duolingo_Streak-(\d+)-brightgreen', readme_content)
    if match:
        duolingo_streak = int(match.group(1))
    else:
        print("Could not find the Duolingo streak in README.md")

except FileNotFoundError:
    print("README.md file not found")
except PermissionError:
    print("Permission denied to access README.md")
except re.error:
    print("Error occurred while using regular expression")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")

if duolingo_streak is None:
    updated_duolingo_streak = 0
else:
    updated_duolingo_streak = duolingo_streak + 1

# Replace the placeholder with the new counter value
updated_readme = readme_content.replace(f"My_Current_Duolingo_Streak-{duolingo_streak}-brightgreen",
                                        f"My_Current_Duolingo_Streak-{updated_duolingo_streak}-brightgreen")

# Write the updated README
with open("README.md", "w", encoding="utf-8") as readme_file:
    readme_file.write(updated_readme)

# print(f"Counter updated to {new_count} days.")
