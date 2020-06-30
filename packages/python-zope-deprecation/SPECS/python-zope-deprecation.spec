%define modname zope.deprecation

Name:           python-zope-deprecation
Version:        4.4.0
Release:        8%{?dist}
Summary:        Zope 3 Deprecation Infrastructure

License:        ZPLv2.1
URL:            https://pypi.python.org/pypi/zope.deprecation
Source0:        https://files.pythonhosted.org/packages/source/z/%{modname}/%{modname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%global _description\
This package provides a simple function called 'deprecated(names, reason)' to\
deprecate the previously mentioned Python objects.

%description %_description

%package -n python3-zope-deprecation
Summary:        Zope 3 Deprecation Infrastructure
%{?python_provide:%python_provide python3-zope-deprecation}


%description -n python3-zope-deprecation
This package provides a simple function called 'deprecated(names, reason)' to
deprecate the previously mentioned Python objects.

%prep
%setup -q -n %{modname}-%{version}

rm -rf %{modname}.egg-info

%build
%py3_build

%install
%py3_install
rm -f %{buildroot}%{python3_sitelib}/zope/deprecation/tests.py*

%check
%{__python3} setup.py test

%files -n python3-zope-deprecation
%doc README.rst LICENSE.txt
%{python3_sitelib}/zope/deprecation/
%{python3_sitelib}/%{modname}-%{version}-*


%changelog
* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 4.4.0-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.4.0-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 30 2019 Miro Hrončok <mhroncok@redhat.com> - 4.4.0-5
- Subpackage python2-zope-deprecation has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 4.4.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 16 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 4.4.0-1
- Upgrade to 4.4.0.
- https://github.com/zopefoundation/zope.deprecation/blob/4.4.0/CHANGES.rst

* Thu Sep 20 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 4.3.0-4
- Fix FTBFS by adding a BR on python2-devel (#1606009).

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 4.3.0-3
- Rebuilt for Python 3.7

* Thu Feb 08 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.3.0-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Tue Feb 06 2018 Lumír Balhar <lbalhar@redhat.com> - 4.3.0-1
- New upstream release
- URLs with SSL

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.1.1-13
- Python 2 binary package renamed to python2-zope-deprecation
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
