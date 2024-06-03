import ipaddress, platform, subprocess, os, datetime, base64

def warp_ip():
    creation_time = os.path.getctime(result_path)
    formatted_time = datetime.datetime.fromtimestamp(creation_time).strftime("%Y-%m-%d %H:%M:%S")
    for i, ip in enumerate(Bestip):
        config_prefix = f'warp://{Bestip[0]}?ifp=10-20&ifps=20-60&ifpd=5-10#@mansor427🇮🇷&&detour=warp://{Bestip[1]}?ifp=10-20&ifps=20-60&ifpd=5-10#ÐΛɌ₭ᑎΞ𐒡𐒡🇩🇪WoW'
    return config_prefix, formatted_time


title = "//profile-title: base64:" + base64.b64encode('ʷᵃʳᵖ〘⬳𓄂𓆃⟿〙ʷᵃʳᵖ'.encode('utf-8')).decode('utf-8') + "\n"
update_interval = "//profile-update-interval: 1\n"
sub_info = "//subscription-userinfo: upload=0; download=0; total=10737418240000000; expire=2546249531\n"
profile_web = "//profile-web-page-url: https://github.com/mansor427\n"
last_modified = "//last update on: " + warp_ip()[1] + "\n"
configs = warp_ip()[0]
with open('warp.json', 'w') as op:
    op.write(title + update_interval + sub_info + profile_web  + last_modified + configs)

with open('Bestip.txt', 'w') as f:
    for ip in Bestip:
        f.write(f"{ip}\n")

os.remove(cfw_ips_txt_path)
os.remove(result_path)
os.remove("warp")
