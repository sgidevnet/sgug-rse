#%%global __strip /bin/true

%if 0%{?fedora} && 0%{?fedora} < 30
%bcond_with unversioned_gpg
%else
%bcond_without unversioned_gpg
%endif

Summary: Utility for secure communication and data storage
Name:    gnupg2
Version: 2.2.20
Release: 4%{?dist}

License: GPLv3+
Source0: ftp://ftp.gnupg.org/gcrypt/%{?pre:alpha/}gnupg/gnupg-%{version}%{?pre}.tar.bz2
Source1: ftp://ftp.gnupg.org/gcrypt/%{?pre:alpha/}gnupg/gnupg-%{version}%{?pre}.tar.bz2.sig
Patch1:  gnupg-2.1.21-insttools.patch
# needed for compatibility with system FIPS mode
Patch3:  gnupg-2.1.10-secmem.patch
# non-upstreamable patch adding file-is-digest option needed for Copr
Patch4:  gnupg-2.2.20-file-is-digest.patch
# fix handling of missing key usage on ocsp replies - upstream T1333
Patch5:  gnupg-2.2.16-ocsp-keyusage.patch
Patch6:  gnupg-2.1.1-fips-algo.patch
# allow 8192 bit RSA keys in keygen UI with large RSA
Patch9:  gnupg-2.1.21-large-rsa.patch
# fix missing uid on refresh from keys.openpgp.org
# https://salsa.debian.org/debian/gnupg2/commit/f292beac1171c6c77faf41d1f88c2e0942ed4437
Patch20: gnupg-2.2.18-tests-add-test-cases-for-import-without-uid.patch
Patch21: gnupg-2.2.18-gpg-allow-import-of-previously-known-keys-even-without-UI.patch
Patch22: gnupg-2.2.18-gpg-accept-subkeys-with-a-good-revocation-but-no-self-sig.patch

Patch100: gnupg2.sgifixes.patch

URL:     http://www.gnupg.org/

#BuildRequires: automake libtool texinfo transfig
BuildRequires: gcc
BuildRequires: bzip2-devel
BuildRequires: curl-devel
BuildRequires: docbook-utils
BuildRequires: gettext
BuildRequires: libassuan-devel >= 2.1.0
BuildRequires: libgcrypt-devel >= 1.7.0
BuildRequires: libgpg-error-devel >= 1.31
BuildRequires: libksba-devel >= 1.3.0
#BuildRequires: openldap-devel
#BuildRequires: libusb-devel
#BuildRequires: pcsc-lite-libs
BuildRequires: npth-devel
BuildRequires: readline-devel ncurses-devel
BuildRequires: zlib-devel
BuildRequires: gnutls-devel
BuildRequires: sqlite-devel
#BuildRequires: fuse
BuildRequires: pinentry

Requires: libgcrypt >= 1.7.0
Requires: libgpg-error >= 1.31

Recommends: pinentry

Recommends: gnupg2-smime

%if %{with unversioned_gpg}
# pgp-tools, perl-GnuPG-Interface requires 'gpg' (not sure why) -- Rex
Provides: gpg = %{version}-%{release}
# Obsolete GnuPG-1 package
Provides: gnupg = %{version}-%{release}
Obsoletes: gnupg < 1.4.24
%endif

Provides: dirmngr = %{version}-%{release}
Obsoletes: dirmngr < 1.2.0-1

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

%package smime
Summary: CMS encryption and signing tool and smart card support for GnuPG
Requires: gnupg2 = %{version}-%{release}


%description
GnuPG is GNU''s tool for secure communication and data storage.  It can
be used to encrypt data and to create digital signatures.  It includes
an advanced key management facility and is compliant with the proposed
OpenPGP Internet standard as described in RFC2440 and the S/MIME
standard as described by several RFCs.

GnuPG 2.0 is a newer version of GnuPG with additional support for
S/MIME.  It has a different design philosophy that splits
functionality up into several modules. The S/MIME and smartcard functionality
is provided by the gnupg2-smime package.

%description smime
GnuPG is GNU''s tool for secure communication and data storage. This
package adds support for smart cards and S/MIME encryption and signing
to the base GnuPG package 

%prep
%setup -q -n gnupg-%{version}

%if %{with unversioned_gpg}
%patch1 -p1 -b .insttools
%endif
%patch3 -p1 -b .secmem
%patch4 -p1 -b .file-is-digest
%patch5 -p1 -b .keyusage
%patch6 -p1 -b .fips
%patch9 -p1 -b .large-rsa

%patch20 -p1 -b .test_missing_uid
%patch21 -p1 -b .prev_known_key
%patch22 -p1 -b .good_revoc

#exit 1

%patch100 -p1

# A place to generate the SGUG patch
#exit 1

# Rewrite some hardcoded paths
perl -pi -e "s|/var/run|%{_prefix}/var/run|g" common/homedir.c

