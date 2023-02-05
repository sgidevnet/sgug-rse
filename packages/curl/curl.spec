%global debug 0

%if 0%{debug}
%global __strip /bin/true
%endif

# This package is able to use optimised linker flags.
%global build_ldflags %{sgug_optimised_ldflags}

Summary: A utility for getting files from remote servers (FTP, HTTP, and others)
Name: curl
Version: 7.61.0
Release: 4%{?dist}
License: MIT
Source: https://curl.haxx.se/download/%{name}-%{version}.tar.gz

# fix memory leaked by parse_metalink()
#Patch1:   0001-curl-7.66.0-metalink-memleak.patch

# patch making libcurl multilib ready
Patch101: 0101-curl-7.32.0-multilib.patch

# prevent configure script from discarding -g in CFLAGS (#496778)
Patch102: 0102-curl-7.36.0-debug.patch

# migrate tests/http_pipe.py to Python 3
#Patch103: 0103-curl-7.59.0-python3.patch

# use localhost6 instead of ip6-localhost in the curl test-suite
#Patch104: 0104-curl-7.19.7-localhost6.patch

# prevent valgrind from reporting false positives on x86_64
#Patch105: 0105-curl-7.63.0-lib1560-valgrind.patch

Provides: curl-full = %{version}-%{release}
Provides: webclient
URL: https://curl.haxx.se/
BuildRequires: automake
#BuildRequires: brotli-devel
BuildRequires: coreutils
BuildRequires: gcc
BuildRequires: groff
#BuildRequires: krb5-devel
#BuildRequires: libidn2-devel
#BuildRequires: libmetalink-devel
#BuildRequires: libnghttp2-devel
#BuildRequires: libpsl-devel
#BuildRequires: libssh-devel
BuildRequires: make
#BuildRequires: openldap-devel
BuildRequires: openssh-clients
#BuildRequires: openssh-server
BuildRequires: openssl-devel
BuildRequires: perl-interpreter
BuildRequires: pkgconfig
#BuildRequires: python3-devel
BuildRequires: sed
#BuildRequires: stunnel
BuildRequires: zlib-devel

# needed to compress content of tool_hugehelp.c after changing curl.1 man page
BuildRequires: perl(IO::Compress::Gzip)

# needed for generation of shell completions
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(Pod::Usage)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)

# gnutls-serv is used by the upstream test-suite
#BuildRequires: gnutls-utils

# nghttpx (an HTTP/2 proxy) is used by the upstream test-suite
#BuildRequires: nghttp2

# perl modules used in the test suite
BuildRequires: perl(Cwd)
BuildRequires: perl(Digest::MD5)
BuildRequires: perl(Exporter)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Copy)
BuildRequires: perl(File::Spec)
BuildRequires: perl(IPC::Open2)
BuildRequires: perl(MIME::Base64)
BuildRequires: perl(Time::Local)
BuildRequires: perl(Time::HiRes)
BuildRequires: perl(vars)

# The test-suite runs automatically through valgrind if valgrind is available
# on the system.  By not installing valgrind into mock's chroot, we disable
# this feature for production builds on architectures where valgrind is known
# to be less reliable, in order to avoid unnecessary build failures (see RHBZ
# #810992, #816175, and #886891).  Nevertheless developers are free to install
# valgrind manually to improve test coverage on any architecture.
%ifarch x86_64 %{ix86}
BuildRequires: valgrind
%endif

# using an older version of libcurl could result in CURLE_UNKNOWN_OPTION
Requires: libcurl%{?_isa} >= %{version}-%{release}

# require at least the version of libpsl that we were built against,
# to ensure that we have the necessary symbols available (#1631804)
%global libpsl_version %(pkg-config --modversion libpsl 2>/dev/null || echo 0)

# require at least the version of libssh that we were built against,
# to ensure that we have the necessary symbols available (#525002, #642796)
#%global libssh_version %(pkg-config --modversion libssh 2>/dev/null || echo 0)

