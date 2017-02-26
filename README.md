Monitor Ansible Role
====================
[![Build Status](https://travis-ci.org/MetaRed/monitor_ansible_role.svg?branch=master)](https://travis-ci.org/MetaRed/monitor_ansible_role)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/5bbc8a8b74c34e40861a74a129ede970)](https://www.codacy.com/app/code_6/monitor_ansible_role?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=MetaRed/monitor_ansible_role&amp;utm_campaign=Badge_Grade)
[![codecov](https://codecov.io/gh/MetaRed/monitor_ansible_role/branch/master/graph/badge.svg)](https://codecov.io/gh/MetaRed/monitor_ansible_role)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Ansible Role: version](https://img.shields.io/badge/Ansible Role-v0.0.2-blue.svg)](https://github.com/MetaRed/monitor_ansible_role/releases/tag/v0.0.2)


Ansible role installs software used for the monitoring and alerting of operating systems and services.

#### Dependencies:
Be aware that some monitoring components are dependent on other software installations in order to run; e.g. Prometheus MySQLd-Exporter requires a running instance of the MySQL Server.  Documenting these use cases is outside the scope of this role.

#### Requirements:
Task lists run on docker containers for testing require the installing the wget package for proper SSL connection handling.

## Role Variables

`Prometheus Server`: Used by Prometheus server task lists.
<table>
  <tr>
    <th>Variable</th>
    <th>Default</th>
  </tr>
  <tr>
    <td><tt>{{ prometheus_user }}</tt></td>
    <td><tt>prometheus</tt></td>
  </tr>
  <tr>
    <td><tt>{{ prometheus_group }}</tt></td>
    <td><tt>prometheus</tt></td>
  </tr>
  <tr>
    <td><tt>{{ prometheus_version }}</tt></td>
    <td><tt>1.4.1</tt></td>
  </tr>
  <tr>
    <td><tt>{{ prometheus_platform_suffix }}</tt></td>
    <td><tt>linux-amd64</tt></td>
  </tr>
  <tr>
    <td><tt>{{ prometheus_go_version }}</tt></td>
    <td><tt>1.7.3</tt></td>
  </tr>
  <tr>
    <td><tt>{{ prometheus_install_path }}</tt></td>
    <td><tt>/opt/prometheus</tt></td>
  </tr>
  <tr>
    <td><tt>{{ prometheus_config_path }}</tt></td>
    <td><tt>/etc/prometheus</tt></td>
  </tr>
  <tr>
    <td><tt>{{ prometheus_rule_path }}</tt></td>
    <td><tt>{{ prometheus_config_path }}/rules</tt></td>
  </tr>
  <tr>
    <td><tt>{{ prometheus_file_sd_config_path }}</tt></td>
    <td><tt>{{ prometheus_config_path }}/tgroups</tt></td>
  </tr>
  <tr>
    <td><tt>{{ prometheus_db_path }}</tt></td>
    <td><tt>/var/lib/prometheus</tt></td>
  </tr>
  <tr>
    <td><tt>{{ prometheus_log_path }}</tt></td>
    <td><tt>/var/log/prometheus</tt></td>
  </tr>
  <tr>
    <td><tt>{{ prometheus_pid_path }}</tt></td>
    <td><tt>/var/run/prometheus</tt></td>
  </tr>
  <tr>
    <td><tt>{{ prometheus_download_path }}</tt></td>
    <td><tt>/tmp</tt></td>
  </tr>
  <tr>
    <td><tt>{{ prometheus_workdir }}</tt></td>
    <td><tt>{{ prometheus_download_path }}/prometheus_workdir</tt></td>
  </tr>
  <tr>
    <td><tt>{{ prometheus_goroot }}</tt></td>
    <td><tt>{{ prometheus_workdir }}/go</tt></td>
  </tr>
  <tr>
    <td><tt>{{ prometheus_gopath }}</tt></td>
    <td><tt>{{ prometheus_workdir }}/gopath</tt></td>
  </tr>
  <tr>
    <td><tt>{{ prometheus_daemon_dir }}</tt></td>
    <td><tt>{{ prometheus_install_path }}/prometheus-{{ prometheus_version }}.linux-amd64</tt></td>
  </tr>
  <tr>
    <td><tt>{{ prometheus_tarball_url }}</tt></td>
    <td><tt>https://<i></i>github.com/prometheus/prometheus/releases/download/v{{ prometheus_version }}/prometheus-{{ prometheus_version }}.linux-amd64.tar.gz</tt></td>
  </tr>
</table>

`Prometheus Node Exporter`: used exclusively by prometheus node exporter tasks.
<table>
  <tr>
    <th>Variable</th>
    <th>Default</th>
  </tr>
  <tr>
    <td><tt>{{ prometheus_node_exporter_version }}</tt></td>
    <td><tt>0.13.0</tt></td>
  </tr>
  <tr>
    <td><tt>{{ prometheus_node_exporter_tarball_url }}</tt></td>
    <td><tt>https://<i></i>github.com/prometheus/node_exporter/releases/download/v{{ prometheus_node_exporter_version }}/node_exporter-{{ prometheus_node_exporter_version }}.linux-amd64.tar.gz</tt></td>
  </tr>
  <tr>
    <td><tt>{{ prometheus_node_exporter_daemon_dir }}</tt></td>
    <td><tt>{{ prometheus_install_path }}/node_exporter-{{ prometheus_node_exporter_version }}.linux-amd64</tt></td>
  </tr>
</table>

`Prometheus MySQLd Exporter`: used exclusively by prometheus mysqld exporter tasks.
<table>
<tr>
  <th>Variable</th>
  <th>Default</th>
</tr>
<tr>
  <td><tt>{{ prometheus_mysqld_exporter_version }}</tt></td>
  <td><tt>0.9.0</tt></td>
</tr>
<tr>
  <td><tt>{{ prometheus_mysqld_exporter_tarball_url }}</tt></td>
  <td><tt>https://<i></i>github.com/prometheus/mysqld_exporter/releases/download/v{{ prometheus_mysqld_exporter_version }}/mysqld_exporter-{{ prometheus_mysqld_exporter_version }}.linux-amd64.tar.gz</tt></td>
</tr>
<tr>
  <td><tt>{{ prometheus_mysqld_exporter_daemon_dir }}</tt></td>
  <td><tt>{{ prometheus_install_path }}/mysqld_exporter-{{ prometheus_mysqld_exporter_version }}.linux-amd64</tt></td>
</tr>
</table>

## Galaxy Playbook Usage

```yaml

    - hosts: servers
      roles:
         - { role: MetaRed.monitor, variable: value }
```


### Tags
`prometheus`: Run all prometheus task lists.

`prometheus-server`: Run only prometheus server task lists.

`node-exporter`: Run only prometheus node exporter tasks.

`mysqld-exporter`: Run only prometheus mysqld exporter tasks.

```bash

ansible-playbook site.yml --tags=prometheus

```


## Testing
`TestInfra`: PyTest integration tests.


```

tests/test_prometheus_server.py
tests/test_prometheus_node_exporter.py
tests/test_prometheus_mysqld_exporter.py


```

## Authors
Authors: Richard Lopez

## Credits
Prometheus tasks inspired by the code in this project: [Ansible-Prometheus](https://github.com/William-Yeh/ansible-prometheus "Ansible Prometheus")
