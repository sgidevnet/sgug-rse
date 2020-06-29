%bcond_without check
%global pypi_name cfgv

Name:           python-%{pypi_name}
Version:        2.0.1
Release:        5%{?dist}
Summary:        Validate configuration and produce human readable error messages

License:        MIT
URL:            https://github.com/asottile/cfgv
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%if %{with check}
BuildRequires:  python3dist(six)
BuildRequires:  python3-mock
BuildRequires:  python3-pytest
%endif

%?python_enable_dependency_generator

%description
%{summary}.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{summary}.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%if %{with check}
%check
%{python3} -m pytest -v
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 24 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 2.0.1-3
- Initial package
