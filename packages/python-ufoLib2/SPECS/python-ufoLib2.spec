%global srcname ufoLib2

Name:           python-%{srcname}
Version:        0.7.1
Release:        3%{?dist}
Summary:        A library to deal with UFO font sources

License:        ASL 2.0
URL:            https://pypi.org/project/ufoLib2
Source0:        %{pypi_source %{srcname} %{version} zip}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(attrs)
BuildRequires:  python3dist(fonttools)
BuildRequires:  python3dist(lxml)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(typing-extensions)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(sphinx)

# Required for running tests
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-randomly)


%global _description %{expand:
ufoLib2 is meant to be a thin representation of the Unified Font Object (UFO)
version 3 data model, intended for programmatic manipulation and fast batch
processing of UFOs.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %{python3} -m pytest -v

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-3
- Rebuilt for Python 3.9

* Tue May 19 2020 Parag Nemade <pnemade AT redhat DOT com> - 0.7.1-2
- Drop the Requires: as they will be picked automatically
- Rename spec to python-ufoLib2.spec

* Thu May 07 2020 Parag Nemade <pnemade AT redhat DOT com> - 0.7.1-1
- Initial packaging