# require at least the version of openssl-libs that we were built against,
# to ensure that we have the necessary symbols available (#1462184, #1462211)
%global openssl_version %(pkg-config --modversion openssl 2>/dev/null || echo 0)

%description
curl is a command line tool for transferring data with URL syntax, supporting
FTP, FTPS, HTTP, HTTPS, SCP, SFTP, TFTP, TELNET, DICT, LDAP, LDAPS, FILE, IMAP,
SMTP, POP3 and RTSP.  curl supports SSL certificates, HTTP POST, HTTP PUT, FTP
uploading, HTTP form based upload, proxies, cookies, user+password
authentication (Basic, Digest, NTLM, Negotiate, kerberos...), file transfer
resume, proxy tunneling and a busload of other useful tricks. 

%package -n libcurl
Summary: A library for getting files from web servers
#Requires: libpsl%{?_isa} >= %{libpsl_version}
#Requires: libssh%{?_isa} >= %{libssh_version}
Requires: openssl-libs%{?_isa} >= 1:%{openssl_version}
Provides: libcurl-full = %{version}-%{release}
Provides: libcurl-full%{?_isa} = %{version}-%{release}

%description -n libcurl
libcurl is a free and easy-to-use client-side URL transfer library, supporting
FTP, FTPS, HTTP, HTTPS, SCP, SFTP, TFTP, TELNET, DICT, LDAP, LDAPS, FILE, IMAP,
SMTP, POP3 and RTSP. libcurl supports SSL certificates, HTTP POST, HTTP PUT,
FTP uploading, HTTP form based upload, proxies, cookies, user+password
authentication (Basic, Digest, NTLM, Negotiate, Kerberos4), file transfer
resume, http proxy tunneling and more.

%package -n libcurl-devel
Summary: Files needed for building applications with libcurl
Requires: libcurl%{?_isa} = %{version}-%{release}

Provides: curl-devel = %{version}-%{release}
Provides: curl-devel%{?_isa} = %{version}-%{release}
Obsoletes: curl-devel < %{version}-%{release}

%description -n libcurl-devel
The libcurl-devel package includes header files and libraries necessary for
developing programs which use the libcurl library. It contains the API
documentation of the library, too.

#%package -n curl-minimal
#Summary: Conservatively configured build of curl for minimal installations
#Provides: curl = %{version}-%{release}
#Conflicts: curl
#RemovePathPostfixes: .minimal

# using an older version of libcurl could result in CURLE_UNKNOWN_OPTION
#Requires: libcurl%{?_isa} >= %{version}-%{release}

#%description -n curl-minimal
#This is a replacement of the 'curl' package for minimal installations.  It
#comes with a limited set of features compared to the 'curl' package.  On the
#other hand, the package is smaller and requires fewer run-time dependencies to
#be installed.

#%package -n libcurl-minimal
#Summary: Conservatively configured build of libcurl for minimal installations
#Requires: openssl-libs%{?_isa} >= 1:%{openssl_version}
#Provides: libcurl = %{version}-%{release}
#Provides: libcurl%{?_isa} = %{version}-%{release}
#Conflicts: libcurl
#RemovePathPostfixes: .minimal
# needed for RemovePathPostfixes to work with shared libraries
#%undefine __brp_ldconfig

#%description -n libcurl-minimal
#This is a replacement of the 'libcurl' package for minimal installations.  It
#comes with a limited set of features compared to the 'libcurl' package.  On the
#other hand, the package is smaller and requires fewer run-time dependencies to
#be installed.

%prep
%setup -q

# upstream patches
#%patch1 -p1

# Fedora patches
%patch101 -p1
%patch102 -p1
#%patch103 -p1
#%patch104 -p1
#%patch105 -p1

