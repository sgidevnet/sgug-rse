# Warning:
# Anyone editing this spec file please make sure the same spec file
# works on other fedora and epel releases, which are supported by this software.
# No quick Rawhide-only fixes will be allowed.

Name:			gpaw-setups
Version:		0.9.20000
Release:		4%{?dist}
Summary:		Atomic GPAW setups

License:		GPLv3+
URL:			https://wiki.fysik.dtu.dk/gpaw/
Source0:		https://wiki.fysik.dtu.dk/gpaw-files/%{name}-%{version}.tar.gz

BuildArch:		noarch


%description
Atomic GPAW setups. A setup is to the PAW method what
a pseudo-potential is to the pseudo-potential method.


%prep
%setup -q -n %{name}-%{version}


%build


%install

mkdir -p %{buildroot}%{_datadir}/%{name}
install -p -m 444 *.{gz,pckl,txt} %{buildroot}%{_datadir}/%{name}


%files
%doc COPYING LICENSE
%{_datadir}/%{name}


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.20000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.20000-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.20000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 13 2018 Marcin Dulak <Marcin.Dulak@gmail.com> - 0.9.20000-1
- new upstream release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11271-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11271-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11271-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11271-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.11271-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.11271-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 30 2014 Marcin Dulak <Marcin.Dulak@gmail.com> - 0.9.11271-2
- COPYING and LICENSE added

* Tue Apr 22 2014 Marcin Dulak <Marcin.Dulak@gmail.com> - 0.9.11271-1
- initial version for Fedora
