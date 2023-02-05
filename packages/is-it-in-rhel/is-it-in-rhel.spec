Name:           is-it-in-rhel
Version:        1.0
Release:        1%{?dist}
Summary:        Command line tool to find out if a package is in RHEL
License:        GPLv2+
URL:            https://pagure.io/is-it-in-rhel
Source0:        https://releases.pagure.org/is-it-in-rhel/is-it-in-rhel-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)


%description
is-it-in-rhel is a command line utility to find out if a specific package is
packaged in RHEL or not.


%prep
%setup -q


%build
%py3_build


%install
%py3_install


%files
%license COPYING
%doc README.rst
%{python3_sitelib}/is_it_in_rhel.py
%{python3_sitelib}/__pycache__/is_it_in_rhel.cpython-%{python3_version_nodots}*.py*
%{python3_sitelib}/is_it_in_rhel-%{version}-py%{python3_version}.egg-info
%{_bindir}/is-it-in-rhel


%changelog
* Thu Aug 29 2019 Carl George <carl@george.computer> - 1.0-1
- Initial package rhbz#1746939
