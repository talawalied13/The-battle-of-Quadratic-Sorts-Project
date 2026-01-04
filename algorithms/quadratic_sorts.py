import random
import time

#ok, guys im basically just going to comment every step 
#so that you dont need to search up anything for the presentation
#But I think for math you'll still need to look up some stuff

# P.S. I'll delete the redundant comments once we're done with the project if needed

# Task A.1: The Challengers (Sorting Algorithms)

def bubble_sort(L): # The parameter is the list that going to be sorted
    n = len(L) # Get the length of the list
    for i in range(n - 1): # Traverse through all elements in the list
        swapped = False # Flag to check if any swapping happened
        
        for j in range(0, n - i - 1): # Last i elements are already sorted at the point we reach here
            if L[j] > L[j + 1]: # Compare adjacent elements
                L[j], L[j + 1] = L[j + 1], L[j] # Swap if they are in the wrong order
                swapped = True # Set the flag to True if a swap occurred
                
        if not swapped:
            break # If no two elements were swapped in the inner loop, the list is sorted

def insertion_sort(L):
    # Start from the second element (index 1)
    for i in range(1, len(L)):
        key = L[i]  # Current element to insert
        j = i - 1
        
        # Move elements of L[0..i-1] that are > key
        # to one position ahead of their current position
        while j >= 0 and L[j] > key: # Basically just moving the unchecked element back until it reaches its correct position if it is not there initially
            L[j + 1] = L[j]
            j -= 1
        L[j + 1] = key # Place the key in its correct position


# Task A.2: The Duel (Performance Test)

def run_benchmark(N=2000):
    print(f"Running benchmark with N={N} elements...")
    
    # Create THREE DISTINCT SCENARIOS (not copies of each other)
    # 1. Sorted List (Best Case)
    sorted_list = list(range(N))
    
    # 2. Reversed List (Worst Case) 
    reversed_list = list(range(N, 0, -1))
    
    # 3. Random List (Average Case)
    random_list = [random.randint(0, 10000) for _ in range(N)]
    
    results = [] # this will store the results of each test case
    
    # Test 1: Sorted List
    print("\n1. Testing Sorted List (Best Case)...")
    
    # For Bubble Sort
    bubble_list = list(sorted_list)  # Copy the scenario list
    start = time.perf_counter()
    bubble_sort(bubble_list)
    bubble_time = time.perf_counter() - start # now we have the time taken for bubble sort - best case
    
    # For Insertion Sort  
    insertion_list = list(sorted_list)  # Another copy of the same scenario list
    start = time.perf_counter()
    insertion_sort(insertion_list)
    insertion_time = time.perf_counter() - start # and the same for insertion sort
    
    # we add every both algorithms' results for the scenario to the results list
    results.append(("Sorted (Best)", bubble_time, insertion_time))
    
    # Test 2: Reversed List
    # We do the same exact steps except for the reversed list scenario 
    print("2. Testing Reversed List (Worst Case)...")
    
    bubble_list = list(reversed_list)
    start = time.perf_counter()
    bubble_sort(bubble_list)
    bubble_time = time.perf_counter() - start
    
    insertion_list = list(reversed_list)
    start = time.perf_counter()
    insertion_sort(insertion_list)
    insertion_time = time.perf_counter() - start
    
    results.append(("Reversed (Worst)", bubble_time, insertion_time))
    
    # Test 3: Random List
    # And for the random list too
    print("3. Testing Random List (Average Case)...")
    
    bubble_list = list(random_list)
    start = time.perf_counter()
    bubble_sort(bubble_list)
    bubble_time = time.perf_counter() - start
    
    insertion_list = list(random_list)
    start = time.perf_counter()
    insertion_sort(insertion_list)
    insertion_time = time.perf_counter() - start
    
    results.append(("Random", bubble_time, insertion_time))
    
    # now we have both algorithms' results for all three scenarios
    return results

# Task A.3: Analysis of Results

def print_results(results, N=2000):
    print("\n" + "="*65)
    print(f"BENCHMARK RESULTS (N={N})")
    print("="*65)
    print(f"{'Scenario':<20} {'Bubble Sort (s)':<20} {'Insertion Sort (s)':<20} {'Winner':<15}")
    print("-"*75)
    
    for scenario, bubble_time, insertion_time in results:
        bubble_str = f"{bubble_time:.6f}"
        insertion_str = f"{insertion_time:.6f}"
        
        if abs(bubble_time - insertion_time) < 0.00001:
            winner = "Tie"
        elif bubble_time < insertion_time:
            winner = "Bubble"
        else:
            winner = "Insertion"
        
        print(f"{scenario:<20} {bubble_str:<20} {insertion_str:<20} {winner:<15}")
    print("="*65)

# Main execution
# I have explicitly separated the main execution and written it below
# so that everything is in the same 
if __name__ == "__main__":
    N = 2000
    results = run_benchmark(N)
    print_results(results, N)