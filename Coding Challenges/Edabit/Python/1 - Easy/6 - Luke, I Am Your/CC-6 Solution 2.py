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
    dict = {
        'leia' : 'sister',
        'darth vader' : 'father',
        'han' : 'brother in law',
        'r2d2' : 'droid' 
    }
    return 'Luke, I am your {}.'.format(dict[person.lower()])

x = input('Who are you? ')
print(relation_to_luke(x))