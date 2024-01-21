#| We are interested in finding the longest (number of characters) absolute path to a file within our file system.
#| For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext",
#| and its length is 32 (not including the double quotes).
#| Given a string representing the file system in the above format,
#| return the length of the longest absolute path to a file in the abstracted file system.
#| If there is no file in the system, return 0.


#-----------------#
# Define Function #
#-----------------#

def path_length(input_string):
    #| Split the input into lines
    lines = input_string.split('\n')
    #| Initialise an empty stack to keep track of current path length
    stack = []
    #| Initialise the variable to store maximum length
    max_length = 0

    for line in lines:
        #| Calculate depth of the current line by counting the number of '\t' chacarters
        depth = line.count('\t')
        #| Extract the name of the file or directory by removing leading '\t' characters
        name = line.lstrip('\t')
        
        #| Pop elements from stack until the current depth is reached
        while len(stack) > depth:
            stack.pop()

        #| Calculate length including '/' separators
        current_length = (stack[-1] if stack else 0) + len(name)

        #| If it's a file, update the max_length
        if '.' in name:
            max_length = max(max_length, current_length)
        else:
            #| If it's a directory, add its length to the stack
            stack.append(current_length + 1)  # Adding 1 for the '/' separator

    return max_length

#------------------#
# Test Application #
#------------------#

file_system = "dir\n\tsubdir1\n\tsubdir2\n\t\tsubsubdir1\n\t\tsubsubdir2\n\t\t\tfile.ext"
result = path_length(file_system)
print(result)
