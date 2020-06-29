%global pypi_name nodeenv


Name:           python-%{pypi_name}
Version:        0.13.6
Release:        20%{?dist}
Summary:        Node.js virtual environment builder

License:        BSD
URL:            https://github.com/ekalinin/nodeenv
Source0:        https://pypi.python.org/packages/source/n/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
nodeenv (node.js virtual environment) is a tool to create isolated node.js
environments.
It creates an environment that has its own installation directories, that
doesn’t share libraries with other node.js virtual environments.

%package -n python3-%{pypi_name}
Summary:        Node.js virtual environment builder
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-setuptools

# test dependencies
BuildRequires:    python3-coverage
BuildRequires:    python3-flake8
BuildRequires:    python3-mock
BuildRequires:    python3-pytest

%description -n python3-%{pypi_name}
nodeenv (node.js virtual environment) is a tool to create isolated node.js
environments.
It creates an environment that has its own installation directories, that
doesn’t share libraries with other node.js virtual environments.

%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build

%py3_build

%install


%py3_install

%check

%{__python3} setup.py test

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{_bindir}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}.py*
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.13.6-20
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.13.6-18
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.13.6-17
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.13.6-14
- Subpackage python2-nodeenv has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.13.6-12
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.13.6-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.13.6-7
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.6-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Nov  9 2015 Toshio Kuratomi <toshio@fedoraproject.org> - - 0.13.6-3
- Fix script mistakenly being included in both the python2 and python3 version
  of the package.

* Wed Sep 30 2015 Chandan Kumar <chkumar246@gmail.com> - 0.13.6-2
- Fixed files duplication

* Tue Sep 29 2015 Chandan Kumar <chkumar246@gmail.com> - 0.13.6-1
- Added python2 and python3 subpackge

* Wed Aug 12 2015 chandankumar <chkumar246@gmail.com> - 0.13.3-1
- Initial package.
