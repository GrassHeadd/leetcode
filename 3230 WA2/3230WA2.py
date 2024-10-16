def distribute(available_sizes, preferences):
    size_mapping = {
        "XXXL": 0,
        "XXL": 1,
        "XL": 2,
        "L": 3,
        "M": 4,
        "S": 5,
        "XS": 6
    }
    
    preferences_freq = [0] * 7  # One slot for each size from XXXL to XS
    for size in preferences:
        preferences_freq[size_mapping[size]] += 1
    
    # Test case 1: Exact match for all sizes
    exact = True
    for i in range(7):
        if preferences_freq[i] > available_sizes[i]:
            exact = False
            break
    if exact:
        print("ALL IS WELL")
        return 0
    
    # Test case 2: +/-1 size match
    almost = True
    for i in range(7):
        # Try to match sizes within +/-1 range
        for j in range(max(0, i - 1), min(7, i + 2)):  # Stay within bounds
            subtract = min(preferences_freq[i], available_sizes[j])
            preferences_freq[i] -= subtract
            available_sizes[j] -= subtract
        
        # If there's still unfulfilled preference, mark as not almost acceptable
        if preferences_freq[i] > 0:
            almost = False
            break
    
    if almost:
        print("still acceptable")
    else:
        print("argh... :(")

    return 0

# Read the input from the file
with open('sampleinput.txt', 'r') as file:
    lines = file.readlines()

# Parse the input into test cases
i = 1  # Start at 1 since first line is the number of test cases
while i < len(lines):
    available_sizes = list(map(int, lines[i].strip().split()))  # Convert available sizes to list of integers
    preferences = lines[i + 2].strip().split()  # Read the preferences (space-separated)
    distribute(available_sizes, preferences)  # Call the function with the current test case
    i += 4  # Move to the next test case (skip 3 lines + 1 for the next case)
