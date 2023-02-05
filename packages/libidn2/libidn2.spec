Summary:          Library to support IDNA2008 internationalized domain names
Name:             libidn2
Version:          2.3.0
Release:          3%{?dist}
License:          (GPLv2+ or LGPLv3+) and GPLv3+
URL:              https://www.gnu.org/software/libidn/#libidn2

Source0:          https://ftp.gnu.org/gnu/libidn/%{name}-%{version}.tar.gz
Source1:          https://ftp.gnu.org/gnu/libidn/%{name}-%{version}.tar.gz.sig
Source2:          gpgkey-1CB27DBC98614B2D5841646D08302DB6A2670428.gpg
Patch0:           libidn2-2.0.0-rpath.patch

#BuildRequires:    gnupg2
BuildRequires:    gcc
BuildRequires:    gettext
BuildRequires:    libunistring-devel
Provides:         bundled(gnulib)

%description
Libidn2 is an implementation of the IDNA2008 specifications in RFC
5890, 5891, 5892, 5893 and TR46 for internationalized domain names
(IDN). It is a standalone library, without any dependency on libidn.

%package devel
Summary:          Development files for libidn2
Requires:         %{name}%{?_isa} = %{version}-%{release}, pkgconfig

%description devel
The libidn2-devel package contains libraries and header files for
developing applications that use libidn2.

%package -n idn2
Summary:          IDNA2008 internationalized domain names conversion tool
License:          GPLv3+
Requires:         %{name}%{?_isa} = %{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} <= 7
Requires(post):   %{_sbindir}/install-info
Requires(preun):  %{_sbindir}/install-info
%endif

%description -n idn2
The idn2 package contains the idn2 command line tool for testing
IDNA2008 conversions.

%prep
#gpgv2 --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%setup -q
%patch0 -p1 -b .rpath
touch -c -r configure.rpath configure
touch -c -r m4/libtool.m4.rpath m4/libtool.m4

%build
%configure --disable-static
%make_build

%install
%make_install

# Clean-up examples for documentation
%make_build -C examples distclean
rm -f examples/Makefile*

# Don't install any libtool .la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

# Some file cleanups
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%find_lang %{name}

%check
%make_build -C tests check

#%%ldconfig_scriptlets

%if 0%{?rhel} && 0%{?rhel} <= 7
%post -n idn2
%{_sbindir}/install-info %{_infodir}/%{name}.info.gz %{_infodir}/dir || :

%preun -n idn2
if [ $1 = 0 ]; then
  %{_sbindir}/install-info --delete %{_infodir}/%{name}.info.gz %{_infodir}/dir || :
fi
%endif

%files -f %{name}.lang
%license COPYING COPYING.LESSERv3 COPYING.unicode COPYINGv2
%doc AUTHORS NEWS README.md
%{_libdir}/%{name}.so.*

%files devel
%doc doc/%{name}.html examples
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/*.h
%{_mandir}/man3/*
%{_datadir}/gtk-doc/

%files -n idn2
%{_bindir}/idn2
%{_mandir}/man1/idn2.1*
%{_infodir}/%{name}.info*

%changelog
* Tue Dec 08 2020 Daniel Hams <daniel.hams@gmail.com> 2.3.0-3
- Remove unpackaged %{_infodir}/dir

* Mon Jun 01 2020 Daniel Hams <daniel.hams@gmail.com> 2.3.0-2
- Upgrade to latest fc31 version, get pre/post included.

* Sat Nov 16 2019 Robert Scheck <robert@fedoraproject.org> 2.3.0-1
- Upgrade to 2.3.0 (#1764345, #1772703)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 23 2019 Robert Scheck <robert@fedoraproject.org> 2.2.0-1
- Upgrade to 2.2.0 (#1713402)
