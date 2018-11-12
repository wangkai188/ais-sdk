# -*- coding:utf-8 -*-
from ais_sdk.gettoken import get_token
from ais_sdk.utils import encode_to_base64
from ais_sdk.clarity_detect import clarity_detect
from ais_sdk.clarity_detect import clarity_detect_aksk

if __name__ == '__main__':
    #
    # access moderation detect,post data by token
    #
    user_name = '******'
    password = '******'
    account_name = '******'  # the same as user_name in commonly use

    demo_data_url = 'https://ais-sample-data.obs.cn-north-1.myhwclouds.com/vat-invoice.jpg'
    token = get_token(user_name, password, account_name)

    # call interface use the url
    result = clarity_detect(token, "", demo_data_url, 0.8)
    print (result)

    # call interface use the file
    result = clarity_detect(token, encode_to_base64('data/moderation-clarity-detect.jpg'), '', 0.8)
    print (result)

    #
    # access moderation detect,post data by ak,sk
    #
    app_key = "*************"
    app_secret = "************"

    # call interface use the url
    result = clarity_detect_aksk(app_key, app_secret, "", demo_data_url, 0.8)
    print(result)

    # call interface use the file
    result = clarity_detect_aksk(app_key, app_secret, encode_to_base64('data/moderation-clarity-detect.jpg'), '', 0.8)
    print (result)