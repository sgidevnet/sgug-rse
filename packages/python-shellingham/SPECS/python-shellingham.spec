%global pypi_name shellingham

Name:           python-%{pypi_name}
Version:        1.2.7
Release:        7%{?dist}
Summary:        Tool to detect surrounding Shell
License:        ISC
URL:            https://github.com/sarugaku/shellingham
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock

%description
Shellingham detects what shell the current Python executable is running in.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Shellingham detects what shell the current Python executable is running in.


%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
export PYTHONPATH=%{buildroot}%{python3_sitelib}
%{__python3} -m pytest -v

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst CHANGELOG.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info/

%changelog
* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.7-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.7-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.7-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 25 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.7-1
- Initial package
