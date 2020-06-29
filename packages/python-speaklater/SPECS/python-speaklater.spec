%global tarName speaklater

Name:           python-%{tarName}
Version:        1.3
Release:        20%{?dist}
Summary:        Implements a lazy string for python useful for use with gettext
License:        BSD
URL:            http://github.com/mitsuhiko/speaklater
Source0:        http://pypi.python.org/packages/source/s/%{tarName}/%{tarName}-%{version}.tar.gz
# Submitted upstream at: https://github.com/mitsuhiko/speaklater/pull/8
# Alternative approach at https://github.com/mitsuhiko/speaklater/pull/3
Patch0:         0001-Enable-building-on-python3-along-with-changes-to-doc.patch
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%global _description\
A module that provides lazy strings for translations. Basically you get an\
object that appears to be a string but changes the value every time the value\
is evaluated based on a callable you provide.

%description %_description

%package -n python3-speaklater
Summary: Implements a lazy string for python3 useful for gettext
%{?python_provide:%python_provide python3-speaklater}

%description -n python3-speaklater
A module that provides lazy strings for translations. Basically you get an
object that appears to be a string but changes the value every time the value
is evaluated based on a callable you provide.

This package provides the python3 version of the module.

%prep
%setup -qn %{tarName}-%{version}
%patch0 -p1

%build
%py3_build

%install
%py3_install

%check
pushd build/lib
%{__python3} -m doctest speaklater.py
popd

%files -n python3-speaklater
%{python3_sitelib}/speaklater*
%{python3_sitelib}/__pycache__/*
%license LICENSE
%doc PKG-INFO README

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3-20
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 24 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3-18
- Subpackage python2-speaklater has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3-17
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3-13
- Rebuilt for Python 3.7

* Wed Feb 14 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.3-12
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3-10
- Python 2 binary package renamed to python2-speaklater
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.3-7
- Rebuild for Python 3.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan  6 2016 Toshio Kuratomi <toshio@fedoraproject.org> - 1.3-5
- Add python3 subpackage
- Enable tests

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Luke Macken <lmacken@redhat.com> - 1.3-1
- Update to 1.3
- Add the README and LICENSE

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Jan 01 2011 Juan Eduardo Barba Olivet <xhaksx@fedoraproject.org> - 1.2-4
- install commands modified
- files commands modified

* Wed Dec 29 2010 Juan Eduardo Barba Olivet <xhaksx@fedoraproject.org> - 1.2-3
- Modifed documentation (get text changed to get-text)

* Mon Nov 15 2010 Juan Eduardo Barba Olivet <xhaksx@fedoraproject.org> - 1.2-2
- Modifed documentation (gettext changed)

* Mon Nov 15 2010 Juan Eduardo Barba Olivet <xhaksx@fedoraproject.org> - 1.2-1
- This is the first release of speaklater
- Added documentation
