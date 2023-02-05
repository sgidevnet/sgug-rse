%global	pidgin_version 2.0.0

Name:		pidgin-musictracker
Version:	0.4.22
Release:	19%{?dist}
Summary:	Musictracker plug-in for Pidgin

License:	GPLv2+
URL:		http://code.google.com/p/pidgin-musictracker/
Source0:	http://%{name}.googlecode.com/files/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:	gtk2-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	pcre-devel
BuildRequires:	pidgin-devel >= %{pidgin_version}
BuildRequires:	gettext-devel

Requires:	pidgin >= %{pidgin_version}

%description
Musictracker is a plug-in for Pidgin which displays the media currently
playing in the status message for any protocol Pidgin supports custom
statuses on.

%prep
%setup -q

%build
%configure --disable-werror --disable-static --enable-debug CFLAGS="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=%{buildroot} INSTALL="install -p" install
rm -f %{buildroot}/%{_libdir}/pidgin/musictracker.la
%find_lang musictracker

%files -f musictracker.lang
%doc AUTHORS ChangeLog COPYING NEWS README THANKS
%{_libdir}/pidgin/musictracker.so

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.22-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.22-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.22-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.22-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.22-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.22-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.22-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.22-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.22-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.22-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.22-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.22-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.22-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 0.4.22-5
- Rebuild against PCRE 8.30

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.4.22-3
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 8 2011 Jan Klepek <jan.klepek at, gmail.com> - 0.4.22-1
- new release

* Tue Oct 13 2009 Jan Klepek <jan.klepek at. gmail.com> - 0.4.20-3
- fix for #528450

* Mon Oct 12 2009 Jan Klepek <jan.klepek at, gmail.com> 0.4.20-2
- enabled debug package and honored RPM_OPT_FLAGS

* Wed Sep 23 2009 Jan Klepek <jan.klepek at, gmail.com> 0.4.20-1
- update to 0.4.20

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr  9 2009 Jan Klepek <jan.klepek at, gmail.com> 0.4.16-1
- combined spec file from all below people and builded package for 0.4.16 version
 
* Wed Mar  4 2009 Jon TURNEY <jon.turney@dronecode.org.uk>
- Cut-n-shut from .spec files cotributed by Jon Hermansen <jon.hermansen@gmail.com>, Julio Cezar <watchman777@gmail.com> and Mattia Verga <mattia.verga@tiscali.it>

* Wed Mar  4 2009 Mattia Verga <mattia.verga@tiscali.it> 0.4.15-2.fc10
- Added BuildRequires section and corrected the Requires section to Pidgin version >= 2.0. Added THANKS file to documentation

* Tue Mar  3 2009 Mattia Verga <mattia.verga@tiscali.it> 0.4.15-1.fc10
- Upgrade to version 0.4.15. See full changelog at http://code.google.com/p/pidgin-musictracker/wiki/ChangeLog0point4

* Mon Feb  2 2009 Mattia Verga <mattia.verga@tiscali.it> 0.4.14-2.fc10
- Added requires

* Sun Feb  1 2009 Mattia Verga <mattia.verga@tiscali.it> 0.4.14-1.fc10
- Initial package
