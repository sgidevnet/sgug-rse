%global pyname ipaddress

Name:           python-%{pyname}
Version:        1.0.18
Release:        7%{?dist}
Summary:        Port of the python 3.3+ ipaddress module to 2.6+

License:        Python
URL:            https://pypi.python.org/pypi/ipaddress/
Source0:        https://pypi.python.org/packages/source/i/%{pyname}/%{pyname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel

%global _description\
ipaddress provides the capabilities to create, manipulate and operate\
on IPv4 and IPv6 addresses and networks.\
\
The functions and classes in this module make it straightforward to\
handle various tasks related to IP addresses, including checking\
whether or not two hosts are on the same subnet, iterating over all\
hosts in a particular subnet, checking whether or not a string\
represents a valid IP address or network definition, and so on.

%description %_description

%package -n python2-%{pyname}
Summary: %summary
%{?python_provide:%python_provide python2-%{pyname}}

%description -n python2-%{pyname} %_description

%prep
%setup -q -n %{pyname}-%{version}


%build
%{__python2} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python2} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%files -n python2-%{pyname}
%doc README.md
%{python2_sitelib}/*


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.18-3
- Python 2 binary package renamed to python2-ipaddress
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 19 2017 Paul Wouters <pwouters@redhat.com> - 1.0.18-1
- Updated to 1.0.18, fixup URL

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.16-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 08 2016 Matěj Cepl <mcepl@redhat.com> - 1.0.16-1
- Update to the latest upstream (#1242475)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Nathaniel McCallum <npmccallum@redhat.com> - 1.0.7-3
- Remove Conflicts: python-ipaddr

* Mon Jun  8 2015 Nathaniel McCallum <npmccallum@redhat.com> - 1.0.7-2
- Add Conflicts: python-ipaddr

* Thu May 14 2015 Nathaniel McCallum <npmccallum@redhat.com> - 1.0.7-1
- Update to 1.0.7

* Wed Mar 20 2013 Matt Domsch <mdomsch@fedoraproject.org> - 1.0.3-1
- initial release
