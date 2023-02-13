import sys
from CreateMatchString import *
from functions import writehelp
from Cleaner import *
import argparse


#a function that parse the args , if only -w is used then it will call the KeywordSearch function with the next arg , if -p/-v/-V is used in any mix (except -v alone) then it will call the MatchstringSearch function
def checkarg():
    parser = argparse.ArgumentParser(description="Search for CVEs in the NVD database")
    parser.add_argument("-w", "--keyword", help="USE ALONE ONLY search for a keyword (use \" \" for multiple words)")
    parser.add_argument("-p", "--product", help="search for a product")
    parser.add_argument("-v", "--version", help="search for a version")
    parser.add_argument("-V", "--vendor", help="search for a vendor")
    #modify the usage message
    args = parser.parse_args()
    if args.keyword is not None:
        return KeywordSearch(args.keyword)
    elif args.product is not None:
        print("product")
        if args.version is not None:
            return MatchstringSearch(createMatchString(args.product, args.version, args.vendor))
        elif args.vendor is not None:
            return MatchstringSearch(createMatchString(args.product, None, args.vendor))
        else:
            return MatchstringSearch(createMatchString(args.product, None, None))
    elif args.vendor is not None:
        print("vendor")
        if args.product is not None:
            print("product")
            return MatchstringSearch(createMatchString(args.product, None, args.vendor))
        else:
            print("no product")
            return MatchstringSearch(createMatchString(None, None, args.vendor))
    else:
        writehelp()
        sys.exit(0)










# def checkarg():
#     # for i in range(len(sys.argv)):
#     #     if sys.argv[i][0] != "-":
#     #         sys.argv[i] = inputcleaner(sys.argv[i])
#     if len(sys.argv) == 4 or len(sys.argv) == 6 or len(sys.argv) > 7:
#         return print("Error: Incorrect arguments provided. Please use the -help option to learn how to use the script.")
#     else:
#         if len(sys.argv) == 2 and sys.argv[1] == "-h" or sys.argv[1] == "--help" or len(sys.argv) == 1:
#             return writehelp()
#
#         if len(sys.argv) == 3:
#             if sys.argv[1].startswith("-w"):
#                 if sys.argv[2].startswith("-"):
#                     return "Error: Incorrect arguments provided. Please use the -help option to learn how to use the script."
#                 else:
#                     return KeywordSearch(sys.argv[2])
#             if sys.argv[1].startswith("-p"):
#                 if sys.argv[2].startswith("-"):
#                     return "Error: Incorrect arguments provided. Please use the -help option to learn how to use the script."
#                 else:
#                     return createMatchString(None, sys.argv[2], None)
#             if sys.argv[1].startswith("-V"):
#                 if sys.argv[2].startswith("-"):
#                     return "Error: Incorrect arguments provided. Please use the -help option to learn how to use the script."
#                 else:
#                     return createMatchString(sys.argv[2], None, None)
#             if sys.argv[1].startswith("-v"):
#                 return "-v (version) can only be used with -p (product)"
#             else:
#                 return "Error: Incorrect arguments provided. Please use the -help option to learn how to use the script."
#
#         if len(sys.argv) == 5:
#             if sys.argv[1].startswith("-p") and sys.argv[3].startswith("-v"):
#                 if sys.argv[2].startswith("-") or sys.argv[4].startswith("-"):
#                     return "Error: Incorrect arguments provided. Please use the -help option to learn how to use the script."
#                 else:
#                     return createMatchString(None, sys.argv[2], sys.argv[4])
#             if sys.argv[1].startswith("-p") and sys.argv[3].startswith("-V"):
#                 if sys.argv[2].startswith("-") or sys.argv[4].startswith("-"):
#                     return "Error: Incorrect arguments provided. Please use the -help option to learn how to use the script."
#                 else:
#                     return createMatchString(sys.argv[2], None, sys.argv[4])
#             else:
#                 return "Error: Incorrect arguments provided. Please use the -help option to learn how to use the script."
#         if len(sys.argv) == 7:
#             if sys.argv[1].startswith("-p") and sys.argv[3].startswith("-v") and sys.argv[5].startswith("-V"):
#                 if sys.argv[2].startswith("-") or sys.argv[4].startswith("-") or sys.argv[6].startswith("-"):
#                     return "Error: Incorrect arguments provided. Please use the -help option to learn how to use the script."
#                 else:
#                     return createMatchString(sys.argv[6], sys.argv[2], sys.argv[4])
#             if sys.argv[1].startswith("-p") and sys.argv[3].startswith("-V") and sys.argv[5].startswith("-v"):
#                 if sys.argv[2].startswith("-") or sys.argv[4].startswith("-") or sys.argv[6].startswith("-"):
#                     return "Error: Incorrect arguments provided. Please use the -help option to learn how to use the script."
#                 else:
#                     return createMatchString(sys.argv[2], sys.argv[4], sys.argv[6])
#             else:
#                 return "Error: Incorrect arguments provided. Please use the -help option to learn how to use the script."
