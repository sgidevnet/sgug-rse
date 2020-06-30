%global srcname pyvit

Name:           python-%{srcname}
Version:        0.2.1
Release:        7%{?dist}
Summary:        Python Vehicle Interface Toolkit

License:        GPLv3+
URL:            https://github.com/linklayer/pyvit
Source0:        %{pypi_source}
BuildArch:      noarch

%description
pyvit is a toolkit for interfacing with cars from Python. It aims to implement
common hardware interfaces and protocols used in the automotive systems.

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
pyvit is a toolkit for interfacing with cars from Python. It aims to implement
common hardware interfaces and protocols used in the automotive systems.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

# Tests are failing at the moment due to a missing file
#%check
#%{__python3} setup.py test

%files -n python3-%{srcname}
%doc CONTRIBUTING.rst README.rst
%license LICENSE.rst
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/%{srcname}/
%exclude %{python3_sitelib}/test/

%changelog
* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.1-7
- Add python3-setuptools as BR

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.1-1
- Initial package for Fedora
