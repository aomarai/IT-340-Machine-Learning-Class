def main():
    # Create dict
    profiles = {}

    # Fill the profiles dict
    with open('Profiles.txt', encoding='latin-1') as file:
        file.readline()
        for line in file.readlines():
            fields = line.split('\t')  # split by tabs
            expert_id = fields[0].strip('\"')  # grab the ID as the key
            concept_name = fields[2].strip('\"')
            if expert_id not in profiles:  # if the expert isn't in the dict, add them. otherwise add to the back
                profiles.update({expert_id: [concept_name]})
            else:  # don't need rank or vocabulary, so don't include
                profiles[expert_id].append([fields[2].strip('\"')])
    file.close()

    # Fill the experts dict
    college_dict = {}
    with open('Experts.txt', encoding='latin-1') as file:
        file.readline()
        for line in file.readlines():
            fields = line.split('\t')
            expert_id = fields[0].strip('\"')
            full_name = fields[2].strip('\"') + " " + fields[1].strip('\"')  # Strip the double quotes from names
            # Dict structure must be: {Uni: {Subject: {Person: [concept list]}}}
            university = fields[5].strip('\"').lstrip().split(',')[0]  # Grab the university name
            try:  # Grab the subject from inside the school
                subject_within_school = fields[5].strip('\" ').split(', ', 2)[2]  # Some data in the file is messed up
            except IndexError:
                subject_within_school = 'RTI Fellows Program'
            if university not in college_dict:
                college_dict[university] = {}
            if subject_within_school not in college_dict[university]:
                college_dict[university][subject_within_school] = {}
            if full_name not in college_dict[university][subject_within_school]:
                concept_list = [profiles.get(expert_id), [concept_name]]
                college_dict[university][subject_within_school][full_name] = []
                college_dict[university][subject_within_school][full_name].append(concept_list)
        file.close()

    # Begin the menu stuff
    loop = True
    print('\t\tWelcome to the NC Scholar System\nWe currently include scholars from the following institutes:\n')
    while loop: # Haha pun am I funny yet
        for key, value in college_dict.items():
            print(key, end=', ')
        print('\nSelect an institute: ')
        input_college = input().upper() # Take the user input for the university
        while input_college not in college_dict: # Check if it's inside the dictionary
            print('Invalid input, try again.')
            input_college = input().upper()
        print(input_college + ' has scholars in the following areas/departments:')
        for key, value in college_dict[university].items():  # Print out all the departments of this university
            print(key)

        print('\nSelect an area (case sensitive):')
        area_selected = input()
        while area_selected not in college_dict[university]:  # Input validation for subject selection
            print('Invalid input. Please try again.')
            area_selected = input()
        for scholar in college_dict[university][area_selected]:
            print(scholar)
        print('\nSelect a scholar (case sensitive):')  # User chooses scholar to look at concepts of
        chosen_scholar = input()
        while chosen_scholar not in college_dict[university][area_selected]: # Input validation
            print('Invalid input. Please try again.')
            chosen_scholar = input()
        for concept in college_dict[university][area_selected][scholar]:
            if not college_dict[university][area_selected][scholar]:
                print('Sorry, there is no information about ' + chosen_scholar) # If no data in the dict on concepts, error message
            else:
                print(*concept, sep=', ')
        print('Press c to continue or press anything else to quit: ')
        if input() != 'c':
            print('Thanks for using the system!')
            loop = False



def print_dict(printable):
    """Iteratively prints the input dictionary by key-value pair."""
    for k, v in printable.items():
        print(k, v)


if __name__ == "__main__":
    main()
