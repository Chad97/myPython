from pygal_maps_world.i18n import COUNTRIES



def get_country_code(country_name):
    """ 根据指定国家 返回2个字符的国别码 """
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    #  没有找到国别码
    return None
