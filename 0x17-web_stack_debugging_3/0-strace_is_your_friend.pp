$wp_settings_file = '/var/www/html/wp-settings.php'

exec { 'fix-wordpress':
  command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/ $wp_settings_file'",
    path => '/usr/bin:/usr/sbin:/bin',
      notify => Service['apache2'],
      }

service { 'apache2':
  ensure => running,
    enable => true,
    }
