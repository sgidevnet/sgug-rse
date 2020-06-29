%global srcname optcomplete

# This appears to be 1.2.1
%global commit 4778834773173d7bf3b1022e23d65d9690eefb5b
%global shortcommit %(c=%{commit}; echo ${c:0:12})

Name:           python-%{srcname}
Version:        1.2.1
Release:        6%{?dist}
Summary:        Shell Completion Self-Generator for Python

License:        BSD
URL:            http://furius.ca/%{srcname}
Source0:        https://bitbucket.org/blais/%{srcname}/get/%{commit}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

%description
This Python module aims at providing almost automatically shell completion
BuildRequires:  python2-devel


%if 0%{?fedora} < 30
%package -n python2-%{srcname}
Summary:        Shell Completion Self-Generator for Python 2
BuildRequires:  python2-devel
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
This Python 2 module aims at providing almost automatically shell completion
for any Python program that already uses the optparse module.
%endif

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Shell Completion Self-Generator for Python 3
BuildRequires:  python%{python3_pkgversion}-devel
# For 2to3
BuildRequires:  /usr/bin/2to3
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
This Python 3 module aims at providing almost automatically shell completion
for any Python program that already uses the optparse module.


%prep
%setup -q -c
%if 0%{?fedora} < 30
cp -a blais-%{srcname}-%{shortcommit} python2
%endif

cp -a blais-%{srcname}-%{shortcommit} python3
2to3 --write --nobackups python3


%build
%if 0%{?fedora} < 30
pushd python2
%py2_build
popd
%endif

pushd python3
%py3_build
popd


%install
# Must do the python3 install first because the scripts in /usr/bin are
# overwritten with every setup.py install (and we want the python2 version
# to be the default for now).
pushd python3
%py3_install
popd

%if 0%{?fedora} < 30
pushd python2
%py2_install
popd
%endif


%if 0%{?fedora} < 30
%files -n python2-%{srcname}
%license python2/COPYING
%doc python2/CHANGES python2/CREDITS python2/doc/*.txt python2/README python2/TODO
%{python2_sitelib}/*
%endif

%files -n python%{python3_pkgversion}-%{srcname}
%license python3/COPYING
%doc python3/CHANGES python3/CREDITS python3/doc/*.txt python3/README python3/TODO
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/*.py
%{python3_sitelib}/__pycache__/*


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr  8 2019 Orion Poplawski <orion@nwra.com> - 1.2.1-1
- Update to 1.2.1 (bug #1697149)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.21.20130428hg9583af7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 07 2018 Orion Poplawski <orion@cora.nwra.com> - 1.2-0.20.20130428hg9583af7
- Drop Python 2 package for Fedora 30+ (bugz #1629742)

* Tue Jul 17 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2-0.19.20130428hg9583af7
- Update Python macros to new packaging standards
  (See https://fedoraproject.org/wiki/Changes/Move_usr_bin_python_into_separate_package)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.18.20130428hg9583af7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2-0.17.20130428hg9583af7
- Rebuilt for Python 3.7

* Tue Feb 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2-0.16.20130428hg9583af7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.15.20130428hg9583af7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.14.20130428hg9583af7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.13.20130428hg9583af7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2-0.12.20130428hg9583af7
- Rebuild for Python 3.6

* Wed Nov 16 2016 Orion Poplawski <orion@cora.nwra.com> - 1.2-0.11.20130428hg9583af7
- Modernize spec

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.10.20130428hg9583af7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.9.20130428hg9583af7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.8.20130428hg9583af7
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.7.20130428hg9583af7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.6.20130428hg9583af7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 02 2014 Orion Poplawski <orion@cora.nwra.com> - 1.2-0.5.20130428hg9583af7
- Rebuild for Python 3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.4.20130428hg9583af7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Apr 28 2013 Orion Poplawski <orion@cora.nwra.com> - 1.2-0.3.20130428hg9583af7
- Update to latest hg version
- Re-add COPYING

* Sat Apr 27 2013 Orion Poplawski <orion@cora.nwra.com> - 1.2-0.2.20130406hg4416852
- Drop COPYING - wrong license

* Sun Apr 7 2013 Orion Poplawski <orion@cora.nwra.com> - 1.2-0.1.20130406hg4416852
- Initial Fedora package
