%global srcname colorzero

Name:           python-%{srcname}
Version:        1.1
Release:        2%{?dist}
Summary:        Yet another Python color library

License:        BSD
URL:            https://github.com/waveform80/colorzero
Source0:        %{url}/archive/release-%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
Colorzero is a color manipulation library for Python (yes, another one)
which aims to be reasonably simple to use and "pythonic" in nature.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-release-%{version}

%build
%py3_build

%install
%py3_install

%check
%{python3} -m pytest

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1-2
- Rebuilt for Python 3.9

* Sun Apr 12 2020 Tomas Hrnciar <thrnciar@redhat.com> - 1.1-1
- Initial package
