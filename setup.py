from pathlib import Path
from subprocess import run
import os
import sys
import yaml
import getopt

git_am = "am"


def clone_tree():
    try:
        makefile = openwrt + "/Makefile"
        if Path(makefile).is_file():
            print("### OpenWrt checkout is already present.")
            return 1

        print("### Cloning tree")
        Path(git_clone_dir).mkdir(exist_ok=True, parents=True)
        if git_ref != "":
            run(["git", "clone", "--reference", git_ref, config["repo"], git_clone_dir], check=True)
        else:
            run(["git", "clone", "--recursive", config["repo"], git_clone_dir], check=True)
        print("### Clone done")
        return 0
    except:
        print("### Cloning the tree failed")
        return 1


def reset_tree():
    try:
        print("### Resetting tree")
        os.chdir(openwrt)
        run(
            ["git", "checkout", config["branch"]],
            check=True,
        )
        run(
            ["git", "reset", "--hard", config.get("revision", config["branch"])],
            check=True,
        )
        run(["rm", "-r", "profiles"], )
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
    try:
        print("### Applying patches")

        patches = []
        for folder in config.get("patch_folders", []):
            patch_folder = base_dir / folder
            if not patch_folder.is_dir():
                print(f"Patch folder {patch_folder} not found")
                sys.exit(-1)

            print(f"Adding patches from {patch_folder}")

            patches.extend(sorted(list((base_dir / folder).glob("*.patch")), key=os.path.basename))

        print(f"Found {len(patches)} patches")

        os.chdir(openwrt)

        for patch in patches:
            run(["git", git_am, "-3", str(base_dir / patch)], check=True)
        run(
            ["ln", "-s", profiles, "profiles"],
            check=True,
        )

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
