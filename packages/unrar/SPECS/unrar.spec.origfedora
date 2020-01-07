Name:           unrar
Version:        5.6.6
Release:        1%{?dist}
Summary:        Utility for extracting, testing and viewing RAR archives
License:        Freeware with further limitations
URL:            http://www.rarlab.com/rar_add.htm
Source0:        https://www.rarlab.com/rar/unrarsrc-%{version}.tar.gz
# Man page from Debian
Source1:        unrar-nonfree.1

BuildRequires:  gcc-c++
Requires(post): chkconfig
Requires(preun): chkconfig


%description
The unrar utility is a freeware program for extracting, testing and
viewing the contents of archives created with the RAR archiver version
1.50 and above.


%package -n libunrar
Summary:        Decompress library for RAR v3 archives

# Packages using libunrar must Requires this:
#{?unrar_version:Requires: libunrar%%{_isa} = %%{unrar_version}}

%description -n libunrar
The libunrar library allows programs linking against it to decompress
existing RAR v3 archives.


%package -n libunrar-devel
Summary:        Development files for libunrar
Requires:       libunrar%{_isa} = %{version}-%{release}

%description -n libunrar-devel
The libunrar-devel package contains libraries and header files for
developing applications that use libunrar.


%prep
%setup -q -n %{name}
cp -p %SOURCE1 .


%build
make %{?_smp_mflags} -f makefile \
  CXX="%{__cxx}" CXXFLAGS="$RPM_OPT_FLAGS -fPIC -DPIC" LDFLAGS="$RPM_LD_FLAGS -pthread" \
  STRIP=: RANLIB=ranlib
make %{?_smp_mflags} -f makefile clean
make %{?_smp_mflags} -f makefile lib \
  CXX="%{__cxx}" CXXFLAGS="$RPM_OPT_FLAGS -fPIC -DPIC" LDFLAGS="$RPM_LD_FLAGS -pthread" \
  STRIP=: RANLIB=ranlib


%install
rm -rf %{buildroot}
install -Dpm 755 unrar %{buildroot}%{_bindir}/unrar-nonfree
install -Dpm 644 unrar-nonfree.1 %{buildroot}%{_mandir}/man1/unrar-nonfree.1
install -Dpm 755 libunrar.so %{buildroot}%{_libdir}/libunrar.so
mkdir -p -m 755 %{buildroot}/%{_includedir}/unrar
for i in *.hpp; do
    install -Dpm 644 $i %{buildroot}/%{_includedir}/unrar
done

# handle alternatives
touch %{buildroot}%{_bindir}/unrar

# RPM Macros support
mkdir -p %{buildroot}%{_sysconfdir}/rpm
cat > %{buildroot}%{_sysconfdir}/rpm/macros.unrar << EOF
# unrar RPM Macros
%unrar_version    %{version}
EOF
touch -r license.txt %{buildroot}%{_sysconfdir}/rpm/macros.unrar


%post
%{_sbindir}/alternatives \
    --install %{_bindir}/unrar unrar %{_bindir}/unrar-nonfree 50 \
    --slave %{_mandir}/man1/unrar.1.gz unrar.1.gz \
    %{_mandir}/man1/unrar-nonfree.1.gz || :

%preun
if [ "$1" -eq 0 ]; then
  %{_sbindir}/alternatives \
      --remove unrar %{_bindir}/unrar-nonfree || :
fi

%ldconfig_scriptlets -n libunrar


%files
%doc readme.txt
%license license.txt
%ghost %{_bindir}/unrar
%{_bindir}/unrar-nonfree
%{_mandir}/man1/unrar-nonfree.1*

