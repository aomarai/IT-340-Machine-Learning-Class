def main():
    # Create big main dicts
    big_dict = {}
    profiles = {}
    experts = {}

    # Fill the profiles dict
    with open('Profiles.txt', encoding='latin-1') as file:
        file.readline()
        for line in file.readlines():
            fields = line.split('\t')  # split by tabs
            expert_id = fields[0].strip('\"') # grab the ID as the key
            if expert_id not in profiles:  # if the expert isn't in the dict, add them. otherwise add to the back
                profiles.update({expert_id: [fields[1].strip('\"'), fields[2].strip('\"'),
                                             fields[3].strip('\"'), fields[4].strip('\"')]})
            else:
                profiles[expert_id].append([fields[1].strip('\"'), fields[2].strip('\"'),
                                            fields[3].strip('\"'), fields[4].strip('\"')])
    file.close()

    # Fill the experts dict
    with open('Experts.txt', encoding='latin-1') as file:
        file.readline()
        for line in file.readlines():
            fields = line.split('\t')
            expert_id = fields[0].strip('\"')
            full_name = fields[2].strip('\"') + " " + fields[1].strip('\"') # Strip the double quotes from names
            # TODO: create a list of the colleges from the beginning of fields[5]
            if expert_id not in experts:
                experts.update({expert_id: [full_name, fields[3].strip('\"'), fields[4].strip('\"'),
                                            fields[5].strip('\"'), fields[6].strip('\"\n')]})
            else:
                profiles[expert_id].append([full_name, fields[3].strip('\"'), fields[4].strip('\"'),
                                            fields[5].strip('\"'), fields[6].strip('\"\n')])
    file.close()


    big_dict.update(profiles)
    big_dict.update(experts)

    for k, v in experts.items():
        print(k,v)

    # Begin the menu stuff
    print('\t\tWelcome to the NC Scholar System\nWe currently include scholars from the following institutes:\n')

def printDict(printable):
    for k, v in printable.items():
        print(k, v)


if __name__ == "__main__":
    main()
