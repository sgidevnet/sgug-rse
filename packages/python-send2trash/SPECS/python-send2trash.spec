%global pypiname Send2Trash

Name:           python-send2trash
Version:        1.4.2
Release:        13%{?dist}
Summary:        Python library to natively send files to Trash

License:        BSD
URL:            https://github.com/hsoft/send2trash

# PyPI sdist lacks tests
Source0:        %url/archive/%{version}/%{pypiname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Send2Trash is a small package that sends files to the Trash (or Recycle Bin)
natively and on all platforms. On OS X, it uses native FSMoveObjectToTrashSync
Cocoa calls, on Windows, it uses native (and ugly) SHFileOperation win32 calls.
On other platforms, if PyGObject and GIO are available, it will use this.
Otherwise, it will fallback to its own implementation of the trash specifications
from freedesktop.org.

%package -n python3-send2trash

Summary:        Python library to natively send files to Trash
Provides:       python3-%{pypiname} == %{version}-%{release}

%{?python_provide:%python_provide python3-%{pypiname}}
%{?python_provide:%python_provide python3-send2trash}

%description -n python3-send2trash
Send2Trash is a small package that sends files to the Trash (or Recycle Bin)
natively and on all platforms. On OS X, it uses native FSMoveObjectToTrashSync
Cocoa calls, on Windows, it uses native (and ugly) SHFileOperation win32 calls.
On other platforms, if PyGObject and GIO are available, it will use this.
Otherwise, it will fallback to its own implementation of the trash specifications
from freedesktop.org.

%prep
%setup -q -n send2trash-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-send2trash
%license LICENSE
%doc README.rst CHANGES.rst
%{python3_sitelib}/send2trash/
%{python3_sitelib}/%{pypiname}-%{version}-py?.?.egg-info

%changelog
* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-13
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-8
- Subpackage python2-send2trash has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-3
- Run tests, use GH tarball
- Be more explicit in %%files
- Add plain pythonX-%%{pypiname} provides
- Correct a typo in Python 2 python_provide

* Sat Jan 06 2018 williamjmorenor@gmail.com - 1.4.2-2
- Initial import of BZ#1529027

* Tue Dec 26 2017 williamjmorenor@gmail.com - 1.4.2-1
- Initial Packaging


