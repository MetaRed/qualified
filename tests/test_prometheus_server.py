import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_prometheus_user(User):
    u = User("prometheus")
    assert u.exists
    assert u.group == 'prometheus'
    assert u.shell == '/sbin/nologin'
    assert u.home == '/home/prometheus'


def test_prometheus_install_path(File):
    d = File('/opt/prometheus')
    assert d.exists
    assert d.is_directory


def test_prometheus_config_path(File):
    d = File('/etc/prometheus')
    assert d.exists
    assert d.is_directory


def test_prometheus_log_path(File):
    d = File('/var/log/prometheus')
    assert d.exists
    assert d.is_directory


def test_prometheus_pid_path(File):
    d = File('/var/run/prometheus')
    assert d.exists
    assert d.is_directory


def test_prometheus_db_path(File):
    d = File('/var/lib/prometheus')
    assert d.exists
    assert d.is_directory


def test_prometheus_startup_script(File):
    f = File('/etc/init.d/prometheus')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_prometheus_conf_file(File):
    f = File('/etc/prometheus/prometheus.yml')
    assert f.exists
    assert f.user == 'prometheus'
    assert f.group == 'prometheus'


def test_wget_is_installed(Package):
    pack = Package("wget")
    assert pack.is_installed


def test_prometheus_socket_is_listening(Socket):
    sock = Socket("tcp://:::9090")
    assert sock.is_listening


def test_prometheus_service(Service):
    service = Service("prometheus")
    assert service.is_running
    assert service.is_enabled
