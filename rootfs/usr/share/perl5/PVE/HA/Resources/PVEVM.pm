package PVE::HA::Resources::PVEVM;

use strict;
use warnings;

use PVE::HA::Tools;

BEGIN {
    if (!$ENV{PVE_GENERATING_DOCS}) {
	require PVE::QemuConfig;
	import  PVE::QemuConfig;
	require PVE::QemuServer;
	import  PVE::QemuServer;
	require PVE::API2::Qemu;
	import  PVE::API2::Qemu;
    }
}

use base qw(PVE::HA::Resources);

sub type {
    return 'vm';
}

sub verify_name {
    my ($class, $name) = @_;

    die "invalid VMID\n" if $name !~ m/^[1-9][0-9]+$/;
}

sub options {
    return {
	state => { optional => 1 },
	group => { optional => 1 },
	comment => { optional => 1 },
	max_restart => { optional => 1 },
	max_relocate => { optional => 1 },
    };
}

sub config_file {
    my ($class, $vmid, $nodename) = @_;

    return PVE::QemuConfig->config_file($vmid, $nodename);
}

sub exists {
    my ($class, $vmid, $noerr) = @_;

    my $vmlist = PVE::Cluster::get_vmlist();

    if(!defined($vmlist->{ids}->{$vmid})) {
	die "resource 'vm:$vmid' does not exists in cluster\n" if !$noerr;
	return undef;
    } else {
	return 1;
    }
}

sub start {
    my ($class, $haenv, $id) = @_;

    my $nodename = $haenv->nodename();

    my $params = {
	node => $nodename,
	vmid => $id
    };

    my $upid = PVE::API2::Qemu->vm_start($params);
    PVE::HA::Tools::upid_wait($upid, $haenv);
}

sub shutdown {
    my ($class, $haenv, $id) = @_;

    my $nodename = $haenv->nodename();
    my $shutdown_timeout = 60; # fixme: make this configurable

    my $params = {
	node => $nodename,
	vmid => $id,
	timeout => $shutdown_timeout,
	forceStop => 1,
    };

    my $upid = PVE::API2::Qemu->vm_shutdown($params);
    PVE::HA::Tools::upid_wait($upid, $haenv);
}


sub migrate {
    my ($class, $haenv, $id, $target, $online) = @_;

    my $nodename = $haenv->nodename();

    my $params = {
	node => $nodename,
	vmid => $id,
	target => $target,
	online => $online,
    };

    # explicitly shutdown if $online isn't true (relocate)
    if (!$online && $class->check_running($haenv, $id)) {
	$class->shutdown($haenv, $id);
    }

    my $oldconfig = $class->config_file($id, $nodename);

    my $upid = PVE::API2::Qemu->migrate_vm($params);
    PVE::HA::Tools::upid_wait($upid, $haenv);

    # check if vm really moved
    return !(-f $oldconfig);
}

sub check_running {
    my ($class, $haenv, $vmid) = @_;

    my $nodename = $haenv->nodename();

    if (PVE::QemuServer::check_running($vmid, 1, $nodename)) {
	# do not count VMs which are suspended for a backup job as running
	my $conf = PVE::QemuConfig->load_config($vmid, $nodename);
	if (defined($conf->{lock}) && $conf->{lock} eq 'backup') {
	    my $qmpstatus = PVE::QemuServer::vm_qmp_command($vmid, {execute => 'query-status'});
	    return 0 if $qmpstatus->{status} eq 'prelaunch';
	}

	return 1;
    } else {
	return 0;
    }
}

sub remove_locks {
    my ($self, $haenv, $id, $locks, $service_node) = @_;

    $service_node = $service_node || $haenv->nodename();

    my $conf = PVE::QemuConfig->load_config($id, $service_node);

    return undef if !defined($conf->{lock});

    foreach my $lock (@$locks) {
	if ($conf->{lock} eq $lock) {
	    delete $conf->{lock};

	    my $cfspath = PVE::QemuConfig->cfs_config_path($id, $service_node);
	    PVE::Cluster::cfs_write_file($cfspath, $conf);

	    return $lock;
	}
    }

    return undef;
}

1;
