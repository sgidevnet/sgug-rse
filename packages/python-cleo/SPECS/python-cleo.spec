%global pypi_name cleo

%{?python_enable_dependency_generator}

%global common_description %{expand:
Create beautiful and testable command-line interfaces.

Cleo is mostly a higher level wrapper for CliKit, so a lot of the
components and utilities comes from it. Refer to its documentation for
more information.}

Name:           python-%{pypi_name}
Summary:        Create beautiful and testable command-line interfaces
Version:        0.7.6
Release:        3%{?dist}
License:        MIT

URL:            https://github.com/sdispater/cleo
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description %{common_description}


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %{common_description}


%prep
%autosetup -n %{pypi_name}-%{version} -p1


%build
%py3_build


%install
%py3_install


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst

%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.6-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 08 2019 Fabio Valentini <decathorpe@gmail.com> - 0.7.6-1
- Update to version 0.7.6.

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.8-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.8-2
- Rebuilt for Python 3.8

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.6.8-1
- Initial package.

