# what it's called on pypi
%global srcname PyGithub
# what it's imported as
%global libname github
# name of egg info directory
%global eggname %{srcname}
# package name fragment
%global pkgname pygithub

Name:           python-%{srcname}
Version:        1.51
Release:        2%{?dist}
Summary:        Python library to work with the Github API
License:        LGPLv3+
URL:            https://github.com/PyGithub/PyGithub
# github tarball (unlike PyPI one) contains tests
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%global _description \
A Python library implementing the full Github API v3.

%description %{_description}

%package -n     python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-jwt
BuildRequires:  python%{python3_pkgversion}-requests
BuildRequires:  python%{python3_pkgversion}-deprecated
BuildRequires:  pyproject-rpm-macros

# Tests
BuildRequires:  python%{python3_pkgversion}-tox-current-env

Provides:       python%{python3_pkgversion}-github = %{version}-%{release}
Obsoletes:      python%{python3_pkgversion}-github < 1.25.2-2
Provides:       python%{python3_pkgversion}-PyGithub = %{version}-%{release}
Obsoletes:      python%{python3_pkgversion}-PyGithub < 1.29-8
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkgname}}

# Needs https://bugzilla.redhat.com/show_bug.cgi?id=PYTEST5
#%%generate_buildrequires
#%%pyproject_buildrequires -t

%description -n python%{python3_pkgversion}-%{pkgname} %{_description}

%prep
%autosetup -p 1 -n %{srcname}-%{version}
rm -rf %{eggname}.egg-info
# this test needs network connection => kill it for Koji builds
#sed -i '/Issue142/d' tests/AllTests.py

%build
%py3_build

%install
%py3_install

%check
# Needs https://bugzilla.redhat.com/show_bug.cgi?id=PYTEST5
#%%tox

%files -n python%{python3_pkgversion}-%{pkgname}
%license COPYING COPYING.LESSER
%doc README.md
%{python3_sitelib}/%{libname}
%exclude %{python3_sitelib}/%{libname}/tests
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.51-2
- Rebuilt for Python 3.9

* Mon May 04 2020 Jiri Popelka <jpopelka@redhat.com> - 1.51-1
- 1.51

* Tue Apr 28 2020 Jiri Popelka <jpopelka@redhat.com> - 1.50-1
- 1.50
- Would run tests with tox but blocked by PYTEST5

* Tue Feb 18 2020 Jiri Popelka <jpopelka@redhat.com> - 1.46-1
- 1.46
- Python 2 support has been removed (upstream & dist-git).

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.45-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 02 2020 Jiri Popelka <jpopelka@redhat.com> - 1.45-2
- BuildRequires:  python-parameterized

* Thu Jan 02 2020 Jiri Popelka <jpopelka@redhat.com> - 1.45-1
- 1.45

* Thu Nov 07 2019 Jiri Popelka <jpopelka@redhat.com> - 1.44.1-1
- 1.44.1

* Wed Oct 23 2019 Jiri Popelka <jpopelka@redhat.com> - 1.44-1
- Latest upstream

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.43.8-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.43.8-2
- Rebuilt for Python 3.8

* Mon Aug 12 2019 Jiri Popelka <jpopelka@redhat.com> - 1.43.8-1
- Latest upstream

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.39-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.39-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 04 2018 Carl George <carl@george.computer> - 1.39-5
- Disable python2 subpackage on F30+

* Wed Oct 03 2018 Carl George <carl@george.computer> - 1.39-4
- Require python-jwt on RHEL, python2-jwt on Fedora rhbz#1634082
- Add patch0 to ensure comments are included in create_review method rhbz#1633197

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.39-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.39-2
- Rebuilt for Python 3.7

* Tue Apr 10 2018 Carl George <carl@george.computer> - 1.39-1
- Latest upstream

* Thu Apr 05 2018 Carl George <carl@george.computer> - 1.38-1
- Latest upstream
- Share doc and license dir between subpackages
- Enable EPEL PY3 build

* Wed Apr  4 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.29-8
- Add missing Provides/Obsoletes for camelcase name (#1559280)
- Rename python3 subpackage to python3-pygithub

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.29-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.29-5
- Python 2 binary package renamed to python2-pygithub
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.29-2
- Rebuild for Python 3.6

* Thu Oct 06 2016 Jiri Popelka <jpopelka@redhat.com> - 1.29-1
- Update to 1.29

* Mon Sep 12 2016 Jiri Popelka <jpopelka@redhat.com> - 1.28-1
- Update to 1.28

* Fri Aug 12 2016 Jiri Popelka <jpopelka@redhat.com> - 1.27.1-1
- Update to 1.27.1
- Use macros

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 15 2015 Slavek Kabrda <bkabrda@redhat.com> - 1.26.0-1
- Update to 1.26.0

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25.2-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 05 2014 Slavek Kabrda <bkabrda@redhat.com> - 1.25.2-2
- Rename python3- subpackage to python3-PyGithub to match python2 package
(Obsoletes/Provides will handle update path)

* Tue Sep 30 2014 Tomas Radej <tradej@redhat.com> - 1.25.2-1
- Updated to latest upstream version

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.25.0-1
- Updated to 1.25.0.
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 02 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1.14.2-2
- Don't run test needing internet connection (fails in Koji).

* Thu May 02 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1.14.2-1
- Renamed to python-PyGithub (the previous name wasn't formed according
to Fedora naming guidelines).
- Updated to 1.14.2.

* Tue Mar 19 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1.11.1-3
- Specfile cleanup.
- Introduce python3 subpackage.

* Wed Feb 20 2013 Jiri Moskovcak <jmoskovc@redhat.com> - 1.11.1-2
- updated according to the review rhbz#910565 c#4

* Tue Feb 12 2013 Jiri Moskovcak <jmoskovc@redhat.com> - 1.11.1-1
- updated to the latest upstream

* Sun Feb 03 2013 Jiri Moskovcak <jmoskovc@redhat.com> - 1.10.0-1
- Initial package
