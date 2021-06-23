def length_cycle(n, a, b, c):
    longest_len = 0
    portion_of_prev_cycle_len = 0  # This length when added to abs(a[i]-b[i]) will make a cycle
    for i in range(1, n):  # We skip the first chain.
        curr_chain_length = c[i] - 1
        upper_node = min(a[i], b[i])
        lower_node = max(a[i], b[i])
        portion_of_prev_chain_len = lower_node - upper_node
        cycle_formed = curr_chain_length + portion_of_prev_chain_len + 2

        if a[i] != b[i]:
            cycle_formed_with_prev_part = portion_of_prev_cycle_len - portion_of_prev_chain_len + curr_chain_length + 2
            cycle_formed = max(cycle_formed, cycle_formed_with_prev_part)
        portion_of_prev_cycle_len = cycle_formed
        longest_len = max(longest_len, cycle_formed)
    return longest_len


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        c = list(map(int, input().split()))
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        print(length_cycle(n, a, b, c))
