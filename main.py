import json
import os
from datetime import datetime

# 1. ตั้งค่าเวลาไทยและข้อมูลผู้สร้าง (สำหรับ Author Tag)
month_th = ["", "มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน", 
            "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"]
now = datetime.now()
date = now.strftime("%d")
mo = int(now.strftime("%m"))
year_th = int(now.strftime("%Y")) + 543
time_now = now.strftime("%H:%M")
timeday = f'วันที่ {date} {month_th[mo]} {year_th} เวลา {time_now}'

# 2. กำหนด Path สำหรับ GitHub Actions หรือ PC ทั่วไป
f_path = "./" 
# กำหนด Dynamic ID สำหรับ URL ทั้งหมด
dynamic_id = "287fe41d125558dc8d5812475124d1f9" # ดึงเฉพาะส่วน ID ที่เหลือมา

def create_smart_w3u(image_urls, save_path):
    # เปลี่ยนชื่อไฟล์ output เป็น luxdo_playlist.w3u
    output_file = os.path.join(save_path, "luxdo_playlist.w3u")

    # Dictionary เก็บ Mapping ระหว่าง "ชื่อช่อง" และ "ลิงก์สตรีม"
    # แก้ไข URL ให้ใช้ dynamic_id ในตำแหน่งที่ถูกต้อง
    stream_mapping = {
        "SPOTV HD": f"https://unpiloted-activism.bitemyshinymetalass.org:9303/v5/MNbehbCqPxpdmQvJndNwyA/1770015914/{dynamic_id}/utSZCMRsV5syriqg-QbUxw/1770026594/live/vx-origin/hd-spotv_720/playlist.m3u8",
        "SPOTV 2 HD": f"https://unpiloted-activism.bitemyshinymetalass.org:9303/v5/dyO1ZtMgbE01E0d22gvM2g/1770015562/{dynamic_id}/MYdazjc1ag4RL4nrQpQPaQ/1770026242/live/vx-origin/hd-spotv2_720/playlist.m3u8",
        "MONOMAX 01": f"https://unpiloted-activism.bitemyshinymetalass.org:9303/v5/zx4_HUIgwZ02j1v-VFAHlw/1770016049/{dynamic_id}/pBETkOAWM1atH1ELXLQmrw/1770026729/live/lx-origin/th-monomax01_720/playlist.m3u8",
        "MONOMAX 02": f"https://monthly-kissable.bitemyshinymetalass.org:9305/v5/ON7BEFgHh4shRdjL3u211g/1770016513/{dynamic_id}/48lsYESJRX-kfqA9gfQGjQ/1770027193/live/lx-origin/th-monomax02_720/playlist.m3u8",
        "MONOMAX 03": f"https://unpiloted-activism.bitemyshinymetalass.org:9303/v5/d7PzmLwamklEblrL7KSf6Q/1770016640/{dynamic_id}/EBQZtcQ77AILv8jPRdyGkw/1770027320/live/lx-origin/th-monomax03_720/playlist.m3u8",
        "MONOMAX 04": f"https://unpiloted-activism.bitemyshinymetalass.org:9303/v5/PkYdRw7A1P-52uogbw3zPA/1770016696/{dynamic_id}/d2iTeejc6lp6Emj8rf3AuQ/1770027376/live/lx-origin/th-monomax04_720/playlist.m3u8",
        "MONOMAX 05": f"https://monthly-kissable.bitemyshinymetalass.org:9305/v5/IgsTKu1adqZsy5buobRqGA/1770016743/{dynamic_id}/9wmGFdi89KRk5Dp8h3LVHA/1770027423/live/lx-origin/th-monomax05_720/playlist.m3u8",
        "MONOMAX 06": f"https://monthly-kissable.bitemyshinymetalass.org:9305/v5/hGZqpjpieugMo-bPkt2E3w/1770016796/{dynamic_id}/qymvcoPrqN2oBctmmb4F6Q/1770027476/live/lx-origin/th-monomax06_720/playlist.m3u8",
        "MONOMAX 07": f"https://unpiloted-activism.bitemyshinymetalass.org:9303/v5/l6Ar-891rqax2P41UOJPdQ/1770017001/{dynamic_id}/jAARSESGG2YQNHKK89BnAA/1770027681/live/lx-origin/th-monomax07_720/playlist.m3u8",
        "MONOMAX 08": f"https://monthly-kissable.bitemyshinymetalass.org:9305/v5/GaVN7Zd9hPqwrPGjNmfgYg/1770016863/{dynamic_id}/iM6hLl9mIA228fDmUb5_kQ/1770027543/live/lx-origin/th-monomax08_720/playlist.m3u8",
        "MONOMAX 09": f"https://monthly-kissable.bitemyshinymetalass.org:9305/v5/CHnS_CGo_v-VjabXwtYUtg/1770016900/{dynamic_id}/4BN2_bM5bjowVKescY_yBA/1770027580/live/lx-origin/th-monomax09_720/playlist.m3u8",
        "MONOMAX 10": f"https://unpiloted-activism.bitemyshinymetalass.org:9303/v5/3d1exY9lEGeIHvo66og88w/1770017093/{dynamic_id}/ClKgQu-5Z1ToSSV2DBWt0g/1770027773/live/lx-origin/th-monomax10_720/playlist.m3u8",
        "TRUESPORTHD 1": f"https://unpiloted-activism.bitemyshinymetalass.org:9303/v5/loqzSYZuO9fUab8aOozmXA/1770017758/{dynamic_id}/TC9NYk_biOP52omg91oqig/1770028438/live/lx-origin/th-tsporthd1_720/playlist.m3u8",
        "TRUESPORTHD 2": f"https://unpiloted-activism.bitemyshinymetalass.org:9303/v5/l5jonZJY88qRbjxMNiefCQ/1770017800/{dynamic_id}/N27GXA8dGAHI9DxuHj4oUg/1770028480/live/lx-origin/th-tsporthd2_720/playlist.m3u8",
        "TRUESPORTHD 3": f"https://unpiloted-activism.bitemyshinymetalass.org:9303/v5/5TE4Usg5BVZI2zzD0cyzwg/1770017834/{dynamic_id}/HQ0fZl_GzKpSQpBsCnxHGA/1770028514/live/lx-origin/th-tsporthd3_720/playlist.m3u8",
        "TRUESPORTHD 4": f"https://monthly-kissable.bitemyshinymetalass.org:9305/v5/iQzZJNiyrY28R0Rkj4Jqjg/1770017868/{dynamic_id}/ksKSd5zO7ZGJTAUaXaoBEw/1770028548/live/lx-origin/hd-tsport4_720/playlist.m3u8",
        "TRUESPORTHD 5": f"https://monthly-kissable.bitemyshinymetalass.org:9305/v5/PO4BOEQ7BGB-wKctKBaLWQ/1770017927/{dynamic_id}/aawY9I0D0sfsZCjojnOT-Q/1770028607/live/vx-origin/sd-tsport5_720/playlist.m3u8",
        "TRUESPORTHD 7": f"https://unpiloted-activism.bitemyshinymetalass.org:9303/v5/Z2F7eTLK8fEDU_3IKpQbxQ/1770017971/{dynamic_id}/jnOuOgcVdwnDGHwDejR4hw/1770028651/live/vx-origin/sd-tsport7_720/playlist.m3u8",
        "BeINSports 1": f"https://unpiloted-activism.bitemyshinymetalass.org:9303/v5/bDAjlNsuGu2pvCA0caTO4Q/1770018074/{dynamic_id}/JWauT3_HETDMjDCqYeDazg/1770028754/live/vx-origin/epl-bein1_720/playlist.m3u8",
        "BeINSports 2": f"https://unpiloted-activism.bitemyshinymetalass.org:9303/v5/tHp9qna5Te_APpTTccxDGQ/1770018103/{dynamic_id}/H93AyDZ9XfjNlMoCVgQldw/1770028783/live/vx-origin/epl-bein2_720/playlist.m3u8",
        "BeINSports 3": f"https://unpiloted-activism.bitemyshinymetalass.org:9303/v5/DcDR4-uPlYVEXIUlf8aBIA/1770018136/{dynamic_id}/5ZAF6_OUnFPFyxWXlonhQQ/1770028816/live/vx-origin/epl-bein3_720/playlist.m3u8",
        "Golf Channel 2": f"https://monthly-kissable.bitemyshinymetalass.org:9305/v5/j_Or2LYsyXO4JL8YzWhgZg/1770018173/{dynamic_id}/IC9mzMLbNC74jYF5KtCMPA/1770028853/live/lx-origin/hd-golf2_720/playlist.m3u8",
        "Tennis Channel": f"https://monthly-kissable.bitemyshinymetalass.org:9305/v5/KnSncEtQkHomzKP2zaDhtQ/1770018225/{dynamic_id}/CNqpfd06-BWY3gBCt_A1SA/1770028905/live/vx-origin/hd-tennis_720/playlist.m3u8",
    }

    # รายชื่อช่องให้ตรงกับลำดับรูปภาพใน image_list
    channel_names = [
        "SPOTV HD", "SPOTV 2 HD", "MONOMAX 01", "MONOMAX 02", "MONOMAX 03",
        "MONOMAX 04", "MONOMAX 05", "MONOMAX 06", "MONOMAX 07", "MONOMAX 08",
        "MONOMAX 09", "MONOMAX 10", "TRUESPORTHD 1", "TRUESPORTHD 2", "TRUESPORTHD 3",
        "TRUESPORTHD 4", "TRUESPORTHD 5", "TRUESPORTHD 7", "BeINSports 1", "BeINSports 2",
        "BeINSports 3", "Golf Channel 2", "Tennis Channel"
    ]

    stations = []
    for name, img_url in zip(channel_names, image_urls):
        stream_url = stream_mapping.get(name, "URL_NOT_FOUND")
        stations.append({"name": name, "image": img_url, "url": stream_url, "referer": ""})

    w3u_data = {
        "name": "My Sport Playlist 2026",
        "author": f"Luxdo update {timeday}",
        "groups": [{"name": "Live Sports", "stations": stations}]
    }

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(w3u_data, f, indent=4, ensure_ascii=False)
    print(f"สร้างไฟล์สำเร็จที่: {output_file}")

