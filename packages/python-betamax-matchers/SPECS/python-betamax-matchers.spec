%global pypi_name betamax-matchers

Name:           python-%{pypi_name}
Version:        0.4.0
Release:        8%{?dist}
Summary:        Set of third-party matchers for Betamax

License:        ASL 2.0
URL:            https://github.com/betamaxpy/betamax_matchers
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
A set of third-party matchers for Betamax.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-betamax
BuildRequires:  python3-requests-toolbelt
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A set of third-party matchers for Betamax.

%prep
%autosetup -n betamax_matchers-%{version}

%build
%py3_build

%install
%py3_install

%check
pytest-%{python3_version} -v tests

%files -n python3-%{pypi_name}
%doc AUTHORS.rst HISTORY.rst README.rst
%license LICENSE
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/betamax_matchers/

%changelog
* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.0-8
- Add python3-setuptools as BR

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 08 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.0-2
- Switch source to GitHub
- Run tests

* Thu May 09 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.0-1
- Initial package for Fedora
