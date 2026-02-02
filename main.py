import json
import os
from datetime import datetime

# 1. ตั้งค่าเวลาไทย (GitHub Actions ใช้เวลา UTC ต้องบวก 7 ชั่วโมง หรือใช้ Format ปกติ)
month_th = ["", "มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน", 
            "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"]
now = datetime.now()
date = now.strftime("%d")
mo = int(now.strftime("%m"))
year_th = int(now.strftime("%Y")) + 543
time_now = now.strftime("%H:%M")
timeday = f'วันที่ {date} {month_th[mo]} {year_th} เวลา {time_now}'

# 2. กำหนด Path สำหรับ GitHub (บันทึกในโฟลเดอร์เดียวกับโค้ด)
f_path = "./" 
dynamic_id = "1770015914/287fe41d125558dc8d5812475124d1f9"

def create_smart_w3u(image_urls, save_path):
    output_file = os.path.join(save_path, "playlist.w3u")
    
    # ... (ส่วน stream_mapping และ channel_names เหมือนเดิมของคุณ) ...
    stream_mapping = {
        "SPOTV HD": f"https://unpiloted-activism.bitemyshinymetalass.org{dynamic_id}/utSZCMRsV5syriqg-QbUxw/1770026594/live/vx-origin/hd-spotv_720/playlist.m3u8",
        # เพิ่มช่องอื่นๆ ให้ครบตามที่คุณเขียนไว้
    }
    channel_names = ["SPOTV HD", "SPOTV 2 HD", "MONOMAX 01"] # แก้ให้ครบ 23 ช่อง

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

# เรียกใช้งาน
image_list = ["https://api.bitemyshinymetalass.org", "https://api.bitemyshinymetalass.org", "https://api.bitemyshinymetalass.org"] # ใส่ให้ครบ
create_smart_w3u(image_list, f_path)
