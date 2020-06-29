%global pypi_name betamax-serializers

Name:           python-%{pypi_name}
Version:        0.2.0
Release:        8%{?dist}
Summary:        Set of third-party serializers for Betamax

License:        ASL 2.0
URL:            https://gitlab.com/betamax/serializers
Source0:        %{pypi_source}
BuildArch:      noarch

%description
A set of third-party serializers for Betamax.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-PyYAML
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A set of third-party serializers for Betamax.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc AUTHORS.rst HISTORY.rst README.rst
%license LICENSE
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/betamax_serializers/

%changelog
* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.0-8
- Add python3-setuptools as BR

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 25 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.0-2
- Fix name
- Remove dep generator

* Thu May 09 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.0-1
- Initial package for Fedora
