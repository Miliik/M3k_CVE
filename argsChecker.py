import sys
from CreateMatchString import *
from functions import writehelp
from Cleaner import *

def checkarg():
    # for i in range(len(sys.argv)):
    #     if sys.argv[i][0] != "-":
    #         sys.argv[i] = inputcleaner(sys.argv[i])
    if len(sys.argv) == 4 or len(sys.argv) == 6 or len(sys.argv) > 7:
        return print("Error: Incorrect arguments provided. Please use the -help option to learn how to use the script.")
    else:
        if len(sys.argv) == 2 and sys.argv[1] == "-h" or sys.argv[1] == "--help" or len(sys.argv) == 1:
            return writehelp()

        if len(sys.argv) == 3:
            if sys.argv[1].startswith("-w"):
                if sys.argv[2].startswith("-"):
                    return "Error: Incorrect arguments provided. Please use the -help option to learn how to use the script."
                else:
                    return KeywordSearch(sys.argv[2])
            if sys.argv[1].startswith("-p"):
                if sys.argv[2].startswith("-"):
                    return "Error: Incorrect arguments provided. Please use the -help option to learn how to use the script."
                else:
                    return createMatchString(None, sys.argv[2], None)
            if sys.argv[1].startswith("-V"):
                if sys.argv[2].startswith("-"):
                    return "Error: Incorrect arguments provided. Please use the -help option to learn how to use the script."
                else:
                    return createMatchString(sys.argv[2], None, None)
            if sys.argv[1].startswith("-v"):
                return "-v (version) can only be used with -p (product)"
            else:
                return "Error: Incorrect arguments provided. Please use the -help option to learn how to use the script."

        if len(sys.argv) == 5:
            if sys.argv[1].startswith("-p") and sys.argv[3].startswith("-v"):
                if sys.argv[2].startswith("-") or sys.argv[4].startswith("-"):
                    return "Error: Incorrect arguments provided. Please use the -help option to learn how to use the script."
                else:
                    return createMatchString(None, sys.argv[2], sys.argv[4])
            if sys.argv[1].startswith("-p") and sys.argv[3].startswith("-V"):
                if sys.argv[2].startswith("-") or sys.argv[4].startswith("-"):
                    return "Error: Incorrect arguments provided. Please use the -help option to learn how to use the script."
                else:
                    return createMatchString(sys.argv[2], None, sys.argv[4])
            else:
                return "Error: Incorrect arguments provided. Please use the -help option to learn how to use the script."
        if len(sys.argv) == 7:
            if sys.argv[1].startswith("-p") and sys.argv[3].startswith("-v") and sys.argv[5].startswith("-V"):
                if sys.argv[2].startswith("-") or sys.argv[4].startswith("-") or sys.argv[6].startswith("-"):
                    return "Error: Incorrect arguments provided. Please use the -help option to learn how to use the script."
                else:
                    return createMatchString(sys.argv[6], sys.argv[2], sys.argv[4])
            if sys.argv[1].startswith("-p") and sys.argv[3].startswith("-V") and sys.argv[5].startswith("-v"):
                if sys.argv[2].startswith("-") or sys.argv[4].startswith("-") or sys.argv[6].startswith("-"):
                    return "Error: Incorrect arguments provided. Please use the -help option to learn how to use the script."
                else:
                    return createMatchString(sys.argv[2], sys.argv[4], sys.argv[6])
            else:
                return "Error: Incorrect arguments provided. Please use the -help option to learn how to use the script."
