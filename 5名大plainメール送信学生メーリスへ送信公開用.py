# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 16:39:36 2020
"""


from email.mime.text import MIMEText
import smtplib

# SMTP認証情報
account = "yamada.hideyuki@i.mbox.nagoya-u.ac.jp"
password = "自分のパスワード"

# 送信先
to_email = "yamada.hideyuki@i.mbox.nagoya-u.ac.jp"
# 送信元 基本accountと同じ
from_email = "yamada.hideyuki@i.mbox.nagoya-u.ac.jp"

# 件名を変数に格納しておく
subject = "研究室の掃除リマインダー Remider of laboratory cleanig"
# 本文をhtmlで書いて変数に格納しておく
message = \
"巨研の皆様お世話になります．\n掃除係のM1山田です．\n \n明日の13時から，研究室の掃除があります．\n \n時間までに，入口すぐのホワイトボードの出欠表にて\nマグネットを研究室の位置へ動かしてください．\n \nよろしくお願いします．\n \nDear all\nThis is Hideyuki Yamada, the cleanning maneger.\n \nLaboratory cleaning will start from 13:00 tommorow .\n \nBy the time, at the attendance table on the entrance whiteboard\nPlease, move your magnet to the lab position\n \nThank you. "

# MINETEXTオブジェクトを作製して，扱いやすいようにmsg変数の中に格納しておく
msg = MIMEText(message, "plain")
# 実際に変数に入れてた件名，送信先，送信元，を辞書型のmsgに指定する
msg["Subject"] = subject
msg["To"] = to_email
msg["From"] = from_email

# メール送信処理
# 実際にポート番号を指定して，メール送信用のオブジェクトを作成する
server = smtplib.SMTP("mail.i.mbox.nagoya-u.ac.jp", 587)
# デバッグ用にログを出力させる
# server.set_debuglevel(True)
# メールシステムサーバーにログインする
server.starttls()
server.login(account, password)
# メールを送信する
server.send_message(msg)
# 送信した文章を確認する
print(msg)
# サーバーへからログアウトする
server.quit()
