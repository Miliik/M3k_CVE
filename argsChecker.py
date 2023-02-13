import sys
from CreateMatchString import *


def checkarg():
    if len(sys.argv) == 1 or len(sys.argv) == 4 or len(sys.argv) == 6 or len(sys.argv) > 7:
        print(len(sys.argv))
        return "Error wrong arguments"
    else:

        if len(sys.argv) == 3:
            if sys.argv[1].startswith("-w"):
                if sys.argv[2].startswith("-"):
                    return "Error wrong arguments"
                else:
                    return KeywordSearch(sys.argv[2])
            if sys.argv[1].startswith("-p"):
                if sys.argv[2].startswith("-"):
                    return "Error wrong arguments"
                else:
                    return createMatchString(None, sys.argv[2], None)
            if sys.argv[1].startswith("-V"):
                if sys.argv[2].startswith("-"):
                    return "Error wrong arguments"
                else:
                    return createMatchString(sys.argv[3], None, None)
            if sys.argv[1].startswith("-v"):
                return "-v (version) can only be used with -p (product)"
            else:
                return "Error wrong arguments"

        if len(sys.argv) == 5:
            if sys.argv[1].startswith("-p") and sys.argv[3].startswith("-v"):
                if sys.argv[2].startswith("-") or sys.argv[4].startswith("-"):
                    return "Error wrong arguments"
                else:
                    return createMatchString(None, sys.argv[2], sys.argv[4])
            if sys.argv[1].startswith("-p") and sys.argv[3].startswith("-V"):
                if sys.argv[2].startswith("-") or sys.argv[4].startswith("-"):
                    return "Error wrong arguments"
                else:
                    return createMatchString(sys.argv[2], None, sys.argv[4])
            else:
                return "Error wrong arguments"
        if len(sys.argv) == 7:
            if sys.argv[1].startswith("-p") and sys.argv[3].startswith("-v") and sys.argv[5].startswith("-V"):
                if sys.argv[2].startswith("-") or sys.argv[4].startswith("-") or sys.argv[6].startswith("-"):
                    return "Error wrong arguments"
                else:
                    return createMatchString(sys.argv[6], sys.argv[2], sys.argv[4])
            if sys.argv[1].startswith("-p") and sys.argv[3].startswith("-V") and sys.argv[5].startswith("-v"):
                if sys.argv[2].startswith("-") or sys.argv[4].startswith("-") or sys.argv[6].startswith("-"):
                    return "Error wrong arguments"
                else:
                    return createMatchString(sys.argv[2], sys.argv[4], sys.argv[6])
            else:
                return "Error wrong arguments"
