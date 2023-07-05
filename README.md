# Requirements

You need the following tools to compile OpenWrt, the package names vary between distributions. A complete list with distribution specific packages is found in the [Build System Setup](https://openwrt.org/docs/guide-developer/build-system/install-buildsystem) documentation.

```
sudo apt install binutils bzip2 diff find flex gawk gcc-6+ getopt grep install libc-dev libz-dev make4.1+ perl python3.6+ rsync subversion unzip which libncurses5-dev zlib1g-dev gawk gcc-multilib g++-multilib flex git-core gettext libssl-dev ocaml sharutils re2c -y
```

And This development tools requires Python 3.6 or higher! Please use the following command to check,

```
python3 --version
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

2. Run `git checkout xxx` to switch gl-infra-builder tag(please refer to the table below about xxx tag), the purpose of this step is to switch to the source code used by different GL.iNet firmware versions.

3. Run `ls configs -hl` to list the openwrt verizon

4. Chose your want version, for example, if you want to use openwrt-21.02.2, Run `python3 setup.py -c configs/config-21.02.2.yml` to download openwrt-21.02.2 source code

5. Run `cd openwrt-21.02/openwrt-21.02.2` to enter openwrt-21.02.2 directory

6. Run `./scripts/gen_config.py list` to get target_xxx and glinet_xxx files. target_xxx is you want to compile products, don't modify. glinet_xxx is you want to add/delete packages, you can modify. Those files in the **profiles** directory.

7. Run `./scripts/gen_config.py <target_profile> <function_profile>` to chose the product target and add some packages. <target_profile> is you want to compile products. <function_profile> is you want to add/delete packages.

8. For example, If you want to compile GL-A1300 product and add luci, you can run `./scripts/gen_config.py target_ipq40xx_gl-a1300 luci`. You can run `make menuconfig` to chose other packages

9. Run `make` to build your firmware.

# Compile GL.iNet standard firmware

10. Base on the steps above, at openwrt-21.02/openwrt-21.02.2 directory, run `git clone https://github.com/gl-inet/glinet4.x.git` to get GL.iNet packages.

12. Run `git checkout xxx` to switch glinet4.x packages tag(please refer to the table below about xxx tag), the purpose of this step is to switch to the packages used by different GL.iNet firmware versions.

13. Run `./scripts/gen_config.py target_ipq40xx_gl-a1300 glinet_depends glinet_nas` to add A1300 GL.iNet packages

14. Run ` make V=s -j5 GL_PKGDIR=`pwd`/glinet4.x/ipq40xx/`  to compile GL.iNet standard firmware.

# The tag of the released version is as follows

AX1800

| Firmware version | gl-infra-builder tag   | glinet4.x tag   |
| ---------------- | ---------------------- | --------------- |
| 4.1.0            | v4.1.0_ax1800_release6 | no record       |
| 4.2.0            | v4.2.0_release3        | v4.2.0_release3 |

AXT1800

| Firmware version | gl-infra-builder tag    | glinet4.x tag   |
| ---------------- | ----------------------- | --------------- |
| 4.0.0            | v4.0.0_release3         | no record       |
| 4.0.2            | v4.0.2_release1         | no record       |
| 4.0.3            | v4.0.3_release1         | no record       |
| 4.1.0            | v4.1.0_axt1800_release7 | no record       |
| 4.2.0            | v4.2.0_release3         | v4.2.0_release3 |

MT3000

| Firmware version | gl-infra-builder tag   | glinet4.x tag |
| ---------------- | ---------------------- | ------------- |
| 4.1.2            | v4.1.2_mt3000_release3 | no record     |
| 4.1.3            | v4.1.3_mt3000_release3 | v4.1.3        |
| 4.2.0            | v4.2.0_mt3000_release1 | v4.2.0_MT3000_release1 |

MT2500

| Firmware version | gl-infra-builder tag   | glinet4.x tag   |
| ---------------- | ---------------------- | --------------- |
| 4.1.1            | v4.1.1_mt2500_release2 | no record       |
| 4.2.0            | v4.2.0_release3        | v4.2.0_release3 |




| Firmware version | gl-infra-builder tag  | glinet4.x tag   |
| ---------------- | --------------------- | --------------- |
| 4.0.0            | v4.0.0_a1300_release1 | no record       |
| 4.1.0            | v4.1.0_a1300_release8 | no record       |
| 4.1.2            | v4.1.2_a1300_release3 | no record       |
| 4.2.0            | v4.2.0_release3       | v4.2.0_release3 |

S200

| Firmware version | gl-infra-builder tag      | glinet4.x tag        |
| ---------------- | ------------------------- | -------------------- |
| 4.1.3            | v4.1.3_s200_release7      | v4.1.3_s200_release7 |
| 4.1.4-0200       | v4.1.4-0200_s200_release1 | no record            |

x300b

| Firmware version | gl-infra-builder tag  | glinet4.x tag        |
| ---------------- | --------------------  | -------------------- |
| 4.2.0            | v4.2.0_x300b_release3 | no record            |

X3000

| Firmware version | gl-infra-builder tag   | glinet4.x tag   |
| ---------------- | ---------------------- | --------------- |
| 4.3.0            | v4.3.0_x3000_release2  | no record       |
| 4.3.1            | v4.3.1_x3000_release1  | no record       |

# Example compile firmware

## 1. Compile MT2500(2023.03.17)

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
cp ./glinet4.x/pkg_config/gl_pkg_config_mt2500.mk  ./glinet4.x/mt7981/gl_pkg_config.mk
```
```
cp ./glinet4.x/pkg_config/glinet_depends_mt2500.yml  ./profiles/glinet_depends.yml
```
```
./scripts/gen_config.py glinet_depends
```
```
make V=s -j5 GL_PKGDIR=`pwd`/glinet4.x/mt7981/
```
## 2. Compile MT3000 V4.2.0 firmware(2023.03.21)

2.1 Compile MT3000 OpenWrt firmware(No GL.iNet packages)
```
git clone https://github.com/gl-inet/gl-infra-builder.git && cd gl-infra-builder
```
```
git checkout v4.2.0_mt3000_release1

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
cp ./glinet4.x/pkg_config/gl_pkg_config_mt3000.mk  ./glinet4.x/mt7981/gl_pkg_config.mk
```
```
cp ./glinet4.x/pkg_config/glinet_depends_mt3000.yml  ./profiles/glinet_depends.yml
```
```
./scripts/gen_config.py glinet_depends
```
```
make -j5 V=s GL_PKGDIR=`pwd`/glinet4.x/mt7981/
```
## 3. Compile AXT1800(2023.03.17)

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
cp ./glinet4.x/pkg_config/gl_pkg_config_axt1800.mk  ./glinet4.x/ipq60xx/gl_pkg_config.mk
```
```
cp ./glinet4.x/pkg_config/glinet_depends_axt1800.yml  ./profiles/glinet_depends.yml
```
```
./scripts/gen_config.py glinet_depends
```
```
make V=s -j5 GL_PKGDIR=`pwd`/glinet4.x/ipq60xx/
```
## 4. Compile AX1800(2023.03.17)

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
cp ./glinet4.x/pkg_config/gl_pkg_config_ax1800.mk  ./glinet4.x/ipq60xx/gl_pkg_config.mk
```
```
cp ./glinet4.x/pkg_config/glinet_depends_ax1800.yml  ./profiles/glinet_depends.yml
```
```
./scripts/gen_config.py glinet_depends
```
```
make V=s -j5 GL_PKGDIR=`pwd`/glinet4.x/ipq60xx/
```
## 5. Compile A1300(2023.03.17)

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
cp ./glinet4.x/pkg_config/gl_pkg_config_a1300.mk  ./glinet4.x/ipq40xx/gl_pkg_config.mk
```
```
cp ./glinet4.x/pkg_config/glinet_depends_a1300.yml  ./profiles/glinet_depends.yml
```
```
./scripts/gen_config.py glinet_depends
```
```
make V=s -j5 GL_PKGDIR=`pwd`/glinet4.x/ipq40xx/
```
## 6. Compile SFT1200(2022.11.23)
```
git clone https://github.com/gl-inet/gl-infra-builder.git && cd gl-infra-builder
```
```
python3 setup.py -c configs/config-siflower-18.x.yml && cd openwrt-18.06/siflower/openwrt-18.06
```
```
./scripts/gen_config.py target_siflower_gl-sft1200 luci
```
```
make V=s -j5
```

## 7. Compile S200(2023.02.24)

7.1 Compile S200 OpenWrt firmware(No GL.iNet packages)
```
git clone https://github.com/gl-inet/gl-infra-builder.git && cd gl-infra-builder
```
```
git checkout v4.1.3_s200_release7
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
7.2 Compile S200 GL.iNet standard firmware
```
git clone https://github.com/gl-inet/glbuilder && cd glbuilder
make menuconfig
--Select GL.iNet router model (GL.iNet s200)
--Select version for s200 (s200 version 4.1.4-0200)
make V=s
```
## 8. Compile x300b(2023.04.20)
8.1 Compile x300b OpenWrt firmware(No GL.iNet packages)
```
git clone https://github.com/gl-inet/gl-infra-builder.git && cd gl-infra-builder
```
```
git checkout v4.2.0_x300b_release3
```
```
python3 setup.py -c ./configs/config-22.03.2.yml && cd openwrt-22.03/openwrt-22.03.2/
```
```
./scripts/gen_config.py target_ath79_gl-x300b-nor luci
```
```
make V=s -j5
```
## 9. Compile X3000 V4.3.1 firmware(2023.05.23)

9.1 Compile X3000 OpenWrt firmware(No GL.iNet packages)
```
git clone https://github.com/gl-inet/gl-infra-builder.git && cd gl-infra-builder
```
```
git checkout v4.3.1_x3000_release1
```
```
python3 setup.py -c configs/config-mt798x-7.6.6.1.yml && cd mt798x
```
```
./scripts/gen_config.py target_mt7981_gl-x3000 luci
```
```
make V=s -j5
```

9.2 Compile X3000 GL.iNet standard firmware

```
git clone https://github.com/gl-inet/glbuilder && cd glbuilder
make menuconfig
--Select GL.iNet router model (GL.iNet x3000)
--Select version for x3000 (x3000 version 4.3.1)
make V=s
```
For more functions, please check https://github.com/gl-inet/glbuilder/blob/main/Readme.md

# How to add own files

In the openwrt system, we can add our own files through the files directory. All files including paths in the files directory will be copied to the file system at the last step of compilation. This feature can be used to add our own files or replace files.

Here is an example of setting the version number from the files directory.

```
mkdir -p files/etc
echo "4.2.0" > files/etc/glversion
echo "release1" > files/etc/version.type
echo "$(date '+%Y-%m-%d %H:%M:%S')" > files/etc/version.date
```

Here is an example of setting a repository address

```
mkdir -p files/etc/opkg/
cat > files/etc/opkg/distfeeds.conf << EOF
src/gz glinet_core https://fw.gl-inet.com/releases/v21.02.3/kmod-4.0/aarch64_cortex-a53/mediatek/mt7981
src/gz glinet_gli_pub https://fw.gl-inet.com/releases/v21.02.3/packages-4.0/aarch64_cortex-a53/glinet
src/gz glinet_gli_packages https://fw.gl-inet.com/releases/v21.02.3/packages-4.0/aarch64_cortex-a53/packages
EOF
```

# How to add own packages

Under openwrt, in order to solve the dependency problem between packages, we add our own packages to the source tree in the form of feeds.

Let's say we have a directory called /home/mypackages where we can store our packages, and we have two packages called package1 and package2.

First, we create a new profile in which we reference the package we want to compile.

```shell
cat > profiles/myprofile.yml  << EOF
feeds:
  - name: myfeeds
    path: /home/mypackages

packages:
  - package1
  - package2
EOF
```

myprofile.yml is our file name, note that the suffix must be .yml.

In the object set of feeds, we specify the source code path through the path parameter.
In the object set of packages, we add the name of the package that needs to be selected for compilation

And then, we can use this profile in the configuration generation step

```shell
./scripts/gen_config.py target_mt7981_gl-mt2500 luci myprofile
```

Compile firmware
```
make V=s
```

or compile signal package

```
make package/feeds/myfeeds/package1 V=s
```

# Note
1. If you gcc version is 10, you will encounter some error, like this:
```
/usr/bin/ld: scripts/dtc/dtc-parser.tab.o:(.bss+0x10): multiple definition of `yylloc'; scripts/dtc/dtc-lexer.lex.o:(.bss+0x0): first defined here
collect2: error：ld returned 1 exit status.
```
You should execute the following command to reduce the gcc version:
```
update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 100
update-alternatives --config gcc
```
