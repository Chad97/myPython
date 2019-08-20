def get_formatted_name(first, last, middle=''):
    """ 拼接姓名 """
    full_name = first + ' ' + middle + ' ' + last if middle else first + " " + last
    return full_name.title()

