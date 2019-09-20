from pygal_maps_world.i18n import COUNTRIES

#  获取2个字母的国别码 排序
for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])
