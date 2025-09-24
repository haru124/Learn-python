def generate_permutations(S, r):
    results = []

    def backtrack(path, remaining):
        # Base case: Desired length reached
        if len(path) == r:
            results.append(path[:])
            return

        for i in range(len(remaining)):
            # Choose element at index i
            path.append(remaining[i])
            # Recurse with remaining elements (excluding the chosen one)
            backtrack(path, remaining[:i] + remaining[i+1:])
            # Backtrack
            path.pop()

    backtrack([], S)
    return results


# Example usage
S = ['A', 'B', 'C']
r = 2
permutations_of_length_r = generate_permutations(S, r)

print(f"All permutations of length {r}:")
for perm in permutations_of_length_r:
    print(perm)