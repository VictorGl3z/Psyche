def body_parts(num_heads, num_arms, num_fingers):
    binary_heads = int(num_heads, 2)
    binary_arms = int(num_arms, 2)
    binary_fingers = int(num_fingers, 2)
    return binary_heads, binary_arms, binary_fingers
