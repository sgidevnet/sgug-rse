%global src_name buildsystem

Name:           netsurf-buildsystem
Version:        1.7
Release:        3%{?dist}
Summary:        Makefiles shared by NetSurf projects
License:        MIT
URL:            http://www.netsurf-browser.org/
Source0:        http://download.netsurf-browser.org/libs/releases/%{src_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators

%description
%{name} contains makefiles shared by NetSurf projects.

%prep
%autosetup -n %{src_name}-%{version} -p1

sed -i -e 1s@/bin/@/usr/bin/@ testtools/testrunner.pl
chmod +x testtools/testrunner.pl

%install
%make_install PREFIX=%{_prefix}

%files
%doc README
%license COPYING
%{_datadir}/%{name}/

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Sep 01 2018 David Tardon <dtardon@redhat.com> - 1.7-1
- new upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 21 2017 David Tardon <dtardon@redhat.com> - 1.6-1
- new upstream release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 18 2016 David Tardon <dtardon@redhat.com> - 1.5-1
- new upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 David Tardon <dtardon@redhat.com> - 1.4-2
- fix perl path

* Sat Jan 16 2016 David Tardon <dtardon@redhat.com> - 1.4-1
- new upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 16 2015 David Tardon <dtardon@redhat.com> - 1.3-1
- new upstream release

* Mon Sep 01 2014 David Tardon <dtardon@redhat.com> - 1.2-1
- new upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 27 2014 David Tardon <dtardon@redhat.com> - 1.1-1
- new upstream release

* Mon Jan 13 2014 David Tardon <dtardon@redhat.com> - 1.0-2
- add support for multilib

* Wed Dec 25 2013 David Tardon <dtardon@redhat.com> - 1.0-1
- initial import
