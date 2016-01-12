#!/usr/bin/env python
# -*- coding: utf-8 -*-
#*****************************************************************************************
import sys
import urllib
import json
 
####
# 変数の型が文字列かどうかチェック
####
def is_str( data = None ) :
  if isinstance( data, str ) or isinstance( data, unicode ) :
    return True
  else :
    return False
 
####
# 初期値設定
####
# クライアントID
client_id  = "RSWG3L5AO0FI4JD0B1UPQCVK1JPMROQFBAOHJREAG3JUF3MR"
# クライアントシークレットキー
client_secret = "YBGUX02YTECOX3XQKRYDZKEJK01WR4TK03RCLWP3LXAWLIM5"
# エンドポイントURL
url = "https://api.foursquare.com/v2/venues/explore"
# Versioning
v = "20130815"
# セクション
section = "food"
# エリア
#near = "秋葉原"
near= "akihabara"
# 表示件数
limit = 1



####
# APIアクセス
####
# URLに続けて入れるパラメータを組立
query = [
  ( "client_id",    client_id    ),
  ( "client_secret",    client_secret     ),
  ( "v",  v  ),
  ( "section",  section  ),
  ( "near",  near  ),
  ( "limit",     limit     )
]
# URL生成
url += "?{0}".format( urllib.urlencode( query ) )
print url
# API実行
try :
  result = urllib.urlopen( url ).read()
except ValueError :
  print u"APIアクセスに失敗しました。"
  sys.exit()
 
####
# 取得した結果を解析
####
data = json.loads( result )
 
# エラーの場合
if "error" in data :
  if "message" in data :
    print u"{0}".format( data["message"] )
  else :
    print u"データ取得に失敗しました。"
  sys.exit()
 
# データがなかったら終了
#if not "venue" in data :
#  print u"データが見つからなかったため終了します。"
#  sys.exit()
 
print data

# データ取得
#results = data["results"]
#for shop in results["shop"] :
#  line                 = []
#  name                 = ""
#  station_name         = ""
#  address              = ""
#
#  # 店舗名
#  if "name" in shop and is_str( shop["name"] ) :
#    name = shop["name"]
#  line.append( name )
#  # 最寄駅
#  if "station_name" in shop and is_str( shop["station_name"] ):
#    station_name = u"{0}駅".format(shop["station_name"])
#  line.append( station_name )
#  # 住所
#  if "address" in shop and is_str( shop["address"] ):
#    address = shop["address"]
#  line.append( address )
#  # タブ区切りで出力
#  print "\t".join( line )
#  disp_count += 1
# 
## 出力件数を表示して終了
##print "----"
##print u"{0}件出力しました。".format( disp_count )
#sys.exit()