%files -n libunrar
%doc readme.txt
%license license.txt
%{_libdir}/*.so

%files -n libunrar-devel
%doc readme.txt
%license license.txt
%config %{_sysconfdir}/rpm/macros.unrar
%{_includedir}/*


%changelog
* Sat Sep 08 2018 Leigh Scott <leigh123linux@googlemail.com> - 5.6.6-1
- Update to 5.6.6

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 5.6.3-3
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 5.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 25 2018 Leigh Scott <leigh123linux@googlemail.com> - 5.6.3-1
- Update to 5.6.3

* Sun Apr 01 2018 Leigh Scott <leigh123linux@googlemail.com> - 5.6.2-1
- Update to 5.6.2

* Mon Mar 12 2018 Leigh Scott <leigh123linux@googlemail.com> - 5.6.1-1
- Update to 5.6.1

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 5.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Hans de Goede <j.w.r.degoede@gmail.com> - 5.5.8-1
- Update to 5.5.8

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 5.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 23 2017 Leigh Scott <leigh123linux@googlemail.com> - 5.5.5-1
- Update to 5.5.5

* Sun Mar 26 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 5.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 17 2016 Leigh Scott <leigh123linux@googlemail.com> - 5.4.5-1
- Update to 5.4.5
- Harden build
- Spec file clean up

* Thu Jun 30 2016 Nicolas Chauvet <kwizart@gmail.com> - 5.4.2-1
- Update to 5.4.2

* Sat Dec 06 2014 Nicolas Chauvet <kwizart@gmail.com> - 5.2.3-1
- Update to 5.2.3

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 5.0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Dec 15 2013 Nicolas Chauvet <kwizart@gmail.com> - 5.0.12-2
- Add isa dependency

* Fri Nov 8 2013 Conrad Meyer <cemeyer@uw.edu> - 5.0.12-1
- Bump to latest upstream
- Drop patch that doesn't apply anymore
- Makefile changed names

* Mon Oct 28 2013 Conrad Meyer <konrad@tylerc.org> - 4.2.4-4
- Remove unrar-4.2.3-fix-build.patch, add clean step to %%build
  per #2869

* Sun Dec 30 2012 Conrad Meyer <konrad@tylerc.org> - 4.2.4-3
- Try at #2357 again :). Instead of arbitrary date, use rpm %%version

* Sun Dec 30 2012 Conrad Meyer <konrad@tylerc.org> - 4.2.4-2
- Add RPM dependency check to ensure dependent packages break at install time
  rather than use time (#2357) (derived from live555 package)

* Sun Dec 30 2012 Conrad Meyer <konrad@tylerc.org> - 4.2.4-1
- Bump version (#2508)
- Fix unrar-4.2.3-fix-build.patch diff to have context

* Mon May 28 2012 Marcos Mello <marcosfrm AT gmail DOT com> - 4.2.3-1
- New version
- Include all header files in the -devel package (#1988)

* Thu Mar 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 4.0.7-3
- Rebuilt for c++ ABI breakage

* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 4.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Jul 9 2011 Conrad Meyer <konrad@tylerc.org> - 4.0.7-1
- Bump to new version.

* Tue Sep 28 2010 Conrad Meyer <konrad@tylerc.org> - 3.9.10-3
- Patch to fix unresolved symbol issues (#1385).

* Thu Sep 2 2010 Conrad Meyer <konrad@tylerc.org> - 3.9.10-1
- Bump to 3.9.10.

* Sun Feb 21 2010 Conrad Meyer <konrad@tylerc.org> - 3.9.9-1
- Bump to 3.9.9.

* Sun Dec 6 2009 Conrad Meyer <konrad@tylerc.org> - 3.8.5-5
- Fix post to use alternatives to manage unrar manpage as well.

* Mon Nov 30 2009 Conrad Meyer <konrad@tylerc.org> - 3.8.5-4
- Fix preun to refer to the correct alternatives files.

* Fri Nov 20 2009 Conrad Meyer <konrad@tylerc.org> - 3.8.5-3
- Add missing post/preun requires on chkconfig (#956).

* Fri Jul 17 2009 Conrad Meyer <konrad@tylerc.org> - 3.8.5-2
- Fix breakages introduced by dropping the versioned SONAME patch.

* Wed Jul 8 2009 Conrad Meyer <konrad@tylerc.org> - 3.8.5-1
- Bump to 3.8.5.

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 3.7.8-4
- rebuild for new F11 features

* Sat Oct 25 2008 Andreas Thienemann <andreas@bawue.net> - 3.7.8-3
- Added libunrar sub-packages
- Clarified license
- Added unrar robustness patches

* Thu Jul 24 2008 Conrad Meyer <konrad@tylerc.org> - 3.7.8-2
- Import into RPM Fusion.

* Sat Oct 13 2007 Ville Skyttä <ville.skytta at iki.fi> - 3.7.8-1
- 3.7.8.

* Sat Sep  8 2007 Ville Skyttä <ville.skytta at iki.fi> - 3.7.7-1
- 3.7.7, fixes CVE-2007-3726.

* Wed Aug 22 2007 Ville Skyttä <ville.skytta at iki.fi> - 3.7.6-2
- Rebuild.

* Sun Jul  8 2007 Ville Skyttä <ville.skytta at iki.fi> - 3.7.6-1
- 3.7.6.

* Fri May 18 2007 Ville Skyttä <ville.skytta at iki.fi> - 3.7.5-1
- 3.7.5.

* Sat Mar 10 2007 Ville Skyttä <ville.skytta at iki.fi> - 3.7.4-1
- 3.7.4.

* Wed Feb 14 2007 Ville Skyttä <ville.skytta at iki.fi> - 3.7.3-1
- 3.7.3.

* Wed Jan 17 2007 Ville Skyttä <ville.skytta at iki.fi> - 3.7.2-1
- 3.7.2.

* Wed Sep 13 2006 Ville Skyttä <ville.skytta at iki.fi> - 3.6.8-1
- 3.6.8.

* Wed Jul 12 2006 Ville Skyttä <ville.skytta at iki.fi> - 3.6.6-1
- 3.6.6.

* Wed May 31 2006 Ville Skyttä <ville.skytta at iki.fi> - 3.6.4-1
- 3.6.4.

* Sat May 20 2006 Ville Skyttä <ville.skytta at iki.fi> - 3.6.3-1
- 3.6.3.

* Thu Mar 09 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- switch to new release field

* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Tue Oct 11 2005 Ville Skyttä <ville.skytta at iki.fi> - 3.5.4-0.lvn.1
- 3.5.4.
- Drop zero Epoch.

* Wed Aug 10 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:3.5.3-0.lvn.1
- 3.5.3.

* Thu May 19 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:3.5.2-0.lvn.1
- 3.5.2.

* Thu Mar 31 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:3.5.1-0.lvn.1
- 3.5.1.

* Wed Nov 24 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:3.4.3-0.lvn.1
- Update to 3.4.3.

* Sun Sep  5 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:3.4.2-0.lvn.1
- Update to 3.4.2, nostrip patch no longer necessary.
- Update Debian patch URL.

* Sat Jul  3 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:3.4.1-0.lvn.1
- Update to 3.4.1 and Debian patch to 3.3.6-2.

* Thu May 20 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:3.3.6-0.lvn.2
- Update Debian patch to 3.3.6-1 (no real changes, just a working URL again).

* Sun Feb  8 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:3.3.6-0.lvn.1
- Update to 3.3.6.

* Mon Jan 19 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:3.3.4-0.lvn.1
- Update to 3.3.4.

* Sat Dec 27 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:3.3.3-0.lvn.1
- Update to 3.3.3.

* Sun Dec 21 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:3.3.2-0.lvn.1
- Update to 3.3.2.

* Wed Nov 26 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:3.3.1-0.lvn.1
- Update to 3.3.1.

* Sun Sep 14 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:3.2.3-0.fdr.1
- Update to 3.2.3.
- Sync with current Fedora spec template.

* Wed Apr 16 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:3.2.1-0.fdr.1
- Update to 3.2.1.

* Sat Apr  5 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:3.2.0-0.fdr.1
- Update to 3.2.0 and current Fedora guidelines.

* Sun Feb  9 2003 Ville Skyttä <ville.skytta at iki.fi> - 3.1.3-1.fedora.1
- First Fedora release, based on Matthias Saou's and PLD work.
