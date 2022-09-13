def main():
    # Create big main dicts
    big_dict = {}
    profiles = {}
    experts = {}
    assignment_dict = {}

    # Fill the profiles dict
    with open('Profiles.txt', encoding='latin-1') as file:
        file.readline()
        for line in file.readlines():
            fields = line.split('\t')  # split by tabs
            expert_id = fields[0].strip('\"')  # grab the ID as the key
            concept_name = fields[2].strip('\"')
            if expert_id not in profiles:  # if the expert isn't in the dict, add them. otherwise add to the back
                profiles.update({expert_id: [concept_name]})
            else:  # don't need rank or vocabulary, s don't include
                profiles[expert_id].append([fields[2].strip('\"')])
    file.close()
    #print_dict(profiles)

    # Fill the experts dict
    college_dict = {}
    with open('Experts.txt', encoding='latin-1') as file:
        file.readline()
        for line in file.readlines():
            fields = line.split('\t')
            expert_id = fields[0].strip('\"')
            full_name = fields[2].strip('\"') + " " + fields[1].strip('\"')  # Strip the double quotes from names
            # TODO: Dict structure must be: {Uni: {Subject: {Person: [concept list]}}}
            university = fields[5].strip('\"').split(',')[0]
            school_within_uni = fields[5].strip('\"').split(',')[1]
            try:
                subject_within_school = fields[5].strip('\"').split(',')[2] # Some data in the file is messed up
            except IndexError:
                subject_within_school = 'null'
            if university not in college_dict:
                #college_dict.update({university: [full_name, expert_id, fields[5].strip('\"')]})
                college_dict.update({university: {subject_within_school: {full_name: [profiles.get(expert_id, [concept_name])]}}})
            #else:
                #college_dict[university].append([full_name, expert_id, fields[5].strip('\"')])

            print_dict(college_dict)

            # TODO: See if this dict is even necessary anymore vs college_dict
            # if expert_id not in experts:
            # experts.update({expert_id: [full_name, fields[5].strip('\"')]})
            # else:
            # profiles[expert_id].append([full_name, fields[5].strip('\"\n')])

            # Separate the colleges and affiliations into
        file.close()

    big_dict.update(profiles)
    big_dict.update(college_dict)


    #print_dict(big_dict)

    # for k, v in experts.items():
    # print(k,v)
    # print_dict(college_dict)

    # Begin the menu stuff
    print('\t\tWelcome to the NC Scholar System\nWe currently include scholars from the following institutes:\n')
    for key, value in college_dict.items():
        print(key, end=', ')
    print('\nSelect an institute: ')
    input_college = input()
    while input_college not in college_dict:
        print('Invalid input, try again.')
        input_college = input()
    print(input_college + ' has scholars in the following areas/departments:\n')

    print('Select an area:')
    area_selected = input()
    # TODO: Make this loop for an incorrect answer with while loop

    print('Select a scholar:')


def print_dict(printable):
    for k, v in printable.items():
        print(k, v)


if __name__ == "__main__":
    main()
