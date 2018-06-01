from pyzabbix import ZabbixAPI
from st2common.runners.base_action import Action
import json


class ZabbixHost(Action):
    def run(self):
        zapi = ZabbixAPI(self.config['zabbix']['url'])
        zapi.login(self.config['zabbix']['username'],self.config['zabbix']['password'])
        ret = zapi.do_request('host.get',{"output":["host"]})
        data = []
        for i in ret['result']:
             data.append(i['host'])
        return sorted(data)

