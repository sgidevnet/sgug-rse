%global pypi_name django-cache-url

Name:           python-%{pypi_name}
Version:        3.1.2
Release:        1%{?dist}
Summary:        Use Cache URLs in your Django application

License:        MIT
URL:            https://github.com/epicserve/django-cache-url
Source0:        %{pypi_source}
BuildArch:      noarch

%description
This simple Django utility allows you to utilize the 12factor inspired
CACHE_URL environment variable to configure your Django application.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This simple Django utility allows you to utilize the 12factor inspired
CACHE_URL environment variable to configure your Django application.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/django_cache_url.py
%{python3_sitelib}/django_cache_url-%{version}-py*.egg-info

%changelog
* Wed Jun 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.1.2-1
- Update to new upstream release 3.1.2

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.0.0-2
- Use var for source URL
- Better use of wildcards (rhbz#1786871)

* Sat Dec 28 2019 Fabian Affolter <mail@fabian-affolter.ch> - 3.0.0-1
- Initial package for Fedora
