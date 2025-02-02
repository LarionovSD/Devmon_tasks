from PIL import Image


monro = Image.open("monro.jpg")

red_monro, green_monro, blue_monro = monro.split()




#обрезан красный канал на 25 пикселей с каждой стороны
coordinates_1 = (25, 0, red_monro.width, red_monro.height)
crop_1_red_monro = red_monro.crop(coordinates_1)
rotate_1_red_monro = crop_1_red_monro.rotate(180)
coordinates_2 = (25, 0, rotate_1_red_monro.width, rotate_1_red_monro.height)
crop_2_red_monro = rotate_1_red_monro.crop(coordinates_2)
crop_red_monro_25x25 = crop_2_red_monro.rotate(180)

#обрезан красный канал на 50 пикселей с левой стороны
coordinates_3 = (50, 0, red_monro.width, red_monro.height)
crop_red_monro_50 = red_monro.crop(coordinates_3)

#наложение красных каналов друг на друга со смещением
blend_red_monro = Image.blend(crop_red_monro_25x25, crop_red_monro_50, 0.5)




#обрезан синий канал на 25 пикселей с каждой стороны
coordinates_4 = (25, 0, blue_monro.width, blue_monro.height)
crop_1_blue_monro = blue_monro.crop(coordinates_4)
rotate_1_blue_monro = crop_1_blue_monro.rotate(180)
coordinates_5 = (25, 0, rotate_1_blue_monro.width, rotate_1_blue_monro.height)
crop_2_blue_monro = rotate_1_blue_monro.crop(coordinates_5)
crop_blue_monro_25x25 = crop_2_blue_monro.rotate(180)

#обрезан синий канал на 50 пикселей с правой стороны
rotate_blue_monro = blue_monro.rotate(180)
coordinates_6 = (50, 0, rotate_blue_monro.width, rotate_blue_monro.height)
crop_rotate_blue_monro = rotate_blue_monro.crop(coordinates_6)
crop_blue_monro_50 = crop_rotate_blue_monro.rotate(180)

#наложение синих каналов друг на друга со смещением
blend_blue_monro = Image.blend(crop_blue_monro_25x25, crop_blue_monro_50, 0.5)




#обрезан зеленый канал на 25 пикселей с каждой стороны
coordinates_7 = (25, 0, green_monro.width, green_monro.height)
crop_1_green_monro = green_monro.crop(coordinates_7)
rotate_1_green_monro = crop_1_green_monro.rotate(180)
coordinates_8 = (25, 0, rotate_1_green_monro.width, rotate_1_green_monro.height)
crop_2_green_monro = rotate_1_green_monro.crop(coordinates_8)
crop_green_monro_25x25 = crop_2_green_monro.rotate(180)



#соединение цветовых каналов
rgb_monro = Image.merge("RGB", (blend_red_monro, crop_green_monro_25x25, blend_blue_monro))

rgb_monro.thumbnail((80, 80))

rgb_monro.save("avatar.jpg", format = "JPEG")