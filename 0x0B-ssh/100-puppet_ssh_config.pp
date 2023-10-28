# the advanced 100-puppet_ssh_config.pp

file { '/etc/ssh/config':
  ensure => present,
  owner => 'root',
  group => 'root',
  mode => '0644',
  content => <<EOF
Host *
  IdentityFile ~/.ssh/school
  PasswordAuthentication no
EOF
}
