import sys

# Commit: Log Analysis Function
def analyze_log(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        cat_visits = 0
        intruder_doused = 0
        total_time_in_house = 0
        longest_visit = 0
        shortest_visit = float('inf')

        for line in lines:
            if line.strip() == 'END':
                break

            parts = line.strip().split(',')
            cat_name, entry_time, exit_time = parts

            entry_time = int(entry_time)
            exit_time = int(exit_time)

            if cat_name == 'OURS':
                cat_visits += 1
                total_time_in_house += exit_time - entry_time

                visit_duration = exit_time - entry_time
                longest_visit = max(longest_visit, visit_duration)
                shortest_visit = min(shortest_visit, visit_duration)

            elif cat_name == 'THEIRS':
                intruder_doused += 1

        if cat_visits == 0:
            avg_visit_length = 0
        else:
            avg_visit_length = total_time_in_house // cat_visits

        # Commit: Print Analysis Results
        print("Log File Analysis")
        print("==================")
        print(f"Cat Visits: {cat_visits}")
        print(f"Other Cats: {intruder_doused}")
        print(f"Total Time in House: {total_time_in_house // 60} Hours, {total_time_in_house % 60} Minutes")
        print(f"Average Visit Length: {avg_visit_length // 60} Minutes, {avg_visit_length % 60} Minutes")
        print(f"Longest Visit: {longest_visit // 60} Minutes, {longest_visit % 60} Minutes")
        print(f"Shortest Visit: {shortest_visit // 60} Minutes, {shortest_visit % 60} Minutes")

    except FileNotFoundError:
        # Handle File Not Found Error
        print(f'Cannot open "{file_path}"!')

# Command Line Argument Check
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Missing command line argument!")
    else:
        # Extract File Path from Command Line Argument
        file_path = sys.argv[1]
        # Perform Log Analysis
        analyze_log(file_path)