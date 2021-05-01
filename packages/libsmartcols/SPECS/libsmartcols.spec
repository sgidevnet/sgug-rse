%global debug 0

%if 0%{debug}
%global __strip /bin/true
%endif

### Header
Summary: Formatting library for ls-like programs.
Name: libsmartcols
Version: 2.34
Release: 5%{?dist}
License: LGPLv2+
URL: http://en.wikipedia.org/wiki/Util-linux

### Macros
%define upstream_version %{version}
%define upstream_major %(eval echo %{version} | %{__sed} -e 's/\([[:digit:]]*\)\.\([[:digit:]]*\)\.[[:digit:]]*$/\1.\2/')

%define compldir %{_datadir}/bash-completion/completions/

%if 0%{?fedora} >= 23
%define pypkg python3
%define pyver 3
%else
%define pypkg python
%define pyver 2
%endif


### Dependencies
BuildRequires: gettext-devel
BuildRequires: ncurses-devel
BuildRequires: zlib-devel
BuildRequires: popt-devel
BuildRequires: gcc

BuildRequires: libdicl-devel

### Sources
Source0: ftp://ftp.kernel.org/pub/linux/utils/util-linux/v%{upstream_major}/util-linux-%{upstream_version}.tar.xz

Patch100:      libsmartcols.sgifixes.patch

%description
This is library for ls-like terminal programs, part of util-linux.

%package -n libsmartcols-devel
Summary: Formatting library for ls-like programs.
License: LGPLv2+
Requires: libsmartcols = %{version}-%{release}
Requires: pkgconfig

%description -n libsmartcols-devel
This is development library and headers for ls-like terminal programs,
part of util-linux.

%prep
%autosetup -p1 -n util-linux-%{upstream_version}

#exit 1

# Place to generate the sgug patch
#exit 1

%build
export CPPFLAGS="-I%{_includedir}/libdicl-0.1 -DLIBDICL_NEED_GETOPT -D_SGI_SOURCE -D_SGI_MP_SOURCE -D_SGI_REENTRANT_FUNCTIONS"
%if 0%{debug}
export CFLAGS="-g -Og"
export CXXFLAGS="-g -Og"
export LDFLAGS="-ldicl-0.1 -Wl,-z,relro -Wl,-z,now"
%else
export LDFLAGS="-ldicl-0.1 $RPM_LD_FLAGS"
%endif

unset LINGUAS || :
autoreconf -fi
%configure

# build util-linux
make %{?_smp_mflags}

%check
#to run tests use "--with check"
%if %{?_with_check:1}%{!?_with_check:0}
make check
%endif


%install
rm -rf ${RPM_BUILD_ROOT}

# install libsmartcols
make install DESTDIR=${RPM_BUILD_ROOT}

# libtool junk
rm -rf ${RPM_BUILD_ROOT}%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/python*/site-packages/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/python*/site-packages/*.a

# remove static libs
rm -f $RPM_BUILD_ROOT%{_libdir}/libsmartcols.a

# remove util-linux bits we don't want
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale

%files
%{!?_licensedir:%global license %%doc}
%license Documentation/licenses/COPYING.LGPL-2.1-or-later libsmartcols/COPYING
%{_libdir}/libsmartcols.so.*

%files -n libsmartcols-devel
%{_libdir}/libsmartcols.so
%{_includedir}/libsmartcols
%{_libdir}/pkgconfig/smartcols.pc

%changelog
* Mon Dec 14 2020 Daniel Hams <daniel.hams@gmail.com> - 2.34-5
- Include dep on libdicl, add debuggable flag

* Sun Aug 16 2020 Daniel Hams <daniel.hams@gmail.com> - 2.34-4
- Extract libsmartcols from util-linux
