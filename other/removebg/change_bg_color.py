# 给去除了背景的图像添加背景颜色

from PIL import Image

# 输入已经去除背景的图像
im = Image.open('./pic/a.jpg_no_bg.png')
x, y = im.size

try:
    # 填充色背景
    p = Image.new('RGBA', im.size, (255, 255, 255))
    p.paste(im, (0, 0, x, y), im)
    # 保存填充后的图片
    p.save('./pic/a.jpg_red_bg.png')
except:
    with open('./error.log', 'a') as f:
        f.write('background change fail .\n')

