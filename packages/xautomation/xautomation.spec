Name:           xautomation
Version:        1.09
Release:        1%{?dist}
Summary:        Tools to automate tasks in X, even detecting on screen images

License:        GPLv2+
URL:            http://hoopajoo.net/projects/xautomation.html
Source0:        http://hoopajoo.net/static/projects/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libpng-devel
BuildRequires:  libXi-devel
BuildRequires:  libXtst-devel

%description
Control X from the command line for scripts, and do "visual scraping" to find
things on the screen. The control interface allows mouse movement, clicking,
button up/down, key up/down, etc, and uses the XTest extension so you don't have
the annoying problems that xse has when apps ignore sent events. The visgrep
program find images inside of images and reports the coordinates, allowing
programs to find buttons, etc, on the screen to click on.


%prep
%autosetup


%build
%configure
%make_build


%install
%make_install


%files
%doc AUTHORS README
%license COPYING
%{_bindir}/pat2ppm
%{_bindir}/patextract
%{_bindir}/png2pat
%{_bindir}/rgb2pat
%{_bindir}/visgrep
%{_bindir}/xmousepos
%{_bindir}/xte
%{_mandir}/man1/*.1.*
%{_mandir}/man7/*.7.*


%changelog
* Tue Aug 13 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.09-1
- Update to 1.09
- Spec cleanup

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 22 2012 Mohamed El Morabity <melmorabity@fedorapeople.org> - 1.07-2
- Add missing BuildRequires libXi-devel

* Mon Oct 22 2012 Mohamed El Morabity <melmorabity@fedorapeople.org> - 1.07-1
- Update to 1.07

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 22 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.06-1
- Update to 1.06
- Spec cleanup

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.05-2
- Rebuild for new libpng

* Thu Sep 15 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.05-1
- Update to 1.05

* Fri Sep 02 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.04-1
- Update to 1.04

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul  6 2010 EL MORABITY Mohamed <melmorabity@fedoraproject.org> 1.03-3
- Bump release

* Wed Jun 23 2010 EL MORABITY Mohamed <melmorabity@fedoraproject.org> 1.03-2
- Fix mispelling in %%description

* Sun Jun 13 2010 EL MORABITY Mohamed <melmorabity@fedoraproject.org> 1.03-1
- Initial RPM release
