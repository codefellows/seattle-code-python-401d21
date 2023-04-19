"""
Warm-Up Exercise
Find the age range.

Feature Tasks
Given a Binary Tree filled with Person objects, where each Person has an age attribute, determine the age range.
"""


def get_age_range(tree):

    def walk(root, youngest=0, oldest=0):

        if not root:
            return 0
        if root.value.age < youngest: # May need to come back to 0
            youngest = root.value.age
        elif root.value.age > oldest:
            oldest = root.value.age

        # call my resucursion
        youngest, oldest = walk(root.left, youngest, oldest)
        youngest, oldest = walk(root.right, youngest, oldest)

        return youngest, oldest

    first_person = tree.root.value
    youngest, oldest = walk(tree.root, first_person.age, first_person.age)

    return oldest - youngest

        #         50
        #
        #     60      18
        #
        # 21    34   34   34
        #
    # check if the current root value < or > youngest and oldets

  return age_range


