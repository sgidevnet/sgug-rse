%global pypi_name aiodnsbrute

Name:           %{pypi_name}
Version:        0.3.2
Release:        4%{?dist}
Summary:        DNS asynchronous brute force utility

License:        GPLv3
URL:            https://github.com/blark/aiodnsbrute
Source0:        https://github.com/blark/aiodnsbrute/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
A Python tool that uses asyncio to brute force domain names asynchronously.

%prep
%autosetup -n %{pypi_name}-%{version}
sed -i -e $'s/ \''asyncio\'',//g' setup.py

%build
%py3_build

%install
%py3_install

%files
%doc CHANGELOG README.md
%license LICENSE.txt
%{_bindir}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-4
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.2-2
- Fix requirement (rhbz#1762675)

* Thu Oct 17 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.2-1
- Initial package for Fedora
