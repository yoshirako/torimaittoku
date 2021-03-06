#!/bin/bash

echo "Content-type: text/html\n\n"
echo ""

read param

##echo $param

IFS='&='
set -- $param
time=${2}
day=${4}
hour=${6}
sex=${8}
category=${10}

##現在時刻の時の処理
if test ${time} = current ; then
  hour=`date +"%H"`

  get_day=`date +"%w"`
  if [ ${get_day} -ge 1 -a ${get_day} -le 5 ] ; then
    day=WD
  elif [ ${get_day} -eq 0 -o ${get_day} -eq 6 ] ; then
    day=WE
  fi
  ##祝日判定
  chk_holiday=`curl http://s-proj.com/utils/checkHoliday.php`
  if test ${chk_holiday} = holiday ; then
    day=WE
#    echo today is holiday
  fi
fi

##時間帯判定
if [ ${hour} -ge 5 -a ${hour} -le 8 ] ; then
  timezone=MO
elif [ ${hour} -ge 9 -a ${hour} -le 10 ] ; then
  timezone=EA
elif [ ${hour} -ge 11 -a ${hour} -le 13 ] ; then
  timezone=NO
elif [ ${hour} -ge 14 -a ${hour} -le 15 ] ; then
  timezone=AF
elif [ ${hour} -ge 16 -a ${hour} -le 17 ] ; then
  timezone=LA
elif [ ${hour} -ge 18 -a ${hour} -le 20 ] ; then
  timezone=EV
elif [ ${hour} -ge 21 -a ${hour} -le 22 ] ; then
  timezone=NI
elif [ ${hour} -ge 23 -o ${hour} -le 4 ] ; then
  timezone=MI
fi

echo ${sex}${category}${day}${timezone}
code=${sex}${category}${day}${timezone}

python /var/www/cgi-bin/scripts/GnaviAPI.py $code
python /var/www/cgi-bin/scripts/HotpepperAPI.py $code
