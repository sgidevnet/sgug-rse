%global debug 0

%if 0%{debug}
%global __strip /bin/true
%endif

%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}

%global so_ver      4
%global reldate     20180305


Name:           json-c
Version:        0.13.1
Release:        14%{?dist}
Summary:        JSON implementation in C

License:        MIT
URL:            https://github.com/%{name}/%{name}
Source0:        %{url}/archive/%{name}-%{version}-%{reldate}.tar.gz

# Cherry-picked from upstream.
Patch0:         %{url}/commit/da4b34355da023c439e96bc6ca31886cd69d6bdb.patch#/%{name}-0.13.1-parse_test_UTF8_BOM.patch
Patch1:         %{url}/commit/f8c632f579c71012f9aca81543b880a579f634fc.patch#/%{name}-0.13.1-fix_incorrect_casts_in_calls_to_ctype_functions.patch
Patch2:         %{url}/commit/8bd62177e796386fb6382db101c90b57b6138afe.patch#/%{name}-0.13.1-fix_typos.patch

# Fixes CVE-2020-12762.
Patch3:         %{name}-0.13.1-fix_CVE_2020_12762.patch

# Fix RDRAND.
Patch4:         %{name}-0.13.1-detect_broken_RDRAND_during_initialization.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
%ifarch %{valgrind_arches}
BuildRequires:  valgrind
%endif

%description
JSON-C implements a reference counting object model that allows you
to easily construct JSON objects in C, output them as JSON formatted
strings and parse JSON formatted strings back into the C representation
of JSON objects.  It aims to conform to RFC 7159.


%package        devel
Summary:        Development files for %{name}

Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.


#%%package        doc
#Summary:        Reference manual for json-c
#
#BuildArch:      noarch
#
#BuildRequires:  doxygen
#BuildRequires:  hardlink
#
#%%description    doc
#This package contains the reference manual for %%{name}.


%prep
%autosetup -n %{name}-%{name}-%{version}-%{reldate} -p 1

for doc in ChangeLog; do
  iconv -f iso-8859-1 -t utf-8 ${doc} > ${doc}.new
  touch -r ${doc} ${doc}.new
  mv -f ${doc}.new ${doc}
done

sed -i -e 's!#ACLOCAL_AMFLAGS!ACLOCAL_AMFLAGS!g' Makefile.am

# Rewrite the dodgy test shell references
perl -pi -e "s|!/bin/sh|!%{_bindir}/sh|g" tests/*.test
perl -pi -e "s|!/bin/sh|!%{_bindir}/sh|g" tests/*.sh

autoreconf -fiv

%build
export CPPFLAGS="-I%{_includedir}/libdicl-0.1 -D_SGI_SOURCE -D_SGI_MP_SOURCE -D_SGI_REENTRANT_FUNCTIONS"
%if 0%{debug}
export CFLAGS="-g -Og"
export CXXFLAGS="$CFLAGS"
export LDFLAGS="-ldicl-0.1 -Wl,-z,relro -Wl,-z,now"
%else
export LDFLAGS="-ldicl-0.1 $RPM_LD_FLAGS"
%endif

%configure               \
  --disable-silent-rules \
  --disable-static       \
  --enable-Bsymbolic     \
  --enable-rdrand        \
  --enable-shared        \
  --enable-threading
%make_build
#doxygen Doxyfile


%install
%make_install

find %{buildroot} -name '*.a' -delete -print
find %{buildroot} -name '*.la' -delete -print

mkdir -p %{buildroot}%{_pkgdocdir}
#cp -pr doc/html ChangeLog README README.* %{buildroot}%{_pkgdocdir}
cp -pr ChangeLog README README.* %{buildroot}%{_pkgdocdir}
#hardlink -cvf %{buildroot}%{_pkgdocdir}


%check
USE_VALGRIND=0 %make_build check
%ifarch %{valgrind_arches}
USE_VALGRIND=1 %make_build check
%endif


#%%ldconfig_scriptlets

%files
%license AUTHORS
%license COPYING
%{_libdir}/lib%{name}.so.%{so_ver}*


%files devel
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/ChangeLog
%doc %{_pkgdocdir}/README*
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


#%%files doc
#%%if 0%%{?fedora} || 0%%{?rhel} >= 7
#%%license %%{_datadir}/licenses/%%{name}*
#%%endif
#%%doc %%{_pkgdocdir}


%changelog
* Fri Nov 13 2020 Daniel Hams <daniel.hams@gmail.com> - 0.13.1-14
- Fix up and add debug option, get tests passing

* Mon May 25 2020 Björn Esser <besser82@fedoraproject.org> - 0.13.1-13
- Add a patch to detect broken RDRAND in some CPUs
- Re-enable the use of RDRAND
- Run the testssuite with valgrind on %%valgrind_arches

* Wed May 13 2020 Björn Esser <besser82@fedoraproject.org> - 0.13.1-12
- Fix CVE-2020-12762

* Sun Apr 12 2020 Björn Esser <besser82@fedoraproject.org> - 0.13.1-11
- Drop bootstrap logic, as the package is no dependency of @build anymore
- Add some explicit BuildRequires, which were implicit
- Small spec file cleanups
