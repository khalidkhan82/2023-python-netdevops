
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get

import os

nr = InitNornir((config_file="../config.yaml")

task = napalm_get
getters = ["get_lldp_neighbors"]

results = nr.run(task=task, getters=getters)

print_result(results)