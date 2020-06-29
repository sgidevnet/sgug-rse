%global pypi_name gast

Name:           python-%{pypi_name}
Version:        0.3.3
Release:        1%{?dist}
Summary:        Python AST that abstracts the underlying Python version

License:        BSD
URL:            https://github.com/serge-sans-paille/gast/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-astunparse
BuildRequires:  python3-setuptools

%description
A generic AST to represent Python2 and Python3's Abstract Syntax Tree (AST).
GAST provides a compatibility layer between the AST of various Python versions,
as produced by ast.parse from the standard ast module.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A generic AST to represent Python2 and Python3's Abstract Syntax Tree (AST).
GAST provides a compatibility layer between the AST of various Python versions,
as produced by ast.parse from the standard ast module.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Sun Jun 07 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-1
- Update to 0.3.3 (#1844892)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 12 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-1
- Update to 0.3.2

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jan 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-1
- Initial package
