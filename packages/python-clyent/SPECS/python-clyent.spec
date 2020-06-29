%global srcname clyent

Name:           python-%{srcname}
Version:        1.2.2
Release:        14%{?dist}
Summary:        Command line client library for posix and windows

# Asked upstream for a license file:
# https://github.com/Anaconda-Platform/clyent/issues/11
License:        BSD
URL:            https://github.com/Anaconda-Platform/%{srcname}
Source0:        https://github.com/Anaconda-Platform/%{srcname}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch


%description
Clyent is a python command line utility library for binstar, binstar-build and
chalmers.


%if 0%{?fedora} < 30
%package -n python2-%{srcname}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-mock
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
Clyent is a python command line utility library for binstar, binstar-build and
chalmers.
%endif

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-mock
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
Clyent is a python command line utility library for binstar, binstar-build and
chalmers.


%prep
%setup -q -n %{srcname}-%{version}

%build
%if 0%{?fedora} < 30
%py2_build
%endif
%py3_build

%install
%if 0%{?fedora} < 30
%py2_install
%endif
%py3_install

%check
%if 0%{?fedora} < 30
%{__python2} -m unittest discover
%endif
%{__python3} -m unittest discover


%if 0%{?fedora} < 30
%files -n python2-%{srcname}
%doc README.md
%{python2_sitelib}/%{srcname}*.egg-info
%{python2_sitelib}/%{srcname}
%endif

%files -n python%{python3_pkgversion}-%{srcname}
%doc README.md
%{python3_sitelib}/%{srcname}*.egg-info
%{python3_sitelib}/%{srcname}


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-14
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 07 2018 Orion Poplawski <orion@cora.nwra.com> - 1.2.2-8
- Drop Python 2 package for Fedora 30+ (bugz #1634885)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-6
- Rebuilt for Python 3.7

* Sun Feb 11 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2.2-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 13 2017 Orion Poplawski <orion@cora.nwra.com> - 1.2.2-2
- Add comment about license file request
- Fix typo

* Mon Jan 9 2017 Orion Poplawski <orion@cora.nwra.com> - 1.2.2-1
- Initial package
