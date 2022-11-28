Name:		rktime
Version:	0.6
Release:	16%{?dist}
Summary:	Multi-zone time display utility
License:	GPLv2
URL:		http://people.redhat.com/rkeech/#rktime
Source0:	http://people.redhat.com/rkeech/%{name}-%{version}.tgz
BuildArch:	noarch

%description
A command-line utility which displays the time
in multiple timezones in an easy-to-read way, using color
to help indicate which locations are currently in business
hours.

%prep
%setup -q

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT

%{__install} -Dp -m0755 rktime $RPM_BUILD_ROOT%{_bindir}/rktime
%{__install} -Dp -m0644 rktime.1 $RPM_BUILD_ROOT%{_mandir}/man1/rktime.1
%{__install} -Dp -m0644 rktime.conf.5 $RPM_BUILD_ROOT%{_mandir}/man5/rktime.conf.5


%files
%doc %{_mandir}/man1/%{name}.1.gz
%doc %{_mandir}/man5/%{name}.conf.5.gz
%doc %{name}.conf.sample
%{_bindir}/%{name}

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Apr 28 2010 Mohammed Imran <imranceh@gmail.com> - 0.6-2
- Used macros for rm and /bin

* Thu Apr 22 2010 Mohammed Imran <imranceh@gmail.com> - 0.6-1
- Spec file changed for fedora 13

* Sun May 09 2004 <rkeech@redhat.com>
- Added rktime.conf.sample.
- Misc cleanups to main script.

* Wed Oct 08 2003 <rkeech@redhat.com>
- Added Asia/Calcutta zone

* Tue Sep 17 2002 <rkeech@redhat.com>
- Added Europe/Paris zone

* Fri Apr 19 2002 <rkeech@redhat.com>
- spec file change only

* Fri Nov 17 2000 <rkeech@redhat.com>
- Corrected for RH7
