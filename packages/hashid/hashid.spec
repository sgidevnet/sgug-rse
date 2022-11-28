%global pypi_name hashID

Name:           hashid
Version:        3.1.4
Release:        2%{?dist}
Summary:        A tool to identify different types of hashes

License:        GPLv3+
URL:            https://github.com/psypanda/hashID
Source0:        https://github.com/psypanda/hashID/archive/v%{version}.tar.gz#/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%description
Identify the different types of hashes used to encrypt data and especially
passwords. hashID is a tool which supports the identification of over 220
unique hash types using regular expressions. A detailed list of supported
hashes can be found here.

It is able to identify a single hash, parse a file or read multiple files in
a directory and identify the hashes within them.

%prep
%autosetup -n %{pypi_name}-%{version}
sed -i -e '/^#!\//, 1d' hashid.py

%build
%py3_build

%install
%py3_install
install -Dp -m 0644 doc/man/%{name}.7 %{buildroot}%{_mandir}/man7/%{name}.7

%files
%doc README.rst doc/CHANGELOG
%license doc/LICENSE
%{_mandir}/man*/%{name}*.*
%{_bindir}/%{name}
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/%{name}.py
%{python3_sitelib}/__pycache__/*

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 25 2019 Fabian Affolter <mail@fabian-affolter.ch> - 3.1.4-1
- Initial package for Fedora
