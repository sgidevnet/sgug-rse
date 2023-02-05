Name:           libdiscid
Version:        0.6.2
Release:        8%{?dist}
Summary:        C Library for creating MusicBrainz DiscIDs
License:        LGPLv2+
URL:            https://musicbrainz.org/doc/libdiscid
Source0:        http://ftp.musicbrainz.org/pub/musicbrainz/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
# BuildRequires:  doxygen

%description
This C library %{name} creates MusicBrainz DiscIDs from audio CDs. It
reads the table of contents (TOC) of a CD and generates an identifier
which can be used to lookup the CD at MusicBrainz. Additionally, it
provides a submission URL for adding the DiscID to the database.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries, header files and documentation for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags}
# make docs


%check
make check


%install
%make_install INSTALL="install -p"
find %{buildroot} -name '*.la' -delete -print


#%%ldconfig_scriptlets


%files
%doc AUTHORS ChangeLog README
%license COPYING
%{_libdir}/%{name}.so.0*

%files devel
#%%doc docs/*
%{_includedir}/discid/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Thu Jul 09 2020  HAL <notes2@gmx.de> - 0.6.2-8
- compiles on Irix 6.5 with sgug-rse gcc 9.2.Two tests passed, two tests were skipped.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 30 2017 David King <amigadave@amigadave.com> - 0.6.2-1
- Update to 0.6.2
- Include doxygen-generated API documentation

* Fri Jul 29 2016 David King <amigadave@amigadave.com> - 0.6.1-6
- Use license macro for COPYING
- Enable tests during check phase
- Improve globs in files section

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Nov 01 2013 Ismael Olea <ismael@olea.org> - 0.6.1-1
- Update to 0.6.1

* Wed Sep 18 2013 Ismael Olea <ismael@olea.org> - 0.5.2-1
- Update to 0.5.2

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Dec 14 2008 Rex Dieter <rdieter@fedoraproject.org> - 0.2.2-2
- rebuild for pkgconfig deps

* Sat Nov 29 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.2.2-1
- Update to latest upstream (0.2.2)

* Sat Feb 09 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.1.1-6
- rebuilt for GCC 4.3 as requested by Fedora Release Engineering

* Fri Nov 16 2007 Alex Lancaster <alexl@users.sourceforge.net> - 0.1.1-5
- Fix description
- devel package Requires: pkgconfig
- save header timestamps

* Fri Nov 16 2007 Alex Lancaster <alexl@users.sourceforge.net> - 0.1.1-4
- Remove unneeded doc directive in -devel package, add COPYING file

* Fri Nov 16 2007 Alex Lancaster <alexl@users.sourceforge.net> - 0.1.1-3
- Fix tarball

* Thu Nov 15 2007 Alex Lancaster <alexl@users.sourceforge.net> - 0.1.1-2
- Update as per packaging guidelines: fix license tag, add docs

* Sun Jul 15 2007 Kyle VanderBeek <kylev@kylev.com> - 0.1.1-1
- Initial version for Fedora 7
