%global		module		Data-miplib3

Name:		coin-or-%{module}
Summary:	COIN-OR mixed integer library
Version:	1.2.7
Release:	2%{?dist}
License:	EPL-1.0
URL:		https://projects.coin-or.org/svn/Data/miplib3
Source0:	https://www.coin-or.org/download/pkgsource/Data/%{module}-%{version}.tgz
BuildArch:	noarch
BuildRequires:	gcc
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel

%description
This package contains the COmputational INfrastructure for Operations
Research (COIN-OR) mixed integer library.

%prep
%autosetup -n %{module}-%{version}

%build
%configure
%make_build

%install
%make_install pkgconfiglibdir=%{_datadir}/pkgconfig

%files
%{_datadir}/coin/
%{_datadir}/pkgconfig/coindatamiplib3.pc

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 2019 Jerry James <loganjerry@gmail.com> - 1.2.7-1
- Initial RPM
