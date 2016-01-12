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
  ini_filepath = home_dir + "profiles" + os.sep + param + os.sep + "profile_gnavi.ini"

####
# 設定ファイルの読み込み
####
  inifile = ConfigParser.SafeConfigParser()
  inifile.read(ini_filepath)
 
####
# 初期値設定
####
  # APIアクセスキー
  keyid     = "b9825ef83c9b068d6c6e4bffeac37cb4"
  # エンドポイントURL
  url       = "http://api.gnavi.co.jp/RestSearchAPI/20150630/"
  # 緯度
  latitude = "35.698358"
  #経度
  longitude = "139.773097"
  # カテゴリ
  category_l_all = inifile.get("gnavi","category_l")
  array_category = category_l_all.split(",")
  category_l_1 = array_category[0]
  category_l_2 = array_category[1]
  
  # その他
  lunch = inifile.get("gnavi","lunch")
  no_smoking = inifile.get("gnavi","no_smoking")
  card = inifile.get("gnavi","card")
  mobilephone = inifile.get("gnavi","mobilephone")
  bottomless_cup = inifile.get("gnavi","bottomless_cup")
  sunday_open = inifile.get("gnavi","sunday_open")
  takeout = inifile.get("gnavi","takeout")
  private_room = inifile.get("gnavi","private_room")
  midnight = inifile.get("gnavi","midnight")
  parking = inifile.get("gnavi","parking")
  memorial_service = inifile.get("gnavi","memorial_service")
  birthday_privilege = inifile.get("gnavi","birthday_privilege")
  betrothal_present = inifile.get("gnavi","betrothal_present")
  kids_menu = inifile.get("gnavi","kids_menu")
  outret = inifile.get("gnavi","outret")
  wifi = inifile.get("gnavi","wifi")
  microphone = inifile.get("gnavi","microphone")
  buffet = inifile.get("gnavi","buffet")
  late_lunch = inifile.get("gnavi","late_lunch")
  sports = inifile.get("gnavi","sports")
  until_morning = inifile.get("gnavi","until_morning")
  lunch_desert = inifile.get("gnavi","lunch_desert")
  projecter_screen = inifile.get("gnavi","projecter_screen")
  with_pet = inifile.get("gnavi","with_pet")
  deliverly = inifile.get("gnavi","deliverly")
  special_holiday_lunch = inifile.get("gnavi","special_holiday_lunch")
  e_money = inifile.get("gnavi","e_money")
  caterling = inifile.get("gnavi","caterling")
  breakfast = inifile.get("gnavi","breakfast")
  desert_buffet = inifile.get("gnavi","desert_buffet")
  lunch_buffet = inifile.get("gnavi","lunch_buffet")
  bento = inifile.get("gnavi","bento")
  lunch_salad_buffet = inifile.get("gnavi","lunch_salad_buffet")
  darts = inifile.get("gnavi","darts")
   
####
# APIアクセス
####
  # URLに続けて入れるパラメータを組立
  query = [
    ( "format",                   "json"                      ),
    ( "keyid",                    keyid                       ),
    ( "latitude",                 latitude                    ),
    ( "longitude",                longitude                   ),
    ( "category_l",               category_l_1                ),
    ( "category_l",               category_l_2                ),
    ( "lunch",                    lunch                       ),
    ( "no_smoking",               no_smoking                  ),
    ( "card",                     card                        ),
    ( "mobilephone",              mobilephone                 ),
    ( "bottomless_cup",           bottomless_cup              ),
    ( "sunday_open",              sunday_open                 ),
    ( "takeout",                  takeout                     ),
    ( "private_room",             private_room                ),
    ( "midnight",                 midnight                    ),
    ( "parking",                  parking                     ),
    ( "memorial_service",         memorial_service            ),
    ( "birthday_privilege",       birthday_privilege          ),
    ( "betrothal_present",        betrothal_present           ),
    ( "kids_menu",                kids_menu                   ),
    ( "outret",                   outret                      ),
    ( "wifi",                     wifi                        ),
    ( "microphone",               microphone                  ),
    ( "buffet",                   buffet                      ),
    ( "late_lunch",               late_lunch                  ),
    ( "sports",                   sports                      ),
    ( "until_morning",            until_morning               ),
    ( "lunch_desert",             lunch_desert                ),
    ( "projecter_screen",         projecter_screen            ),
    ( "with_pet",                 with_pet                    ),
    ( "deliverly",                deliverly                   ),
    ( "special_holiday_lunch",    special_holiday_lunch       ),
    ( "e_money",                  e_money                     ),
    ( "caterling",                caterling                   ),
    ( "breakfast",                breakfast                   ),
    ( "desert_buffet",            desert_buffet               ),
    ( "lunch_buffet",             lunch_buffet                ),
    ( "bento",                    bento                       ),
    ( "lunch_salad_buffet",       lunch_salad_buffet          ),
    ( "darts",                    darts                       )
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
 
# ヒット件数取得
  total_hit_count = None
  if "total_hit_count" in data :
    total_hit_count = data["total_hit_count"]
   
# ヒット件数が0以下、または、ヒット件数がなかったら終了
  if total_hit_count is None or total_hit_count <= 0 :
    print u"指定した内容ではヒットしませんでした。"
    sys.exit()
 
# レストランデータがなかったら終了
  if not "rest" in data :
    print u"レストランデータが見つからなかったため終了します。"
    sys.exit()
 
# ヒット件数表示
#print "{0}件ヒットしました。".format( total_hit_count )
#print "----"
 
# 出力件数
  disp_count = 0

# レストランデータ取得
  for rest in data["rest"] :
    line                 = []
    name                 = ""
    access_station       = ""
    address              = ""
  # 店舗名
    if "name" in rest and is_str( rest["name"] ) :
      name = u"{0}".format( rest["name"] )
    line.append( name )
    if "access" in rest :
      access = rest["access"]
      # 最寄の駅
      if "station" in access and is_str( access["station"] ) :
        access_station = u"{0}".format( access["station"] )
      line.append( access_station )
    # 住所
      if "address" in rest and is_str( rest["address"] ) :
        address = u"{0}".format(rest["address"])
      line.append( address )
    # タブ区切りで出力
  #    print "\t".join( line ).encode('utf-8')

    content+="\t".join( line )
    content+=u"<br />"

  return content

# 出力件数を表示して終了
#print "----"
#print u"{0}件出力しました。".format( disp_count )
  sys.exit()
