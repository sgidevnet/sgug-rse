%{?python_enable_dependency_generator}

Name:           python-repoze-tm2
Version:        2.1
Release:        2%{?dist}
Summary:        Zope-like transaction manager via WSGI middleware

License:        BSD
URL:            https://pypi.python.org/pypi/repoze.tm2
Source0:        https://pypi.python.org/packages/source/r/repoze.tm2/repoze.tm2-%{version}.tar.gz
BuildArch:      noarch

%global _description\
The ZODB transaction manager is a completely generic transaction manager.  It\
can be used independently of the actual "object database" part of ZODB.  One\
of the purposes of creating repoze.tm was to allow for systems other than\
Zope to make use of two-phase commit transactions in a WSGI context.

%description %_description

%package -n python3-repoze-tm2
Summary: Zope-like transaction manager via WSGI middleware
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-nose
BuildRequires: python3-transaction
%{?python_provide:%python_provide python3-repoze-tm2}

%description -n python3-repoze-tm2
The ZODB transaction manager is a completely generic transaction manager.  It
can be used independently of the actual "object database" part of ZODB.  One
of the purposes of creating repoze.tm was to allow for systems other than
Zope to make use of two-phase commit transactions in a WSGI context.

This package contains the python3 version of the library.


%prep
%setup -q -n repoze.tm2-%{version}


%build
%py3_build


%install
%py3_install


%check
nosetests-3


%files -n python3-repoze-tm2
%license LICENSE.txt
%doc README.rst COPYRIGHT.txt CHANGES.rst
%{python3_sitelib}/*


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1-2
- Rebuilt for Python 3.9

* Thu Apr 16 2020 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 2.1-1
- Update to upstream
- Update URLs to https

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0-19
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0-18
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 04 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0-15
- Enable python dependency generator

* Fri Jan 04 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0-14
- Subpackage python2-repoze-tm2 has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Tue Jul 17 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0-13
- Update Python macros to new packaging standards
  (See https://fedoraproject.org/wiki/Changes/Move_usr_bin_python_into_separate_package)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0-11
- Rebuilt for Python 3.7

* Wed Feb 14 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.0-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.0-8
- Python 2 binary package renamed to python2-repoze-tm2
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.0-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan  7 2016 Toshio Kuratomi <toshio@fedoraproject.org> - - 2.0-2
- Really create the python3 subpackage this time.

* Wed Jan  6 2016 Toshio Kuratomi <toshio@fedoraproject.org> - 2.0-1
- Add a python3 subpackage

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.16.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.15.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Dec 06 2013 Pierre-Yves Chibon <pingou@pingoured>fr - 1.0-0.14.b1
- Change BR from python-setuptools-devel to python-setuptools
  See https://fedoraproject.org/wiki/Changes/Remove_Python-setuptools-devel

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.13.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.12.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.11.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.10.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 23 2011 Luke Macken <lmacken@redhat.com> - 1.0-0.9.b1
- Update to 1.0b1

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.8.a5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.0-0.7.a5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed May 05 2010 Luke Macken <lmacken@redhat.com> - 1.0-0.5.a5
- Update to 1.0a5
- Run the test suite in %%check

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.5.a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 01 2009 Luke Macken <lmacken@redhat.com> - 1.0-0.4.a4
- Update to 1.0a4

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.3.a3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.0-0.2.a3
- Rebuild for Python 2.6

* Tue Oct 21 2008 Luke Macken <lmacken@redhat.com> - 1.0-0.1.a2
- Initial package
