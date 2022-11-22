
# Under development, please do not use

## Requirements

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

1. Run `git clone https://github.com/gl-inet/gl-infra-builder.git && cd gl-infra-builder` to clone repository

2. Run `ls configs -hl` to list the openwrt verizon

3. Chose your want version, for example, if you want to use openwrt-19.07.8, Run `python3 setup.py -c configs/config-19.07.8.yml` to download openwrt-19.07.8 source code

4. Run `cd openwrt-19.07/openwrt-19.07.8/` to enter openwrt-19.07.8 directory

5. Run `./scripts/gen_config.py list` to get target_xxx and glinet_xxx files. target_xxx is you want to compile products, don't modify. glinet_xxx is you want to add/delete packages, you can modify. Those files in the **profiles** directory.

6. Run `./scripts/gen_config.py <target_profile> <function_profile>` to chose the product target and add some packages. <target_profile> is you want to compile products. <function_profile> is you want to add/delete packages. 

7. For example, If you want to compile GL-AR150 product and add luci, you can run `./scripts/gen_config.py target_ath79_gl-ar150 luci`. You can run `make menuconfig` to chose other packages

8. Run `make` to build your firmware.

   
### Example
1. Compile MT2500(2022.11.22)
```
 git clone https://github.com/gl-inet/gl-infra-builder.git
```
```
 cd gl-infra-builder
```
```
 python3 setup.py -c  configs/config-mt798x-7.6.6.1.yml
```
```
 cd mt7981
```
```
 ./scripts/gen_config.py target_mt7981_gl-mt2500 luci
```
```
 make -j5
```

### Note
1. If you gcc version is 10, you will encounter some error, like this:
```
/usr/bin/ld: scripts/dtc/dtc-parser.tab.o:(.bss+0x10): multiple definition of `yylloc'; scripts/dtc/dtc-lexer.lex.o:(.bss+0x0): first defined here
collect2: error：ld returned 1 exit status.
```
You should execute the following command to reduce the gcc version:
```
$ update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 100
$ update-alternatives --config gcc
```