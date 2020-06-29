%bcond_without check
%global pypi_name identify

Name:           python-%{pypi_name}
Version:        1.4.16
Release:        2%{?dist}
Summary:        File identification library for Python

License:        MIT
URL:            https://github.com/chriskuehl/identify
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%if %{with check}
BuildRequires:  python3dist(editdistance)
BuildRequires:  python3-pytest
%endif

%?python_enable_dependency_generator

%description
Given a file (or some information about a file), return a set of standardized
tags identifying what the file is.


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
%{_bindir}/%{pypi_name}-cli
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.16-2
- Rebuilt for Python 3.9

* Thu May 21 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.4.16-1
- Update to 1.4.16

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.4.10-1
- Update to 1.4.10

* Thu Oct 24 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.4.7-5
- Initial package
