#!/usr/bin/env python3
import sys, sxtwl
from datetime import datetime
Gan = ["甲","乙","丙","丁","戊","己","庚","辛","壬","癸"]
Zhi = ["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]
if len(sys.argv) < 2: print("用法: bazi 'YYYY-MM-DD HH:MM'"); sys.exit(1)
dt = datetime.strptime(sys.argv[1], "%Y-%m-%d %H:%M")
day = sxtwl.fromSolar(dt.year, dt.month, dt.day)
y, m, d, h = day.getYearGZ(), day.getMonthGZ(), day.getDayGZ(), day.getHourGZ(dt.hour)
print(f"{Gan[y.tg]}{Zhi[y.dz]} {Gan[m.tg]}{Zhi[m.dz]} {Gan[d.tg]}{Zhi[d.dz]} {Gan[h.tg]}{Zhi[h.dz]}")













