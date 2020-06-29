%{?python_enable_dependency_generator}

%global modname repoze.who

Name:           python-repoze-who
Version:        2.4
Release:        1%{?dist}
Summary:        An identification and authentication framework for WSGI

License:        BSD
URL:            https://pypi.python.org/pypi/%{modname}
Source0:        https://pypi.python.org/packages/source/r/%{modname}/%{modname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:      python3-devel
BuildRequires:      python3-setuptools
BuildRequires:      python3-nose
BuildRequires:      python3-coverage
BuildRequires:      python3-zope-interface
BuildRequires:      python3-webob


%global _description\
repoze.who is an identification and authentication framework for arbitrary WSGI\
applications.  It acts as WSGI middleware.\
\
repoze.who is inspired by Zope 2's Pluggable Authentication Service (PAS) (but\
repoze.who is not dependent on Zope in any way; it is useful for any WSGI\
application).  It provides no facility for authorization (ensuring whether a\
user can or cannot perform the operation implied by the request).  This is\
considered to be the domain of the WSGI application.\


%description %_description

%package -n python3-repoze-who
Summary:        An identification and authentication framework for WSGI

%description -n python3-repoze-who
repoze.who is an identification and authentication framework for arbitrary WSGI
applications.  It acts as WSGI middleware.

repoze.who is inspired by Zope 2's Pluggable Authentication Service (PAS) (but
repoze.who is not dependent on Zope in any way; it is useful for any WSGI
application).  It provides no facility for authorization (ensuring whether a
user can or cannot perform the operation implied by the request).  This is
considered to be the domain of the WSGI application.

%prep
%setup -q -n %{modname}-%{version}

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info


%build
%py3_build


%install
%py3_install

%check
PYTHONPATH=$(pwd) %{__python3} setup.py test


%files -n python3-repoze-who
%doc README.rst CHANGES.rst CONTRIBUTORS.txt
%license COPYRIGHT.txt LICENSE.txt
%{python3_sitelib}/repoze/who/
%{python3_sitelib}/%{modname}-*


%changelog
* Thu Jun 04 2020 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 2.4-1
- Update to upstream

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.3-3
- Rebuilt for Python 3.9

* Sun May 10 2020 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 2.3-2
- Fix compatibility with zope-interface >= 5 (bz#1825462)

* Thu Apr 16 2020 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 2.3-1
- Update to upstream
- Update URLs to https
- Marked COPYRIGHT and LICENSE files as licenses

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1-22
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1-21
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1-18
- Enable python dependency generator

* Mon Jan 14 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1-17
- Subpackage python2-repoze-who has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1-15
- Rebuilt for Python 3.7

* Wed Feb 14 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.1-14
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 17 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.1-12
- Python 2 binary package renamed to python2-repoze-who
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.1-9
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 04 2013 Luke Macken <lmacken@redhat.com> - 2.1-1
- Update to 2.1
- Add a python3 subpackage
- Remove setuptools patch

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 26 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 1.0.18-4
- Add missing BR: python-coverage

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue May 04 2010 Luke Macken <lmacken@redhat.com> - 1.0.18-2
- Run the test suite in %%check

* Mon Apr 26 2010 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 1.0.18-1
- Update to the latest upstream release.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May 06 2009 Luke Macken <lmacken@redhat.com> - 1.0.13-1
- Update to the latest upstream release.

* Tue Oct 21 2008 Luke Macken <lmacken@redhat.com> - 1.0.7-1
- Initial package
