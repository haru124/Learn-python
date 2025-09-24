def subset_sum(S, target):
    call_counter = 0

    def backtrack(index, current_subset, current_sum):
        nonlocal call_counter
        call_counter += 1
        print(f"Call {call_counter}: index={index}, subset={current_subset}, sum={current_sum}")

        # ✅ Base case: if sum reached target
        if current_sum == target:
            print(f"🎯 Found subset: {current_subset}")
            results.append(current_subset[:])
            return

        # Stop exploring if out of bounds OR sum exceeds target
        if index == len(S) or current_sum > target:
            return

        # Choose S[index]
        current_subset.append(S[index])
        backtrack(index + 1, current_subset, current_sum + S[index])

        # Backtrack: don’t choose S[index]
        current_subset.pop()
        backtrack(index + 1, current_subset, current_sum)

    results = []
    backtrack(0, [], 0)
    return results


# Example
S = [2, 3, 7, 8, 10]
target = 10
print("\nSubsets summing to target:")
ans = subset_sum(S, target)
print("All valid subsets:", ans)
