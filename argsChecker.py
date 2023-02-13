import argparse
import sys

from CreateMatchString import *
from Search import *
from functions import writehelp


def checkarg():  # check if the user has entered the right arguments and if not, print the help , then execute the
    # right function
    output = None
    parser = argparse.ArgumentParser(description="Search for CVEs in the NVD database")
    parser.add_argument("-w", "--keyword", help="USE ALONE ONLY search for a keyword (use \" \" for multiple words)")
    parser.add_argument("-p", "--product", help="search for a product")
    parser.add_argument("-v", "--version", help="search for a version")
    parser.add_argument("-V", "--vendor", help="search for a vendor")
    parser.add_argument("-o", "--output", help="output to a file", action="store_true")
    args = parser.parse_args()
    if args.output:  # if the user wants to output to a file
        output = True
    if args.keyword is not None:  # if the user wants to search for a keyword
        return KeywordSearch(args.keyword, output)
    elif args.product is not None:  # if the user wants to search for a product
        print("product")
        if args.version is not None:  # if the user wants to search for a product and a version
            return MatchstringSearch(createMatchString(args.product, args.version, args.vendor), output)
        elif args.vendor is not None:  # if the user wants to search for a product and a vendor
            return MatchstringSearch(createMatchString(args.product, None, args.vendor), output)
        else:
            return MatchstringSearch(createMatchString(args.product, None, None), output)
    elif args.vendor is not None:
        print("vendor")
        if args.product is not None:  # if the user wants to search for a vendor and a product
            print("product")
            return MatchstringSearch(createMatchString(args.product, None, args.vendor), output)
        else:
            print("no product")
            return MatchstringSearch(createMatchString(None, None, args.vendor), output)
    else:
        writehelp()  # if the user didn't enter the right arguments, print the help
        sys.exit(0)

# the proof i can make useless long functions

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
