# Problem Statement
# Luke Skywalker has family and friends. Help him remind them who is who.
# Given a string with a name, return the relation of that person to Luke.
# Person       Relation
# Darth Vader  father
# Leia         sister
# Han          brother in law
# R2D2         droid
# Examples
# relation_to_luke("Darth Vader") -> "Luke, I am your father."
# relation_to_luke("Leia") -> "Luke, I am your sister."

def relation_to_luke(person):
    if person.lower() == 'darth vader':
        relation = "Luke, I am your father."
    elif person.lower() == 'leia':
        relation = "Luke, I am your sister."
    elif person.lower() == 'han':
        relation = "Luke, I am your brother in law."
    elif person.lower() == 'r2d2':
        relation = "Luke, I am your droid"
    else:
        relation = "Luke, I don't know you."
    return relation

x = input('Who are you? ')
print(relation_to_luke(x))