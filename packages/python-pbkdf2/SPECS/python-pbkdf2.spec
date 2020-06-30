%global srcname pbkdf2
%global sum A module for a password-based key derivation function

Name:           python-%{srcname}
Version:        1.3
Release:        18%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://www.dlitz.net/software/python-pbkdf2/
Source0:        https://pypi.python.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
Patch1:         pbkdf2-license.patch
Patch2:         pbkdf2-remove-shebang.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%description
A pure Python Implementation of the password-based key derivation function,
PBKDF2, specified in RSA PKCS#5 v2.0.

%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
A pure Python Implementation of the password-based key derivation function,
PBKDF2, specified in RSA PKCS#5 v2.0.


%prep
%autosetup -n %{srcname}-%{version}

rm -rf %{srcname}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} -m unittest test/*

%files -n python3-%{srcname}
%doc PKG-INFO
%doc README.txt
%license LICENSE
%{python3_sitelib}/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3-18
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3-16
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3-15
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jonny Heggheim <hegjon@gmail.com> - 1.3-11
- Removed python2 sub-package

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3-10
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.3-6
- Rebuild for Python 3.6

* Tue Nov 08 2016 Jonny Heggheim <jonnyheggheim@sigaint.org> - 1.3-5
- Use autosetup
- Corrrected the LICENSE file to MIT
- Enable tests

* Mon Apr 25 2016 Samuel Gyger <gygers@fsfe.org> - 1.3-4
- Build for python2 and python3
- Use pybuild and pyinstall

* Mon Apr 25 2016 Samuel Gyger <gygers@fsfe.org> - 1.3-3
- Added proper license file and fixed license

* Tue Jan 27 2015 Samuel Gyger <gygers@fsfe.org> - 1.3-2
- Fixed to be only for python2

* Tue Jan 27 2015 Samuel Gyger <gygers@fsfe.org> - 1.3-1
- Created the initial packaging for pkbdf2 on fedora.
