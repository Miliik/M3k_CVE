from Search import *


def createMatchString(vendor, product, version):

    if vendor is None and product is None:
        return None
    elif vendor is None:
        if version is None:
            return MatchstringSearch("cpe:2.3:*:*:" + product + ":*:*:*:*:*:*:*")
        else:
            return MatchstringSearch("cpe:2.3:*:*:" + product + ":" + version + ":*:*:*:*:*:*")
    elif product is None:
        if version is None:
            return MatchstringSearch("cpe:2.3:*:" + vendor + ":*:*:*:*:*:*:*:*")
        else:
            return MatchstringSearch("cpe:2.3:*:" + vendor + ":*:" + version + ":*:*:*:*:*:*")
    elif version is None:
        return MatchstringSearch("cpe:2.3:*:" + vendor + ":" + product + ":*:*:*:*:*:*:*:*")
    else:
        return MatchstringSearch("cpe:2.3:*:" + vendor + ":" + product + ":" + version + ":*:*:*:*:*:*:*")

