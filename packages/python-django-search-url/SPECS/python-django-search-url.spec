%global pypi_name dj-search-url
%global pkg_name django-search-url

Name:           python-%{pkg_name}
Version:        0.1
Release:        4%{?dist}
Summary:        Use Search URLs in your Django Application

License:        BSD
URL:            https://github.com/dstufft/dj-search-url
Source0:        %{pypi_source}
BuildArch:      noarch

%description
This simple Django utility allows you to utilize the 12factor inspired
SEARCH_URL environment variable to configure your application.

%package -n     python3-%{pkg_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pkg_name}
This simple Django utility allows you to utilize the 12factor inspired
SEARCH_URL environment variable to configure your application.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pkg_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/dj_search_url.py
%{python3_sitelib}/dj_search_url-%{version}-py*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1-2
- Use var for source URL
- Better use of wildcards (rhbz#1786869)

* Sat Dec 28 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.1-1
- Initial package for Fedora
