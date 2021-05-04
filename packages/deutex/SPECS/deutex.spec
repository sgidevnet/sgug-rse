%define waddir  %{_datadir}/doom

Name:           deutex
Version:        5.2.1
Release:        1%{?dist}
Summary:        DOOM wad file manipulator

# All files LGPLv2+ or GPLv2+ except ./src/lzw.c which is MIT
License:        GPLv2+ and MIT
URL:            https://github.com/Doom-Utils/deutex
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         deutex-5.2.0-waddir.patch
BuildRequires:	gcc, autoconf, automake, asciidoc

%description
DeuTex is a wad composer for Doom, Heretic, Hexen and Strife. It can be
used to extract the lumps of a wad and save them as individual files.
Conversely, it can also build a wad from separate files. When extracting
a lump to a file, it does not just copy the raw data, it converts it to
an appropriate format (such as PPM for graphics, Sun audio for samples,
etc.). Conversely, when it reads files for inclusion in pwads, it does
the necessary conversions (for example, from PPM to Doom picture
format). In addition, DeuTex has functions such as merging wads, etc. If
you're doing any wad hacking beyond level editing, DeuTex is a must.


%prep
%setup -q
%patch0 -p0


%build
autoreconf -if
%configure
make CFLAGS="$RPM_OPT_FLAGS -DDOOMDIR=\"\\\"%{waddir}\\\"\"" %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%{_bindir}/deutex
%{_mandir}/man6/*
%license LICENSE
%doc COPYING COPYING.LIB AUTHORS README.adoc NEWS.adoc


%changelog
* Mon Aug 12 2019 Gwyn Ciesla <gwync@protonmail.com> - 5.2.1-1
- 5.2.1

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Gwyn Ciesla <gwync@protonmail.com> - 5.2.0-1
- 5.2.0

* Fri May 17 2019 Gwyn Ciesla <gwync@protonmail.com> - 5.1.2-1
- 5.1.2

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Gwyn Ciesla <limburgher@gmail.com> - 5.1.1-1
- 5.1.1.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct 27 2017 Gwyn Ciesla <limburgher@gmail.com> - 5.1.0-1
- 5.1.0, new upstream location.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 8 2008 Wart <wart at kobold.org> 4.4.0-6
- Rebuild for gcc 3.4

* Sun Aug 19 2007 Wart <wart at kobold.org> 4.4.0-5
- License tag clarification

* Wed Apr 11 2007 Wart <wart at kobold.org> 4.4.0-4
- Set default wad directory to the fedora default

* Sun Aug 27 2006 Wart <wart at kobold.org> 4.4.0-3
- Rebuild for FC-6

* Thu Apr 20 2006 Wart <wart at kobold.org> 4.4.0-2
- Add freedoom to the list of known iwads.

* Sun Mar 19 2006 Wart <wart at kobold.org> 4.4.0-1
- Initial spec file.
