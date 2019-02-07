'''

define the function animal count with two parameters

1. animal_dict: A dictionary of animals with its count

2. animal: Animal to be added to the dictionary

If the element already exists in the dictionary, then just increment its count

If the element is not present in the dictionary, then add it to the dictionary and initialize its count to 1

'''

def animal_count(animal_dict, animal):

    # check if animal is present in dictionary

    if animal in animal_dict:

        # if animal is present, then just increment the count

        animal_dict[animal]=animal_dict[animal]+1

    else:

        # if animal is not present, then insert it to the dictionary

        animal_dict[animal]=1

# Initialize the animal dictionary

animal_dict={}

# Add the animals to the dictionary

animal_count(animal_dict,"dog")

animal_count(animal_dict,"cat")

animal_count(animal_dict,"rabbit")

animal_count(animal_dict,"dog")

animal_count(animal_dict,"rabbit")

animal_count(animal_dict,"cat")

# To get a particular animal's count

print("Number of dogs are: ",animal_dict['dog'])

# Get all animals count

print('The complete dictionary is: ', animal_dict)
