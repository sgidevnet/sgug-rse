#!/usr/sgug/bin/bash
set -e

update-desktop-database-bin $@

rm -f /tmp/uddw.log
echo "Running" >> /tmp/uddw.log

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
	echo "Removed $EXISTING_CATALOG_ENTRY" >> /tmp/uddw.log
done

# Update missing entries
for DESKTOP_FILE_PATH in $(find $SGUG_DATADIR_APPS/*.desktop -type f); do
	echo "Checking $DESKTOP_FILE_PATH" >> /tmp/uddw.log
	APPNAME=$(basename $DESKTOP_FILE_PATH | sed 's,\..*,,g')
	echo "APPNAME $APPNAME" >> /tmp/uddw.log

	_get_key_from_desktop $DESKTOP_FILE_PATH "Exec"
	DESKTOP_KEY_EXEC=$DFI_LAST_KEY
	DESKTOP_KEY_EXEC_BASENAME="$(basename $DESKTOP_KEY_EXEC)"
	echo "DESKTOP_KEY_EXEC $DESKTOP_KEY_EXEC" >> /tmp/uddw.log
	echo "DESKTOP_KEY_EXEC_BASENAME $DESKTOP_KEY_EXEC_BASENAME" >> /tmp/uddw.log

	_get_key_from_desktop $DESKTOP_FILE_PATH "Terminal"
	TERMINAL_KEY=$DFI_LAST_KEY
	echo "TERMINAL_KEY $TERMINAL_KEY" >> /tmp/uddw.log

	if [ -f $CATALOG_ROOT/$APPNAME ]; then
		continue
	fi

	echo "Writing $CATALOG_ROOT/$APPNAME" >> /tmp/uddw.log
	touch $CATALOG_ROOT/$APPNAME
	chmod 755 $CATALOG_ROOT/$APPNAME
	echo "#!/usr/sgug/bin/bash" >> $CATALOG_ROOT/$APPNAME
	echo "export PATH=/usr/sgug/bin:$PATH" >> $CATALOG_ROOT/$APPNAME
	# Urgh, python
	echo "export PYTHONHOME=/usr/sgug" >> $CATALOG_ROOT/$APPNAME
	if [ "$TERMINAL_KEY" = "true" ]; then
	    echo "exec /usr/sbin/winterm $DESKTOP_KEY_EXEC_BASENAME" >> $CATALOG_ROOT/$APPNAME
	else
	    echo "exec $DESKTOP_KEY_EXEC_BASENAME" >> $CATALOG_ROOT/$APPNAME
	fi
	echo "Finished writing $CATALOG_ROOT/$APPNAME" >> /tmp/uddw.log
done

