# -*- coding:utf-8 -*-
import sys
import time
import json
print sys.getdefaultencoding()
reload(sys)
sys.setdefaultencoding("utf8")
print sys.getdefaultencoding()

str="[ {\"fundcode\": \"519180\",\"fundname\": \"万家180指\" ,\"gpnum\":1,\"gpcode\":\"601318\",\"gpname\":\"中国平安\",\"gprate\":\"7.55%\"},{\"fundcode\": \"519180\",\"fundname\": \"万家180指\" ,\"gpnum\":2,\"gpcode\":\"600036\",\"gpname\":\"招商银行\",\"gprate\":\"3.39%\"},{\"fundcode\": \"519180\",\"fundname\": \"万家180指\" ,\"gpnum\":3,\"gpcode\":\"600519\",\"gpname\":\"贵州茅台\",\"gprate\":\"3.35%\"},{\"fundcode\": \"519180\",\"fundname\": \"万家180指\" ,\"gpnum\":4,\"gpcode\":\"601398\",\"gpname\":\"工商银行\",\"gprate\":\"2.79%\"},{\"fundcode\": \"519180\",\"fundname\": \"万家180指\" ,\"gpnum\":5,\"gpcode\":\"601166\",\"gpname\":\"兴业银行\",\"gprate\":\"2.77%\"},{\"fundcode\": \"519180\",\"fundname\": \"万家180指\" ,\"gpnum\":6,\"gpcode\":\"600016\",\"gpname\":\"民生银行\",\"gprate\":\"2.44%\"},{\"fundcode\": \"519180\",\"fundname\": \"万家180指\" ,\"gpnum\":7,\"gpcode\":\"601328\",\"gpname\":\"交通银行\",\"gprate\":\"2.23%\"},{\"fundcode\": \"519180\",\"fundname\": \"万家180指\" ,\"gpnum\":8,\"gpcode\":\"600887\",\"gpname\":\"伊利股份\",\"gprate\":\"2.15%\"},{\"fundcode\": \"519180\",\"fundname\": \"万家180指\" ,\"gpnum\":9,\"gpcode\":\"601288\",\"gpname\":\"农业银行\",\"gprate\":\"1.88%\"},{\"fundcode\": \"519180\",\"fundname\": \"万家180指\" ,\"gpnum\":10,\"gpcode\":\"600000\",\"gpname\":\"浦发银行\",\"gprate\":\"1.86%\"} ]"

#str="{\"fundcode\": \"519180\",\"fundname\": \"\u4e07\u5bb6180\u6307\" ,\"gpnum\":1,\"gpcode\":\"601318\",\"gpname\":\"\u4e2d\u56fd\u5e73\u5b89\",\"gprate\":\"7.55%\"}"

jsonstr2 = json.loads(str)

print jsonstr2[3]["fundcode"]