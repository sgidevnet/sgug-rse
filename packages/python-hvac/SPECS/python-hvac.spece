# Created by pyp2rpm-3.3.2
%global pypi_name hvac

# Enable Python dependency generation
%{?python_enable_dependency_generator}

Name:           python-%{pypi_name}
Version:        0.9.5
Release:        3%{?dist}
Summary:        HashiCorp Vault API client for Python

License:        ASL 2.0
URL:            https://github.com/hvac/hvac
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
This package provides a Python API client for HashiCorp Vault.

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        HashiCorp Vault API client for Python 3
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

# Extra dependency is not mandatory but quite useful
## Making this EPEL8 compatible...
Recommends:     python%{python3_version}dist(pyhcl) >= 0.3.10

%description -n python%{python3_pkgversion}-%{pypi_name}
This package provides a Python API client for HashiCorp Vault.

This is for Python 3.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%if 0%{?el8}
# Lower dependency to requests 2.20+ for EL8
sed -e "s/requests>=2.21.0/requests>=2.20.0/" -i setup.py
%endif

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README.md
%license LICENSE.txt
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.5-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 24 18:27:43 EDT 2019 Neal Gompa <ngompa@datto.com> - 0.9.5-1
- Initial packaging for Fedora (RH#1765350)
