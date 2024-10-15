can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001


def can_create_bits(user_permissions):
    if can_create_guild & user_permissions == 8:
        return True


def can_review_bits(user_permissions):
    if can_review_guild & user_permissions == 4:
        return True


def can_delete_bits(user_permissions):
    if can_delete_guild & user_permissions == 2:
        return True


def can_edit_bits(user_permissions):
    if can_edit_guild & user_permissions == 1:
        return True