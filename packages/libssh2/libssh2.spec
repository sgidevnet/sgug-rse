Name:		libssh2
Version:	1.9.0
Release:	4%{?dist}
Summary:	A library implementing the SSH2 protocol
License:	BSD
URL:		http://www.libssh2.org/
Source0:	http://libssh2.org/download/libssh2-%{version}.tar.gz

# fix integer overflow in SSH_MSG_DISCONNECT logic (CVE-2019-17498)
Patch1:     0001-libssh2-1.9.0-CVE-2019-17498.patch

BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	openssl-devel > 1:1.0.1
BuildRequires:	sed
BuildRequires:	zlib-devel
BuildRequires:	/usr/sgug/bin/man

# Test suite requirements - we run the OpenSSH server and try to connect to it
BuildRequires:	openssh-server
# Need a valid locale to run the mansyntax check
%if 0%{?fedora} > 23 || 0%{?rhel} > 7
BuildRequires:	glibc-langpack-en
%endif

%description
libssh2 is a library implementing the SSH2 protocol as defined by
Internet Drafts: SECSH-TRANS(22), SECSH-USERAUTH(25),
SECSH-CONNECTION(23), SECSH-ARCH(20), SECSH-FILEXFER(06)*,
SECSH-DHGEX(04), and SECSH-NUMBERS(10).

%package	devel
Summary:	Development files for libssh2
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	pkgconfig

%description	devel
The libssh2-devel package contains libraries and header files for
developing applications that use libssh2.

%package	docs
Summary:	Documentation for libssh2
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	docs
The libssh2-docs package contains man pages and examples for
developing applications that use libssh2.

%prep
%setup -q
%patch1 -p1

# Replace hard wired port number in the test suite to avoid collisions
# between 32-bit and 64-bit builds running on a single build-host
sed -i s/4711/47%{__isa_bits}/ tests/ssh2.{c,sh}

# Rewrite hardcoded paths
perl -pi -e "s|/bin/sh|%{_bindir}/sh|g" test-driver
perl -pi -e "s|/bin/sh|%{_bindir}/sh|g" tests/*.sh
perl -pi -e "s|/bin/sh|%{_bindir}/sh|g" tests/*.sh.in

%build
%configure --disable-silent-rules --disable-static --enable-shared
%{make_build}

%install
%{make_install} INSTALL="install -p"
find %{buildroot} -name '*.la' -delete

# clean things up a bit for packaging
make -C example clean
rm -rf example/.deps
find example/ -type f '(' -name '*.am' -o -name '*.in' ')' -delete

# avoid multilib conflict on libssh2-devel
mv -v example example.%{_arch}

%check
echo "Running tests for %{_arch}"
# The SSH test will fail if we don't have /dev/tty, as is the case in some
# versions of mock (#672713)
if [ ! -c /dev/tty ]; then
	echo Skipping SSH test due to missing /dev/tty
	echo "exit 0" > tests/ssh2.sh
fi
# Apparently it fails in the sparc and arm buildsystems too
%ifarch %{sparc} %{arm}
echo Skipping SSH test on sparc/arm
echo "exit 0" > tests/ssh2.sh
%endif
# mansyntax check fails on PPC* and aarch64 with some strange locale error
%ifarch ppc %{power64} aarch64
echo "Skipping mansyntax test on PPC* and aarch64"
echo "exit 0" > tests/mansyntax.sh
%endif
#LC_ALL=en_US.UTF-8 make -C tests check
LC_ALL=C make -C tests check

#%%ldconfig_scriptlets

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc docs/AUTHORS README RELEASE-NOTES
%{_libdir}/libssh2.so.1
%{_libdir}/libssh2.so.1.*

%files docs
%doc docs/BINDINGS docs/HACKING docs/TODO NEWS
%{_mandir}/man3/libssh2_*.3*

%files devel
%doc example.%{_arch}/
%{_includedir}/libssh2.h
%{_includedir}/libssh2_publickey.h
%{_includedir}/libssh2_sftp.h
%{_libdir}/libssh2.so
%{_libdir}/pkgconfig/libssh2.pc

%changelog
* Sat Oct 10 2020 Daniel Hams <daniel.hams@gmail.com> - 1.9.0-4
- Upgrade to latest fc31, get all tests working, clean up some hardcoded paths

* Sun Jun 07 2020  Alexander Tafarte <notes2@gmx.de> - 1.9.0-3
- compiles on Irix 6.5 with sgug-rse gcc 9.2, compile with --nocheck since 1 test fails.

* Wed Oct 30 2019 Kamil Dudka <kdudka@redhat.com> - 1.9.0-3
- fix integer overflow in SSH_MSG_DISCONNECT logic (CVE-2019-17498)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild
