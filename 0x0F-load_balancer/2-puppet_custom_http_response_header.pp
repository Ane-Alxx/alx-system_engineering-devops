# The automation task for a few exec/commands
exec { 'command':
  command  => 'apt-get -y update;
  apt-get -y install nginx;
  sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
  service nginx restart',
  provider => shell,
}
class nginx_custom_header {
  package { 'nginx':
    ensure => present,
  }

  file { '/etc/nginx/sites-available/default':
    ensure => present,
    content => template('nginx/default.conf.erb'),
  }

  service { 'nginx':
    ensure => running,
    enable => true,
  }
}