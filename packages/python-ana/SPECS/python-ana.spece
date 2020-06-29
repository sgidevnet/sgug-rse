%global pypi_name ana

Name:           python-%{pypi_name}
Version:        0.06
Release:        2%{?dist}
Summary:        Python module to provide easy distributed data storage

License:        MIT
URL:            https://pypi.org/project/ana/
Source0:        %{pypi_source}
BuildArch:      noarch

%description
ANA is a project to provide easy distributed data storage. It provides every
object with a UUID and, when pickled, will first serialize the object's state
to a central location and then "pickle" the object into just its UUID.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
ANA is a project to provide easy distributed data storage. It provides every
object with a UUID and, when pickled, will first serialize the object's state
to a central location and then "pickle" the object into just its UUID.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.06-2
- Rebuilt for Python 3.9

* Tue Feb 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.06-1
- Initial package for Fedora
