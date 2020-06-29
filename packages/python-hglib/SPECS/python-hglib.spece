%if 0%{?fedora} < 31 && 0%{?rhel} < 8
%global         with_python2 1
%endif

Summary:        Mercurial Python library
Name:           python-hglib
Version:        2.6.1
Release:        11%{?dist}
License:        MIT
URL:            http://selenic.com/repo/python-hglib
Source0:        https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
Patch0:         python-hglib-hg-52.patch
BuildArch:      noarch
BuildRequires:  mercurial
%if 0%{?with_python2}
BuildRequires:  python2-devel
BuildRequires:  python2-nose
%endif
BuildRequires:  python3-devel
BuildRequires:  python3-nose
%description
python-hglib is a library with a fast, convenient interface to
Mercurial. It uses Mercurials command server for communication with
hg.

%if 0%{?with_python2}
%package     -n python2-hglib
Summary:        Mercurial Python library
%{?python_provide:%python_provide python2-hglib}
%description -n python2-hglib
python-hglib is a library with a fast, convenient interface to
Mercurial. It uses Mercurials command server for communication with
hg.
%endif

%package     -n python3-hglib
Summary:        Mercurial Python library
%{?python_provide:%python_provide python3-hglib}
%description -n python3-hglib
python-hglib is a library with a fast, convenient interface to
Mercurial. It uses Mercurials command server for communication with
hg.

%prep
%setup -q
%patch0 -p1

%build
%if 0%{?with_python2}
%{py2_build}
%endif
%{py3_build}

%install
%if 0%{?with_python2}
%{py2_install}
%endif
%{py3_install}

%check
%if 0%{?with_python2}
%{__python2} test.py --with-doctest
%endif
%{__python3} test.py --with-doctest

%if 0%{?with_python2}
%files -n python2-hglib
%license LICENSE
%{python2_sitelib}/hglib
%{python2_sitelib}/python_hglib-*-py*.egg-info
%endif

%files -n python3-hglib
%license LICENSE
%{python3_sitelib}/hglib
%{python3_sitelib}/python_hglib-*-py*egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.6.1-11
- Rebuilt for Python 3.9

* Sat Feb 01 2020 Terje Rosten <terje.rosten@ntnu.no> - 2.6.1-10
- Add mercurial 5.2 compat patch

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.6.1-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.6.1-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 05 2019 Terje Rosten <terje.rosten@ntnu.no> - 2.6.1-5
- Remove Python 2 subpackage on Fedora 31+ and el8+

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.6.1-2
- Rebuilt for Python 3.7

* Mon May 21 2018 Terje Rosten <terje.rosten@ntnu.no> - 2.6.1-1
- 2.6.1

* Thu Apr 26 2018 Terje Rosten <terje.rosten@ntnu.no> - 2.6-1
- 2.6

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 02 2018 Terje Rosten <terje.rosten@ntnu.no> - 2.5-1
- 2.5

* Fri Jan 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.4-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 04 2017 Terje Rosten <terje.rosten@ntnu.no> - 2.4-1
- 2.4

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Terje Rosten <terje.rosten@ntnu.no> - 2.3-1
- 2.3

* Wed Dec 28 2016 Adam Williamson <awilliam@redhat.com> - 2.2-1
- 2.2 (should fix issue between tests and recent hg)

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.0-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Feb 02 2016 Terje Rosten <terje.rosten@ntnu.no> - 2.0-1
- 2.0

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sat Oct 03 2015 Terje Rosten <terje.rosten@ntnu.no> - 1.9-1
- 1.9

* Wed Sep 02 2015 Terje Rosten <terje.rosten@ntnu.no> - 1.8-1
- 1.8

* Sun Aug 02 2015 Terje Rosten <terje.rosten@ntnu.no> - 1.7-1
- 1.7

* Wed Jun 24 2015 Terje Rosten <terje.rosten@ntnu.no> - 1.6-2
- use license macro (bz #1231330)

* Fri Jun 12 2015 Terje Rosten <terje.rosten@ntnu.no> - 1.6-1
- initial package
