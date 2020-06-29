%global srcname pytest-metadata
%global srcname_ pytest_metadata

Name:		python-%{srcname}
Version:	1.7.0
Release:	3%{?dist}
Summary:	Pytest plugin that provides access to test session metadata

License:	MPLv2.0
URL:		https://github.com/pytest-dev/%{srcname}
Source0:	%{pypi_source}

BuildArch:	noarch

%{?python_enable_dependency_generator}

%description
Pytest plugin that provides access to test session metadata


%package -n python3-%{srcname}
Summary:	%{summary}
BuildRequires:	python3-devel
BuildRequires:	python3-pytest >= 2.9.0
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm

%{?python_provide:%python_provide python3-%{srcname}}


%description -n python3-%{srcname}
Pytest plugin that provides access to test session metadata


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%check
python3 -m pytest -v -r a


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname_}
%{python3_sitelib}/%{srcname_}-%{version}-py?.?.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 20 2018 Petr Schindler <pschindl@redhat.com - 1.7.0-1
- Initial package release.
