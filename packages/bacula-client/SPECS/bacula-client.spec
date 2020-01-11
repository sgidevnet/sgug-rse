Summary: Bacula Client
Name: bacula-client
Version: 9.4.4
Release: 1%{?dist}
License: AGPLv3 with exceptions
URL: http://www.bacula.org
Source: http://downloads.sourceforge.net/bacula/bacula-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: automake, autoconf, libtool, pkgconfig

%description
Bacula is a set of programs that allow you to manage the backup, recovery, and
verification of computer data across a network of different computers. It is
based on a client/server architecture and is efficient and relatively easy to
use, while offering many advanced storage management features that make it easy
to find and recover lost or damaged files.

%prep
%setup -n bacula-%{version}
%patch0 -p1 -b .libtool-irix-fix

%build
export SHELL=%{_bindir}/sh
export SHELL_PATH="$SHELL"
export CONFIG_SHELL="$CONFIG_SHELL"
export LDFLAGS="-lpthread $RPM_LD_FLAGS"
#pushd autoconf
#aclocal -I bacula-macros/ -I gettext-macros/ -I libtool/
#popd
#autoconf -I autoconf/ -o configure autoconf/configure.in

%{configure} --enable-client-only --disable-nls --disable-acl --disable-conio --with-readline=%{_prefix} --with-sqlite3=%{_prefix} --with-openssl=%{_prefix} --with-archivedir=%{_prefix}/tmp --with-working-dir=%{_prefix}/bacula/working --with-subsys-dir=%{_prefix}/var/lock/subsys

# Overwrite the crappy libtool from the project. No idea the correct
# way to get it regenerated.
cp %{_bindir}/libtool ./

make %{?_smp_mflags} V=1

%check
make check

%install
make install DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix} INSTALL='install -p'

rm $RPM_BUILD_ROOT%{_libdir}/*.la
rm -rf $RPM_BUILD_ROOT%{_docdir}

%files
%config(noreplace) %{_sysconfdir}/bacula-fd.conf %attr(640,root,root)
%{_mandir}/*
%{_libdir}/*
%{_sbindir}/*
%{_sysconfdir}/*

%changelog
* Sat Jan 11 2020 Daniel Hams <daniel.hams@gmail.com> - 9.4.4
- First build
