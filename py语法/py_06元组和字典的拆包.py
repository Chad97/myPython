def demo(*args, **kwargs):
    print(args)
    print(kwargs)


gl_nums = (1, 'a', '6')
gl_dict = {'name': 'zs',  'age': '18'}

demo(*gl_nums, **gl_dict)
