import subprocess
import platform


def ping_ip(mevcut_ip_adresi):
    try:
        output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower(
        ) == "windows" else 'c', mevcut_ip_adresi), shell=True, universal_newlines=True)
        if 'unreachable' in output:
            return False
        else:
            return True
    except Exception:
        return False


if __name__ == '__main__':
    mevcut_ip_adresi = ['185.203.171.50', '185.106.211.101', '157.240.27.45']
    for each in mevcut_ip_adresi:
        if ping_ip(each):
            print(f"{each} adresine ping atıldı")
        else:
            print(f"{each} adresine ping atılamadı")