#!/usr/bin/env python
# -*- coding: utf-8 -*-
#*****************************************************************************************
import sys
import urllib
import json
import os
import ConfigParser

def func(param):
  content=""
   
  ####
  # 変数の型が文字列かどうかチェック
  ####
  def is_str( data = None ) :
    if isinstance( data, str ) or isinstance( data, unicode ) :
      return True
    else :
      return False
   
  ####
  # パス指定
  ####
  sys.path.append(os.curdir)
  current_dir = os.path.abspath(os.path.dirname(__file__))
  home_dir = os.path.abspath(current_dir + os.sep + os.pardir) + os.sep
  ini_filepath = home_dir + "profiles" + os.sep + param + os.sep + "profile_foursquare.ini"

  ####
  # 設定ファイルの読み込み
  ####
  inifile = ConfigParser.SafeConfigParser()
  inifile.read(ini_filepath)
  
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
  # 緯度経度
  ll = "35.698358,139.773097"
  # 範囲
  radius = "1000"
  # 結果のリミット
  limit = "10"
  
  # セクション
  section = inifile.get("foursquare","section")
  
  # 予算
  price = inifile.get("foursquare","price")
  
  # その他
  day = inifile.get("foursquare","day")
  time = inifile.get("foursquare","time")
  
  ####
  # APIアクセス
  ####
  # URLに続けて入れるパラメータを組立
  query = [
    ( "client_id",        client_id       ),
    ( "client_secret",    client_secret   ),
    ( "v",                v               ),
    ( "ll",               ll              ),
    ( "radius",           radius          ),
    ( "limit",            limit           ),
    ( "section",          section         ),
    ( "price",            price           ),
    ( "day",              day             ),
    ( "time",             time            )
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
  #pprint.pprint(data)

  #data = json.dumps(data, ensure_ascii=False)
   
  # エラーの場合
  if "error" in data :
    if "message" in data :
      print u"{0}".format( data["message"] )
    else :
      print u"データ取得に失敗しました。"
    sys.exit()
   
  # データがなかったら終了
  if not "response" in data :
    print u"データが見つからなかったため終了します。"
    sys.exit()

  # データ取得
  for item in data['response']['groups'][0]['items']:
    venue = item['venue']
    line                 = []
    name                 = ""
    cityaddress          = ""

    # 店舗名
    if 'name' in venue and is_str( venue['name'] ) :
      name = venue['name']
    line.append( name )
    # 住所
    if 'location' in venue :
      city = venue['location']['city']
      address = venue['location']['address']
      cityaddress = city + " " + address
    line.append ( cityaddress )
  
    # タブ区切りで出力
    #print "\t".join( line ).encode('utf-8')
    #content+="\t".join( line ).encode('utf-8')
    #content+=("</br>").encode('utf-8')
    content+="\t".join( line )
    content+="</br>"

  return content

  ## 出力件数を表示して終了
  ##print "----"
  ##print u"{0}件出力しました。".format( disp_count )
  sys.exit()