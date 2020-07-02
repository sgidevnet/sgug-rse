%global srcname django-debug-toolbar

Name:           python-%{srcname}
Version:        2.0
Release:        3%{?dist}
Summary:        Configurable set of panels that display various debug information

License:        BSD
URL:            https://github.com/jazzband/django-debug-toolbar
Source:         %{pypi_source}

BuildArch:      noarch

%global _description\
The Django Debug Toolbar is a configurable set of panels that display various\
debug information about the current request/response and when clicked, display\
more details about the panel's content.\
\
Currently, the following panels have been written and are working:\
\
 -   Django version\
 -   Request timer\
 -   A list of settings in settings.py\
 -   Common HTTP headers\
 -   GET/POST/cookie/session variable display\
 -   Templates and context used, and their template paths\
 -   SQL queries including time to execute and links to EXPLAIN each query\
 -   List of signals, their args and receivers\
 -   Logging output via Python's built-in logging, or via the logbook module

%description %_description

%package -n python3-%{srcname}
Summary:       %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
Obsoletes:     python-django-debug-toolbar < 1.9.1-3
Obsoletes:     python2-django-debug-toolbar < 1.9.1-3

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}
rm -vr *.egg-info/

%build
%py3_build

%install
%py3_install

%check
# test needs config
# %{__python3} setup.py test

%files -n python3-%{srcname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/debug_toolbar/
%{python3_sitelib}/django_debug_toolbar-*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 31 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0-1
- Update to 2.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.1-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.9.1-4
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Miro Hrončok <mhroncok@redhat.com> - 1.9.1-3
- Removed Python 2 subpackage for https://fedoraproject.org/wiki/Changes/Django20

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Matthias Runge <mrunge@redhat.com> - 1.9.1-1
- update to 1.9.1

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.4-8
- Python 2 binary package renamed to python2-django-debug-toolbar
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.4-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat May 21 2016 Matthias Runge <mrunge@redhat.com> - 1.4-3
- modernize specfile
- enable python3 (rhbz#1311523)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 10 2015 Matthias Runge <mrunge@redhat.com> - 1.4-1
- update to 1.4 and add requirement to python-sqlparse (rhbz#1287269)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 13 2015 Matthias Runge <mrunge@redhat.com> - 1.3.0-1
- update to 1.3.0
- modernize spec, add python3 support

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 07 2014 Matthias Runge <mrunge@redhat.com> - 1.0.1-1
- update to 1.0.1 (rhbz#1049249)

* Thu Jan 02 2014 Matthias Runge <mrunge@redhat.com> - 1.0-1
- update to version 1.0 (rhbz#1023925)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug 06 2012 Matthias Runge <mrunge@matthias-runge.de> - 0.9.4-1
- update to upstream version 0.9.4

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 23 2012 Matthias Runge <mrunge@matthias-runge.de> 0.9.3-2
- change requirement from Django to python-django

* Mon Jan 23 2012 Matthias Runge <mrunge@matthias-runge.de> 0.9.3-1
- initial packaging