# make tests/*.py use Python 3
sed -e '1 s|^#!/.*python|#!%{__python3}|' -i tests/*.py

# regenerate Makefile.in files
aclocal -I m4
automake

# disable test 1112 (#565305), test 1455 (occasionally fails with 'bind failed
# with errno 98: Address already in use' in Koji environment), and test 1801
# <https://github.com/bagder/curl/commit/21e82bd6#commitcomment-12226582>
# and test 1900, which is flaky and covers a deprecated feature of libcurl
# <https://github.com/curl/curl/pull/2705>
printf "1112\n1455\n1801\n1900\n" >> tests/data/DISABLED

# disable test 1319 on ppc64 (server times out)
%ifarch ppc64
echo "1319" >> tests/data/DISABLED
%endif

# temporarily disable test 582 on s390x (client times out)
%ifarch s390x
echo "582" >> tests/data/DISABLED
%endif

# adapt test 323 for updated OpenSSL
sed -e 's/^35$/35,52/' -i tests/data/test323

%build

#mkdir build-{full,minimal}
mkdir build-full
export common_configure_opts=" \
    --disable-static \
    --enable-symbol-hiding \
    --with-ssl --with-ca-bundle=%{_sysconfdir}/pki/tls/certs/ca-bundle.crt"

#    --cache-file=../config.cache \ #
#     --enable-ipv6 \ #
#     --enable-threaded-resolver \ #
#     --with-gssapi \ #
#     --with-nghttp2 \ #
 
%global _configure ../configure

# configure minimal build
#(
#    cd build-minimal
#    %%configure $common_configure_opts \
#        --disable-ldap \
#        --disable-ldaps \
#        --disable-manual \
#        --without-brotli \
#        --without-libidn2 \
#        --without-libmetalink \
#        --without-libpsl \
#        --without-libssh
#)
%if 0%{debug}
export CFLAGS="-g -O0"
export CXXFLAGS="$CFLAGS"
export LDFLAGS="-Wl,-z,relro -Wl,-z,now"
%endif

# configure full build
(
    cd build-full
    %configure $common_configure_opts \
        --disable-ldap \
        --disable-ldaps \
        --enable-manual \
        --without-brotli \
        --with-libidn2 \
        --without-libmetalink \
        --without-libpsl \
        --with-libssh

#         --enable-ldap \ #
#         --enable-ldaps \ #
#         --with-brotli \ #
#         --with-libidn2 \ #
#         --with-libmetalink \ #
#         --with-libpsl \ #
#        --with-libssh #
)

# avoid using rpath
#sed -e 's/^runpath_var=.*/runpath_var=/' \
#    -e 's/^hardcode_libdir_flag_spec=".*"$/hardcode_libdir_flag_spec=""/' \
#    -i build-{full,minimal}/libtool

#make %{?_smp_mflags} V=1 -C build-minimal
make %{?_smp_mflags} V=1 -C build-full

%check

# we have to override LD_LIBRARY_PATH because we eliminated rpath
LD_LIBRARYN32_PATH="$RPM_BUILD_ROOT%{_libdir}:$LD_LIBRARYN32_PATH"
export LD_LIBRARYN32_PATH

# compile upstream test-cases
cd build-full/tests
make %{?_smp_mflags} V=1

# relax crypto policy for the test-suite to make it pass again (#1610888)
export OPENSSL_SYSTEM_CIPHERS_OVERRIDE=XXX
export OPENSSL_CONF=

# run the upstream test-suite
srcdir=../../tests perl -I../../tests ../../tests/runtests.pl -a -p -v '!flaky'

%install

## install and rename the library that will be packaged as libcurl-minimal
#make DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p" install -C build-minimal/lib
#rm -f ${RPM_BUILD_ROOT}%{_libdir}/libcurl.{la,so}
#for i in ${RPM_BUILD_ROOT}%{_libdir}/*; do
#    mv -v $i $i.minimal
#done
#
## install and rename the executable that will be packaged as curl-minimal
#make DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p" install -C build-minimal/src
#mv -v ${RPM_BUILD_ROOT}%{_bindir}/curl{,.minimal}

# install libcurl.m4
install -d $RPM_BUILD_ROOT%{_datadir}/aclocal
install -m 644 docs/libcurl/libcurl.m4 $RPM_BUILD_ROOT%{_datadir}/aclocal

