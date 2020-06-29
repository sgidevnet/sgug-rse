%global pypi_name prawcore

Name:           python-%{pypi_name}
Version:        1.4.0
Release:        1%{?dist}
Summary:        Low-level communication layer for PRAW 4+ library

License:        BSD
URL:            https://github.com/praw-dev/prawcore
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Low-level communication layer for PRAW 4+ library

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  mock
BuildRequires:  python3-mock
BuildRequires:  python3-betamax
BuildRequires:  python3-betamax-matchers
BuildRequires:  python3-betamax-serializers
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-testfixtures
%{?python_provide:%python_provide python3-nng}

%description -n python3-%{pypi_name}
Low-level communication layer for PRAW 4+ library.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests

%files -n python3-%{pypi_name}
%doc AUTHORS.rst CHANGES.rst README.rst
%license LICENSE.txt
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/%{pypi_name}/

%changelog
* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.0-1
- Update to latest upstream release 1.4.0

* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.0-3
- Add python3-setuptools as BR

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-2
- Rebuilt for Python 3.9

* Sat May 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.0-1
- Update to latest upstream release 1.3.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.1-2
- Disable tests

* Thu May 09 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.1-1
- Initial package for Fedora
