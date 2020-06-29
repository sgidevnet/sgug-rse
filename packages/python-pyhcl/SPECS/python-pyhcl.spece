# Created by pyp2rpm-3.3.2
%global pypi_name pyhcl

# Enable Python dependency generation
%{?python_enable_dependency_generator}

Name:           python-%{pypi_name}
Version:        0.3.13
Release:        4%{?dist}
Summary:        HCL configuration parser for Python

License:        MPLv2.0
URL:            https://github.com/virtuald/pyhcl
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  (python3dist(ply) >= 3.8 with python3dist(ply) < 4)
BuildRequires:  python3dist(setuptools)

%description
Implements a parser for HCL (HashiCorp Configuration Language) in Python.

This implementation aims to be compatible with the original Go version
of the parser.

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
Implements a parser for HCL (HashiCorp Configuration Language) in Python.

This implementation aims to be compatible with the original Go version
of the parser.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/hcltool
%{python3_sitelib}/hcl/
%{python3_sitelib}/%{pypi_name}-*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.13-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 24 18:52:27 EDT 2019 Neal Gompa <ngompa13@gmail.com> - 0.3.13-2
- Fix parameter for subpackage name in description section

* Thu Oct 24 18:22:07 EDT 2019 Neal Gompa <ngompa@datto.com> - 0.3.13-1
- Initial packaging for Fedora (RH#1765347)
