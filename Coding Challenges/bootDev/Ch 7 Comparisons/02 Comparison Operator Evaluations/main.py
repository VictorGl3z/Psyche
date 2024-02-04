def compare_heights(elon_height, sara_height, jill_height, bob_height):
    is_bob_elon_same_height = elon_height == bob_height
    is_sara_elon_same_height = elon_height == sara_height
    is_jill_sara_same_height = jill_height == sara_height
    return is_bob_elon_same_height, is_sara_elon_same_height, is_jill_sara_same_height
