#!/usr/sgug/bin/bash
set -e

desktop-file-install-bin $@

for DFI_DESKTOP_FILE in $@; do :; done

while test -n "$1"; do
	case "$1" in
		--dir)
			DFI_DIR=$2
			shift 2
			;;
		*)
			break
			;;
    esac
done

# We should only do this for an rpmbuild
if [[ "$DFI_DIR" != *"BUILDROOT"* ]]; then
  exit
fi

# Grab stuff out of the desktop file
_get_key_from_desktop() {
	DFI_LAST_KEY=$(cat $1 | grep "$2=" | sed "s,$2=,," | awk '{print $1}')
}

_get_key_from_desktop $DFI_DESKTOP_FILE "Exec"
DFI_DESKTOP_KEY_EXEC=$DFI_LAST_KEY

INSTALL_ROOT=$(dirname $DFI_DIR | sed 's,/usr/sgug/.*,,')
CATALOG_ROOT=$INSTALL_ROOT/usr/lib/desktop/iconcatalog/pages/C/RSE

mkdir -p $CATALOG_ROOT
cp /usr/sgug/share/desktop-file-utils/sgugenv.sh $CATALOG_ROOT/$DFI_DESKTOP_KEY_EXEC

chmod 755 $CATALOG_ROOT/$DFI_DESKTOP_KEY_EXEC
echo "exec $DFI_DESKTOP_KEY_EXEC" >> $CATALOG_ROOT/$DFI_DESKTOP_KEY_EXEC