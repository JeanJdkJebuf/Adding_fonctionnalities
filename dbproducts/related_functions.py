import unidecode

def symbol_removal(sub_category):
    """ This function removes three first characters of sub_category and special characters"""
    sub_category = sub_category[3:]
    sub_category = sub_category.replace("-", "_")
    sub_category = unidecode.unidecode(sub_category)
    sub_category = sub_category.replace(" ", "_")
    return sub_category
