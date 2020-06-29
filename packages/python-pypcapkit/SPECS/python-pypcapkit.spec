%global pypi_name pypcapkit

Name:           python-%{pypi_name}
Version:        0.15.2
Release:        1%{?dist}
Summary:        Python multi-engine PCAP analyse kit

License:        MPLv2.0
URL:            https://github.com/JarryShaw/pypcapkit
Source0:        https://github.com/JarryShaw/PyPCAPKit/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
The pcapkit project is an open source Python program focus on PCAP parsing
and analysis, which works as a stream PCAP file extractor. With support of
dictdumper, it shall support multiple output report formats.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
The pcapkit project is an open source Python program focus on PCAP parsing
and analysis, which works as a stream PCAP file extractor. With support of
dictdumper, it shall support multiple output report formats.

%prep
%autosetup -n PyPCAPKit-%{version}
chmod -x LICENSE

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{_bindir}/pcapkit*
%{python3_sitelib}/pcapkit/
%{python3_sitelib}/%{pypi_name}*.egg-info

%changelog
* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.15.2-1
- Update to latest upstream release 0.15.2

* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.14.5-4
- Add python3-setuptools as BR

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.14.5-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.14.5-1
- Update to latest upstream release 0.14.5

* Mon Jun 10 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.14.2-1
- Update to latest upstream release 0.14.2
- Use upstream source instead of PyPI (rhbz#1714013)

* Sun May 26 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.13.3-1.post2
- Initial package for Fedora
