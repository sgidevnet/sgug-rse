%global srcname j1m.sphinxautointerface

Name:           python-%{srcname}
Version:        0.3.0
Release:        14%{?dist}
Summary:        Sphinx extension for documenting zope.interface interfaces

License:        BSD
URL:            https://pypi.python.org/pypi/j1m.sphinxautointerface/
Source0:        %pypi_source
# This package is forked from the sphinx-contrib package, namely the zopeext
# extension.  This is the license file for the entire sphinx-contrib package.
Source1:        https://bitbucket.org/birkenfeld/sphinx-contrib/raw/8e295053a27d5914127fbb01e2a8fb57421897a7/LICENSE
# Adapt to changes in sphinx 3.x
Patch0:         %{name}-sphinx3.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(zope.interface)

%description
This sphinx extension provides an autointerface directive for Zope
interfaces.

%package     -n python3-%{srcname}
Summary:        Sphinx extension for documenting zope.interface interfaces

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
This sphinx extension provides an autointerface directive for Zope
interfaces.

%prep
%autosetup -n %{srcname}-%{version} -p1
cp -p %{SOURCE1} .

%build
%py3_build
rst2html --no-datestamp README.rst README.html

%install
%py3_install

#%%check
#%%{__python3} setup.py test

%files -n python3-%{srcname}
%doc README.html
%{python3_sitelib}/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-14
- Rebuilt for Python 3.9

* Thu Apr 16 2020 Jerry James <loganjerry@gmail.com> - 0.3.0-13
- Add -sphinx3 patch

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.3.0-7
- Subpackage python2-j1m.sphinxautointerface has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 25 2017 Jerry James <loganjerry@gmail.com> - 0.3.0-3
- Add LICENSE file from upstream repository

* Wed Jul 26 2017 Jerry James <loganjerry@gmail.com> - 0.3.0-2
- Comment out useless check script

* Sat Mar 25 2017 Jerry James <loganjerry@gmail.com> - 0.3.0-1
- Initial RPM
