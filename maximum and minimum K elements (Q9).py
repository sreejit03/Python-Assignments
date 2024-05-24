import heapq

def find_max_min_k_elements(lst, k):
    if k <= 0 or k > len(lst):
        raise ValueError("k must be between 1 and the length of the list")

    # Find the k largest elements
    max_k_elements = heapq.nlargest(k, lst)
    
    # Find the k smallest elements
    min_k_elements = heapq.nsmallest(k, lst)
    
    return max_k_elements, min_k_elements

# Example usage
if __name__ == "__main__":
    lst = [12, 3, 5, 7, 19, 0, -4, 15, 8]
    k = 3
    max_k, min_k = find_max_min_k_elements(lst, k)
    print(f"The {k} largest elements are: {max_k}")
    print(f"The {k} smallest elements are: {min_k}")