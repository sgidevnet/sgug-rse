Name:          enchant2
Version:       2.2.7
Release:       1%{?snap}%{?dist}
Summary:       An Enchanting Spell Checking Library

License:       LGPLv2+
URL:           https://github.com/AbiWord/enchant
Source0:       https://github.com/AbiWord/enchant/releases/download/v%{version}/enchant-%{version}.tar.gz

# Look for aspell using pkg-config, instead of AC_CHECK_LIB which adds -laspell
# to the global LIBS and over-links libenchant (#1574893)
Patch0:        enchant_aspell.patch

BuildRequires: automake autoconf libtool

BuildRequires: gcc-c++
BuildRequires: glib2-devel
BuildRequires: aspell-devel
BuildRequires: hunspell-devel
BuildRequires: libvoikko-devel

Provides:      bundled(gnulib)


%description
A library that wraps other spell checking backends.


%package aspell
Summary:       Integration with aspell for libenchant
Requires:      enchant2%{?_isa} = %{version}-%{release}

%description aspell
Libraries necessary to integrate applications using libenchant with aspell.

%package voikko
Summary:       Integration with voikko for libenchant
Requires:      enchant2%{?_isa} = %{version}-%{release}
Supplements:   (enchant2 and langpacks-fi)

%description voikko
Libraries necessary to integrate applications using libenchant with voikko.


%package devel
Summary:       Development files for %{name}
Requires:      enchant2%{?_isa} = %{version}-%{release}
Requires:      glib2-devel

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n enchant-%{version}

# Needed for Patch0
autoreconf -ifv


%build
%configure \
    --with-aspell \
    --with-hunspell-dir=%{_datadir}/myspell \
    --without-hspell \
    --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g;
        s|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build pkgdatadir=%{_datadir}/enchant-2


%install
%make_install pkgdatadir=%{_datadir}/enchant-2
find %{buildroot} -name '*.la' -delete


#%%ldconfig_scriptlets


%files
%doc AUTHORS NEWS README
%license COPYING.LIB
%{_bindir}/enchant-2
%{_bindir}/enchant-lsmod-2
%{_libdir}/libenchant-2.so.*
%dir %{_libdir}/enchant-2
%{_libdir}/enchant-2/enchant_hunspell.so
%{_mandir}/man1/*
%{_datadir}/enchant-2

%files aspell
%{_libdir}/enchant-2/enchant_aspell.so*

%files voikko
%{_libdir}/enchant-2/enchant_voikko.so*

%files devel
%{_libdir}/libenchant-2.so
%{_libdir}/pkgconfig/enchant-2.pc
%{_includedir}/enchant-2


%changelog
* Sat Jun 20 2020  HAL <notes2@gmx.de> - 2.2.7-1
- compiles on Irix 6.5 with sgug-rse gcc 9.2.

* Sun Sep 15 2019 Sandro Mani <manisandro@gmail.com> - 2.2.7-1
- Update to 2.2.7

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 01 2019 Sandro Mani <manisandro@gmail.com> - 2.2.5-1
- Update to 2.2.5

* Fri Jun 28 2019 Sandro Mani <manisandro@gmail.com> - 2.2.4-2
- Add patch to fix memory leaks (#1718084)
- Pass --without-hspell

* Tue Jun 18 2019 Sandro Mani <manisandro@gmail.com> - 2.2.4-1
- Update to 2.2.4

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Sandro Mani <manisandro@gmail.com> - 2.2.3-4
- Add patch to avoid unnecessary linking of libenchant against libaspell (#1574893)

* Wed May 16 2018 Parag Nemade <pnemade AT redhat DOT com> - 2.2.3-3
- Make enchant2-voikko installed by langpacks-fi package (#1578352)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Sandro Mani <manisandro@gmail.com> - 2.2.3-1
- Update to 2.2.3

* Wed Jan 03 2018 Sandro Mani <manisandro@gmail.com> - 2.2.1-1
- Update to 2.2.1

* Thu Dec 14 2017 Sandro Mani <manisandro@gmail.com> - 2.2.0-2
- Add patch to fix FSF addresses
- Kill rpath

* Wed Dec 13 2017 Sandro Mani <manisandro@gmail.com> - 2.2.0-1
- Initial package
