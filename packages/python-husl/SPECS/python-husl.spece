%global upname husl

Name: python-%{upname}
Version: 4.0.3
Release: 17%{?dist}
Summary: A Python implementation of HUSL
License: MIT

URL: http://github.com/boronine/pyhusl
Source0: https://pypi.python.org/packages/source/h/husl/husl-%{version}.tar.gz
# By mistake the license is not packaged (fixed in devel version upstream)
Source1: https://raw.githubusercontent.com/husl-colors/husl-python/master/LICENSE.txt
BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%global _description\
HUSL is a human-friendly alternative to HSL (Hue, Saturation and Lightness)\
color space. This package provides Python2 support

%description %_description

%package -n python3-%{upname}
Summary: A Python implementation of HUSL
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description -n python3-%{upname}
HUSL is a human-friendly alternative to HSL (Hue, Saturation and Lightness)
color space. This package provides Python3 support


%prep
%setup -q -n %{upname}-%{version}

find . -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'

%build
cp -p %{SOURCE1} .
%py3_build

%install
%py3_install

%files -n python3-%{upname}
%doc README.md
%license LICENSE.txt
%{python3_sitelib}/husl*
%{python3_sitelib}/__pycache__/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0.3-17
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.3-15
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.3-14
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Miro Hrončok <mhroncok@redhat.com> - 4.0.3-11
- Subpackage python2-husl has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.0.3-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.0.3-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.0.3-6
- Python 2 binary package renamed to python2-husl
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4.0.3-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.3-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat Jul 02 2016 José Abílio Matos <jamatos@fc.up.pt> - 4.0.3-1
- update to 4.0.3

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Nov 21 2014 Sergio Pascual <sergiopr at fedoraproject.com> - 4.0.1-1
- Initial SPEC
