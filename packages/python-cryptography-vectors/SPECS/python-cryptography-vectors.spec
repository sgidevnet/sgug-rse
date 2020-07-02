%if 0%{?fedora} || 0%{?rhel} > 7
# Enable python3 build by default
%bcond_without python3
%else
%bcond_with python3
%endif

%if 0%{?fedora} > 31 || 0%{?rhel} > 7
# Disable python2 build by default
%bcond_with python2
%else
%bcond_without python2
%endif

%global srcname cryptography-vectors
%global pysrcname cryptography_vectors

Name:           python-%{srcname}
Version:        2.9
Release:        2%{?dist}
License:        ASL 2.0 or BSD
Summary:        Test vectors for the cryptography package
URL:            https://pypi.python.org/pypi/cryptography-vectors
Source0:        https://pypi.io/packages/source/c/%{srcname}/cryptography_vectors-%{version}.tar.gz

BuildArch:      noarch

%description
Test vectors for the cryptography package.

The only purpose of this package is to be a building requirement for
python-cryptography, otherwise it has no use. Don’t install it unless
you really know what you are doing.

%if 0%{?with_python2}
%package -n  python2-%{srcname}
Summary:        Test vectors for the cryptography package
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
Test vectors for the cryptography package.

The only purpose of this package is to be a building requirement for
python-cryptography, otherwise it has no use. Don’t install it unless
you really know what you are doing.
%endif

%if 0%{?with_python3}
%package -n  python%{python3_pkgversion}-%{srcname}
Summary:        Test vectors for the cryptography package
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
Test vectors for the cryptography package.

The only purpose of this package is to be a building requirement for
python-cryptography, otherwise it has no use. Don’t install it unless
you really know what you are doing.
%endif

%prep
%setup -q -n %{pysrcname}-%{version}
rm -vrf %{pysrcname}.egg-info

%build
%if 0%{?with_python2}
%py2_build
%endif
%if 0%{?with_python3}
%py3_build
%endif

%check
%if 0%{?with_python2}
%{__python2} setup.py test
%endif
%if 0%{?with_python3}
%{__python3} setup.py test
%endif

%install
%if 0%{?with_python2}
%py2_install
%endif
%if 0%{?with_python3}
%py3_install
%endif

%if 0%{?with_python2}
%files -n python2-%{srcname}
%license LICENSE LICENSE.APACHE LICENSE.BSD
%{python2_sitelib}/%{pysrcname}/
%{python2_sitelib}/%{pysrcname}-%{version}-py*.egg-info
%endif

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE LICENSE.APACHE LICENSE.BSD
%{python3_sitelib}/%{pysrcname}/
%{python3_sitelib}/%{pysrcname}-%{version}-py*.egg-info
%endif

%changelog
* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 2.9-2
- Rebuilt for Python 3.9

* Fri Apr 03 2020 Christian Heimes <cheimes@redhat.com> - 2.9-1
- Update to 2.9 (#1820347)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 17 2019 Christian Heimes <cheimes@redhat.com> - 2.8-1
- Update to 2.8
- Resolves: rhbz#1762778

* Sat Oct 12 2019 Christian Heimes <cheimes@redhat.com> - 2.7-2
- Drop Python 2 package
- Resolves: rhbz#1761082

* Tue Sep 03 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.7-1
- Update to 2.7 (#1715681).

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 2.6.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 28 2019 Christian Heimes <cheimes@redhat.com> - 2.6.1-1
- New upstream release 2.6.1, resolves RHBZ#1683692

* Wed Feb 13 2019 Alfredo Moralejo <amoralej@redhat.com> - 2.5-1
- Update to 2.5.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 18 2018 Christian Heimes <cheimes@redhat.com> - 2.3-1
- New upstream release 2.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-5
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Christian Heimes <cheimes@redhat.com> - 2.2.1-4
- Fix typo

* Tue Jun 19 2018 Christian Heimes <cheimes@redhat.com> - 2.2.1-3
- Build Python 2 package conditionally

* Fri Jun 15 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-2
- Rebuilt for Python 3.7

* Wed Mar 21 2018 Christian Heimes <cheimes@redhat.com> - 2.2.1-1
- New upstream release 2.2.1

* Sun Feb 18 2018 Christian Heimes <cheimes@redhat.com> - 2.1.4-1
- New upstream release 2.1.4

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
