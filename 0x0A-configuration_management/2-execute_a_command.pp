# Using Puppet, kill a process named killmenow using pkill.
exec { 'killmenow':
  command => 'pkill killmenow',
  onlyif  => 'pgrep killmenow',
}
