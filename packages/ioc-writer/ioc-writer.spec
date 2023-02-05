%global pypi_name ioc_writer

Name:           ioc-writer
Version:        0.3.3
Release:        3%{?dist}
Summary:        A tool to create and edit OpenIOC objects

License:        ASL 2.0
URL:            https://github.com/mandiant/ioc_writer
Source0:        https://github.com/mandiant/ioc_writer/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-lxml

%description
A tool that allows for basic creation and editing of OpenIOC objects. It
supports a basic CRUD (create, read, update, delete) for various items.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files
%doc README.md
%license LICENSE
%{_bindir}/iocdump
%{_bindir}/openioc*
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/%{pypi_name}/

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.3-2
- Change source location (rhbz#1720861)

* Sat Jun 15 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.3-1
- Initial package for Fedora
