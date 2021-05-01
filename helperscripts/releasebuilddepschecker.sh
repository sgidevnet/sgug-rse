#!/usr/sgug/bin/bash

# Clean up old working files
rm /tmp/specrequires.txt
rm /tmp/specprovides.txt

# Add package + dependencies
while read package; do
    [ "${package:0:1}" = "#" ] && continue
    # Find .spec of it and output the requires
    # and provides
    SPECFILE="packages/$package/SPECS/$package.spec"
    BUILDREQSFILE="packages/$package/buildrequires"
    REQSFILE="packages/$package/requires"
    PRVSFILE="packages/$package/provides"
    
    if [ ! -f "$BUILDREQSFILE" ]; then
      rpmspec -q --buildrequires "$SPECFILE" > "$BUILDREQSFILE"
    fi
    # Just cat existing file on the end
    cat "$BUILDREQSFILE" >> /tmp/specrequires.txt

    if [ ! -f "$REQSFILE" ]; then
      rpmspec -q --requires "$SPECFILE" >> "$REQSFILE"
    fi
    # Just cat existing file on the end
    cat "$REQSFILE" >> /tmp/specrequires.txt

    # By default spit out a provide for the package name along
    echo "$package" >> /tmp/specprovides.txt
    if [ ! -f "$PRVSFILE" ]; then
      rpmspec -q --provides "$SPECFILE" >> "$PRVSFILE"
    fi
    # Just cat existing file on the end
    cat "$PRVSFILE" >> /tmp/specprovides.txt

    #exit 1
    #break
done <releasepackages.lst

# REQUIRES
# Tweak any lines that have = or >= in them
cp /tmp/specrequires.txt /tmp/tweakedspecrequires.txt
perl -pi -e "s|^(\\S+)\\s\\=\\s.*|\$1|g" /tmp/tweakedspecrequires.txt
perl -pi -e "s|^(\\S+)\\s\\>\\=\\s.*|\$1|g" /tmp/tweakedspecrequires.txt
# And remove and (mips-32) entries
perl -pi -e "s|^(.+)\\(mips\\-32\\).*|\$1|g" /tmp/tweakedspecrequires.txt

# Now sort it and unique it
sort /tmp/tweakedspecrequires.txt |uniq >/tmp/sorteduniqspecrequires.txt

# PROVIDES
# Tweak any lines that have = version in them
cp /tmp/specprovides.txt /tmp/tweakedspecprovides.txt
perl -pi -e "s|^(\\S+)\\s\\=\\s.*|\$1|g" /tmp/tweakedspecprovides.txt
# And remove and (mips-32) entries
perl -pi -e "s|^(.+)\\(mips\\-32\\).*|\$1|g" /tmp/tweakedspecprovides.txt

# Now sort it and unique it
sort /tmp/tweakedspecprovides.txt |uniq >/tmp/sorteduniqspecprovides.txt

# Now spit out the missing "provides" by comparison
comm -1 -3 /tmp/sorteduniqspecprovides.txt /tmp/sorteduniqspecrequires.txt >/tmp/missingprovides.txt

echo "We are missing provides for:"
cat /tmp/missingprovides.txt

MISPROVFILE="/tmp/missingprovideslookup.txt"
rm -f "$MISPROVFILE"
while read missingprovide; do
    rpm -q --whatprovides "$missingprovide" >> "$MISPROVFILE"
done </tmp/missingprovides.txt
sort "$MISPROVFILE" |uniq >/tmp/blah.out
mv /tmp/blah.out "$MISPROVFILE"
cat "$MISPROVFILE"

exit 0
