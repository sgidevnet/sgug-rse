%global srcname fs

Name:           python-%{srcname}
Version:        2.4.11
Release:        5%{?dist}
Summary:        Python's Filesystem abstraction layer

License:        MIT
URL:            https://pypi.org/project/fs/
Source0:        https://github.com/PyFilesystem/pyfilesystem2/archive/v%{version}/%{srcname}-%{version}.tar.gz
Patch0:         fix-for-py3.9-release.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

BuildRequires:  python3dist(appdirs)
BuildRequires:  python3dist(pytz)
BuildRequires:  python3dist(six)
# Required for running tests
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-randomly)


%global _description %{expand:
Think of PyFilesystem's FS objects as the next logical step to Python's file
objects. In the same way that file objects abstract a single file, FS objects
abstract an entire filesystem.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n pyfilesystem2-%{version} -p1

%build
%py3_build

%install
%py3_install

%check
# tests/test_ftpfs.py needs pyftpdlib (not packaged yet)
%{python3} -m pytest --ignore tests/test_ftpfs.py --ignore tests/test_osfs.py --ignore tests/test_subfs.py --ignore tests/test_tempfs.py

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/

%changelog
* Wed Jun 24 2020 Parag Nemade <pnemade AT redhat DOT com> - 2.4.11-5
- Add missing BR: python3-setuptools

* Mon Jun 01 2020 Parag Nemade <pnemade AT redhat DOT com> - 2.4.11-4
- Disable few tests temporary for now (rhbz#1820916, rhbz#1841708)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.4.11-3
- Rebuilt for Python 3.9

* Mon Mar 30 2020 Parag Nemade <pnemade AT redhat DOT com> - 2.4.11-2
- enable tests and use upstream source tarball

* Mon Mar 30 2020 Parag Nemade <pnemade AT redhat DOT com> - 2.4.11-1
- Initial packaging

