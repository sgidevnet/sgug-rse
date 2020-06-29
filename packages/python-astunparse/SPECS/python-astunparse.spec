%global pypi_name astunparse

Name:           python-%{pypi_name}
Version:        1.6.3
Release:        1%{?dist}
Summary:        An AST unparser for Python
# Primarily under the terms of BSD
# The unparse and the test_unparse modules are under the PSF license.
License:        BSD and Python
URL:            https://github.com/simonpercivall/astunparse
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  python3-wheel

%description
This is a factored out version of unparse found in the Python source
distribution; under Tools/parser in Python 3.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This is a factored out version of unparse found in the Python source
distribution; under Tools/parser in Python 3.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

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
* Sun Jun 07 2020 Miro Hrončok <mhroncok@redhat.com> - 1.6.3-1
- Update to 1.6.3 (#1844891)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 12 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.2-5
- Python 3.8 fixes (#1758472)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jan 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.2-1
- Initial package