# pcsc-lite library major: 0 in 1.2.0, 1 in 1.2.9+ (dlopen()'d in pcsc-wrapper)
# Note: this is just the name of the default shared lib to load in scdaemon,
# it can use other implementations too (including non-pcsc ones).
%global pcsclib %(basename $(ls -1 %{_libdir}/libpcsclite.so.? 2>/dev/null ) 2>/dev/null )

sed -i -e 's/"libpcsclite\.so"/"%{pcsclib}"/' scd/scdaemon.c


%build
export CPPFLAGS="-I%{_includedir}/libdicl-0.1 -D_SGI_SOURCE -D_SGI_REENTRANT_FUNCTIONS"
export LDFLAGS="-ldicl-0.1 -lintl $RPM_LD_FLAGS"
export ac_cv_func_unsetenv=yes
%configure \
%if %{without unversioned_gpg}
  --enable-gpg-is-gpg2 \
%endif
  --disable-gpgtar \
  --enable-g13 \
  --enable-large-secmem

#  --disable-rpath \
#

# need scratch gpg database for tests
mkdir -p $HOME/.gnupg

make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot} \
  INSTALL="install -p" \
  docdir=%{_pkgdocdir}

%if %{without unversioned_gpg}
# rename file conflicting with gnupg-1.x
rename gnupg.7 gnupg2.7 %{buildroot}%{_mandir}/man7/gnupg.7*
%endif

%find_lang %{name}

# gpgconf.conf
mkdir -p %{buildroot}%{_sysconfdir}/gnupg
touch %{buildroot}%{_sysconfdir}/gnupg/gpgconf.conf

# more docs
install -m644 -p AUTHORS NEWS THANKS TODO \
  %{buildroot}%{_pkgdocdir}

%if %{with unversioned_gpg}
# compat symlinks
ln -sf gpg %{buildroot}%{_bindir}/gpg2
ln -sf gpgv %{buildroot}%{_bindir}/gpgv2
ln -sf gpg.1 %{buildroot}%{_mandir}/man1/gpg2.1
ln -sf gpgv.1 %{buildroot}%{_mandir}/man1/gpgv2.1
ln -sf gnupg.7 %{buildroot}%{_mandir}/man7/gnupg2.7
%endif

# info dir
rm -f %{buildroot}%{_infodir}/dir

# drop the gpg scheme interpreter
rm -f %{buildroot}%{_bindir}/gpgscm

# Move the systemd user units to appropriate directory
#install -d -m755 %{buildroot}%{_userunitdir}
#mv %{buildroot}%{_pkgdocdir}/examples/systemd-user/*.socket %{buildroot}%{_userunitdir}
#mv %{buildroot}%{_pkgdocdir}/examples/systemd-user/*.service %{buildroot}%{_userunitdir}

%check
# need scratch gpg database for tests
mkdir -p $HOME/.gnupg
make -k check


%files -f %{name}.lang
%{!?_licensedir:%global license %%doc}
%license COPYING
#doc AUTHORS NEWS README THANKS TODO
%{_pkgdocdir}
%dir %{_sysconfdir}/gnupg
%ghost %config(noreplace) %{_sysconfdir}/gnupg/gpgconf.conf
## docs say to install suid root, but fedora/rh security folk say not to
%{_bindir}/gpg2
%{_bindir}/gpgv2
%{_bindir}/gpg-connect-agent
%{_bindir}/gpg-agent
%{_bindir}/gpgconf
%{_bindir}/gpgparsemail
%{_bindir}/g13
%{_bindir}/dirmngr
%{_bindir}/dirmngr-client
%if %{with unversioned_gpg}
%{_bindir}/gpg
%{_bindir}/gpgv
%{_bindir}/gpgsplit
%{_bindir}/gpg-zip
%endif
%{_bindir}/watchgnupg
%{_bindir}/gpg-wks-server
%{_sbindir}/*
%{_datadir}/gnupg/
%{_libexecdir}/*
%{_infodir}/*.info*
%{_mandir}/man?/*
#%%{_userunitdir}/*
%exclude %{_mandir}/man?/gpgsm*

%files smime
%{_bindir}/gpgsm*
%{_bindir}/kbxutil
%{_mandir}/man?/gpgsm*


%changelog
* Sun Dec 02 2020 Daniel Hams <daniel.hams@gmail.com> - 2.2.20-4
- Fix up the /var/run unix socket to live in /usr/sgug/var/run

* Sun Nov 08 2020 Daniel Hams <daniel.hams@gmail.com> - 2.2.20-3
- Updated now we have pinentry (but leave weak to avoid pulling in gtk)

* Thu Apr 30 2020 Tomáš Mráz <tmraz@redhat.com> - 2.2.20-2
- move systemd user units to _userunitdir (no activation by default)

* Tue Apr 14 2020 Tomáš Mráz <tmraz@redhat.com> - 2.2.20-1
- upgrade to 2.2.20
