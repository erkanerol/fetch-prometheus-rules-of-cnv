#! /usr/bin/python
import copy
import json

import urllib3
from kubernetes import config, client


def fetch_alert_rules():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    config.load_kube_config()
    api = client.CustomObjectsApi()

    response = api.list_namespaced_custom_object(namespace="openshift-cnv", group="monitoring.coreos.com", version="v1", plural="prometheusrules", watch=False)
    return response["items"]


def print_rules_to_file(prometheus_rules):
    f = open("alert-rules-of-cnv.md", "w")
    f.write("# Alerting Rules of OpenShift Virtualization\n")

    for prometheus_rule in prometheus_rules:
        groups = prometheus_rule["spec"]["groups"]

        for group in groups:
            f.write(f'## Group: {group["name"]} \n\n')

            for rule in group["rules"]:
                if "alert" in rule:
                    print_rule = copy.deepcopy(rule)
                    del print_rule["alert"]
                    rule_as_json = json.dumps(print_rule ,indent = 4)
                    f.write(f'#### - Rule: {rule["alert"]}\n')
                    f.write(f'```\n{rule_as_json}\n```\n')

                if "record" in rule:
                    print_rule = copy.deepcopy(rule)
                    del print_rule["record"]
                    rule_as_json = json.dumps(print_rule ,indent = 4)
                    f.write(f'#### - Record: {rule["record"]}\n')
                    f.write(f'```\n{rule_as_json}\n```\n')

    f.close()


if __name__ == "__main__":
    rules = fetch_alert_rules()
    print_rules_to_file(rules)







