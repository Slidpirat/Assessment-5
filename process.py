log_file = open("um-server-01.txt") # log_files is saved as a variable and used to open um-server-01.txt


def sales_reports(log_file): # function with the name sales_reports with the argument log_file

    for line in log_file: # for in loop that iterates through the log_file, saved to the variable "line"

        line = line.rstrip() # line.rstrip will return a copy of the string by removing trailing characters on in the "line" variable

        day = line[0:3] # day variable will look at the log_file and goes what whatever is specificed in the index, in this case it'll start at 0 at the index and goes 3 over

        if day == "Mon": # If day equals to Mon, the console log will print the line, which will show the log_file since its saved to "line"

            print(line) # print the line or a stored variable 


sales_reports(log_file) # returns the code from the created function