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
  
### edit by kobayashi 2016-01-19
  #フリーワード検索
#  query = inifile.get("foursquare","query") 


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
 #   ( "query",            query           ),
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

  priority             = 1

  # データ取得
  for item in data['response']['groups'][0]['items']:
    venue = item['venue']
    tips  = item['tips'][0]
    line                 = []
    pc_url               = ""
    name                 = ""
    c_name               = ""


    # URL
    if 'canonicalUrl' in tips :
      pc_url = tips['canonicalUrl']
      print pc_url
    # 店舗名
    if 'name' in venue and is_str( venue['name'] ) :
      name = venue['name']
    line.append( name )
    # カテゴリ名
    if 'categories' in venue :
      c_name = venue['categories'][0]['name']
    line.append( c_name )
    # タブ区切りで出力
    #print "\t".join( line ).encode('utf-8')
    #優先度
    priority += 1
    priority_str = "<div class=\"prio\">" + str(priority) + "</div>"
    line.append( priority_str )

    # アイコン
    icon = "<div class=\"icon\"><img src=\"/images/foursquare_icon.png\" width=\"30\" height=\"30\"></div>"
    line.append( icon )

    content+=u"<tr><td><a href=\""
    content+=u"{0}".format( pc_url )
    content+=u"\">"
    content+=u"</td><td>".join( line )
    content+=u"</td></tr>"

  return content

  ## 出力件数を表示して終了
  ##print "----"
  ##print u"{0}件出力しました。".format( disp_count )
  sys.exit()
