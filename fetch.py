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

            alerting_rules = []
            records = []

            for rule in group["rules"]:
                if "alert" in rule:
                    alerting_rules.append(rule)
                if "record" in rule:
                    records.append(rule)

            if len(records) > 0:
                for record in records:
                    f.write(f'### Record: `{record["record"]}`\n')
                    f.write(f'```\n{record["expr"]}\n```\n')
                    f.write("<br><br>\n")
                    f.write("\n\n---\n\n")

            if len(alerting_rules) > 0:
                for alerting_rule in alerting_rules:
                    f.write(f'### Alerting Rule: `{alerting_rule["alert"]}`\n\n')

                    if "annotations" in alerting_rule:
                        if "summary" in alerting_rule["annotations"]:
                            f.write(f'***Summary:***\n\n{alerting_rule["annotations"]["summary"]}\n\n')
                        if "description" in alerting_rule["annotations"]:
                            f.write(f'***Description:***\n\n{alerting_rule["annotations"]["description"]}\n\n')

                    f.write(f'***Expression:***\n```\n{alerting_rule["expr"]}\n```\n')

                    if "for" in alerting_rule:
                        f.write(f'***For:*** ```{alerting_rule["for"]}```\n\n')

                    if "labels" in alerting_rule:
                        f.write(f'***Labels:***\n\n')
                        for label in alerting_rule["labels"]:
                            f.write(f'- {label}={alerting_rule["labels"][label]}\n')
                        f.write(f'\n')

                        if "severity" in alerting_rule["labels"]:
                           f.write(f'***Severity:*** ```{alerting_rule["labels"]["severity"]}```\n')

                    f.write("\n\n---\n\n")

    f.close()


if __name__ == "__main__":
    rules = fetch_alert_rules()
    print_rules_to_file(rules)







