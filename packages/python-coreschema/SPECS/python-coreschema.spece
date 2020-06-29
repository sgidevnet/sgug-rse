%global srcname coreschema

Name:           python-%{srcname}
Version:        0.0.4
Release:        2%{?dist}
Summary:        Core Schema

# License file is missing on github and there is no way to open issue there
# since project is archived
License:        BSD
URL:            https://github.com/core-api/python-coreschema
Source:         %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
%{summary}.}

%description %{_description}

%package     -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version} -p1
rm -vr *.egg-info

%build
%py3_build

%install
%py3_install

# Tests are not on PyPI
#%%check
#%%python3 -m pytest -v

%files -n python3-%{srcname}
%{python3_sitelib}/coreschema/
%{python3_sitelib}/coreschema-*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.4-2
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.0.4-1
- Initial package
