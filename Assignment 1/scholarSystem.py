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
    with open('testline.txt', encoding='latin-1') as file:
        file.readline()
        for line in file.readlines():
            fields = line.split('\t')
            expert_id = fields[0].strip('\"')
            full_name = fields[2].strip('\"') + " " + fields[1].strip('\"')  # Strip the double quotes from names
            # TODO: Dict structure must be: {Uni: {Subject: {Person: [concept list]}}}
            university = fields[5].strip('\"').lstrip().split(',')[0]  # Grab the university name
            school_within_uni = fields[5].strip('\"').split(', ')[1]  # Grab the school within the uni
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
            # TODO: Append this list to employees
        file.close()

    print_dict(college_dict)
    # Begin the menu stuff
    print('\t\tWelcome to the NC Scholar System\nWe currently include scholars from the following institutes:\n')
    for key, value in college_dict.items():
        print(key, end=', ')
    print('\nSelect an institute: ')
    input_college = input().upper()
    while input_college not in college_dict:
        print('Invalid input, try again.')
        input_college = input().upper()
    print(input_college + ' has scholars in the following areas/departments:')
    for key, value in college_dict[university].items(): # Print out all the departments of this university
        print(key)

    print('\nSelect an area (case sensitive):')
    area_selected = input()
    while area_selected not in college_dict[university]: # Input validation for subject selection
        print('Invalid input. Please try again.')
        area_selected = input()
    # TODO: Make this loop for an incorrect answer with while loop
    for scholar in college_dict[university][area_selected]:
        print(scholar)
    print('\nSelect a scholar:') # User chooses scholar to look at concepts of


def print_dict(printable):
    for k, v in printable.items():
        print(k, v)


if __name__ == "__main__":
    main()
