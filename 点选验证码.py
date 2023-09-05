import base64
from src import captcha
import requests

img = requests.get('https://static.geetest.com/captcha_v3/batch/v3/46135/2023-09-05T14/word/6ecd9b67ba344887b0ef929fec218181.jpg?challenge=b0fdd37cfedd8a2279d434a7567dfced').content
# print(img)


# # 将图片数据转为base64编码
# base64_data = base64.b64encode(img)
# base64_str = base64_data.decode('utf-8')
# print(base64_str)

# data_ = {
#   "dataType": 2,
#   "imageSource": base64_str,
# }
# url = 'http://127.0.0.1:8000/clickOn'
#
# response = requests.post(url,
#                          # data=data_,
#                          json=data_
#                          )
#
# print(response.text)

cap = captcha.TextSelectCaptcha()
#送入模型识别
for i in range(10):
    plan = cap.run(img)
    print(plan)
