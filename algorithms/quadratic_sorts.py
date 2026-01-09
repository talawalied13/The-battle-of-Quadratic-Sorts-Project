import random
import time

# Task A.1: The Challengers (Sorting Algorithms)

def bubble_sort(L):
    n = len(L)
    for i in range(n - 1):
        swapped = False # Flag to check if any swapping happened
        
        for j in range(0, n - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j] # Swap if they are in the wrong order
                swapped = True
                
        if not swapped:
            break

def insertion_sort(L):
    for i in range(1, len(L)):
        key = L[i]  # Current element to insert
        j = i - 1
        
        while j >= 0 and L[j] > key:
            L[j + 1] = L[j]
            j -= 1
        L[j + 1] = key


# Task A.2: The Duel (Performance Test)

def run_benchmark(N=2000):
    print(f"Running benchmark with N={N} elements...")
    
    # Create THREE DISTINCT SCENARIOS (not copies of each other)
    sorted_list = list(range(N)) # best case
    
    reversed_list = list(range(N, 0, -1)) # worst case
    
    random_list = [random.randint(0, 10000) for _ in range(N)] # average case
    
    results = []
    
    # Test 1: Sorted List
    print("\n1. Testing Sorted List (Best Case)...")
    
    # For Bubble Sort
    bubble_list = list(sorted_list)
    start = time.perf_counter()
    bubble_sort(bubble_list)
    bubble_time = time.perf_counter() - start
    
    # For Insertion Sort  
    insertion_list = list(sorted_list)
    start = time.perf_counter()
    insertion_sort(insertion_list)
    insertion_time = time.perf_counter() - start
    
    results.append(("Sorted (Best)", bubble_time, insertion_time))
    
    # Test 2: Reversed List
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

if __name__ == "__main__":
    N = 2000
    results = run_benchmark(N)
    print_results(results, N)