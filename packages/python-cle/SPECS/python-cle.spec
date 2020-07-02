%global srcname cle

Name:           python-%{srcname}
Version:        8.20.6.8
Release:        1%{?dist}
Summary:        A Python interface for analyzing binary formats

License:        BSD
URL:            https://github.com/angr/cle
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
CLE loads binaries and their associated libraries, resolves imports
and provides an abstraction of process memory the same way as if it was
loader by the OS's loader.

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
CLE loads binaries and their associated libraries, resolves imports
and provides an abstraction of process memory the same way as if it was
loader by the OS's loader.

%prep
rm -f %{srcname}.egg-info/
%autosetup -n %{srcname}-%{version} -p1

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/cle/

%changelog
* Tue Jun 23 2020 W. Michael Petullo <mike@flyn.org> - 8.20.6.8-1
- New upstream version

* Sun Jun 14 2020 W. Michael Petullo <mike@flyn.org> - 8.20.6.1-1
- New upstream version
- Drop upstreamed patch

* Thu May 28 2020 W. Michael Petullo <mike@flyn.org> - 8.20.1.7-2
- Add commentary for patch: upstream merge request

* Mon May 25 2020 W. Michael Petullo <mike@flyn.org> - 8.20.1.7-1
- Initial package
