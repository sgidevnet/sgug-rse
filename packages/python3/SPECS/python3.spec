Summary: WIP spec for python 3.8
Name: python3
Version: 3.8.1
Release: 4wip%{?dist}
License: GPLv3+
URL: https://www.python.org
Source: https://www.python.org/ftp/python/%{version}/Python-%{version}.tgz

Source100: python3.sgifixesbinsh.list
Source101: python3.sgifixesbinbash.list
Source102: python3.sgifixeslocalbinpython.list
Source103: python3.sgifixesbinpython.list

Provides: %{_bindir}/python
Provides: %{_bindir}/python3
Provides: %{_bindir}/python3.8
Provides: %{_bindir}/python3-config
Provides: %{_bindir}/python3.8-config

Provides: python(abi) = 3.8
Provides: python3(abi) = 3.8
Provides: python3
Provides: python3-devel
Provides: python3-devel(abi) = 3.8
Provides: 2to3
Provides: pkgconfig(python) = 3.8
Provides: pkgconfig(python3) = 3.8
Provides: pkgconfig(python-3.8) = 3.8

BuildRequires: gcc
BuildRequires: automake, autoconf, libtool, pkgconfig
BuildRequires: python-rpm-macros

Patch100: python3.sgifixes.patch

%description
A minimal port of python 3.8.1 against sgug-rse.

%prep

%setup -q -n Python-%{version}

# To create an "orig" that patches can be diff''d against
#exit 1

%patch100 -p1

# For patching
#exit 1

# Fix /bin/sh
for filetofix in `cat %{SOURCE100}`; do
    perl -pi -e "s|/bin/sh|%{_bindir}/sh|g" ${filetofix}
done
# Fix /bin/bash
for filetofix in `cat %{SOURCE101}`; do
    perl -pi -e "s|/bin/bash|%{_bindir}/bash|g" ${filetofix}
done
# Fix local/bin/python
for filetofix in `cat %{SOURCE102}`; do
    perl -pi -e "s|/usr/local/bin/python|%{_bindir}/python|g" ${filetofix}
done
# Fix /bin/python
for filetofix in `cat %{SOURCE103}`; do
    perl -pi -e "s|/usr/bin/python|%{_bindir}/python|g" ${filetofix}
done

# Remove bundled libraries to ensure that we're using the system copy
rm -rf Modules/expat

%build
#export LDFLAGS="-lpthread -Wl,-rpath -Wl,%{_libdir}"
export ac_cv_func_strsignal=no
%{configure} --enable-shared --with-system-expat --with-system-ffi --with-ssl-default-suites=openssl --without-ensurepip --with-computed-gotos=yes
# this can't be set through configure
X=`mktemp`
sed 's,^SCRIPTDIR.*$,SCRIPTDIR=     $(prefix)/lib32,g' < Makefile > $X
cat $X > Makefile
rm -f $X
make %{?_smp_mflags}

%check
# Do the tests by hand
#make check

%install
make install DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix} INSTALL='install -p'
# ugly, but can't be done otherwise
tar -C $RPM_BUILD_ROOT%{_prefix}/lib/python3.8/ -cf - . | tar -C $RPM_BUILD_ROOT%{_libdir}/python3.8/ -xvf -
rm -rf $RPM_BUILD_ROOT%{_prefix}/lib

# Setup a symbolic link so that we "provide" %{_bindir}/python
export PREV_WD=`pwd`
cd $RPM_BUILD_ROOT%{_bindir}
ln -s python3 python
cd $PREV_WD

# Remove some ugly archives containing hard references to bash
rm $RPM_BUILD_ROOT%{_libdir}/python3.8/test/ziptestdata/exe_with_z64
rm $RPM_BUILD_ROOT%{_libdir}/python3.8/test/ziptestdata/exe_with_zip

rm -rf $RPM_BUILD_ROOT%{_libdir}/python3.8/lib2to3/tests
rm -rf $RPM_BUILD_ROOT%{_libdir}/python3.8/test

# Remove setup tools which comes from it's own package
rm -rf $RPM_BUILD_ROOT%{_libdir}/python3.8/site-packages/setuptools

# Remove pip which comes from it's own package
rm -rf $RPM_BUILD_ROOT%{_libdir}/python3.8/site-packages/pip
rm -rf $RPM_BUILD_ROOT%{_bindir}/pip*

# Remove shebang lines from .py files that aren't executable, and
# remove executability from .py files that don't have a shebang line:
find %{buildroot} -name \*.py \
  \( \( \! -perm /u+x,g+x,o+x -exec sed -e '/^#!/Q 0' -e 'Q 1' {} \; \
  -print -exec sed -i '1d' {} \; \) -o \( \
  -perm /u+x,g+x,o+x ! -exec grep -m 1 -q '^#!' {} \; \
  -exec chmod a-x {} \; \) \)

%files
%{_bindir}/*
%{_libdir}/libpython3*
%{_libdir}/pkgconfig/*
%{_libdir}/python3.8/*

%{_prefix}/include/python3.8/*
%{_mandir}/*

%changelog
* Sat Jun 06 2020 Daniel Hams <daniel.hams@gmail.com> - 3.8.1-4wip
- Move to single patch, fix up things broken by new rpm macros coming online

* Mon May 25 2020 Daniel Hams <daniel.hams@gmail.com> - 3.8.1-3wip
- Get a little more aggressive about rewriting /bin/sh etc.

* Sun Apr 12 2020 Daniel Hams <daniel.hams@gmail.com> - 3.8.1-2
- Rename to python3, Provides: of python3 and python3-devel
  Fix up hardcoded paths + bug fix to system lib path

* Sat Feb 15 2020 Erno Palonheimo <esp@iki.fi> - 3.8.1-1
- Initial attempt at spec
