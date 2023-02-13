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
    return url
