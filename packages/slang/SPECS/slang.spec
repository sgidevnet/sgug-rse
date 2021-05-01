%if 0%{?fedora:1}
%bcond_without oniguruma
%else
%bcond_with oniguruma
%endif

Summary:	The shared library for the S-Lang extension language
Name:		slang
Version:	2.3.2
Release:	7%{?dist}
License:	GPLv2+
URL:		https://www.jedsoft.org/slang/
Source:		https://www.jedsoft.org/releases/%{name}/%{name}-%{version}.tar.bz2
# don't use memcpy() on overlapping buffers
Patch1:		slang-getkey-memmove.patch
# disable test that fails with SIGHUP ignored (e.g. in koji)
Patch2:		slang-sighuptest.patch
BuildRequires:	gcc libpng-devel pcre-devel zlib-devel
%{?with_oniguruma:BuildRequires: oniguruma-devel}
# static removed in 2.3.1a-3
Obsoletes:	 slang-static < 2.3.1a-3

%description
S-Lang is an interpreted language and a programming library.  The
S-Lang language was designed so that it can be easily embedded into
a program to provide the program with a powerful extension language.
The S-Lang library, provided in this package, provides the S-Lang
extension language.  S-Lang''s syntax resembles C, which makes it easy
to recode S-Lang procedures in C if you need to.

%package slsh
Summary:	Interpreter for S-Lang scripts
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description slsh
slsh (slang-shell) is a program for interpreting S-Lang scripts. 
It supports dynamic loading of S-Lang modules and includes a readline
interface for interactive use.

This package also includes S-Lang modules that are distributed with
the S-Lang distribution.

%package devel
Summary:	Development files for the S-Lang extension language
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains files which you''ll need if you want to
develop S-Lang based applications.  Documentation which may help
you write S-Lang based applications is also included.

Install the slang-devel package if you want to develop applications
based on the S-Lang extension language.

%prep
%setup -q
%patch1 -p1 -b .getkey-memmove
%patch2 -p1 -b .sighuptest

# fix permissions of installed modules
sed -i '/^INSTALL_MODULE=/s/_DATA//' configure

# disable test failing on 32-bit archs
sed -i '/TEST_SCRIPTS_SLC = /s/array //' src/test/Makefile

# Rewrite some hardcoded paths
perl -pi -e "s|/usr/bin/env slsh|/usr/sgug/bin/env slsh|g" ./doc/text/*
perl -pi -e "s|/usr/bin/env slsh|/usr/sgug/bin/env slsh|g" ./doc/tm/*
perl -pi -e "s|/usr/bin/env slsh|/usr/sgug/bin/env slsh|g" ./doc/tm/rtl/*
perl -pi -e "s|/usr/bin/env slsh|/usr/sgug/bin/env slsh|g" ./doc/tm/tools/*
perl -pi -e "s|/usr/bin/env slsh|/usr/sgug/bin/env slsh|g" ./examples/*
perl -pi -e "s|/usr/bin/env slsh|/usr/sgug/bin/env slsh|g" ./modules/*
perl -pi -e "s|/usr/bin/env slsh|/usr/sgug/bin/env slsh|g" ./modules/examples/*
perl -pi -e "s|/usr/bin/env slsh|/usr/sgug/bin/env slsh|g" ./slsh/scripts/*
perl -pi -e "s|/usr/bin/env slsh|/usr/sgug/bin/env slsh|g" ./src/util/mkslarith2.sl
perl -pi -e "s|/usr/bin/env slsh|/usr/sgug/bin/env slsh|g" ./utf8/tools/mktables

perl -pi -e "s|/bin/sh|/usr/sgug/bin/sh|g" ./slsh/lib/test/runtests.sh
perl -pi -e "s|/bin/sh|/usr/sgug/bin/sh|g" ./src/slsignal.c
perl -pi -e "s|/bin/sh|/usr/sgug/bin/sh|g" ./src/test/runtests.sh
perl -pi -e "s|/bin/sh|/usr/sgug/bin/sh|g" ./modules/test/runtests.sh

%build
# Slang X11 detection clashes with other packages
# By setting CPPFLAGS to something unusual, we ensure it will
# use it's own config.cache
export CPPFLAGS="-DSLANGNEEDSISOLCCACHE"
%configure \
	--with-{pcre,png,z}lib=%{_libdir} \
	--with-{pcre,png,z}inc=%{_includedir} \
%if %{with oniguruma}
	--with-oniglib=%{_libdir} \
	--with-oniginc=%{_includedir} \
%endif
;

# fails with %{?_smp_mflags}
# install_doc_dir sets SLANG_DOC_DIR macro
#make RPATH="" install_doc_dir=%{_pkgdocdir} all

# Work around to allow use of parallel make
export PREV_WD=`pwd`
cd src
make config.h
make terminfo.inc
make sltermin.o
make sldisply.o
mkdir -p objs
mkdir -p elfobjs
cd $PREV_WD
make %{?_smp_mflags}

%install
make install-all INSTALL="install -p" RPATH="" DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{_docdir}/{slang,slsh}
rm -f $RPM_BUILD_ROOT%{_libdir}/libslang.a

mkdir $RPM_BUILD_ROOT%{_includedir}/slang
for h in slang.h slcurses.h; do
	ln -s ../$h $RPM_BUILD_ROOT%{_includedir}/slang/$h
done

%check
export LD_LIBRARYN32_PATH=%{buildroot}%{_libdir}
make %{?_smp_mflags} check

#%%ldconfig_scriptlets

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc NEWS
%{_libdir}/libslang*.so.2*

%files slsh
%doc slsh/doc/html/slsh*.html
%config(noreplace) %{_sysconfdir}/slsh.rc
%{_bindir}/slsh
%{_libdir}/slang
%{_mandir}/man1/slsh.1*
%{_datadir}/slsh

%files devel
%doc doc/*/cslang*.txt doc/*/cref.txt doc/README doc/*/slang*.txt doc/*.txt
%{_libdir}/libslang*.so
%{_libdir}/pkgconfig/slang.pc
%{_includedir}/sl*.h
%{_includedir}/slang

%changelog
* Fri Oct 09 2020 Daniel Hams <daniel.hams@gmail.com> - 2.3.2-7
- Little spec cleanups, get parallel make working.

* Tue Oct 06 2020  HAL <notes2@gmx.de> - 2.3.2-6
- compiles on Irix 6.5 with sgug-rse gcc 9.2 passing all tests.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
