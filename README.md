# Requirements

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

# Compile OpenWrt firmware(No GL.iNet packages)

1. Run `git clone https://github.com/gl-inet/gl-infra-builder.git && cd gl-infra-builder` to clone repository

2. Run `ls configs -hl` to list the openwrt verizon

3. Chose your want version, for example, if you want to use openwrt-21.02.2, Run `python3 setup.py -c configs/config-21.02.2.yml` to download openwrt-21.02.2 source code

4. Run `cd openwrt-21.02/openwrt-21.02.2` to enter openwrt-21.02.2 directory

5. Run `./scripts/gen_config.py list` to get target_xxx and glinet_xxx files. target_xxx is you want to compile products, don't modify. glinet_xxx is you want to add/delete packages, you can modify. Those files in the **profiles** directory.

6. Run `./scripts/gen_config.py <target_profile> <function_profile>` to chose the product target and add some packages. <target_profile> is you want to compile products. <function_profile> is you want to add/delete packages. 

7. For example, If you want to compile GL-A1300 product and add luci, you can run `./scripts/gen_config.py target_ipq40xx_gl-a1300 luci`. You can run `make menuconfig` to chose other packages

8. Run `make` to build your firmware.

# Compile GL.iNet standard firmware

9. Base on the steps above, at openwrt-21.02/openwrt-21.02.2 directory, run `git clone https://github.com/gl-inet/glinet4.x.git` to get GL.iNet packages.

10. Run `./scripts/gen_config.py target_ipq40xx_gl-a1300 glinet_depends` to add A1300 GL.iNet packages

11. Run ` make V=s -j5 GL_PKGDIR=`pwd`/glinet4.x/ipq40xx/`  to compile GL.iNet standard firmware.

# Example compile firmware

## 1. Compile MT2500(2023.02.22)

  1.1  Compile MT2500 OpenWrt firmware(No GL.iNet packages)
```
 git clone https://github.com/gl-inet/gl-infra-builder.git && cd gl-infra-builder
```
```
 python3 setup.py -c configs/config-mt798x-7.6.6.1.yml && cd mt7981
```
```
 ./scripts/gen_config.py target_mt7981_gl-mt2500 luci
```
```
 make V=s -j5
```

1.2 Compile MT2500 GL.iNet standard firmware
```
 git clone https://github.com/gl-inet/glinet4.x.git
```
```
 cp ./glinet4.x/pkg_config/gl_pkg_config_mt7981_mt2500.mk  ./glinet4.x/mt7981/gl_pkg_config.mk
```
```
 ./scripts/gen_config.py target_mt7981_gl-mt2500 glinet_depends
```
```
 make V=s -j5 GL_PKGDIR=`pwd`/glinet4.x/mt7981/
```
## 2. Compile MT3000(2023.02.22)

2.1 Compile MT3000 OpenWrt firmware(No GL.iNet packages)
```
 git clone https://github.com/gl-inet/gl-infra-builder.git && cd gl-infra-builder
```
```
 python3 setup.py -c configs/config-mt798x-7.6.6.1.yml && cd mt7981
```
```
 ./scripts/gen_config.py target_mt7981_gl-mt3000 luci
```
```
 make V=s -j5
```

2.2 Compile MT3000 GL.iNet standard firmware(Base on the steps above)
```
 git clone https://github.com/gl-inet/glinet4.x.git
```
```
 cp ./glinet4.x/pkg_config/gl_pkg_config_mt7981_mt3000.mk ./glinet4.x/mt7981/gl_pkg_config.mk
```
```
 ./scripts/gen_config.py target_mt7981_gl-mt3000 glinet_depends
```
```
 make -j5 V=s GL_PKGDIR=`pwd`/glinet4.x/mt7981/
```

## 3. Compile AXT1800(2023.02.22)

3.1 Compile AXT1800 OpenWrt firmware(No GL.iNet packages)
```
 git clone https://github.com/gl-inet/gl-infra-builder.git && cd gl-infra-builder
```
```
 python3 setup.py -c configs/config-wlan-ap.yml && cd wlan-ap/openwrt
```
```
 ./scripts/gen_config.py target_wlan_ap-gl-axt1800 luci
```
```
 make V=s -j5
```
3.2 Compile AXT1800 GL.iNet standard firmware(Base on the steps above)
```
 git clone https://github.com/gl-inet/glinet4.x.git
```
```
 ./scripts/gen_config.py target_wlan_ap-gl-axt1800 glinet_depends
```
```
 make V=s -j5 GL_PKGDIR=`pwd`/glinet4.x/ipq60xx/
```
## 4. Compile AX1800(2023.02.22)

4.1 Compile AX1800 OpenWrt firmware(No GL.iNet packages)
```
 git clone https://github.com/gl-inet/gl-infra-builder.git && cd gl-infra-builder
```
```
 python3 setup.py -c configs/config-wlan-ap.yml && cd wlan-ap/openwrt
```
```
 ./scripts/gen_config.py target_wlan_ap-gl-ax1800 luci
```
```
 make V=s -j5
```
4.2 Compile AX1800 GL.iNet standard firmware
```
 git clone https://github.com/gl-inet/glinet4.x.git
```
```
 ./scripts/gen_config.py target_wlan_ap-gl-ax1800 glinet_depends
```
```
 make V=s -j5 GL_PKGDIR=`pwd`/glinet4.x/ipq60xx/
```
## 5. Compile A1300(2023.02.22)

5.1 Compile A1300 OpenWrt firmware(No GL.iNet packages)
```
 git clone https://github.com/gl-inet/gl-infra-builder.git && cd gl-infra-builder
```
```
 python3 setup.py -c configs/config-21.02.2.yml && cd openwrt-21.02/openwrt-21.02.2
```
```
 ./scripts/gen_config.py target_ipq40xx_gl-a1300 luci
```
```
 make V=s -j5
```
5.2 Compile A1300 GL.iNet standard firmware
```
 git clone https://github.com/gl-inet/glinet4.x.git
```
```
 ./scripts/gen_config.py target_ipq40xx_gl-a1300 glinet_depends
```
```
 make V=s -j5 GL_PKGDIR=`pwd`/glinet4.x/ipq40xx/
```

## 6. Compile SFT1200(2022.11.23)
```
 git clone https://github.com/gl-inet/gl-infra-builder.git && cd gl-infra-builder
```
```
 python3 setup.py -c config-siflower-18.x.yml && cd openwrt-18.06/siflower/openwrt-18.06
```
```
 ./scripts/gen_config.py target_siflower_gl-sft1200 luci
```
```
 make V=s -j5
```

## 7. Compile S200(2023.02.24)

4.1 Compile S200 OpenWrt firmware(No GL.iNet packages)
```
 git clone https://github.com/gl-inet/gl-infra-builder.git && cd gl-infra-builder
```
```
 python3 setup.py -c configs/config-21.02.2.yml && cd openwrt-21.02/openwrt-21.02.2
```
```
 ./scripts/gen_config.py target_ath79_gl-s200 luci
```
```
 make V=s -j5
```
4.2 Compile S200 GL.iNet standard firmware
```
 git clone https://github.com/gl-inet/glinet4.x.git
```
```
 ./scripts/gen_config.py target_ath79_gl-s200 glinet_depends_s200
```
```
 make V=s -j5 GL_PKGDIR=`pwd`/glinet4.x/ath79/
```

# Note
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
