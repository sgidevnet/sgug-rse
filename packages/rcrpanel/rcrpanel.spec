Name:           rcrpanel
Version:        3.5
Release:        19%{?dist}
Summary:        Lay out front panel for electronics project
License:        GPLv2+
URL:            http://gitorious.org/panel-dial/rcrpanel
Source0:        http://ares-mi.org/qslmaker/downloads/rcrpanel-3.5.tar.gz

#BuildRequires: 
#Requires:       

BuildRequires:  gcc
%description
rcrpanel is an application to lay out a front panel for a radio or similar
electronics device.  rcrpanel can provide dials for potentiometers or variable
capacitors as well as lay out cutouts for switches and jacks.  rcrpanel
accepts a panel description file and produces PostScript output.

%prep
%setup -q

%build
#uses make
make rpmdeps

%install
install -D -m 0755 rcrpanel $RPM_BUILD_ROOT%{_bindir}/rcrpanel
install -D -m 0644 rcrpanel.1 $RPM_BUILD_ROOT%{_mandir}/man1/rcrpanel.1

%files
%doc rcrpanel.txt Changelog README COPYING AUTHORS
%{_bindir}/rcrpanel
%{_mandir}/man?/rcrpanel*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.5-16
- Escape macros in %%changelog

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Apr 13 2011 John McDonough <jjmcd@fedoraproject.org> - 3.5-4
- Update web locations to new server

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov  2 2010 John McDonough <jjmcd@fedoraproject.org> - 3.5-2
- Remove prelim clean of $RPM_BUILD_ROOT per 529387
- Leaving %%clean for now due to build for F12

* Mon Oct 19 2009 John McDonough <jjmcd@fedoraproject.org> - 3.5-1
- Use source from the web
- Update README to eliminate references to Dial
- Include Changelog
- Reflect GPLV2+ in specfile

* Fri Oct 16 2009 John McDonough <jjmcd@fedoraproject.org> - 3.4-2
- Rebuild for F11

* Wed Apr 08 2009 John McDonough <jjmcd@fedoraproject.org> - 3.4-1
- Clean up source to reflect new name
- Check into RCS so rev updated
- Add licensing statement

* Wed Apr 08 2009 John McDonough <jjmcd@fedoraproject.org> - 3.2-1
- First packaging attempt

