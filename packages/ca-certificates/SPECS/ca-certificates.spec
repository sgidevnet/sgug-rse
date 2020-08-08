# This package is able to use optimised linker flags.
%global build_ldflags %{sgug_optimised_ldflags}

%define pkidir %{_sysconfdir}/pki
%define catrustdir %{_sysconfdir}/pki/ca-trust
%define classic_tls_bundle ca-bundle.crt
%define openssl_format_trust_bundle ca-bundle.trust.crt
%define p11_format_bundle ca-bundle.trust.p11-kit
%define legacy_default_bundle ca-bundle.legacy.default.crt
%define legacy_disable_bundle ca-bundle.legacy.disable.crt
%define java_bundle java/cacerts

Summary: The Mozilla CA root certificate bundle
Name: ca-certificates

# For the package version number, we use: year.{upstream version}
#
# The {upstream version} can be found as symbol
# NSS_BUILTINS_LIBRARY_VERSION in file nss/lib/ckfw/builtins/nssckbi.h
# which corresponds to the data in file nss/lib/ckfw/builtins/certdata.txt.
#
# The files should be taken from a released version of NSS, as published
# at https://ftp.mozilla.org/pub/mozilla.org/security/nss/releases/
#
# The versions that are used by the latest released version of 
# Mozilla Firefox should be available from:
# https://hg.mozilla.org/releases/mozilla-release/raw-file/default/security/nss/lib/ckfw/builtins/nssckbi.h
# https://hg.mozilla.org/releases/mozilla-release/raw-file/default/security/nss/lib/ckfw/builtins/certdata.txt
#
# The most recent development versions of the files can be found at
# http://hg.mozilla.org/projects/nss/raw-file/default/lib/ckfw/builtins/nssckbi.h
# http://hg.mozilla.org/projects/nss/raw-file/default/lib/ckfw/builtins/certdata.txt
# (but these files might have not yet been released).
#
# (until 2012.87 the version was based on the cvs revision ID of certdata.txt,
# but in 2013 the NSS projected was migrated to HG. Old version 2012.87 is 
# equivalent to new version 2012.1.93, which would break the requirement 
# to have increasing version numbers. However, the new scheme will work, 
# because all future versions will start with 2013 or larger.)

Version: 2020.2.40
# for Rawhide, please always use release >= 2
# for Fedora release branches, please use release < 2 (1.0, 1.1, ...)
Release: 1.1%{?dist}
License: Public Domain

URL: https://fedoraproject.org/wiki/CA-Certificates

#Please always update both certdata.txt and nssckbi.h
Source0: certdata.txt
Source1: nssckbi.h
Source2: update-ca-trust
Source3: trust-fixes
Source4: certdata2pem.py
Source5: ca-legacy.conf
Source6: ca-legacy
Source9: ca-legacy.8.txt
Source10: update-ca-trust.8.txt
Source11: README.usr
Source12: README.etc
Source13: README.extr
Source14: README.java
Source15: README.openssl
Source16: README.pem
Source17: README.edk2
Source18: README.src

BuildArch: noarch

Requires(post): bash
Requires(post): grep
Requires(post): sed
Requires(post): coreutils
Requires: bash
Requires: grep
Requires: sed
Requires(post): p11-kit >= 0.23.16
Requires(post): p11-kit-trust >= 0.23.16
Requires: p11-kit >= 0.23.16
Requires: p11-kit-trust >= 0.23.16

BuildRequires: perl-interpreter
BuildRequires: python3
BuildRequires: openssl
BuildRequires: asciidoc
BuildRequires: libxslt

%description
This package contains the set of CA certificates chosen by the
Mozilla Foundation for use with the Internet PKI.

%prep
rm -rf %{name}
mkdir %{name}
mkdir %{name}/certs
mkdir %{name}/certs/legacy-default
mkdir %{name}/certs/legacy-disable
mkdir %{name}/java

%build
export PREV_WD=`pwd`
cd %{name}/certs
 pwd
 cp %{SOURCE0} .
 python3 %{SOURCE4} >c2p.log 2>c2p.err
