%global pypi_name diskcache

Name:           python-%{pypi_name}
Version:        4.1.0
Release:        3%{?dist}
Summary:        Disk and file backed persistent cache

License:        ASL 2.0
URL:            http://www.grantjenks.com/docs/diskcache/
Source0:        %{pypi_source}
BuildArch:      noarch

%description
DiskCache is an Apache 2 licensed disk and file backed cache library,
written in pure-Python, and compatible with Django. The cloud-based
computing of 2019 puts a premium on memory. Gigabytes of empty space 
is left on disks asprocesses vie for memory. Among these processes is
Memcached (and sometimes Redis) which is used as a cache. Wouldn't it 
be nice to leverage.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-tox
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
DiskCache is an Apache 2 licensed disk and file backed cache library,
written in pure-Python, and compatible with Django. The cloud-based
computing of 2019 puts a premium on memory. Gigabytes of empty space 
is left on disks asprocesses vie for memory. Among these processes is
Memcached (and sometimes Redis) which is used as a cache. Wouldn't it 
be nice to leverage.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.1.0-3
- Rebuilt for Python 3.9

* Sun Jan 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 4.1.0-2
- Address issues (rhbz#1795068)

* Sun Jan 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 4.1.0-1
- Initial package
