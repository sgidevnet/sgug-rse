%global srcname lmdb
%global sum Python binding for the LMDB 'Lightning' Database (CPython & CFFI included)

Name:           python-%{srcname}
Version:        0.92
Release:        13%{?dist}
Summary:        %{sum}

License:        OpenLDAP
URL:            https://github.com/dw/py-lmdb
Source0:        https://pypi.python.org/packages/1b/ac/a1cd245e076d6bd35130a540201d5dbc0d64ecfa1a0bdd8af0c9ea72359d/lmdb-0.92.tar.gz

Patch0:         tests.patch
Patch1:         tests-disable-gh-issue-160.patch

BuildRequires:  gcc
BuildRequires:  python3-cffi
BuildRequires:  python3-devel
BuildRequires:  python3-nose
BuildRequires:  lmdb-devel

%description
%{sum}

%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{sum}


%prep
%autosetup -n lmdb-%{version}
%patch0 -p1
%patch1 -p1

%build
# do not use bundled LMDB library
export LMDB_FORCE_SYSTEM=1
unset LMDB_FORCE_CFFI
%py3_build

%install
export LMDB_FORCE_SYSTEM=1
unset LMDB_FORCE_CFFI
%py3_install

%check
export LMDB_FORCE_SYSTEM=1
unset LMDB_FORCE_CFFI

# The tests may jump between dirs!
# As a result some tests cannot find the binding in current working directory.
export PYTHONPATH=$(pwd)
nosetests-%{python3_version} -v
# % {__python2} setup.py test
# % {__python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE
%doc ChangeLog
%doc PKG-INFO
%{python3_sitearch}/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.92-13
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.92-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.92-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.92-7
- Subpackage python2-lmdb has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.92-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Petr Špaček <petr.spacek@nic.cz> - 0.92-1
 Initial build using CPython extension and system LMDB library by default.

 The code was imported from PyPI package v0.92 MD5 00520384f53f0c9f6347e681d4bb8140
 + test from Git repo 4651bb3a865c77008ac261443899fe25f88173f2.

 Known problems:
 - crash on put if Environment(writemap=True) and data is too big for FS
   https://github.com/dw/py-lmdb/issues/161
 - crash on Environment(readonly=True).db_open(create=True)
   https://github.com/dw/py-lmdb/issues/160
