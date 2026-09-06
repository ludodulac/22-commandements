#!/usr/bin/env python3
"""Génère le jeu A4 recto-verso des 22 commandements, cartes 80 × 125 mm.
Source canonique: data/commandements.json. Verso: assets/verso-final.png(.base64).
"""
import json, base64, pathlib
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.colors import Color
ROOT=pathlib.Path(__file__).resolve().parents[1]
DATA=ROOT/'data/commandements.json'; ASSET=ROOT/'assets/verso-final.png'; B64=ROOT/'assets/verso-final.png.base64'; OUT=ROOT/'output/22-commandements-80x125-duplex.pdf'
if not ASSET.exists() and B64.exists(): ASSET.write_bytes(base64.b64decode(B64.read_text().strip()))
OUT.parent.mkdir(exist_ok=True); cards=json.loads(DATA.read_text(encoding='utf-8'))
CW,CH=80*mm,125*mm; PW,PH=A4; GAP=4*mm; LEFT=(PW-(2*CW+GAP))/2; BOTTOM=(PH-(2*CH+GAP))/2
BLUE=Color(.30,.52,.73); DARK=Color(.16,.28,.40); SOFT=Color(.55,.68,.78); CUT=Color(.78,.78,.78)
pdfmetrics.registerFont(TTFont('TarotSerif','/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf'))
pdfmetrics.registerFont(TTFont('TarotSerifBold','/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Body','/usr/share/fonts/truetype/lato/Lato-Medium.ttf'))
ROMAN=['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIII','XIV','XV','XVI','XVII','XVIII','XIX','XX','XXI','XXII']
def wrap(text,font,size,width):
    lines=[]; cur=''
    for word in text.split():
        test=word if not cur else cur+' '+word
        if stringWidth(test,font,size)<=width: cur=test
        else:
            if cur: lines.append(cur)
            cur=word
    if cur: lines.append(cur)
    return lines
def drop(c,cx,cy,s):
    # Pointe vers le bas, y compris les deux gouttes du bas.
    p=c.beginPath(); p.moveTo(cx,cy-s*.62); p.curveTo(cx-s*.48,cy-s*.08,cx-s*.40,cy+s*.50,cx,cy+s*.62); p.curveTo(cx+s*.40,cy+s*.50,cx+s*.48,cy-s*.08,cx,cy-s*.62); p.close()
    c.setStrokeColor(BLUE); c.setFillColor(Color(.97,.985,1)); c.setLineWidth(.45); c.drawPath(p,stroke=1,fill=1)
def frame(c,x,y):
    c.setStrokeColor(BLUE); c.setLineWidth(.55); c.roundRect(x+2.1*mm,y+2.1*mm,CW-4.2*mm,CH-4.2*mm,3*mm,stroke=1,fill=0); c.setLineWidth(.22); c.roundRect(x+2.9*mm,y+2.9*mm,CW-5.8*mm,CH-5.8*mm,2.5*mm,stroke=1,fill=0)
    for cx,cy in [(x+6.3*mm,y+CH-6.3*mm),(x+CW-6.3*mm,y+CH-6.3*mm),(x+6.3*mm,y+6.3*mm),(x+CW-6.3*mm,y+6.3*mm)]: drop(c,cx,cy,2.6*mm)
def fit(d):
    inner=64*mm
    for ts in [12.2,11.8,11.4,11,10.6,10.2,9.8,9.4,9.0,8.6]:
        tl=wrap(d['commandement'].upper(),'TarotSerifBold',ts,inner)
        if len(tl)<=9: break
    for bs in [9.45,9.2,9,8.8,8.6,8.4,8.2,8,7.8,7.6,7.4,7.2,7.0]:
        ms=max(8.0,min(10.3,bs+.75)); ml=wrap('« '+d['mantra']+' »','TarotSerif',ms,inner); bl=wrap(d['mouvement'],'Body',bs,inner)
        used=7*mm+len(tl)*ts*1.12+6*mm+len(ml)*ms*1.18+8*mm+len(bl)*bs*1.25
        if used<=96*mm: break
    return ts,ms,bs,tl,ml,bl
def front(c,x,y,d):
    frame(c,x,y); ts,ms,bs,tl,ml,bl=fit(d); inner=64*mm; ix=x+(CW-inner)/2; cx=x+CW/2; yy=y+CH-13*mm
    c.setFillColor(BLUE); c.setFont('TarotSerif',14.5); c.drawCentredString(cx,yy,ROMAN[d['numero']-1]); yy-=7.5*mm
    c.setFillColor(DARK); c.setFont('TarotSerifBold',ts)
    for line in tl: c.drawCentredString(cx,yy,line); yy-=ts*1.12
    yy-=1.5*mm; c.setStrokeColor(SOFT); c.setLineWidth(.35); c.line(cx-12*mm,yy,cx-2.8*mm,yy); drop(c,cx,yy,1.3*mm); c.line(cx+2.8*mm,yy,cx+12*mm,yy); yy-=5.8*mm
    c.setFillColor(BLUE); c.setFont('TarotSerif',ms)
    for line in ml: c.drawCentredString(cx,yy,line); yy-=ms*1.18
    yy-=3.2*mm; c.setFillColor(SOFT); c.setFont('Body',7.3); c.drawCentredString(cx,yy,'MOUVEMENT'); yy-=4.6*mm; c.setFillColor(DARK); c.setFont('Body',bs)
    for line in bl: c.drawString(ix,yy,line); yy-=bs*1.25
def back(c,x,y):
    c.drawImage(str(ASSET),x,y,CW,CH,preserveAspectRatio=False,mask='auto'); c.setStrokeColor(CUT); c.setLineWidth(.22); c.rect(x,y,CW,CH,stroke=1,fill=0)
def positions(): return [(LEFT,BOTTOM+CH+GAP),(LEFT+CW+GAP,BOTTOM+CH+GAP),(LEFT,BOTTOM),(LEFT+CW+GAP,BOTTOM)]
c=canvas.Canvas(str(OUT),pagesize=A4)
for i in range(0,len(cards),4):
    batch=cards[i:i+4]
    for p,d in zip(positions(),batch): front(c,*p,d)
    c.showPage()
    for p in positions()[:len(batch)]: back(c,*p)
    c.showPage()
c.save(); print(OUT)
