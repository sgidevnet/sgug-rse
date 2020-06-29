%global srcname funcy

Name:           python-%{srcname}
Version:        1.14
Release:        2%{?dist}
Summary:        Fancy and practical functional tools

License:        BSD
URL:            https://github.com/Suor/funcy
Source:         %{pypi_source}

BuildArch:      noarch

%global _description \
A collection of fancy functional tools focused on practicality.

%description %{_description}

%package     -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(whatever)

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version}
rm -vr *.egg-info tests/__pycache__

%build
%py3_build

%install
%py3_install

%check
%python3 -m pytest -v

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst CHANGELOG
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.14-2
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.14-1
- Initial package
