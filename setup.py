from os import path
from pathlib import Path
from subprocess import run
from subprocess import call
import os
import sys
import yaml
import getopt

git_am = "am"

def copy_local_file(src,dest):
    try:
        call("cp  -r %s %s" % (src,dest), shell=True)
        return 0
    except:
        print("### copy "+src+" to "+ dest +" failed")
        return 1

def clone_tree():
    #try:
        makefile = openwrt + "/Makefile"
        if Path(makefile).is_file():
            print("### OpenWrt checkout is already present.")
            return 1

        print("### Cloning or copy tree")
        Path(git_clone_dir).mkdir(exist_ok=True, parents=True)

        if not  config["repo"].startswith("https:") and not  config["repo"].startswith("git@"):
            print("### copy local tree")
            return copy_local_file(config["repo"]+"/.",git_clone_dir)

        if git_ref != "":
            run(["git", "clone", "--reference", git_ref, config["repo"], git_clone_dir], check=True)
        else:
            run(["git", "clone", "--recursive", config["repo"], git_clone_dir], check=True)
        print("### Clone done")
        return 0
    #except:
        print("### Cloning the tree failed")
        return 1


def qsdk_reset_tree():
        os.chdir(git_clone_dir)

        if not Path("qca-networking-spf").exists():
            if not  config["qca_spf_repo"].startswith("https:") and not  config["qca_spf_repo"].startswith("git@"):
                copy_local_file(config["qca_spf_repo"]+"/.","qca-networking-spf")
            else:
                run(["git", "clone", config["qca_spf_repo"], "-b", config["qca_spf_branch"]], check=True)
            os.chdir("qca-networking-spf")
            os.system("rm -rf BOOT.AK.1.0 BOOT.BF.3.* IPQ8064.ILQ* IPQ4019.ILQ* IPQ8074.ILQ* RPM.AK.1.0 TZ.AK.1.0 TZ.BF.2.7 TZ.BF.4.0.8 WIGIG.TLN* BOOT.BF.3.3.1.1 TZ.WNS.4.0 IPQ5018.ILQ.11.* BTFW.MAPLE.* WIGIG.TLN.7.5")
            os.system("cp -rf */* .")
            os.chdir(path.join(base_dir, git_clone_dir))

        if not Path(".repo").exists():
            print("Uncompress qsdk repo...")
            run(["tar", "Jxvf", config["qsdk_repo"]], check=True)

            run(["rm", "-rf", path.join(base_dir, openwrt)], check=True)

            print("sync qsdk repo...")
            run(["repo", "sync", "-j8", "--no-tags", "-c"], check=True)

            print("Gen qsdk framework...")
            run([path.join(".", config["gen_script"])], check=True)

def wlan_ap_reset_tree():
    os.chdir(git_clone_dir)
    run(["rm", "-rf", "openwrt"])
    run(["git", "reset", "--hard", config.get("revision", config.get("branch"))], check=True)
    run(["./setup.py", "--setup"])

def reset_tree():
    try:
        print("### Resetting tree")

        if config.get("qsdk"):
            qsdk_reset_tree()
        elif config.get("wlan_ap"):
            wlan_ap_reset_tree()
        else:
            os.chdir(openwrt)
            run(["git", "reset", "--hard", config.get("revision", config.get("branch"))], check=True)
            run(["rm", "-rf", "profiles"], )
        print("### Reset done")
    except:
        print("### Resetting tree failed")
        sys.exit(1)
    finally:
        os.chdir(base_dir)


def pull_tree():
    try:
        makefile = openwrt + "/Makefile"
        if not Path(makefile).is_file():
            print("### OpenWrt checkout is not present. Please run --setup")
            sys.exit(-1)

        print("### Pull tree")
        os.chdir(openwrt)
        run(["git", "pull"], check=True)
        print("### Pull done")
    except:
        print("### Pulling the tree failed")
        sys.exit(1)
    finally:
        os.chdir(base_dir)


