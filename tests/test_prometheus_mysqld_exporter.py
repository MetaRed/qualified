import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_mysql_exporter_socket_is_listening(Socket):
    sock = Socket("tcp://:::9104")
    assert sock.is_listening


def test_mysqld_exporter(Service):
    service = Service("mysqld_exporter")
    assert service.is_running
    assert service.is_enabled


def test_prometheus_startup_script(File):
    f = File('/etc/init.d/mysqld_exporter')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_prometheus_mysql_conf_file(File):
    f = File('/etc/prometheus/tgroups/mysqld_exporter.yml')
    assert f.exists
    assert f.user == 'prometheus'
    assert f.group == 'prometheus'