# install the executable and library that will be packaged as curl and libcurl
cd build-full
make DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p" install

# install zsh completion for curl
# (we have to override LD_LIBRARY_PATH because we eliminated rpath)
LD_LIBRARY_PATH="$RPM_BUILD_ROOT%{_libdir}:$LD_LIBRARY_PATH" \
    make DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p" install -C scripts

# do not install /usr/share/fish/completions/curl.fish which is also installed
# by fish-3.0.2-1.module_f31+3716+57207597 and would trigger a conflict
rm -rf ${RPM_BUILD_ROOT}%{_datadir}/fish

rm -f ${RPM_BUILD_ROOT}%{_libdir}/libcurl.la

#%ldconfig_scriptlets -n libcurl

#%ldconfig_scriptlets -n libcurl-minimal

%files
%doc CHANGES
%doc README
%doc docs/BUGS
%doc docs/FAQ
%doc docs/FEATURES
%doc docs/RESOURCES
%doc docs/TODO
%doc docs/TheArtOfHttpScripting
%{_bindir}/curl
%{_mandir}/man1/curl.1*
%{_datadir}/zsh

%files -n libcurl
%license COPYING
%{_libdir}/libcurl.so.4
%{_libdir}/libcurl.so.4.[0-9].[0-9]

%files -n libcurl-devel
%doc docs/examples/*.c docs/examples/Makefile.example docs/INTERNALS.md
%doc docs/CONTRIBUTE.md docs/libcurl/ABI
%{_bindir}/curl-config*
%{_includedir}/curl
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man1/curl-config.1*
%{_mandir}/man3/*
%{_datadir}/aclocal/libcurl.m4

#%files -n curl-minimal
#%{_bindir}/curl.minimal
#%{_mandir}/man1/curl.1*

#%files -n libcurl-minimal
#%license COPYING
#%{_libdir}/libcurl.so.4.minimal
#%{_libdir}/libcurl.so.4.[0-9].[0-9].minimal

%changelog
* Sun Aug 30 2020 Daniel Hams <daniel.hams@gmail.com> - 7.61.0-4
- Enable libidn2, libssh, switch for debug non-stripped lib in the spec

* Fri Apr 10 2020 Daniel Hams <daniel.hams@gmail.com> - 7.61.0-3
- Disable curl-minimal, libcurl-minimal

* Wed Sep 11 2019 Kamil Dudka <kdudka@redhat.com> - 7.66.0-1
- new upstream release, which fixes the following vulnerabilities
    CVE-2019-5481 - double free due to subsequent call of realloc()
    CVE-2019-5482 - heap buffer overflow in function tftp_receive_packet()

* Tue Aug 27 2019 Kamil Dudka <kdudka@redhat.com> - 7.65.3-4
- avoid reporting spurious error in the HTTP2 framing layer (#1690971)

* Thu Aug 01 2019 Kamil Dudka <kdudka@redhat.com> - 7.65.3-3
- improve handling of gss_init_sec_context() failures

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.65.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 20 2019 Paul Howarth <paul@city-fan.org> - 7.65.3-1
- new upstream release

* Wed Jul 17 2019 Kamil Dudka <kdudka@redhat.com> - 7.65.2-1
- new upstream release

* Wed Jun 05 2019 Kamil Dudka <kdudka@redhat.com> - 7.65.1-1
- new upstream release

* Thu May 30 2019 Kamil Dudka <kdudka@redhat.com> - 7.65.0-2
- fix spurious timeout events with speed-limit (#1714893)

* Wed May 22 2019 Kamil Dudka <kdudka@redhat.com> - 7.65.0-1
- new upstream release, which fixes the following vulnerabilities
    CVE-2019-5436 - TFTP receive buffer overflow
    CVE-2019-5435 - integer overflows in curl_url_set()

* Thu May 09 2019 Kamil Dudka <kdudka@redhat.com> - 7.64.1-2
- do not treat failure of gss_init_sec_context() with --negotiate as fatal
