def createMatchString(product, version, vendor): #this is the function that creates the match string proper to be used in the search in the nvd api
    if product is None:
        product = "*"
    if version is None:
        version = "*"
    if vendor is None:
        vendor = "*"
    url = "cpe:2.3:*:" + vendor + ":" + product + ":" + version + ":*:*:*:*:*:*:*" #this is the Virtual matchstring that is used to search the nvd api
    print(url)
    return url
