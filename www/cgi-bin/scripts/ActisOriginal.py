#!/usr/bin/env python
# -*- coding: utf-8 -*-
#******************************************************************************************

import sys
import urllib
import json
import os
import ConfigParser
import sqlite3


def func(param):
  content=""

  ####
  # パス指定
  ####
  sys.path.append(os.curdir)
  current_dir = os.path.abspath(os.path.dirname(__file__))
  home_dir = os.path.abspath(current_dir + os.sep + os.pardir) + os.sep
  ini_filepath = home_dir + "profiles" + os.sep + param + os.sep + "profile_original.ini"

  ####
  # 設定ファイルの読み込み
  ####
  inifile = ConfigParser.SafeConfigParser()
  inifile.read(ini_filepath)

  ####
  # 変数定義
  ####
  # 取得数
  limit = 10
  # カテゴリ
  category = inifile.get("original","category")
  # 予算
  price = inifile.get("original","price")

  ####
  # メイン処理
  ####
  connector = sqlite3.connect("/tmp/api_db.sqlite3")
  cursor    = connector.cursor()
#  cursor.execute("select url, name, section from api_tbl where price = 2 and category = \"food\" limit 10;")
  cursor.execute("select url, name, section from api_tbl where price = {price} and category = \"{category}\" limit {limit};".format(**vars()))

  result = cursor.fetchall()

  for row in result:
    line  = [] 
    # URL
    url = unicode(row[0])

    #店舗名
    name = unicode(row[1])
    line.append( name )

    #カテゴリ
    section=unicode(row[2])
    line.append( section )

    #優先度
    priority = 1
    priority_str = "<div class=\"prio\">" + str(priority) + "</div>"
    line.append( priority_str )

    # アイコン
    icon = "<div class=\"icon\"><img src=\"/images/PremiumIcon.png\" width=\"30\" height=\"30\"></div>"
    line.append( icon )
     
    content+=u"<tr><td><a href=\""
    content+=u"{0}".format( url )
    content+=u"\"  target=\"_blank\">"
    content+=u"</td><td>".join( line )
    content+=u"</td></tr>"
  
  return content
#  print content

  cursor.close()
  connector.close()

  sys.exit() 

