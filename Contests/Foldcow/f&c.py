#dropbox_f&c

contents = []
#reading input from stdin over multiple lines and waiting for EOFerror
while True:
    try:
        line = raw_input('')
    except EOFError: #Ctrl+D
        break
    contents.append(line)

#storing the inputs into variables that can be processed
number_cows = contents[0]
number_confidential_files = int(contents[1].split(" ")[1])
number_shared_files = int(contents[1].split(" ")[0])
shared_access_list = {}
confidential_access_list = {}
total_cows_list = []
for i in xrange(number_shared_files):
    folder_id = contents[2+i].split(" ")[0]
    shared_access_list[folder_id] = contents[2+i].split(" ")[2:]
    total_cows_list.extend(contents[2+i].split(" ")[2:])
    #getting counts of all cows
    
for i in xrange(number_confidential_files):
    folder_id = contents[2+number_shared_files+i].split(" ")[0]
    confidential_access_list[folder_id] = contents[2+number_shared_files+i].split(" ")[2:]
    total_cows_list.extend(contents[2+number_shared_files+i].split(" ")[2:])
    #getting counts of all cows
    
number_tree_links = int(contents[2+number_shared_files+number_confidential_files])

parents = []
children = []
for i in xrange(number_tree_links):
    #now reading the links that form the tree structure
    parent, child = contents[2+number_shared_files+number_confidential_files+1+i].split(" ")
    parents.append(parent)
    children.append(child)
    #creating a list of all parents and children
    if shared_access_list:
        if child in shared_access_list.keys() and shared_access_list[parent] and not set(shared_access_list[parent]).issubset(shared_access_list[child]):
            shared_access_list[child].extend(shared_access_list[parent])
            #extending the shared foldrs access list to include cows 
            #that have access to parents of the shared folders
        
if shared_access_list:
    access_list = dict(shared_access_list, **confidential_access_list)
#print access_list
#combine the dictionaries of shared and confidential folders into one

leaves_list = list(set(children) - set(parents))
#find the list of leaves by subtracting the set of all nodes that are
#parents from the set of all children 

uncool_cows = []
#for every leaf node, find the difference between the set of all cows
#and the set of cows that can access that leaf. They are all uncool
for i in leaves_list:
    uncool_cows.extend(list(set(total_cows_list) - set(access_list[i])))
    
#print the final set of uncool cows
for i in sorted(set(uncool_cows)):
    print i,










