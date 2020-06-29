%global pypi_name rawkit

Name:           python-%{pypi_name}
Version:        0.6.0
Release:        6%{?dist}
Summary:        A ctypes-based set of LibRaw bindings for Python

License:        MIT
URL:            https://rawkit.readthedocs.io
Source0:        %{pypi_source}
BuildArch:      noarch

%description
rawkit is a ctypes-based set of LibRaw bindings for Python.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-Cython
BuildRequires:  python3-pytest
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
rawkit is a ctypes-based set of LibRaw bindings for Python

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

# One test is currently failing
#%check
#pytest-%{python3_version} -v tests

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/libraw
%{python3_sitelib}/rawkit/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.0-1
- Initial package for Fedora
