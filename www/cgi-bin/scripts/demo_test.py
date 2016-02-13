#!/usr/bin/env python
# -*- coding: utf-8 -*-
#*****************************************************************************************
import sys
import urllib
import json
import cgi
import datetime
import RestSearchAPI
import HotpepperAPI
import FoursquareAPI
#import get_geocode

###
# HTML
###
html_body = u"""
<div class="container">
<div class="row wow fadeInUp">
      %s
</div>
</div>
  <script type="text/javascript">
  $(document).ready(function()
    {
        $("#result_tb").tablesorter({
          sortList:[[2,0]],
          widgets: ['zebra'],
          widgetOptions : {
            zebra : [ "normal-row", "alt-row" ]
          }
        });
    }
  );
  </script>
  <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery.tablesorter/2.25.1/js/jquery.tablesorter.js" ></script>
  <script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
"""

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
#address=form.getvalue(u'address', '')

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

#latlng=get_geocode.adr2geo(address)
#lat=latlng[0]
#lng=latlng[1]

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
content+=u"<div class=\"col-md-8\">"

#content+=u"<table id=\"result_tb\" class=\"tablesorter\" bgcolor=\"#ffffff\">"

content+=u"<table style=\"font-size:20px;\" id=\"result_tb\" class=\"tablesorter\" bgcolor=\"#ffd5ea\">"

content+=u"<thead>"
content+=u"<tr>"

content+=u"<th class=\"header headerSortUp\">店名</th>"
content+=u"<th class=\"header\">カテゴリ</th>"
content+=u"<th class=\"header\"></th>"
content+=u"<th class=\"header\">ソース</th>"

content+=u"</tr>"
content+=u"</thead>"

content+=u"<tbody>"
content+=RestSearchAPI.func(param_result)
content+=HotpepperAPI.func(param_result)
content+=FoursquareAPI.func(param_result)

content+=u"</tbody>"
content+=u"</table>"
content+=u"</div>"

##表示
print (html_body % content).encode('utf-8')

sys.exit()
