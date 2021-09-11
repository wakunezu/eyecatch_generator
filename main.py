from PIL import Image, ImageDraw, ImageFont
from webcolors import name_to_rgb  # pip install webcolors
from config import config


# 初期設定。
img = Image.open(config['template_img'])
img_cp = img.copy()
W, H = img_cp.size
img_cp.putalpha(255)  # アルファチャンネルを追加する。ただし画像自体は透過しない。

# 背景色の設定。threshが80くらいできれいに塗りつぶせる
bg_rgb = tuple(name_to_rgb(config['bg_color']))
ImageDraw.floodfill(img_cp, (1, 1), (*bg_rgb, config['bg_alpha']), border=None, thresh=80)
ImageDraw.floodfill(img_cp, (100, 100), (*bg_rgb, config['bg_alpha']), border=None, thresh=80)
draw = ImageDraw.Draw(img_cp)

# subtitle の設置
fnt_st = ImageFont.truetype(config['font'], config['fs_st'])
w, h = draw.textsize(config['subtitle'], font=fnt_st)
draw.text(((W-w)/2, 130), config['subtitle'], fill=config['font_color'], font=fnt_st)

# title1 = 一段目の設置
fnt_ti = ImageFont.truetype(config['font'], config['fs_ti'])
w, h = draw.textsize(config['title1'], font=fnt_ti)
draw.text(((W-w)/2, 250), config['title1'], fill=config['font_color'], font=fnt_ti)

# title2 = 一段目の設置
w, h = draw.textsize(config['title2'], font=fnt_ti)
draw.text(((W-w)/2, 350), config['title2'], fill=config['font_color'], font=fnt_ti)

img_cp.save(config['save_path'])
