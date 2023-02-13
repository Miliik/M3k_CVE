from Search import *


def createMatchString(product, version, vendor):
    if product is None:
        product = "*"
    if version is None:
        version = "*"
    if vendor is None:
        vendor = "*"
    url="cpe:2.3:*:" + vendor + ":" + product + ":" + version + ":*:*:*:*:*:*:*"
    print(url)
    return MatchstringSearch(url)

    # if vendor is None and product is None:
    #     exit("Error: Incorrect arguments provided. Please use the -help option to learn how to use the script.")
    # elif version is None:
    #     return MatchstringSearch("cpe:2.3:*:" + vendor + ":" + product + ":*:*:*:*:*:*:*:*")
    # elif vendor is None:
    #     if version is None:
    #         return MatchstringSearch("cpe:2.3:*:*:" + product + ":*:*:*:*:*:*:*")
    #     else:
    #         return MatchstringSearch("cpe:2.3:*:*:" + product + ":" + version + ":*:*:*:*:*:*")
    # elif product is None:
    #         return MatchstringSearch("cpe:2.3:*:" + vendor + ":*:*:*:*:*:*:*:*")
    #
    # else:
    #     return MatchstringSearch("cpe:2.3:*:" + vendor + ":" + product + ":" + version + ":*:*:*:*:*:*:*")