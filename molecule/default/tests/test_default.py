import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/logrotate.d/test')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_logrotate_is_installed(host):
    logrotate = host.package("logrotate")
    assert logrotate.is_installed