# รายการรูปภาพที่คุณระบุ
image_list = [
    "https://api.bitemyshinymetalass.org/images/png/hd-spotv.png",
    "https://api.bitemyshinymetalass.org/images/png/hd-spotv2.png",
    "https://api.bitemyshinymetalass.org/images/png/th-monomax01.png",
    "https://api.icandothisallday.online",
    "https://api.bitemyshinymetalass.org/images/png/th-monomax03.png",
    "https://api.icandothisallday.online/images/png/th-monomax04.png",
    "https://api.icandothisallday.online/images/png/th-monomax05.png",
    "https://api.icandothisallday.online/images/png/th-monomax06.png",
    "https://api.bitemyshinymetalass.org/images/png/th-monomax07.png",
    "https://api.icandothisallday.online/images/png/th-monomax08.png",
    "https://api.icandothisallday.online/images/png/th-monomax09.png",
    "https://api.icandothisallday.online/images/png/th-monomax10.png",
    "https://api.icandothisallday.online/images/png/th-tsporthd1.png",
    "https://api.icandothisallday.online/images/png/th-tsporthd2.png",
    "https://api.icandothisallday.online/images/png/th-tsporthd3.png",
    "https://api.icandothisallday.online/images/png/hd-tsport4.png",
    "https://api.icandothisallday.online/images/png/sd-tsport5.png",
    "https://api.icandothisallday.online/images/png/sd-tsport7.png",
    "https://api.icandothisallday.online/images/png/epl-bein1.png",
    "https://api.icandothisallday.online/images/png/epl-bein2.png",
    "https://api.icandothisallday.online/images/png/epl-bein3.png",
    "https://api.icandothisallday.online/images/png/hd-golf2.png",
    "https://api.icandothisallday.online/images/png/hd-tennis.png",
]

create_smart_w3u(image_list, f_path)
