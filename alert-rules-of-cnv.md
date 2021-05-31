# Alerting Rules of OpenShift Virtualization
## Group: kubevirt.hyperconverged.rules 

### Alerting Rule: `KubevirtHyperconvergedClusterOperatorCRModification`

***Summary:***

{{ $value }} out-of-band CR modifications were detected in the last 10 minutes.

***Description:***

Out-of-band modification for {{ $labels.component_name }} .

***Expression:***
```
sum by(component_name) ((round(increase(kubevirt_hco_out_of_band_modifications_count[10m]))>0 and kubevirt_hco_out_of_band_modifications_count offset 10m) or (kubevirt_hco_out_of_band_modifications_count != 0 unless kubevirt_hco_out_of_band_modifications_count offset 10m))
```
***Labels:***

- severity=warning

***Severity:*** ```warning```


---

## Group: cnv.rules 

### Record: `cnv:vmi_status_running:count`
```
sum(kubevirt_vmi_phase_count{phase="running"}) by (node,os,workload,flavor)
```
<br><br>


---

## Group: kubevirt.rules 

### Record: `kubevirt_virt_api_up_total`
```
sum(up{namespace='openshift-cnv', pod=~'virt-api-.*'})
```
<br><br>


---

### Record: `num_of_allocatable_nodes`
```
count(count (kube_node_status_allocatable) by (node))
```
<br><br>


---

### Record: `num_of_kvm_available_nodes`
```
num_of_allocatable_nodes - count(kube_node_status_allocatable{resource="devices_kubevirt_io_kvm"} == 0)
```
<br><br>


---

### Record: `kubevirt_virt_controller_up_total`
```
sum(up{pod=~'virt-controller-.*', namespace='openshift-cnv'})
```
<br><br>


---

### Record: `kubevirt_virt_controller_ready_total`
```
sum(kubevirt_virt_controller_ready{namespace='openshift-cnv'})
```
<br><br>


---

### Record: `vec_by_virt_controllers_all_client_rest_requests_in_last_hour`
```
sum by (pod) (sum_over_time(rest_client_requests_total{pod=~'virt-controller-.*', namespace='openshift-cnv'}[60m]))
```
<br><br>


---

### Record: `vec_by_virt_controllers_failed_client_rest_requests_in_last_hour`
```
sum by (pod) (sum_over_time(rest_client_requests_total{pod=~'virt-controller-.*', namespace='openshift-cnv', code=~'(4|5)[0-9][0-9]'}[60m]))
```
<br><br>


---

### Record: `vec_by_virt_controllers_all_client_rest_requests_in_last_5m`
```
sum by (pod) (sum_over_time(rest_client_requests_total{pod=~'virt-controller-.*', namespace='openshift-cnv'}[5m]))
```
<br><br>


---

### Record: `vec_by_virt_controllers_failed_client_rest_requests_in_last_5m`
```
sum by (pod) (sum_over_time(rest_client_requests_total{pod=~'virt-controller-.*', namespace='openshift-cnv', code=~'(4|5)[0-9][0-9]'}[5m]))
```
<br><br>


---

### Record: `kubevirt_virt_operator_up_total`
```
sum(up{namespace='openshift-cnv', pod=~'virt-operator-.*'})
```
<br><br>


---

### Record: `vec_by_virt_operators_all_client_rest_requests_in_last_hour`
```
sum by (pod) (sum_over_time(rest_client_requests_total{pod=~'virt-operator-.*', namespace='openshift-cnv'}[60m]))
```
<br><br>


---

### Record: `vec_by_virt_operators_failed_client_rest_requests_in_last_hour`
```
sum by (pod) (sum_over_time(rest_client_requests_total{pod=~'virt-operator-.*', namespace='openshift-cnv', code=~'(4|5)[0-9][0-9]'}[60m]))
```
<br><br>


---

### Record: `vec_by_virt_operators_all_client_rest_requests_in_last_5m`
```
sum by (pod) (sum_over_time(rest_client_requests_total{pod=~'virt-operator-.*', namespace='openshift-cnv'}[5m]))
```
<br><br>


---

### Record: `vec_by_virt_operators_failed_client_rest_requests_in_last_5m`
```
sum by (pod) (sum_over_time(rest_client_requests_total{pod=~'virt-operator-.*', namespace='openshift-cnv', code=~'(4|5)[0-9][0-9]'}[5m]))
```
<br><br>


---

### Record: `kubevirt_virt_operator_ready_total`
```
sum(kubevirt_virt_operator_ready{namespace='openshift-cnv'})
```
<br><br>


---

### Record: `kubevirt_virt_operator_leading_total`
```
sum(kubevirt_virt_operator_leading{namespace='openshift-cnv'})
```
<br><br>


