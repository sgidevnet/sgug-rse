%global pypi_name text-unidecode

Name:           python-%{pypi_name}
Version:        1.3
Release:        3%{?dist}
Summary:        A Python module for handling non-Roman text data

License:        GPL+ or Artistic
URL:            https://github.com/kmike/text-unidecode/
Source0:        https://github.com/kmike/text-unidecode/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch  

%description
text-unidecode is the most basic port of the Text::Unidecode Perl library.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
text-unidecode is the most basic port of the Text::Unidecode Perl library.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/text_unidecode/
%{python3_sitelib}/text_unidecode-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 31 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.3-1
- Upgrade to latest upstream release 1.3
- Update license details (rhbz#1726400, rhbz#1725788)

* Tue Jun 25 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.2-1
- Initial package for Fedora
