%global		sname pagila
%global		_pagiladir  %{_datadir}/%{name}

Summary:	A sample database for PostgreSQL
Name:		%{sname}
Version:	0.10.1
Release:	10%{?dist}
License:	BSD
URL:		http://pgfoundry.org/projects/dbsamples

Source0:	http://pgfoundry.org/frs/download.php/1719/%{sname}-%{version}.zip

Buildarch:	noarch

%description
Pagila is a port of the Sakila example database available for MySQL, which was
originally developed by Mike Hillyer of the MySQL AB documentation team. It
is intended to provide a standard schema that can be used for examples in
books, tutorials, articles, samples, etc.

%prep
%setup -q -n %{sname}-%{version}

%build

%install
install -d %{buildroot}%{_pagiladir}
install -m 644 -p *.sql %{buildroot}%{_pagiladir}

%files
%doc README
%dir %{_pagiladir}
%{_pagiladir}/*.sql

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 12 2015 Pavel Kajaba <pkajaba@redhat.com> 0.10.1-3
- Added changes to work under Fedora

* Mon Sep 27 2010 Devrim Gunduz <devrim@gunduz.org> 0.10.1-2
- Apply some minor fixes for new PostgreSQL RPM layout.

* Sat Jun 14 2008 Devrim Gunduz <devrim@gunduz.org> 0.10.1-1
- Update to 0.10.1

* Fri Feb 1 2008 Devrim Gunduz <devrim@gunduz.org> 0.10.0-1
- Initial packaging for Fedora/EPEL
