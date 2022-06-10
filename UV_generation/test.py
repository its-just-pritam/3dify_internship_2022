from uv_map import UV_Map
import cv2 as cv

final_img = UV_Map('tshirt2.jpg', 'tp_back.txt', 'tp_back_uv.txt')
cv.imwrite('tshirt1_transformed.jpg', final_img)

'''
http://localhost:5000/?image=https://www.mydesignation.com/wp-content/uploads/2019/06/but-why-tshirt-mydesignation-image-latest.jpg
http://192.168.101.8:5000/?image=https://i.imgur.com/DOmYCmr.png
http://192.168.101.8:5000/?image=https://i.imgur.com/ukOa5vd.jpg
http://192.168.101.8:5000/?image=https://i.imgur.com/zelh7NM.png
'''

'''
npx serve -p 5000

[[(392, 218), (335, 213), (365, 95)], [(335, 213), (392, 218), (344, 222)], [(144, 92), (225, 82), (170, 201)], [(225, 82), (144, 92), (213, 63)], [(108, 206), (144, 92), (170, 201)], [(170, 201), (225, 82), (254, 90)], [(365, 95), (335, 213), (288, 82)], [(295, 62), (365, 95), (288, 82)], [(254, 90), (288, 82), (335, 213)], [(335, 213), (328, 315), (179, 304)], [(335, 213), (179, 304), (170, 201)], [(254, 90), (335, 213), (170, 201)], [(328, 315), (252, 431), (179, 304)], [(252, 431), (328, 315), (329, 428)], [(179, 304), (252, 431), (182, 426)], [(108, 206), (170, 201), (160, 216)]]
'''