def main():
    # Read in the experts
    expertsDict = {}
    with open("Experts.txt","r") as f:
        lines = f.readlines()

    # Grab all the fields to fill the experts dict
    for s in lines:
        fields = s.split("\t")
        expert_id = fields[0]
        last_name = fields[1]
        first_name = fields[2]
        h_index = fields[3]
        client_id = fields[4]
        affiliation = fields[5]
        publication_num = fields[6]

        expertsDict[expert_id] = {"Last Name" : last_name, "First Name" : first_name,
                                  "H Index" : h_index, "Client ID" : client_id,
                                  "Affiliation" : [a.strip() for a in affiliation.split(",")],
                                  "Number of Publications" : publication_num.strip()}

    #for record in expertsDict.items():
        #print(record)

    # Open the profiles file and create dict for it
    profiles = {}
    with open("Profiles.txt") as f:
        lines = f.readlines()

    # Have to create yet another dictionary for all the concepts for each expert
    for s in lines:
        fields = s.split("\t")
        expert_id = fields[0]
        concept_id = fields[1]
        concept_name = fields[2]
        rank = fields[3]
        vocabulary = fields[4]

        profiles[expert_id] = {"Concept ID" : concept_id, "Concept Name" : concept_name,
                               "Rank" : rank, "Vocabulary" : vocabulary.strip()}

    for record in profiles.items():
        print(record)
    #print("\t\tWelcome to the NC Scholar System\nWe currently include scholars from the following institutes:\n")



if __name__ == "__main__":
    main()