---

### Record: `kubevirt_virt_handler_up_total`
```
sum(up{pod=~'virt-handler-.*', namespace='openshift-cnv'})
```
<br><br>


---

### Record: `vec_by_virt_handlers_all_client_rest_requests_in_last_5m`
```
sum by (pod) (sum_over_time(rest_client_requests_total{pod=~'virt-handler-.*', namespace='openshift-cnv'}[5m]))
```
<br><br>


---

### Record: `vec_by_virt_handlers_all_client_rest_requests_in_last_hour`
```
sum by (pod) (sum_over_time(rest_client_requests_total{pod=~'virt-handler-.*', namespace='openshift-cnv'}[60m]))
```
<br><br>


---

### Record: `vec_by_virt_handlers_failed_client_rest_requests_in_last_5m`
```
sum by (pod) (sum_over_time(rest_client_requests_total{pod=~'virt-handler-.*', namespace='openshift-cnv', code=~'(4|5)[0-9][0-9]'}[5m]))
```
<br><br>


---

### Record: `vec_by_virt_handlers_failed_client_rest_requests_in_last_hour`
```
sum by (pod) (sum_over_time(rest_client_requests_total{pod=~'virt-handler-.*', namespace='openshift-cnv', code=~'(4|5)[0-9][0-9]'}[60m]))
```
<br><br>


---

### Record: `kubevirt_vm_container_free_memory_bytes`
```
sum by(pod, container) ( kube_pod_container_resource_limits_memory_bytes{pod=~'virt-launcher-.*', container='compute'} - on(pod,container) container_memory_working_set_bytes{pod=~'virt-launcher-.*', container='compute'})
```
<br><br>


---

### Record: `kubevirt_num_virt_handlers_by_node_running_virt_launcher`
```
count by(node)(node_namespace_pod:kube_pod_info:{pod=~'virt-launcher-.*'} ) * on (node) group_left(pod) (1*(kube_pod_container_status_ready{pod=~'virt-handler-.*'} + on (pod) group_left(node) (0 * node_namespace_pod:kube_pod_info:{pod=~'virt-handler-.*'} ))) or on (node) (0 * node_namespace_pod:kube_pod_info:{pod=~'virt-launcher-.*'} )
```
<br><br>


---

### Alerting Rule: `VirtAPIDown`

***Summary:***

All virt-api servers are down.

***Expression:***
```
kubevirt_virt_api_up_total == 0
```
***For:*** ```5m```



---

### Alerting Rule: `LowVirtAPICount`

***Summary:***

More than one virt-api should be running if more than one worker nodes exist.

***Expression:***
```
(num_of_allocatable_nodes > 1) and (kubevirt_virt_api_up_total < 2)
```
***For:*** ```60m```



---

### Alerting Rule: `LowKVMNodesCount`

***Summary:***

At least two nodes with kvm resource required for VM life migration.

***Description:***

Low number of nodes with KVM resource available.

***Expression:***
```
(num_of_allocatable_nodes > 1) and (num_of_kvm_available_nodes < 2)
```
***For:*** ```5m```

***Labels:***

- severity=warning

***Severity:*** ```warning```


---

### Alerting Rule: `LowReadyVirtControllersCount`

***Summary:***

Some virt controllers are running but not ready.

***Expression:***
```
kubevirt_virt_controller_ready_total <  kubevirt_virt_controller_up_total
```
***For:*** ```5m```



---

### Alerting Rule: `NoReadyVirtController`

***Summary:***

No ready virt-controller was detected for the last 5 min.

***Expression:***
```
kubevirt_virt_controller_ready_total == 0
```
***For:*** ```5m```



---

### Alerting Rule: `VirtControllerDown`

***Summary:***

No running virt-controller was detected for the last 5 min.

***Expression:***
```
kubevirt_virt_controller_up_total == 0
```
***For:*** ```5m```



---

### Alerting Rule: `LowVirtControllersCount`

***Summary:***

More than one virt-controller should be ready if more than one worker node.

***Expression:***
```
(num_of_allocatable_nodes > 1) and (kubevirt_virt_controller_ready_total < 2)
```
***For:*** ```5m```



---

### Alerting Rule: `VirtControllerRESTErrorsHigh`

***Summary:***

More than 5% of the rest calls failed in virt-controller for the last hour

***Expression:***
```
(vec_by_virt_controllers_failed_client_rest_requests_in_last_hour / vec_by_virt_controllers_all_client_rest_requests_in_last_hour) >= 0.05
```
***For:*** ```5m```



---

### Alerting Rule: `VirtControllerRESTErrorsBurst`

***Summary:***

More than 80% of the rest calls failed in virt-controller for the last 5 minutes

