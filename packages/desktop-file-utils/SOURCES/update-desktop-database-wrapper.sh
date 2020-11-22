#!/usr/sgug/bin/bash
set -e

update-desktop-database-bin $@

SGUG_DATADIR_APPS=/usr/sgug/share/applications
CATALOG_ROOT=/usr/lib/desktop/iconcatalog/pages/C/RSE

# Grab stuff out of the desktop file
_get_key_from_desktop() {
	DFI_LAST_KEY=$(cat $1 | grep "^$2=" | sed "s,$2=,," | awk '{print $1}')
}

mkdir -p $CATALOG_ROOT

# Clean stuff that no longer exists
for EXISTING_CATALOG_ENTRY in $(find $CATALOG_ROOT -type f); do
	if [ -f "$SGUG_DATADIR_APPS/$EXISTING_CATALOG_ENTRY.desktop" ]; then
		continue
	fi
	
	rm $EXISTING_CATALOG_ENTRY
done

# Update missing entries
for DESKTOP_FILE_PATH in $(find $SGUG_DATADIR_APPS/*.desktop -type f); do
	APPNAME=$(basename $DESKTOP_FILE_PATH | sed 's,\..*,,g')

	_get_key_from_desktop $DESKTOP_FILE_PATH "Exec"
	DESKTOP_KEY_EXEC=$DFI_LAST_KEY

	if [ -f $CATALOG_ROOT/$APPNAME ]; then
		continue
	fi
	cp /usr/sgug/share/desktop-file-utils/sgugenv.sh $CATALOG_ROOT/$APPNAME

	chmod 755 $CATALOG_ROOT/$APPNAME
	echo "#!/usr/sgug/bin/bash" >> $CATALOG_ROOT/$APPNAME
	echo "export PATH=$PATH:/usr/sgug/bin" >> $CATALOG_ROOT/$APPNAME
    echo "exec $DESKTOP_KEY_EXEC" >> $CATALOG_ROOT/$APPNAME 
done

