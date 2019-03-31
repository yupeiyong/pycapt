from PIL import Image
import pycapt.make_captcha
import pycapt.solve_it
import pycapt

name = "pycapt"

# 图像转化为01 np数组 Threshold为阀值
def get_mode(img,Threshold=100):
    mode = pycapt.solve_it.de_line.get_modes(img,Threshold)
    return mode

# 将np数组噪点处理，mode 数组，N是加噪率（边缘存在1个以上的黑点那么这个点有一点概率变黑） Z 加噪次数 返回数组
def show_noise_mode(mode, N, Z):
    new_mode = pycapt.pycapt.show_noise_mode(mode, N, Z)
    return new_mode

# 将np数组噪点处理，mode 数组，N是加噪率（边缘存在1个以上的黑点那么这个点有一点概率变黑） Z 加噪次数 返回图片
def show_noise_img(mode, N, Z):
    new_img = pycapt.pycapt.show_noise_img(mode, N, Z)
    return new_img

# 偏移 传入np数组，横向偏移(默认右移)，纵向偏移，传出新的mode
def mode_pan(mode,width_x,height_y):
    new_mode = pycapt.pycapt.mode_pan(mode,width_x,height_y)
    return new_mode

# 生成验证码 长宽 字符串个数 背景颜色 一般要上线用的话看源码改一改就好了
def make_capt_img(width,height,num_of_str,gray_value=255):
    image = pycapt.pycapt.make_capt_img(width,height,num_of_str,gray_value=255)
    return image

# 生成简单的大写字母训练集图片
def get_train_img():
    file_name,image = pycapt.pycapt.get_train_img()
    return file_name,image

# 将np数组转化为图片
def mode_img(mode,background=None):
    img = pycapt.solve_it.mode_img(mode,background)
    return img

# 将01数组转化为黑白图片
def mode_white_img(mode):
    img = pycapt.pycapt.mode_img(mode,background=255)
    return img

# 消除噪点，N是周围相异像素个数喵，Z是处理次数
def dele_noise(image, N, Z):
    img = pycapt.solve_it.dele_noise(image, N, Z)
    return img

# 处理干扰线
def dele_line(image, N, pans=None):
    img = pycapt.solve_it.dele_line(image, N, pans=None)
    return img

# 清理一般有干扰线的验证码
def clear_train_img(image):
    img = pycapt.solve_it.clear_train_img(image)
    return img

# 清理一般有干扰线的斜体验证码
def clear_lib_line(image):
    img = pycapt.solve_it.clear_lib_line(image)
    return img

# 将图片切割为np数组列表
def cut_img_to_mode_list(image,max_width):
    img_mode_list = pycapt.solve_it.cut_img_to_mode_list(image,max_width)
    return img_mode_list

# 将图片切割为图片列表
def cut_img_to_img_list(image,max_width,background=None):
    if background:
        return pycapt.solve_it.cut_img_to_img_list(image,max_width,background=255)
    else:
        return pycapt.solve_it.cut_img_to_img_list(image,max_width,background=None)

# 图片斜体纠正 pans是图片高度长度的列表
def rectify_img(image, pans):
    return pycapt.solve_it.rectify_img(image,pans)

# 数组斜体纠正
def rectify_mode(mode, pans):
    return pycapt.solve_it.rectify_mode(mode,pans)

# 二值化图片，变为黑白
def two_value(img,Threshold=100):
    mode = get_mode(img,Threshold)
    return mode_img(mode,background=255)

# 图片翻转并旋转90度
def tran_90(img):
    mode = get_mode(img)
    img = mode_img(mode.T,255)
    return img

# 生成验证码
def do_captcha(my_str_list,width,height,num_of_str,font=30,gray_value=255,font_family='ヒラギノ角ゴシック W8.ttc'):
    return pycapt.make_captcha.my_any_img.mk_captcha(my_str_list,width,height,num_of_str,font,gray_value,font_family)