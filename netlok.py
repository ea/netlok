import rumps
import subprocess
import requests
import time

def get_cmd_output(cmd):
    return subprocess.check_output(cmd,encoding="utf-8")

def get_net_locations():
    return get_cmd_output(["networksetup","-listlocations"]).split("\n")[:-1]
def get_current_location():
    return get_cmd_output(["networksetup","-getcurrentlocation"]).strip()

def get_public_ip():
    r = requests.get(url='https://serverstatus.apple.com/services/internetaccess/v1/my_external_ip')
    if r.ok:
        return r.json()['ip']
    else:
        return 'None'

class NetlokApp(object):
    def __init__(self):
        self.app = rumps.App("Netlok", f"{get_current_location()} : {get_public_ip()}")
        self.lok_buttons = []
        self.timer = rumps.Timer(self.update,5)
    def run(self):
        self.make_buttons()
        self.app.run()
    def make_buttons(self):
        for l in get_net_locations():
            self.lok_buttons.append(rumps.MenuItem(title=l,callback=self.switch_location))
        self.app.menu = self.lok_buttons

    def switch_location(self,sender):
        get_cmd_output(["networksetup","-switchtolocation", sender.title])
        app.timer.start()

    def update(self,sender):
        self.app.title = f"{get_current_location()} : {get_public_ip()}"
        self.timer.stop()
if __name__ == '__main__':
    app = NetlokApp()
    app.run()
    print("Hello")
