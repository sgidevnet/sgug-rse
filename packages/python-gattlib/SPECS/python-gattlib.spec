%global modname gattlib

Name:               python-gattlib
Version:            0.20200122
Release:            3%{?dist}
Summary:            Library to access Bluetooth LE devices

License:            ASL 2.0 and GPLv2+ and LGPLv2+
# main package under ASL 2.0
# src/bluez under GPLv2+ and LGPLv2+
URL:                https://bitbucket.org/OscarAcena/pygattlib
Source0:            https://files.pythonhosted.org/packages/source/g/%{modname}/%{modname}-%{version}.tar.gz
Source1:	    COPYING

BuildRequires:      gcc-c++

%description
%{summary}.

%package -n python%{python3_pkgversion}-%{modname}
Summary:            %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}}
BuildRequires:      python%{python3_pkgversion}-devel
BuildRequires:      python%{python3_pkgversion}-setuptools
BuildRequires:      boost-python3-devel
BuildRequires:      glib2-devel
BuildRequires:      bluez-libs-devel

%description -n python%{python3_pkgversion}-%{modname}
%{summary}.

Python %{python3_version} version.

%prep
%autosetup -n %{modname}-%{version}
cp %{S:1} .

find . -type f | xargs chmod -x

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python%{python3_pkgversion}-%{modname}
%license COPYING
%{python3_sitearch}/gattlib*
%{python3_sitearch}/%{modname}*.egg-info/

%changelog
* Sat May 30 2020 Jonathan Wakely <jwakely@redhat.com> - 0.20200122-3
- Rebuilt for Boost 1.73

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.20200122-2
- Rebuilt for Python 3.9

* Wed Jan 22 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.20200122-1
- 0.20200122

* Tue Jan 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.20200121-1
- 0.20200121

* Fri Jan 17 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.20200117-1.post3
- 0.2020017.post3

* Sat Nov 02 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.20150805-12
- Drop Python 2.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.20150805-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20150805-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 22 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.20180805-9
- Update patch to fix 3.8 FTBFS.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20150805-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Jonathan Wakely <jwakely@redhat.com> - 0.20150805-7
- Patch for Boost.Python library names in Boost 1.69.0

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 0.20150805-7
- Rebuilt for Boost 1.69

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20150805-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.20150805-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20150805-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 0.20150805-3
- Rebuilt for Boost 1.66

* Tue Dec 12 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.20150805-2
- License clarification.

* Mon Dec 11 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.20150805-1
- Add license file, fix URL, explain patch.

* Mon Dec 11 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.20150805-0
- Initial package.
