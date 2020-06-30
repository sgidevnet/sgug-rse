%global pypi_name dictdumper

Name:           python-%{pypi_name}
Version:        0.8.3
Release:        1%{?dist}
Summary:        Python dict formatted dumper

License:        MPLv2.0
URL:            https://github.com/JarryShaw/DictDumper
Source0:        %{url}/archive/v%{version}/DictDumper-%{version}.tar.gz
BuildArch:      noarch

%description
The dictdumper project is an open source Python program works as a stream
formatted output dumper for dict.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
The dictdumper project is an open source Python program works as a stream
formatted output dumper for dict.

%prep
%autosetup -n DictDumper-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc AUTHORS.md CHANGELOG.md README.md
%license LICENSE
%{python3_sitelib}/*.egg-info/
%{python3_sitelib}/%{pypi_name}/

%changelog
* Mon Jun 01 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.3-1
- Update to latest upstream release 0.8.3 (rhbz#1842236)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.2-2
- Rebuilt for Python 3.9

* Fri Mar 20 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.2-1
- Update to latest upstream release 0.8.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 03 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.1-1
- Update to latest upstream release 0.7.1

* Sat Jun 08 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.0-1.post2
- Change version schema (rhbz#1714009)
- Use upstream source
- Add license file and fix license

* Sat May 25 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.0.post2-1
- Initial package for Fedora
