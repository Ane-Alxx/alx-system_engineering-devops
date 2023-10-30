#!/usr/bin/pup
# This script will create a file in the tmp directory
file { '/tmp/school':
  ensure => present,
  mode   => '0744',
  owner  => 'www-data',
  group  => 'www-data',
  content => 'I love Puppet',
}