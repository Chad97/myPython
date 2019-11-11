import yaml

# 读写
with open("user.yml", "r+") as yaml_file:
    yaml_obj = yaml.load(yaml_file, Loader=yaml.FullLoader)  # load加第二个参数避免警告
    print(yaml_obj['user'])
    print(yaml_obj['password'])
    print(yaml_obj['list'])

    info = {'a': 'AAA'}
    yaml.dump(info, yaml_file)


# 追加写入
with open("user.yml", "a") as yf:
    f_obj = {'test': ['阿萨德', 'asd', '123']}
    yaml.dump(f_obj, yf)
