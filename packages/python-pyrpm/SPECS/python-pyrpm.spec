%global pypi_name pyrpm
%global reponame python-rpm-spec

%bcond_without tests

%global common_description %{expand:
Python-rpm-spec is a Python module for parsing RPM spec files. RPMs are build
from a package's sources along with a spec file. The spec file controls how the
RPM is built. This module allows you to parse spec files and gives you simple
access to various bits of information that is contained in the spec file.}

Name:           python-%{pypi_name}
Version:        0.9
Release:        1%{?dist}
Summary:        Python module for parsing RPM spec files

License:        MIT
URL:            https://github.com/bkircher/python-rpm-spec
Source0:        %pypi_source %{reponame}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with tests}
BuildRequires:  python3-pytest
%endif

%description
%{common_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{common_description}

%prep
%autosetup -n %{reponame}-%{version}

%build
%py3_build

%install
%py3_install

%if %{with tests}
%check
%{__python3} -m pytest -v
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc AUTHORS CHANGELOG.md README.md examples/
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/python_rpm_spec-%{version}-py*.egg-info


%changelog
* Fri Jun 19 23:43:38 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.9-1
- Update to 0.9 (#1830524)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 27 00:01:23 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.8-1
- Initial package
