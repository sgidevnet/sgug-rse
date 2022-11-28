%global modname idna-ssl

# Circular dependency with aiohttp
%bcond_with check

Name:           python-%{modname}
Version:        1.1.0
Release:        9%{?dist}
Summary:        Patch ssl.match_hostname for Unicode(idna) domains support

License:        MIT
URL:            https://github.com/aio-libs/idna_ssl
Source0:        %{url}/archive/v%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%description
%{summary}.

%package -n python3-%{modname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with check}
BuildRequires:  python3dist(pytest-runner)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(aiohttp) > 2.3
BuildRequires:  python3dist(idna) >= 2
%endif
%{?python_provide:%python_provide python3-%{modname}}

%description -n python3-%{modname}
%{summary}.

%prep
%autosetup -n %{modname}-%{version}

%build
%py3_build

%install
%py3_install

%if %{with check}
%check
%{__python3} setup.py pytest
%endif

%files
%license LICENSE
%doc README.rst example.py
%{python3_sitelib}/idna_ssl-*.egg-info/
%{python3_sitelib}/idna_ssl.py
%{python3_sitelib}/__pycache__/idna_ssl.*

%changelog
* Fri May 29 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.0-9
- Fix typo in provide macro

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-2
- Rebuilt for Python 3.7

* Sat Feb 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-1
- Initial package
