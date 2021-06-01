
# Under development, please do not use

## Development

### Requirements

You need the following tools to compile OpenWrt, the package names vary between distributions. A complete list with distribution specific packages is found in the [Build System Setup](https://openwrt.org/docs/guide-developer/build-system/install-buildsystem) documentation.

```
$ sudo apt install binutils bzip2 diff find flex gawk gcc-6+ getopt grep install libc-dev libz-dev make4.1+ perl python3.6+ rsync subversion unzip which libncurses5-dev zlib1g-dev gawk gcc-multilib g++-multilib flex git-core gettext libssl-dev ocaml sharutils re2c -y
```

And This development tools requires Python 3.6 or higher! Please use the following command to check,

```
$ python3 --version
Python 3.6.13

$ ls -l /usr/bin/python3*
 /usr/bin/python3 -> python3.6
 /usr/bin/python3.5
 /usr/bin/python3.5-config -> x86_64-linux-gnu-python3.5-config
 /usr/bin/python3.5m
 /usr/bin/python3.5m-config -> x86_64-linux-gnu-python3.5m-config
 /usr/bin/python3.6
 /usr/bin/python3.6-config -> x86_64-linux-gnu-python3.6-config
 /usr/bin/python3.6m
 /usr/bin/python3.6m-config -> x86_64-linux-gnu-python3.6m-config
 /usr/bin/python3.9
 /usr/bin/python3.9-config -> x86_64-linux-gnu-python3.9-config
 /usr/bin/python3-config -> python3.5-config
 /usr/bin/python3m -> python3.5m
 /usr/bin/python3m-config -> python3.5m-config
```

### Quickstart

1. Clone repository,

```
$ git clone https://github.com/gl-inet/gl-infra-builder.git
```

2. If you have a [offline dl folder](https://sources.openwrt.org/), you can make a symlink to feeds/dl, it will make compilation easier,

```
$ cd gl-infra-builder
$ cd feeds/
$ ln -sf /data/dl .
```

3. Setup, auto download openwrt-19.07.7 by default and auto config,

```
$ python3 setup.py
```

4. Generate your target configuration,

```
$ ./scripts/gen_config.py list		# show available profile
$ ./scripts/gen_config.py <target_profile> <function_profile>
```

5. Run `make` to build your firmware.

