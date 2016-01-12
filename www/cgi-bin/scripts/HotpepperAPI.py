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
  ini_filepath = home_dir + "profiles" + os.sep + param + os.sep + "profile_hotpepper.ini"
  
  ####
  # 設定ファイルの読み込み
  ####
  inifile = ConfigParser.SafeConfigParser()
  inifile.read(ini_filepath)
   
  ####
  # 初期値設定
  ####
  # APIアクセスキー
  key     = "16f0ad71c8fce0ef"
  # エンドポイントURL
  url       = "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/"
  # 緯度
  Latitude = "35.698358"
  # 経度
  Longitude = "139.773097"
  # 範囲
  Range = "2"
  # 取得数
  Count = "10"
  
  # カテゴリ
  GenreCD_all = inifile.get("hotpepper","GenreCD")
  array_genre = GenreCD_all.split(",")
  GenreCD_1 = array_genre[0]
  GenreCD_2 = array_genre[1]
  
  # 予算
  BudgetCD = inifile.get("hotpepper","BudgetCD")
  
  # その他
  Course = inifile.get("hotpepper","Course")
  FreeDrink = inifile.get("hotpepper","FreeDrink")
  FreeFood = inifile.get("hotpepper","FreeFood")
  PrivateRoom = inifile.get("hotpepper","PrivateRoom")
  Horigotatsu = inifile.get("hotpepper","Horigotatsu")
  Tatami = inifile.get("hotpepper","Tatami")
  Cocktail = inifile.get("hotpepper","Cocktail")
  Shochu = inifile.get("hotpepper","Shochu")
  Sake = inifile.get("hotpepper","Sake")
  Wine = inifile.get("hotpepper","Wine")
  Card = inifile.get("hotpepper","Card")
  NonSmoking = inifile.get("hotpepper","NonSmoking")
  Charter = inifile.get("hotpepper","Charter")
  Ktai = inifile.get("hotpepper","Ktai")
  Parking = inifile.get("hotpepper","Parking")
  BarrierFree = inifile.get("hotpepper","BarrierFree")
  Sommelier = inifile.get("hotpepper","Sommelier")
  NightView = inifile.get("hotpepper","NightView")
  OpenAir = inifile.get("hotpepper","OpenAir")
  Show = inifile.get("hotpepper","Show")
  Equipment = inifile.get("hotpepper","Equipment")
  Karaoke = inifile.get("hotpepper","Karaoke")
  Band = inifile.get("hotpepper","Band")
  Lunch = inifile.get("hotpepper","Lunch")
  Midnight = inifile.get("hotpepper","Midnight")
  MidnightMeal = inifile.get("hotpepper","MidnightMeal")
  English = inifile.get("hotpepper","English")
  Pet = inifile.get("hotpepper","Pet")
  Child = inifile.get("hotpepper","Child")
  
  ####
  # APIアクセス
  ####
  # URLに続けて入れるパラメータを組立
  query = [
    ( "format",                  "json"       ),
    ( "key",                     key          ),
    ( "Count",                   Count        ),
    ( "Latitude",                Latitude     ),
    ( "Longitude",               Longitude    ),
    ( "Range",                   Range        ),
    ( "GenreCD",                 GenreCD_1    ),
    ( "GenreCD",                 GenreCD_2    ),
    ( "BudgetCD",                BudgetCD     ),
    ( "Course",                  Course       ),
    ( "FreeDrink",               FreeDrink    ),
    ( "FreeFood",                FreeFood     ),
    ( "PrivateRoom",             PrivateRoom  ),
    ( "Horigotatsu",             Horigotatsu  ),
    ( "Tatami",                  Tatami       ),
    ( "Cocktail",                Cocktail     ),
    ( "Shochu",                  Shochu       ),
    ( "Sake",                    Sake         ),
    ( "Wine",                    Wine         ),
    ( "Card",                    Card         ),
    ( "NonSmoking",              NonSmoking   ),
    ( "Charter",                 Charter      ),
    ( "Ktai",                    Ktai         ),
    ( "Parking",                 Parking      ),
    ( "BarrierFree",             BarrierFree  ),
    ( "Sommelier",               Sommelier    ),
    ( "NightView",               NightView    ),
    ( "OpenAir",                 OpenAir      ),
    ( "Show",                    Show         ),
    ( "Equipment",               Equipment    ),
    ( "Karaoke",                 Karaoke      ),
    ( "Band",                    Band         ),
    ( "Lunch",                   Lunch        ),
    ( "Midnight",                Midnight     ),
    ( "MidnightMeal",            MidnightMeal ),
    ( "English",                 English      ),
    ( "Pet",                     Pet          ),
    ( "Child",                   Child        )
  ]
  # URL生成
  url += "?{0}".format( urllib.urlencode( query ) )
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
   
  # レストランデータがなかったら終了
  if not "results" in data :
    print u"レストランデータが見つからなかったため終了します。"
    sys.exit()
   
  # 出力件数
  disp_count = 0
   
  # レストランデータ取得
  results = data["results"]
  for shop in results["shop"] :
    line                 = []
    name                 = ""
    station_name         = ""
    address              = ""
    # 店舗名
    if "name" in shop and is_str( shop["name"] ) :
      name = shop["name"]
    line.append( name )
    # 最寄駅
    if "station_name" in shop and is_str( shop["station_name"] ):
      station_name = u"{0}駅".format(shop["station_name"])
    line.append( station_name )
    # 住所
    if "address" in shop and is_str( shop["address"] ):
      address = shop["address"]
    line.append( address )
    # タブ区切りで出力
    # print "\t".join( line ).encode('utf-8')
  

    content+="\t".join( line )
    content+=u"<br />"

  return content
 
  # 出力件数を表示して終了
  #print "----"
  #print u"{0}件出力しました。".format( disp_count )
  sys.exit()
