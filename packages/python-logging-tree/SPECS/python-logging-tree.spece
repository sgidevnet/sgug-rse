%global pypi_name logging-tree
%global mod_name logging_tree

Name:               python-%{pypi_name}
Version:            1.8.1
Release:            3%{?dist}
Summary:            Introspect and display the logger tree inside "logging"

License:            BSD
URL:                https://github.com/brandon-rhodes/logging_tree
Source0:            https://github.com/brandon-rhodes/logging_tree/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:          noarch

%description
Introspection for the 'logging' logger tree in the Standard Library.

While you can write programs that call this package's 'tree()'
function and examine the hierarchy of logger objects that it finds
inside of the Standard Library 'logging' module, the simplest use of
this package for debugging is to call 'printout()' to print the
loggers, filters, and handlers that your application has configured::

    >>> logging.getLogger('a')
    >>> logging.getLogger('a.b').setLevel(logging.DEBUG)
    >>> logging.getLogger('x.c')
    >>> from logging_tree import printout
    >>> printout()
       ""
       Level WARNING
       |
       o<--"a"
       |   |
       |   o<--"a.b"
       |       Level DEBUG
       |
       o<--[x]
           |
           o<--"x.c"

%package -n python3-%{pypi_name}
Summary:            Introspect and display the logger tree inside "logging"

BuildRequires:      python3-devel
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Introspection for the ``logging`` logger tree in the Standard Library.

While you can write programs that call this package's ``tree()``
function and examine the hierarchy of logger objects that it finds
inside of the Standard Library ``logging`` module, the simplest use of
this package for debugging is to call ``printout()`` to print the
loggers, filters, and handlers that your application has configured::

    >>> logging.getLogger('a')
    >>> logging.getLogger('a.b').setLevel(logging.DEBUG)
    >>> logging.getLogger('x.c')
    >>> from logging_tree import printout
    >>> printout()
       ""
       Level WARNING
       |
       o<--"a"
       |   |
       |   o<--"a.b"
       |       Level DEBUG
       |
       o<--[x]
           |
           o<--"x.c"

%prep
%autosetup -n %{mod_name}-%{version}

%build
%py3_build

%install
%py3_install

# Need fixing upstream
#%check
#%{__python3} -v -m unittest discover %{mod_name}

%files -n python3-%{pypi_name}
%doc README.md
%license COPYRIGHT 
%{python3_sitelib}/%{mod_name}/
%{python3_sitelib}/%{mod_name}-%{version}-*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.8.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.8.1-1
- Update to new upstream version 1.8.1

* Mon Sep 09 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.8-1
- Add docs and license
- Update to latest upstream release 1.8
- Update spec file

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7-14
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.7-11
- Subpackage python2-logging-tree has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.7-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.7-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.7-6
- Python 2 binary package renamed to python2-logging-tree
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.7-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Apr 04 2016 Ralph Bean <rbean@redhat.com> - 1.7-1
- new version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 18 2015 Ralph Bean <rbean@redhat.com> - 1.6-1
- new version

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Jan 28 2014 Ralph Bean <rbean@redhat.com> - 1.4-1
- Latest upstream.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 03 2012 Ralph Bean <rbean@redhat.com> - 1.1-1
- Initial package for Fedora
