Name:           wad
Version:        0.4.5
Release:        1%{?dist}
Summary:        Tool for detecting technologies used by web applications

# wad is GPLv3, wappalyzer source is MIT
License:        GPLv3 and MIT
URL:            https://github.com/CERN-CERT/WAD
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-mock

%description
WAD lets you analyze given URL(s) and detect technologies used by web
application behind that URL, from the OS and web server level, to the
programming platform and frameworks, as well as server- and client-side
applications, tools and libraries.

%prep
%autosetup -n %{name}-%{version}
rm -rf %{pypi_name}.egg-info
mv wad/etc/README.md wad/etc/README-wappalyzer.md

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v %{name}/tests

%files
%license LICENSE
%doc README.md wad/etc/README-wappalyzer.md
%{_bindir}/wad
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-%{version}-py*.egg-info/

%changelog
* Fri Sep 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.5-1
- Update to latest upstream release 0.4.5 (#1882610)

* Thu Aug 20 2020 Fabian Affolter  <mail@fabian-affolter.ch> - 0.4.4-1
- Update to latest upstream release 0.4.4

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.3-2
- Rebuilt for Python 3.9

* Sat May 16 2020 Fabian Affolter  <mail@fabian-affolter.ch> - 0.4.3-1
- Update to latest upstream release 0.4.3

* Sat May 16 2020 Fabian Affolter  <mail@fabian-affolter.ch> - 0.4.2-1
- Update to latest upstream release 0.4.2
- Fix for Python 3.9 (rhbz#1834183)
 
* Thu Apr 30 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.1-1
- Initial package for Fedora