def setup_tree():
    if not config.get("wlan_ap"):
        print("copy build scripts to " +openwrt + "/scripts")
        call("cp ./scripts/openwrt/* %s" % (path.join(openwrt,"scripts")), shell=True)

    try:
        print("### Copying files")
        for folder in config.get("files_folders", []):
            file_folder = base_dir / folder
            if not file_folder.is_dir():
                print(f"File folder {file_folder} not found")
                sys.exit(-1)

            print(f"Coping files from {file_folder}")
            call("cp -r %s/* %s" % (base_dir / file_folder, git_clone_dir), shell=True)

        print("### Applying patches")

        patches = []
        patches_openwrt = []

        for folder in config.get("patch_folders", []):
            patch_folder = base_dir / folder
            if not patch_folder.is_dir():
                print(f"Patch folder {patch_folder} not found")
                sys.exit(-1)

            print(f"Adding patches from {patch_folder}")

            if patch_folder / "openwrt":
                patches_openwrt.extend(sorted(list((base_dir / folder / "openwrt").glob("*.patch")), key=os.path.basename))
                patches.extend(sorted(list((base_dir / folder).glob("*.patch")), key=os.path.basename))
            else:
                patches_openwrt.extend(sorted(list((base_dir / folder).glob("*.patch")), key=os.path.basename))

        print(f"Found {len(patches) + len(patches_openwrt)} patches")

        os.chdir(git_clone_dir)

        for patch in patches:
            run(["git", git_am, "-3", str(patch)], check=True)

        os.chdir(base_dir / openwrt)

        for patch in patches_openwrt:
            run(["git", git_am, "-3", str(patch)], check=True)

        if not Path("profiles").exists():
            os.mkdir("profiles")

        os.chdir("profiles")

        for profile in os.listdir(profiles):
            run(["ln", "-fs", path.join(profiles, profile), profile], check=True)

        os.chdir(base_dir / openwrt)

        feeds_dir = str(base_dir) + "/feeds"

        if not Path("feeds_dir").exists():
            run(
                ["ln", "-s", feeds_dir, "feeds_dir"],
                check=True,
            )

        offline_dl_dir = str(base_dir) + "/feeds/dl"

        if os.path.exists(offline_dl_dir):
            if not Path("dl").exists():
                print(f"Install offline dl folder...")
                run(
                    ["ln", "-s", offline_dl_dir, "dl"],
                    check=True,
                )
        print("### Patches done")
    except:
        print("### Setting up the tree failed")
        sys.exit(1)
    finally:
        os.chdir(base_dir)
    if  config.get("wlan_ap"):
        print("copy build scripts to " +openwrt + "/scripts")
        call("cp ./scripts/wlan-ap/* %s" % (path.join(openwrt,"scripts")), shell=True)

def remove_feeds():
    try:
        print("### Remove feeds")
        os.chdir(openwrt)
        if Path("feeds").exists():
            os.system('rm feeds -fr')
        if Path("package/feeds").exists():
            os.system('rm package/feeds -fr')
        if Path("dl").exists():
            os.system('rm -r dl')
        print("### Remove feeds done")
    except:
        print("### Remove feeds failed")
        sys.exit(1)
    finally:
        os.chdir(base_dir)

base_dir = Path.cwd().absolute()
config = "config-19.x.yml"
profiles = os.getcwd() + "/" + "profiles"
openwrt = "openwrt"
git_clone_dir = ""
git_ref = ""

if not sys.version_info >= (3, 6):
    print("This script requires Python 3.6 or higher!")
    print("You are using Python {}.{} by default.".format(sys.version_info.major, sys.version_info.minor))
    print("The following versions of Python3 have been installed on your system.")
    print("You can use the command 'cd /usr/bin/ && ln -sf <python3_version> python3' to change it.")
    os.system("ls -l /usr/bin/python3*")
    sys.exit(1)

try:
    opts, args = getopt.getopt(sys.argv[1:], "c:", ["config="])
except getopt.GetoptError as err:
    print(err)
    sys.exit(2)

for o, a in opts:
    if o in ("-c", "--config"):
        config = a
    else:
        assert False, "unhandled option"

if not Path(config).is_file():
    print(f"Missing {config}")
    sys.exit(1)
config = yaml.safe_load(open(config))

git_clone_dir = config['git_clone_dir']
openwrt = config['openwrt_root_dir']

clone_tree()
# pull_tree()
reset_tree()
setup_tree()

if git_clone_dir == "openwrt-18.06/siflower":
    remove_feeds()
