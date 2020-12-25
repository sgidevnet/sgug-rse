Name:           chrpath
Version:        0.16
Release:        14%{?dist}
Summary:        Modify rpath of compiled programs

License:        GPL+
URL:            https://chrpath.alioth.debian.org/

#Source0:	https://alioth-archive.debian.org/releases/chrpath/chrpath/%{version}/chrpath-%{version}.tar.gz
#BuildRequires:  gcc
#BuildRequires: libdicl-devel >= 0.1.19
#Requires: libdicl >= 0.1.26

%description
chrpath allows you to modify the dynamic library load path (rpath) of
compiled programs.  Currently, only removing and modifying the rpath
is supported.

chrpath does nothing on RSE: https://github.com/sgidevnet/sgug-rse/issues/145

#%build
#export CFLAGS="-I%{_includedir}/libdicl-0.1"
#export LDFLAGS="$RPM_LD_FLAGS -ldicl-0.1 -ltinfo"
#%configure
#%make_build

%install
mkdir -p %{buildroot}%{_bindir}
ln -s %{_bindir}/true %{buildroot}%{_bindir}/chrpath
#make install DESTDIR=%{buildroot} INSTALL="install -p"
#rm -fr %{buildroot}/usr/sgug/doc

%files
%{_bindir}/chrpath
#%doc AUTHORS README NEWS ChangeLog*
#%license COPYING
#%{_mandir}/man1/chrpath.1*

%changelog
* Sat Nov 14 2020 David Stancu <dstancu@nyu.edu> - 0.16-14
- Make chrpath do nothing https://github.com/sgidevnet/sgug-rse/issues/145

* Thu Jun 18 2020 David Stancu <dstancu@nyu.edu> - 0.16-13
- Rebuilt for SGI IRIX
- Update source URL

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 David King <amigadave@amigadave.com> - 0.16-8
- Add BuildRequires on gcc
- Remove Group tag, reorder other tags

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 25 2015 David King <amigadave@amigadave.com> - 0.16-1
- Update to 0.16 (#1144863)
- Remove clean section and BuildRoot tag
- Update URL and Sourc0
- Use license macro for COPYING
- Use parallel make flags
- Preserve timestamps during install

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr  8 2013 Petr Machata <pmachata@redhat.com> - 0.13-12
- Add missing help for -k|--keepgoing option
  (chrpath-0.13-help.patch)

* Thu Apr  4 2013 Petr Machata <pmachata@redhat.com> - 0.13-11
- Add missing last entry in long options array
  (chrpath-0.13-getopt_long.patch)
- Update config.sub and config.guess to support aarch64
  (chrpath-0.13-aarch64.patch)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 23 2009 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.13-5
- Fix last entry in .dynamic (by Christian Krause <chkr@plauener.de>).

* Sat Sep  8 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.13-2
- License: GPL+

* Sun Mar 12 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.13-1
- Initial build.

