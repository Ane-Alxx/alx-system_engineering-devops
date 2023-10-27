this is a read me file for 0x0A-configuration_management
```
# This project contains a set of Puppet manifests that can be used to manage a system.

## Requirements

* Ubuntu 20.04 LTS
* Puppet 5.5

## Installation

```
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
```

## Usage

To apply the Puppet manifests, run the following command:

```
$ puppet apply .


This will apply all of the Puppet manifests in the current directory.

## Contributing

We encourage you to contribute to this project! If you find any errors or have any suggestions, please feel free to open an issue or submit a pull request.