***Expression:***
```
(vec_by_virt_controllers_failed_client_rest_requests_in_last_5m / vec_by_virt_controllers_all_client_rest_requests_in_last_5m) >= 0.8
```
***For:*** ```5m```



---

### Alerting Rule: `VirtOperatorDown`

***Summary:***

All virt-operator servers are down.

***Expression:***
```
kubevirt_virt_operator_up_total == 0
```
***For:*** ```5m```



---

### Alerting Rule: `LowVirtOperatorCount`

***Summary:***

More than one virt-operator should be running if more than one worker nodes exist.

***Expression:***
```
(num_of_allocatable_nodes > 1) and (kubevirt_virt_operator_up_total < 2)
```
***For:*** ```60m```



---

### Alerting Rule: `VirtOperatorRESTErrorsHigh`

***Summary:***

More than 5% of the rest calls failed in virt-operator for the last hour

***Expression:***
```
(vec_by_virt_operators_failed_client_rest_requests_in_last_hour / vec_by_virt_operators_all_client_rest_requests_in_last_hour) >= 0.05
```
***For:*** ```5m```



---

### Alerting Rule: `VirtOperatorRESTErrorsBurst`

***Summary:***

More than 80% of the rest calls failed in virt-operator for the last 5 minutes

***Expression:***
```
(vec_by_virt_operators_failed_client_rest_requests_in_last_5m / vec_by_virt_operators_all_client_rest_requests_in_last_5m) >= 0.8
```
***For:*** ```5m```



---

### Alerting Rule: `LowReadyVirtOperatorsCount`

***Summary:***

Some virt-operators are running but not ready.

***Expression:***
```
kubevirt_virt_operator_ready_total <  kubevirt_virt_operator_up_total
```
***For:*** ```5m```



---

### Alerting Rule: `NoReadyVirtOperator`

***Summary:***

No ready virt-operator was detected for the last 5 min.

***Expression:***
```
kubevirt_virt_operator_up_total == 0
```
***For:*** ```5m```



---

### Alerting Rule: `NoLeadingVirtOperator`

***Summary:***

No leading virt-operator was detected for the last 5 min.

***Expression:***
```
kubevirt_virt_operator_leading_total == 0
```
***For:*** ```5m```



---

### Alerting Rule: `VirtHandlerDaemonSetRolloutFailing`

***Summary:***

Some virt-handlers failed to roll out

***Expression:***
```
(kube_daemonset_status_number_ready{namespace='openshift-cnv', daemonset='virt-handler'} - kube_daemonset_status_desired_number_scheduled{namespace='openshift-cnv', daemonset='virt-handler'}) != 0
```
***For:*** ```15m```



---

### Alerting Rule: `VirtHandlerRESTErrorsHigh`

***Summary:***

More than 5% of the rest calls failed in virt-handler for the last hour

***Expression:***
```
(vec_by_virt_handlers_failed_client_rest_requests_in_last_hour / vec_by_virt_handlers_all_client_rest_requests_in_last_hour) >= 0.05
```
***For:*** ```5m```



---

### Alerting Rule: `VirtHandlerRESTErrorsBurst`

***Summary:***

More than 80% of the rest calls failed in virt-handler for the last 5 minutes

***Expression:***
```
(vec_by_virt_handlers_failed_client_rest_requests_in_last_5m / vec_by_virt_handlers_all_client_rest_requests_in_last_5m) >= 0.8
```
***For:*** ```5m```



---

### Alerting Rule: `KubevirtVmHighMemoryUsage`

***Summary:***

VM is at risk of being terminated by the runtime.

***Description:***

Container {{ $labels.container }} in pod {{ $labels.pod }} free memory is less than 20 MB and it is close to memory limit

***Expression:***
```
kubevirt_vm_container_free_memory_bytes < 20971520
```
***For:*** ```1m```

***Labels:***

- severity=warning

***Severity:*** ```warning```


---

### Alerting Rule: `OrphanedVirtualMachineImages`

***Summary:***

No virt-handler pod detected on node {{ $labels.node }} with running vmis for more than an hour

***Expression:***
```
(kubevirt_num_virt_handlers_by_node_running_virt_launcher) == 0
```
***For:*** ```60m```

***Labels:***

- severity=warning

***Severity:*** ```warning```


---

### Alerting Rule: `VMCannotBeEvicted`

***Summary:***

The VM's eviction strategy is set to Live Migration but the VM is not migratable

***Description:***

Eviction policy for {{ $labels.name }} (on node {{ $labels.node }}) is set to Live Migration but the VM is not migratable

***Expression:***
```
kubevirt_vmi_non_evictable > 0
```
***For:*** ```1m```

***Labels:***

- severity=warning

***Severity:*** ```warning```


---

