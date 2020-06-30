%global pypi_name pygments_pytest
%global dash_name pygments-pytest

# this is BRed by pytest, so we need to run without tests when bootstrapping
# also pygments-ansi-color is not available in Fedora yet
%bcond_with tests

Name:           python-%{dash_name}
Version:        2.0.0
Release:        1%{?dist}
Summary:        A pygments lexer for pytest output
License:        MIT
URL:            https://github.com/asottile/pygments-pytest
Source0:        %{url}/archive/v%{version}/%{dash_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with tests}
BuildRequires:  python3-pygments
BuildRequires:  python3-pygments-ansi-color
BuildRequires:  python3-pytest
%endif

%description
This library provides a pygments lexer called pytest.
This library also provides a sphinx extension.

%package -n     python3-%{dash_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{dash_name}
This library provides a pygments lexer called pytest.
This library also provides a sphinx extension.


%prep
%autosetup -n %{dash_name}-%{version}

%build
%py3_build

%install
%py3_install

%if %{with tests}
%check
%pytest -v
%endif

%files -n python3-%{dash_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue Jun 02 2020 Charalampos Stratakis <cstratak@redhat.com> - 2.0.0-1
- Update to 2.0.0 (#1747425)

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 12 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-1
- Initial package
