# Alerting Rules of OpenShift Virtualization
## Group: kubevirt.hyperconverged.rules 

#### - Rule: KubevirtHyperconvergedClusterOperatorCRModification
```
{
    "annotations": {
        "description": "Out-of-band modification for {{ $labels.component_name }} .",
        "summary": "{{ $value }} out-of-band CR modifications were detected in the last 10 minutes."
    },
    "expr": "sum by(component_name) ((round(increase(kubevirt_hco_out_of_band_modifications_count[10m]))>0 and kubevirt_hco_out_of_band_modifications_count offset 10m) or (kubevirt_hco_out_of_band_modifications_count != 0 unless kubevirt_hco_out_of_band_modifications_count offset 10m))",
    "labels": {
        "severity": "warning"
    }
}
```
## Group: cnv.rules 

#### - Record: cnv:vmi_status_running:count
```
{
    "expr": "sum(kubevirt_vmi_phase_count{phase=\"running\"}) by (node,os,workload,flavor)"
}
```
## Group: kubevirt.rules 

#### - Record: kubevirt_virt_api_up_total
```
{
    "expr": "sum(up{namespace='openshift-cnv', pod=~'virt-api-.*'})"
}
```
#### - Rule: VirtAPIDown
```
{
    "annotations": {
        "summary": "All virt-api servers are down."
    },
    "expr": "kubevirt_virt_api_up_total == 0",
    "for": "5m"
}
```
#### - Record: num_of_allocatable_nodes
```
{
    "expr": "count(count (kube_node_status_allocatable) by (node))"
}
```
#### - Rule: LowVirtAPICount
```
{
    "annotations": {
        "summary": "More than one virt-api should be running if more than one worker nodes exist."
    },
    "expr": "(num_of_allocatable_nodes > 1) and (kubevirt_virt_api_up_total < 2)",
    "for": "60m"
}
```
#### - Record: num_of_kvm_available_nodes
```
{
    "expr": "num_of_allocatable_nodes - count(kube_node_status_allocatable{resource=\"devices_kubevirt_io_kvm\"} == 0)"
}
```
#### - Rule: LowKVMNodesCount
```
{
    "annotations": {
        "description": "Low number of nodes with KVM resource available.",
        "summary": "At least two nodes with kvm resource required for VM life migration."
    },
    "expr": "(num_of_allocatable_nodes > 1) and (num_of_kvm_available_nodes < 2)",
    "for": "5m",
    "labels": {
        "severity": "warning"
    }
}
```
#### - Record: kubevirt_virt_controller_up_total
```
{
    "expr": "sum(up{pod=~'virt-controller-.*', namespace='openshift-cnv'})"
}
```
#### - Record: kubevirt_virt_controller_ready_total
```
{
    "expr": "sum(kubevirt_virt_controller_ready{namespace='openshift-cnv'})"
}
```
#### - Rule: LowReadyVirtControllersCount
```
{
    "annotations": {
        "summary": "Some virt controllers are running but not ready."
    },
    "expr": "kubevirt_virt_controller_ready_total <  kubevirt_virt_controller_up_total",
    "for": "5m"
}
```
#### - Rule: NoReadyVirtController
```
{
    "annotations": {
        "summary": "No ready virt-controller was detected for the last 5 min."
    },
    "expr": "kubevirt_virt_controller_ready_total == 0",
    "for": "5m"
}
```
#### - Rule: VirtControllerDown
```
{
    "annotations": {
        "summary": "No running virt-controller was detected for the last 5 min."
    },
    "expr": "kubevirt_virt_controller_up_total == 0",
    "for": "5m"
}
```
#### - Rule: LowVirtControllersCount
```
{
    "annotations": {
        "summary": "More than one virt-controller should be ready if more than one worker node."
    },
    "expr": "(num_of_allocatable_nodes > 1) and (kubevirt_virt_controller_ready_total < 2)",
    "for": "5m"
}
```
#### - Record: vec_by_virt_controllers_all_client_rest_requests_in_last_hour
```
{
    "expr": "sum by (pod) (sum_over_time(rest_client_requests_total{pod=~'virt-controller-.*', namespace='openshift-cnv'}[60m]))"
}
```
#### - Record: vec_by_virt_controllers_failed_client_rest_requests_in_last_hour
```
{
    "expr": "sum by (pod) (sum_over_time(rest_client_requests_total{pod=~'virt-controller-.*', namespace='openshift-cnv', code=~'(4|5)[0-9][0-9]'}[60m]))"
}
```
#### - Record: vec_by_virt_controllers_all_client_rest_requests_in_last_5m
```
{
    "expr": "sum by (pod) (sum_over_time(rest_client_requests_total{pod=~'virt-controller-.*', namespace='openshift-cnv'}[5m]))"
}
```
#### - Record: vec_by_virt_controllers_failed_client_rest_requests_in_last_5m
```
{
    "expr": "sum by (pod) (sum_over_time(rest_client_requests_total{pod=~'virt-controller-.*', namespace='openshift-cnv', code=~'(4|5)[0-9][0-9]'}[5m]))"
}
```
#### - Rule: VirtControllerRESTErrorsHigh
```
{
    "annotations": {
        "summary": "More than 5% of the rest calls failed in virt-controller for the last hour"
    },
    "expr": "(vec_by_virt_controllers_failed_client_rest_requests_in_last_hour / vec_by_virt_controllers_all_client_rest_requests_in_last_hour) >= 0.05",
    "for": "5m"
}
```
#### - Rule: VirtControllerRESTErrorsBurst
```
{
    "annotations": {
        "summary": "More than 80% of the rest calls failed in virt-controller for the last 5 minutes"
    },
    "expr": "(vec_by_virt_controllers_failed_client_rest_requests_in_last_5m / vec_by_virt_controllers_all_client_rest_requests_in_last_5m) >= 0.8",
    "for": "5m"
}
```
#### - Record: kubevirt_virt_operator_up_total
```
{
    "expr": "sum(up{namespace='openshift-cnv', pod=~'virt-operator-.*'})"
}
```
#### - Rule: VirtOperatorDown
```
{
    "annotations": {
        "summary": "All virt-operator servers are down."
    },
    "expr": "kubevirt_virt_operator_up_total == 0",
    "for": "5m"
}
```
#### - Rule: LowVirtOperatorCount
```
{
    "annotations": {
        "summary": "More than one virt-operator should be running if more than one worker nodes exist."
    },
    "expr": "(num_of_allocatable_nodes > 1) and (kubevirt_virt_operator_up_total < 2)",
    "for": "60m"
}
```
#### - Record: vec_by_virt_operators_all_client_rest_requests_in_last_hour
```
{
    "expr": "sum by (pod) (sum_over_time(rest_client_requests_total{pod=~'virt-operator-.*', namespace='openshift-cnv'}[60m]))"
}
```
#### - Record: vec_by_virt_operators_failed_client_rest_requests_in_last_hour
```
{
    "expr": "sum by (pod) (sum_over_time(rest_client_requests_total{pod=~'virt-operator-.*', namespace='openshift-cnv', code=~'(4|5)[0-9][0-9]'}[60m]))"
}
```
#### - Record: vec_by_virt_operators_all_client_rest_requests_in_last_5m
```
{
    "expr": "sum by (pod) (sum_over_time(rest_client_requests_total{pod=~'virt-operator-.*', namespace='openshift-cnv'}[5m]))"
}
```
#### - Record: vec_by_virt_operators_failed_client_rest_requests_in_last_5m
```
{
    "expr": "sum by (pod) (sum_over_time(rest_client_requests_total{pod=~'virt-operator-.*', namespace='openshift-cnv', code=~'(4|5)[0-9][0-9]'}[5m]))"
}
```
#### - Rule: VirtOperatorRESTErrorsHigh
```
{
    "annotations": {
        "summary": "More than 5% of the rest calls failed in virt-operator for the last hour"
    },
    "expr": "(vec_by_virt_operators_failed_client_rest_requests_in_last_hour / vec_by_virt_operators_all_client_rest_requests_in_last_hour) >= 0.05",
    "for": "5m"
}
```
#### - Rule: VirtOperatorRESTErrorsBurst
```
{
    "annotations": {
        "summary": "More than 80% of the rest calls failed in virt-operator for the last 5 minutes"
    },
    "expr": "(vec_by_virt_operators_failed_client_rest_requests_in_last_5m / vec_by_virt_operators_all_client_rest_requests_in_last_5m) >= 0.8",
    "for": "5m"
}
```
#### - Record: kubevirt_virt_operator_ready_total
```
{
    "expr": "sum(kubevirt_virt_operator_ready{namespace='openshift-cnv'})"
}
```
#### - Record: kubevirt_virt_operator_leading_total
```
{
    "expr": "sum(kubevirt_virt_operator_leading{namespace='openshift-cnv'})"
}
```
#### - Rule: LowReadyVirtOperatorsCount
```
{
    "annotations": {
        "summary": "Some virt-operators are running but not ready."
    },
    "expr": "kubevirt_virt_operator_ready_total <  kubevirt_virt_operator_up_total",
    "for": "5m"
}
```
#### - Rule: NoReadyVirtOperator
```
{
    "annotations": {
        "summary": "No ready virt-operator was detected for the last 5 min."
    },
    "expr": "kubevirt_virt_operator_up_total == 0",
    "for": "5m"
}
```
#### - Rule: NoLeadingVirtOperator
```
{
    "annotations": {
        "summary": "No leading virt-operator was detected for the last 5 min."
    },
    "expr": "kubevirt_virt_operator_leading_total == 0",
    "for": "5m"
}
```
#### - Record: kubevirt_virt_handler_up_total
```
{
    "expr": "sum(up{pod=~'virt-handler-.*', namespace='openshift-cnv'})"
}
```
#### - Rule: VirtHandlerDaemonSetRolloutFailing
```
{
    "annotations": {
        "summary": "Some virt-handlers failed to roll out"
    },
    "expr": "(kube_daemonset_status_number_ready{namespace='openshift-cnv', daemonset='virt-handler'} - kube_daemonset_status_desired_number_scheduled{namespace='openshift-cnv', daemonset='virt-handler'}) != 0",
    "for": "15m"
}
```
#### - Record: vec_by_virt_handlers_all_client_rest_requests_in_last_5m
```
{
    "expr": "sum by (pod) (sum_over_time(rest_client_requests_total{pod=~'virt-handler-.*', namespace='openshift-cnv'}[5m]))"
}
```
#### - Record: vec_by_virt_handlers_all_client_rest_requests_in_last_hour
```
{
    "expr": "sum by (pod) (sum_over_time(rest_client_requests_total{pod=~'virt-handler-.*', namespace='openshift-cnv'}[60m]))"
}
```
#### - Record: vec_by_virt_handlers_failed_client_rest_requests_in_last_5m
```
{
    "expr": "sum by (pod) (sum_over_time(rest_client_requests_total{pod=~'virt-handler-.*', namespace='openshift-cnv', code=~'(4|5)[0-9][0-9]'}[5m]))"
}
```
#### - Record: vec_by_virt_handlers_failed_client_rest_requests_in_last_hour
```
{
    "expr": "sum by (pod) (sum_over_time(rest_client_requests_total{pod=~'virt-handler-.*', namespace='openshift-cnv', code=~'(4|5)[0-9][0-9]'}[60m]))"
}
```
#### - Rule: VirtHandlerRESTErrorsHigh
```
{
    "annotations": {
        "summary": "More than 5% of the rest calls failed in virt-handler for the last hour"
    },
    "expr": "(vec_by_virt_handlers_failed_client_rest_requests_in_last_hour / vec_by_virt_handlers_all_client_rest_requests_in_last_hour) >= 0.05",
    "for": "5m"
}
```
#### - Rule: VirtHandlerRESTErrorsBurst
```
{
    "annotations": {
        "summary": "More than 80% of the rest calls failed in virt-handler for the last 5 minutes"
    },
    "expr": "(vec_by_virt_handlers_failed_client_rest_requests_in_last_5m / vec_by_virt_handlers_all_client_rest_requests_in_last_5m) >= 0.8",
    "for": "5m"
}
```
#### - Record: kubevirt_vm_container_free_memory_bytes
```
{
    "expr": "sum by(pod, container) ( kube_pod_container_resource_limits_memory_bytes{pod=~'virt-launcher-.*', container='compute'} - on(pod,container) container_memory_working_set_bytes{pod=~'virt-launcher-.*', container='compute'})"
}
```
#### - Rule: KubevirtVmHighMemoryUsage
```
{
    "annotations": {
        "description": "Container {{ $labels.container }} in pod {{ $labels.pod }} free memory is less than 20 MB and it is close to memory limit",
        "summary": "VM is at risk of being terminated by the runtime."
    },
    "expr": "kubevirt_vm_container_free_memory_bytes < 20971520",
    "for": "1m",
    "labels": {
        "severity": "warning"
    }
}
```
#### - Record: kubevirt_num_virt_handlers_by_node_running_virt_launcher
```
{
    "expr": "count by(node)(node_namespace_pod:kube_pod_info:{pod=~'virt-launcher-.*'} ) * on (node) group_left(pod) (1*(kube_pod_container_status_ready{pod=~'virt-handler-.*'} + on (pod) group_left(node) (0 * node_namespace_pod:kube_pod_info:{pod=~'virt-handler-.*'} ))) or on (node) (0 * node_namespace_pod:kube_pod_info:{pod=~'virt-launcher-.*'} )"
}
```
#### - Rule: OrphanedVirtualMachineImages
```
{
    "annotations": {
        "summary": "No virt-handler pod detected on node {{ $labels.node }} with running vmis for more than an hour"
    },
    "expr": "(kubevirt_num_virt_handlers_by_node_running_virt_launcher) == 0",
    "for": "60m",
    "labels": {
        "severity": "warning"
    }
}
```
#### - Rule: VMCannotBeEvicted
```
{
    "annotations": {
        "description": "Eviction policy for {{ $labels.name }} (on node {{ $labels.node }}) is set to Live Migration but the VM is not migratable",
        "summary": "The VM's eviction strategy is set to Live Migration but the VM is not migratable"
    },
    "expr": "kubevirt_vmi_non_evictable > 0",
    "for": "1m",
    "labels": {
        "severity": "warning"
    }
}
```
