feast = ['lambs', 'sloths', 'orangutans',
             'breakfast cereals', 'fruit bats']

comprehension = [delicacy.capitalize() for delicacy in feast]

comprehension[1]


feast = ['spam', 'sloths', 'orangutans', 'breakfast cereals',
            'fruit bats']

comp = [delicacy for delicacy in feast if len(delicacy) > 6]

len(feast)

len(comp)

list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]

comprehension = [ skit * number for number, skit in list_of_tuples ]

len(comprehension[2])


eggs = ['poached egg', 'fried egg']

meats = ['lite spam', 'ham spam', 'fried spam']

comprehension = \
[ '{0} and {1}'.format(egg, meat) for egg in eggs for meat in meats]


comprehension = { c for c in 'aabbbcccc'}

dict_of_weapons = {'first': 'fear',
                       'second': 'surprise',
                       'third':'ruthless efficiency',
                       'forth':'fanatical devotion',
                       'fifth': None}

dict_comprehension = \
{ k.upper(): weapon for k, weapon in dict_of_weapons.items() if weapon}