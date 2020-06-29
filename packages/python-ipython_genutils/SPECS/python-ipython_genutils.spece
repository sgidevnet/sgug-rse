%global srcname ipython_genutils

Name:           python-%{srcname}
Version:        0.1.0
Release:        22%{?dist}
Summary:        IPython vestigial utilities

License:        BSD
URL:            https://github.com/ipython/%{srcname}
Source0:        https://pypi.python.org/packages/source/i/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
This package is a stop-gap that contains some common utilities shared by
Jupyter and IPython projects during The Big Split™. As soon as possible,
those packages will remove their dependency on this, and this repo will go
away.

No functionality should be added to this repository, and no packages outside
IPython/Jupyter should depend on it.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        IPython vestigial utilities
BuildRequires:  python%{python3_pkgversion}-devel
# For tests
BuildRequires:  python%{python3_pkgversion}-nose
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
This package is a stop-gap that contains some common utilities shared by
Jupyter and IPython projects during The Big Split™. As soon as possible,
those packages will remove their dependency on this, and this repo will go
away.

No functionality should be added to this repository, and no packages outside
IPython/Jupyter should depend on it.


%prep
%setup -q -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%check
export LANG=C.UTF-8
nosetests-%{python3_version} -v

 
%files -n python%{python3_pkgversion}-%{srcname}
%doc README.md
%license COPYING.md
%{python3_sitelib}/*


%changelog
* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-22
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-20
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-19
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar  8 2019 Orion Poplawski <orion@nwra.com> - 0.1.0-17
- Drop python2 package (bugz #1686355)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.1.0-15
- Use C.UTF-8 locale
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-13
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.1.0-12
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-8
- Rebuild for Python 3.6

* Fri Oct 14 2016 Orion Poplawski <orion@cora.nwra.com> - 0.1.0-7
- No python2 package for EPEL6 (needs python 2.7)

* Thu Oct 13 2016 Orion Poplawski <orion@cora.nwra.com> - 0.1.0-7
- Properly ship python2-ipython_genutils

* Thu Oct 13 2016 Orion Poplawski <orion@cora.nwra.com> - 0.1.0-6
- Enable python3 builds for EPEL
- Ship python2-ipython_genutils
- Modernize spec

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sat Jul 11 2015 Orion Poplawski <orion@cora.nwra.com> - 0.1.0-2
- Use nosetests

* Fri Jul 10 2015 Orion Poplawski <orion@cora.nwra.com> - 0.1.0-1
- Initial package
