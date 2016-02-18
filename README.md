#FileGrouper

CLI for sorting files from one folder into individual 
folders for files with similar names.

    Parameters\n
    ----------

    SOURCE : source directory with files needing to be grouped\n
        (must exist)

    TARGET : target directory where new folders will be place\n
        (must exist)

    PATTERN : regular expression pattern for grouping files\n
        (enclose this in quotation marks)


    ---------

    Example to group all files based on first 5 letters:\n

    $groupfiles ./junk_folder ./sorted_stuff '^[a-zA-Z]{5}'

    ---------

    Other examples of regular expression patterns that may be useful:

    '^' : (Caret) start your regular expression with this to match\n
        at start of string

    '.' : (Dot) any character

    '+' : (Plus) one or more repetitions of the preceeding expression

    '*' : (Star) 0 or more repetitions of the preceeding expression

    '?' : 0 or 1 repetitions of the preceeding expression

    {m} : Exactly m copies of the preceeding expression

    {m,n} : From m to n copies of the preceeding expression

    \d : digit
    
    Put together :

    ^/d{5}.+/d{5} : 5 digits, then 1 or more of any character,\n
        then 5 more digits.

Installation

clone repository, activate your virtualenvironment (optional), and execute:

$python setup.py install