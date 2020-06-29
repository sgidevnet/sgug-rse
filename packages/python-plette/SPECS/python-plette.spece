%global         pypi_name plette
%global         _description %{expand:
Plette implements Pipfile and Pipfile.lock parsers}

Name:           python-%{pypi_name}
Version:        0.2.2
Release:        5%{?dist}
License:        ISC
URL:            https://github.com/sarugaku/plette
Source0:        https://github.com/sarugaku/plette/archive/%{version}/plette-%{version}.tar.gz
BuildArch:      noarch
Summary:        Python library which contains Pipfile parser

%description %{_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-tomlkit
BuildRequires:  python3-six
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %{_description}

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
# one test is failing with tomlkit 0.5.5
# filed: https://github.com/sarugaku/plette/issues/9
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} -m pytest -v -k 'not test_pipfile_load'

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}-*.egg-info/
%{python3_sitelib}/%{pypi_name}/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-2
- Rebuilt for Python 3.8

* Sun May 12 2019 Patrik Kopkan <pkopkan@redhat.com> 0.2.2-1
- initial package
