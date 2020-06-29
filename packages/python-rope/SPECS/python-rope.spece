%global srcname rope
%if 0%{?rhel} && 0%{?rhel} <= 7
%bcond_without python2
%else
%bcond_with python2
%endif

Name:           python-%{srcname}
Version:        0.17.0
Release:        4%{?dist}
Summary:        Python Code Refactoring Library

License:        LGPLv3+
URL:            https://github.com/python-rope/rope
Source0:        https://files.pythonhosted.org/packages/source/r/rope/rope-%{version}.tar.gz

Patch0:         isalive_fix.patch

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3-setuptools

# pysvn, hg, git, and darcs are optional.  If installed, they give integration
# between rope and the version control system.  (So refactorings that rename a
# file, for instance, will be checked into version control.)

%global _description\
A python refactoring library. It provides features like refactorings and coding\
assists.

%description %_description

%if %{with python2}
%package -n python2-rope
Summary: %summary
%{?python_provide:%python_provide python2-rope}
BuildRequires: python2-devel

%description -n python2-rope %_description
%endif

%package -n python%{python3_pkgversion}-rope
Summary: %summary
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-rope %_description


%prep
%autosetup -p1 -n rope-%{version}

%build
%if %{with python2}
%py2_build
%endif
%py3_build

%install
%if %{with python2}
%py2_install
%endif
%py3_install

%check
%if %{with python2}
%{__python2} setup.py test
%endif
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-3 -v -k "not ( advanced_oi_test )"

%if %{with python2}
%files -n python2-rope
%license COPYING
%doc README.rst docs
%{python2_sitelib}/*
%endif

%files -n python%{python3_pkgversion}-rope
%license COPYING
%doc README.rst docs
%{python3_sitelib}/*

%changelog
* Tue Jun 23 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.17.0-4
- Add BR:python3-setuptools

* Wed Jun 03 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.17.0-3
- Add patch to fix failing tests

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.17.0-2
- Rebuilt for Python 3.9

* Tue May 05 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.17.0-1
- Update to 0.17.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Tuomo Soini <tis@foobar.fi> - 0.16.0-2
- Build with python2 support (#1695212).

* Sat Jan 11 2020 Matěj Cepl <mcepl@cepl.eu> - 0.16.0-1
- Update to the latest upstream release.

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.14.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.14.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 23 2019 Matěj Cepl <mcepl@cepl.eu> - 0.14.0-1
- Update to the latest upstream release.
- Change license from GPLv2+ to LGPLv3+

* Fri Mar 08 2019 Troy Dawson <tdawson@redhat.com> - 0.12.0-2
- Rebuilt to change main python from 3.4 to 3.6

* Mon Feb 11 2019 Matěj Cepl <mcepl@cepl.eu> - 0.12.0-1
- Update to the latest upstream release.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 28 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.11.0-2
- Drop python2 package

* Thu Aug 09 2018 Matěj Cepl <mcepl@cepl.eu> - 0.11.0-1
- Upgrade to the latest upstream release
- Remove unnecessary patch

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.10.7-4
- Disable py3 tests temporarily

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.10.7-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 08 2017 Charalampos Stratakis <cstratak@redhat.com> - 0.10.7-1
- Update to 0.10.7.
- Add python3 subpackage.

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.10.3-3
- Python 2 binary package renamed to python2-rope
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 21 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.10.3-1
- Update to 0.10.3

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Matěj Cepl <mcepl@redhat.com> - 0.10.2-4
- Upgrade to the latest upstream release (finally!)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 18 2012 Toshio Kuratomi <toshio@fedoraproject.org> - 0.9.4-1
- New upstream release

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-4.20101213hg1585
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-3.20101213hg1585
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 13 2010 Toshio Kuratomi <toshio@fedoraproject.org> 0.9.3-2.20101213hg1585
- Update to a snapshot to fix https://bugzilla.redhat.com/show_bug.cgi?id=649211

* Wed Sep 8 2010 Toshio Kuratomi <toshio@fedoraproject.org> 0.9.3-1
- Update to upstream 0.9.3.

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 22 2009 Toshio Kuratomi <toshio@fedoraproject.org> 0.9.2-1
- Update to upstream 0.9.2.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Nov 19 2008 Toshio Kuratomi <toshio@fedoraproject.org> 0.9.1-1
- Initial Fedora build
