#!/usr/bin/env python
# -*- coding: utf-8 -*-
#*****************************************************************************************
import sys
import urllib
import json
import cgi
import datetime
import RestSearchAPI2
import HotpepperAPI
import FoursquareAPI

###
# HTML
###
html_body = u"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
  <title>とりま、いっとく君</title>

  <!-- Bootstrap -->
  <link rel="stylesheet" href="../../bootstrap-3.3.6-dist/bootflat.github.io-master/css/bootstrap.min.css">

  <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
  <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
</head>
<!--
<body style="background-color: #ADD5F7;">
-->
<body style="background-color: #F0FFFF;">
  <div class="docs-header">
    <div class="topic" style="background-color: #16193B;">
      <div class="container">
        <div class="col-md-12">
          </br>
          </br>
          </br>
            <b><div style="text-align:center"><font color="white" size="7">とりま、いっとく？（仮）</font></div></b>
          </br>
          </br>
          </br>
        </div>
      </div>
    </div>
  </div>

  <div class="container">
    <div class="row">
      %s
    </div>
  </div>
  </br>
  </br>
  </body>
</html>"""

content=''

form=cgi.FieldStorage()

####
# 変数の型が文字列かどうかチェック
####
def is_str( data = None ) :
  if isinstance( data, str ) or isinstance( data, unicode ) :
    return True
  else :
    return False

####
# 入力フォーム情報読み込み
####

time=form.getvalue('time', '')
hour=form.getvalue('hour', '')
day=form.getvalue('day', '')
sex=form.getvalue('sex', '')
category=form.getvalue('category', '')

if time == "current":
  todaydetail  =    datetime.datetime.today()
  hour = todaydetail.hour
  youbi = todaydetail.isoweekday()
  if youbi >= 1 and youbi <= 5:
    day = "WD"
  else:
    day = "WE"

if time == "select":
  hour=int(hour)


if hour >= 5 and hour <= 8:
  timezone = "MO"
elif hour >= 9 and hour <= 10:
  timezone = "EA"
elif hour >= 11 and hour <= 13:
  timezone = "NO"
elif hour >= 14 and hour <= 15:
  timezone = "AF"
elif hour >= 16 and hour <= 17:
  timezone = "LA"
elif hour >= 18 and hour <= 20:
  timezone = "EV"
elif hour >= 21 and hour <= 22:
  timezone = "NI"
elif hour >= 23 or hour <= 4:
  timezone = "MI"

hour = str(hour)
param_result = sex+category+day+timezone

content+=u"<div class=\"col-md-2\" style=\"margin-top:60px\">"
content+=u"--------------------------------"
content+=u"<br>"
content+=u"時刻取得方法:"
content+=time
content+=u"<br>"
content+=u"検索時刻:"
content+= hour
content+=u"<br>"
content+=u"曜日種別:"
content+=day
content+=u"<br>"
content+=u"性別:"
content+=sex
content+=u"<br>"
content+=u"カテゴリー:"
content+=category
content+=u"<br>"
content+=u"時間帯コード:"
content+=timezone
content+=u"<br>"
content+=u"検索パラメータ:"
content+=param_result
content+=u"<br>"
content+=u"--------------------------------"
content+=u"<br>"
content+=u"<a href=../../index.html>←back</a>"
content+=u"</div>"

content+=u"<div class=\"col-md-1\">"
content+=u"</div>"

##メインコンテンツ
content+=u"<div class=\"col-md-9\" style=\"margin-top:60px\">"

content+=u"<h1>ぐるなび</h1>"
content+=u"<h4>"
content+=RestSearchAPI2.func(param_result)
content+=u"</h4>"

content+=u"<h1>ホットペッパー</h1>"
content+=u"<h4>"
content+=HotpepperAPI.func(param_result)
content+=u"</h4>"

content+=u"<h1>Foursquare</h1>"
content+=u"<h4>"
content+=FoursquareAPI.func(param_result)
content+=u"</h4>"

content+="</div>"

##表示
print (html_body % content).encode('utf-8')

sys.exit()
