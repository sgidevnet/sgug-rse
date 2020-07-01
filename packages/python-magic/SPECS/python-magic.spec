%global pypi_name python-magic
%global srcname magic

Name:           %{pypi_name}
Version:        0.4.15
Release:        3%{?dist}
Summary:        File type identification using libmagic

License:        MIT
URL:            https://github.com/ahupp/python-magic
Source0:        https://github.com/ahupp/python-magic/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
This module uses ctypes to access the libmagic file type identification
library. It makes use of the local magic database and supports both textual
and MIME-type output.

%package -n     python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
This module uses ctypes to access the libmagic file type identification
library. It makes use of the local magic database and supports both textual
and MIME-type output.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

# https://github.com/ahupp/python-magic/issues/105
#%check
#%{__python3} setup.py test

%files -n python3-%{srcname}
%doc README.md
%license LICENSE
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/magic.py
%{python3_sitelib}/python_magic-%{version}-py*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.15-3
- Rebuilt for Python 3.9

* Thu Jan 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.15-2
- Rename package (rhbz#1790100)

* Sat Jan 11 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.15-1
- Initial package.

