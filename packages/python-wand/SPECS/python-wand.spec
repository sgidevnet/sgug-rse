%global srcname wand
%global sum Ctypes-based simple MagickWand API binding for Python

Name:           python-%{srcname}
Version:        0.5.5
Release:        5%{?dist}
Summary:        %{sum}

License:        MIT
URL:            http://%{srcname}-py.org
Source0:        https://github.com/emcconville/%{srcname}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
Requires:       ImageMagick

Patch0:         load-library.patch

%description
Wand is a ctypes-based simple ImageMagick binding for Python. It doesn't cover
all functionalities of MagickWand API currently.

%package     -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Wand is a ctypes-based simple ImageMagick binding for Python. It doesn't cover
all functionalities of MagickWand API currently.


%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%py3_build

%install
%py3_install

rm $RPM_BUILD_ROOT/usr/README.rst

%files -n python3-%{srcname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/*


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.5-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.5-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.5-2
- Rebuilt for Python 3.8

* Tue Jul 30 2019 Dennis Chen <barracks510@gmail.com> - 0.5.5-1
- Update to Wand Version 0.5.5

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 29 2019 Dennis Chen <barracks510@gmail.com> - 0.5.2-1
- Minor version bump

* Tue Mar 05 2019 Dennis Chen <barracks510@gmail.com> - 0.5.1-1
- Updated to Wand Version 0.5.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4.4-8
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.4-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.4-2
- Rebuild for Python 3.6

* Sun Oct 30 2016 Dennis Chen <barracks510@gmail.com> - 0.4.4-1
- Updated to Wand Version 0.4.4.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jun 24 2016 Dennis Chen <barracks510@gmail.com> - 0.4.3-1
- Updated to Wand Version 0.4.3.
- Modernized SPEC file.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 25 2015 Dennis Chen <barracks510@gmail.com> - 0.4.2-1
- Updated to Wand version 0.4.2.

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Nov 5 2015 Dennis Chen <barracks510@gmail.com> 0.4.1-3
- Python3.5 rawhide rebuild

* Wed Oct 28 2015 Dennis Chen <barracks510@gmail.com> 0.4.1-2
- Fix python3 runtime dependency
- Fix spec errors

* Tue Oct 27 2015 Dennis Chen <barracks510@gmail.com> 0.4.1-1
- First Fedora Packaging