cd $PREV_WD
cd %{name}
 (
   cat <<EOF
# This is a bundle of X.509 certificates of public Certificate
# Authorities.  It was generated from the Mozilla root CA list.
# These certificates and trust/distrust attributes use the file format accepted
# by the p11-kit-trust module.
#
# Source: nss/lib/ckfw/builtins/certdata.txt
# Source: nss/lib/ckfw/builtins/nssckbi.h
#
# Generated from:
EOF
   cat %{SOURCE1}  |grep -w NSS_BUILTINS_LIBRARY_VERSION | awk '{print "# " $2 " " $3}';
   echo '#';
 ) > %{p11_format_bundle}

 touch %{legacy_default_bundle}
 NUM_LEGACY_DEFAULT=`find certs/legacy-default -type f | wc -l`
 if [ $NUM_LEGACY_DEFAULT -ne 0 ]; then
     for f in certs/legacy-default/*.crt; do 
       echo "processing $f"
       tbits=`sed -n '/^# openssl-trust/{s/^.*=//;p;}' $f`
       alias=`sed -n '/^# alias=/{s/^.*=//;p;q;}' $f | sed "s/'//g" | sed 's/"//g'`
       targs=""
       if [ -n "$tbits" ]; then
          for t in $tbits; do
             targs="${targs} -addtrust $t"
          done
       fi
       if [ -n "$targs" ]; then
          echo "legacy default flags $targs for $f" >> info.trust
          openssl x509 -text -in "$f" -trustout $targs -setalias "$alias" >> %{legacy_default_bundle}
       fi
     done
 fi

 touch %{legacy_disable_bundle}
 NUM_LEGACY_DISABLE=`find certs/legacy-disable -type f | wc -l`
 if [ $NUM_LEGACY_DISABLE -ne 0 ]; then
     for f in certs/legacy-disable/*.crt; do 
       echo "processing $f"
       tbits=`sed -n '/^# openssl-trust/{s/^.*=//;p;}' $f`
       alias=`sed -n '/^# alias=/{s/^.*=//;p;q;}' $f | sed "s/'//g" | sed 's/"//g'`
       targs=""
       if [ -n "$tbits" ]; then
          for t in $tbits; do
             targs="${targs} -addtrust $t"
          done
       fi
       if [ -n "$targs" ]; then
          echo "legacy disable flags $targs for $f" >> info.trust
          openssl x509 -text -in "$f" -trustout $targs -setalias "$alias" >> %{legacy_disable_bundle}
       fi
     done
 fi

 P11FILES=`find certs -name \*.tmp-p11-kit | wc -l`
 if [ $P11FILES -ne 0 ]; then
   for p in certs/*.tmp-p11-kit; do 
     cat "$p" >> %{p11_format_bundle}
   done
 fi
 # Append our trust fixes
 cat %{SOURCE3} >> %{p11_format_bundle}
cd $PREV_WD

#manpage
cp %{SOURCE10} %{name}/update-ca-trust.8.txt
asciidoc.py -v -d manpage -b docbook %{name}/update-ca-trust.8.txt
xsltproc --nonet -o %{name}/update-ca-trust.8 %{_datadir}/asciidoc/docbook-xsl/manpage.xsl %{name}/update-ca-trust.8.xml

cp %{SOURCE9} %{name}/ca-legacy.8.txt
asciidoc.py -v -d manpage -b docbook %{name}/ca-legacy.8.txt
xsltproc --nonet -o %{name}/ca-legacy.8 %{_datadir}/asciidoc/docbook-xsl/manpage.xsl %{name}/ca-legacy.8.xml


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p -m 755 $RPM_BUILD_ROOT%{pkidir}/tls/certs
mkdir -p -m 755 $RPM_BUILD_ROOT%{pkidir}/java
mkdir -p -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/ssl
mkdir -p -m 755 $RPM_BUILD_ROOT%{catrustdir}/source
mkdir -p -m 755 $RPM_BUILD_ROOT%{catrustdir}/source/anchors
mkdir -p -m 755 $RPM_BUILD_ROOT%{catrustdir}/source/blacklist
mkdir -p -m 755 $RPM_BUILD_ROOT%{catrustdir}/extracted
mkdir -p -m 755 $RPM_BUILD_ROOT%{catrustdir}/extracted/pem
mkdir -p -m 755 $RPM_BUILD_ROOT%{catrustdir}/extracted/openssl
mkdir -p -m 755 $RPM_BUILD_ROOT%{catrustdir}/extracted/java
mkdir -p -m 755 $RPM_BUILD_ROOT%{catrustdir}/extracted/edk2
mkdir -p -m 755 $RPM_BUILD_ROOT%{_datadir}/pki/ca-trust-source
mkdir -p -m 755 $RPM_BUILD_ROOT%{_datadir}/pki/ca-trust-source/anchors
mkdir -p -m 755 $RPM_BUILD_ROOT%{_datadir}/pki/ca-trust-source/blacklist
mkdir -p -m 755 $RPM_BUILD_ROOT%{_datadir}/pki/ca-trust-legacy
mkdir -p -m 755 $RPM_BUILD_ROOT%{_bindir}
mkdir -p -m 755 $RPM_BUILD_ROOT%{_mandir}/man8

install -p -m 644 %{name}/update-ca-trust.8 $RPM_BUILD_ROOT%{_mandir}/man8
install -p -m 644 %{name}/ca-legacy.8 $RPM_BUILD_ROOT%{_mandir}/man8
install -p -m 644 %{SOURCE11} $RPM_BUILD_ROOT%{_datadir}/pki/ca-trust-source/README
install -p -m 644 %{SOURCE12} $RPM_BUILD_ROOT%{catrustdir}/README
install -p -m 644 %{SOURCE13} $RPM_BUILD_ROOT%{catrustdir}/extracted/README
install -p -m 644 %{SOURCE14} $RPM_BUILD_ROOT%{catrustdir}/extracted/java/README
install -p -m 644 %{SOURCE15} $RPM_BUILD_ROOT%{catrustdir}/extracted/openssl/README
install -p -m 644 %{SOURCE16} $RPM_BUILD_ROOT%{catrustdir}/extracted/pem/README
install -p -m 644 %{SOURCE17} $RPM_BUILD_ROOT%{catrustdir}/extracted/edk2/README
install -p -m 644 %{SOURCE18} $RPM_BUILD_ROOT%{catrustdir}/source/README

install -p -m 644 %{name}/%{p11_format_bundle} $RPM_BUILD_ROOT%{_datadir}/pki/ca-trust-source/%{p11_format_bundle}

install -p -m 644 %{name}/%{legacy_default_bundle} $RPM_BUILD_ROOT%{_datadir}/pki/ca-trust-legacy/%{legacy_default_bundle}
install -p -m 644 %{name}/%{legacy_disable_bundle} $RPM_BUILD_ROOT%{_datadir}/pki/ca-trust-legacy/%{legacy_disable_bundle}

install -p -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{catrustdir}/ca-legacy.conf

touch -r %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/pki/ca-trust-source/%{p11_format_bundle}

touch -r %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/pki/ca-trust-legacy/%{legacy_default_bundle}
touch -r %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/pki/ca-trust-legacy/%{legacy_disable_bundle}

# TODO: consider to dynamically create the update-ca-trust script from within
#       this .spec file, in order to have the output file+directory names at once place only.
install -p -m 755 %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/update-ca-trust
# Rewrites
perl -pi -e "s|/bin/sh|%{_bindir}/sh|g" $RPM_BUILD_ROOT%{_bindir}/update-ca-trust
perl -pi -e "s|/usr/bin/p11-kit|%{_bindir}/p11-kit|g" $RPM_BUILD_ROOT%{_bindir}/update-ca-trust
perl -pi -e "s|/etc/pki/ca-trust|%{_prefix}/etc/pki/ca-trust|g" $RPM_BUILD_ROOT%{_bindir}/update-ca-trust

install -p -m 755 %{SOURCE6} $RPM_BUILD_ROOT%{_bindir}/ca-legacy
# Rewrites
perl -pi -e "s|/bin/sh|%{_bindir}/sh|g" $RPM_BUILD_ROOT%{_bindir}/ca-legacy
perl -pi -e "s|/usr/bin/|%{_bindir}/|g" $RPM_BUILD_ROOT%{_bindir}/ca-legacy
perl -pi -e "s|/etc/pki/ca-trust|%{_prefix}/etc/pki/ca-trust|g" $RPM_BUILD_ROOT%{_bindir}/ca-legacy
perl -pi -e "s|/usr/share/pki/|%{_datadir}/pki/|g" $RPM_BUILD_ROOT%{_bindir}/ca-legacy

# touch ghosted files that will be extracted dynamically
# Set chmod 444 to use identical permission
touch $RPM_BUILD_ROOT%{catrustdir}/extracted/pem/tls-ca-bundle.pem
chmod 444 $RPM_BUILD_ROOT%{catrustdir}/extracted/pem/tls-ca-bundle.pem
touch $RPM_BUILD_ROOT%{catrustdir}/extracted/pem/email-ca-bundle.pem
chmod 444 $RPM_BUILD_ROOT%{catrustdir}/extracted/pem/email-ca-bundle.pem
touch $RPM_BUILD_ROOT%{catrustdir}/extracted/pem/objsign-ca-bundle.pem
chmod 444 $RPM_BUILD_ROOT%{catrustdir}/extracted/pem/objsign-ca-bundle.pem
touch $RPM_BUILD_ROOT%{catrustdir}/extracted/openssl/%{openssl_format_trust_bundle}
chmod 444 $RPM_BUILD_ROOT%{catrustdir}/extracted/openssl/%{openssl_format_trust_bundle}
touch $RPM_BUILD_ROOT%{catrustdir}/extracted/%{java_bundle}
chmod 444 $RPM_BUILD_ROOT%{catrustdir}/extracted/%{java_bundle}
touch $RPM_BUILD_ROOT%{catrustdir}/extracted/edk2/cacerts.bin
chmod 444 $RPM_BUILD_ROOT%{catrustdir}/extracted/edk2/cacerts.bin

# /etc/ssl/certs symlink for 3rd-party tools
ln -s ../pki/tls/certs \
    $RPM_BUILD_ROOT%{_sysconfdir}/ssl/certs
# legacy filenames
ln -s %{catrustdir}/extracted/pem/tls-ca-bundle.pem \
    $RPM_BUILD_ROOT%{pkidir}/tls/cert.pem
ln -s %{catrustdir}/extracted/pem/tls-ca-bundle.pem \
    $RPM_BUILD_ROOT%{pkidir}/tls/certs/%{classic_tls_bundle}
ln -s %{catrustdir}/extracted/openssl/%{openssl_format_trust_bundle} \
    $RPM_BUILD_ROOT%{pkidir}/tls/certs/%{openssl_format_trust_bundle}
ln -s %{catrustdir}/extracted/%{java_bundle} \
    $RPM_BUILD_ROOT%{pkidir}/%{java_bundle}


%pre
if [ $1 -gt 1 ] ; then
  # Upgrade or Downgrade.
  # If the classic filename is a regular file, then we are upgrading
  # from an old package and we will move it to an .rpmsave backup file.
  # If the filename is a symbolic link, then we are good already.
  # If the system will later be downgraded to an old package with regular 
  # files, and afterwards updated again to a newer package with symlinks,
  # and the old .rpmsave backup file didn't get cleaned up,
  # then we don't backup again. We keep the older backup file.
  # In other words, if an .rpmsave file already exists, we don't overwrite it.
  #
  if ! test -e %{pkidir}/%{java_bundle}.rpmsave; then
    # no backup yet
    if test -e %{pkidir}/%{java_bundle}; then
      # a file exists
        if ! test -L %{pkidir}/%{java_bundle}; then
        # it's an old regular file, not a link
        mv -f %{pkidir}/%{java_bundle} %{pkidir}/%{java_bundle}.rpmsave
      fi
    fi
  fi

  if ! test -e %{pkidir}/tls/certs/%{classic_tls_bundle}.rpmsave; then
    # no backup yet
    if test -e %{pkidir}/tls/certs/%{classic_tls_bundle}; then
      # a file exists
      if ! test -L %{pkidir}/tls/certs/%{classic_tls_bundle}; then
        # it's an old regular file, not a link
        mv -f %{pkidir}/tls/certs/%{classic_tls_bundle} %{pkidir}/tls/certs/%{classic_tls_bundle}.rpmsave
      fi
    fi
  fi

  if ! test -e %{pkidir}/tls/certs/%{openssl_format_trust_bundle}.rpmsave; then
    # no backup yet
    if test -e %{pkidir}/tls/certs/%{openssl_format_trust_bundle}; then
      # a file exists
      if ! test -L %{pkidir}/tls/certs/%{openssl_format_trust_bundle}; then
        # it's an old regular file, not a link
        mv -f %{pkidir}/tls/certs/%{openssl_format_trust_bundle} %{pkidir}/tls/certs/%{openssl_format_trust_bundle}.rpmsave
      fi
    fi
  fi
fi


%post
#if [ $1 -gt 1 ] ; then
#  # when upgrading or downgrading
#fi
%{_bindir}/ca-legacy install
%{_bindir}/update-ca-trust


%files
%dir %{_sysconfdir}/ssl
%dir %{pkidir}/tls
%dir %{pkidir}/tls/certs
%dir %{pkidir}/java
%dir %{catrustdir}
%dir %{catrustdir}/source
%dir %{catrustdir}/source/anchors
%dir %{catrustdir}/source/blacklist
%dir %{catrustdir}/extracted
%dir %{catrustdir}/extracted/pem
%dir %{catrustdir}/extracted/openssl
%dir %{catrustdir}/extracted/java
%dir %{_datadir}/pki
%dir %{_datadir}/pki/ca-trust-source
%dir %{_datadir}/pki/ca-trust-source/anchors
%dir %{_datadir}/pki/ca-trust-source/blacklist
%dir %{_datadir}/pki/ca-trust-legacy

%config(noreplace) %{catrustdir}/ca-legacy.conf

%{_mandir}/man8/update-ca-trust.8.gz
%{_mandir}/man8/ca-legacy.8.gz
%{_datadir}/pki/ca-trust-source/README
%{catrustdir}/README
%{catrustdir}/extracted/README
%{catrustdir}/extracted/java/README
%{catrustdir}/extracted/openssl/README
%{catrustdir}/extracted/pem/README
%{catrustdir}/extracted/edk2/README
%{catrustdir}/source/README

# symlinks for old locations
%{pkidir}/tls/cert.pem
%{pkidir}/tls/certs/%{classic_tls_bundle}
%{pkidir}/tls/certs/%{openssl_format_trust_bundle}
%{pkidir}/%{java_bundle}
# symlink directory
%{_sysconfdir}/ssl/certs

# master bundle file with trust
%{_datadir}/pki/ca-trust-source/%{p11_format_bundle}

%{_datadir}/pki/ca-trust-legacy/%{legacy_default_bundle}
%{_datadir}/pki/ca-trust-legacy/%{legacy_disable_bundle}
# update/extract tool
%{_bindir}/update-ca-trust
%{_bindir}/ca-legacy
%ghost %{catrustdir}/source/ca-bundle.legacy.crt
# files extracted files
%ghost %{catrustdir}/extracted/pem/tls-ca-bundle.pem
%ghost %{catrustdir}/extracted/pem/email-ca-bundle.pem
%ghost %{catrustdir}/extracted/pem/objsign-ca-bundle.pem
%ghost %{catrustdir}/extracted/openssl/%{openssl_format_trust_bundle}
%ghost %{catrustdir}/extracted/%{java_bundle}
%ghost %{catrustdir}/extracted/edk2/cacerts.bin


%changelog
* Sat Jun 13 2020 Daniel Hams <daniel.hams@gmail.com> - 2020.2.40-1.1
- Upgrade to 2020 ca certs bundle and enable local processing using python

* Tue Jan 28 2020 Daiki Ueno <dueno@redhat.com> - 2020.2.40-1.1
- Update versioned dependency on p11-kit

*Thu Jan 23 2020 Daiki Ueno <dueno@redhat.com> - 2020.2.40-1.0
- Update to CKBI 2.40 from NSS 3.48
-    Removing:
-     # Certificate "UTN USERFirst Email Root CA"
-     # Certificate "Certplus Class 2 Primary CA"
-     # Certificate "Deutsche Telekom Root CA 2"
-     # Certificate "Swisscom Root CA 2"
-     # Certificate "Certinomis - Root CA"
-    Adding:
-     # Certificate "Entrust Root Certification Authority - G4"

* Fri Apr 10 2020 Daniel Hams <daniel.hams@gmail.com> - 2019.2.32-4
- Remove hard coded shell paths, bashisms

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.2.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

*Wed Jun 19 2019 Bob Relyea <rrelyea@redhat.com> 2019.2.32-2
 - Update to CKBI 2.32 from NSS 3.44
   Removing: 
    # Certificate "Visa eCommerce Root"
    # Certificate "AC Raiz Certicamara S.A."
    # Certificate "Certplus Root CA G1"
    # Certificate "Certplus Root CA G2"
    # Certificate "OpenTrust Root CA G1"
    # Certificate "OpenTrust Root CA G2"
    # Certificate "OpenTrust Root CA G3"
   Adding: 
    # Certificate "GTS Root R1"
    # Certificate "GTS Root R2"
    # Certificate "GTS Root R3"
    # Certificate "GTS Root R4"
    # Certificate "UCA Global G2 Root"
    # Certificate "UCA Extended Validation Root"
    # Certificate "Certigna Root CA"
    # Certificate "emSign Root CA - G1"
    # Certificate "emSign ECC Root CA - G3"
    # Certificate "emSign Root CA - C1"
    # Certificate "emSign ECC Root CA - C3"
    # Certificate "Hongkong Post Root CA 3"

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.2.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 24 2018 Bob Relyea <rrelyea@redhat.com> - 2018.2.26-2
- Update to CKBI 2.26 from NSS 3.39
