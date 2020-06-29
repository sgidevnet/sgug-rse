%bcond_with tests

%global pypi_name xnat

%global desc %{expand: \
A new XNAT client that exposes XNAT objects/functions as python objects/functions.
The aim is to abstract as much of the REST API away as possible and make xnatpy feel
like native Python code. This reduces the need for the user to know the details
of the REST API. Low level functionality can still be accessed via the connection object
which has get, head, put, post, delete methods for more directly calling the REST API.}

Name:           python-%{pypi_name}
Version:        0.3.22
Release:        2%{?dist}
Summary:        A new XNAT client that exposes XNAT objects/functions as python objects/functions.
License:        ASL 2.0
URL:            http://pypi.python.org/pypi/%{pypi_name}/%{version}
Source0:        https://pypi.python.org/packages/source/x/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
%{desc}

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-isodate
BuildRequires: python3-requests
BuildRequires: python3-utils
BuildRequires: python3-progressbar2
BuildRequires: python3-sphinx_rtd_theme
BuildRequires: python3-six

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{desc}

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%if %{with tests}
%{__python3} setup.py test
%endif
 
%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/xnat_cp_project
%{python3_sitelib}/xnat/
%{python3_sitelib}/xnat*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.22-2
- Rebuilt for Python 3.9

* Fri Feb 28 2020 Luis Bazan <lbazan@fedoraproject.org> - 0.3.22-1
- New upstream version

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 23 2019 Aniket Pradhan <major AT fedoraproject DOT org> - 0.3.21-1
- Upgraded to v0.3.21

* Sun Sep 22 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.3.19-1
- New upstream

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.18-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 06 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.3.18-1
- New upstream version

* Mon Apr 08 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.3.17-1
- New upstream version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 19 2018 Luis Bazan <lbazan@fedoraproject.org> - 0.3.11-4
- enable python-progressbar2

* Thu Nov 29 2018 Luis Bazan <lbazan@fedoraproject.org> - 0.3.11-3
- Use template of neuro-sig

* Tue Nov 20 2018 Luis Bazan <lbazan@fedoraproject.org> - 0.3.11-2
- Add remove bundled egg info

* Mon Nov 19 2018 Luis Bazan <lbazan@fedoraproject.org> - 0.3.11-1
- New upstream
