%global modname cssselect

%bcond_without tests

Name:           python-cssselect
Version:        0.9.2
Release:        15%{?dist}
Summary:        Parses CSS3 Selectors and translates them to XPath 1.0

License:        BSD
URL:            https://github.com/scrapy/cssselect
Source0:        %{url}/archive/v%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
Cssselect parses CSS3 Selectors and translates them to XPath 1.0 expressions.\
Such expressions can be used in lxml or another XPath engine to find the\
matching elements in an XML or HTML document.

%description %{_description}

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with tests}
BuildRequires:  python3-lxml
%endif

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
%autosetup -n %{modname}-%{version}
mv %{modname}/tests.py .

%build
%py3_build

%install
%py3_install

%if %{with tests}
%check
%{__python3} tests.py -v
%endif

%files -n python3-%{modname}
%license LICENSE
%doc README.rst CHANGES AUTHORS
%{python3_sitelib}/%{modname}-*.egg-info/
%{python3_sitelib}/%{modname}/

%changelog
* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.2-15
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 09 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.2-13
- Subpackage python2-cssselect has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.2-12
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.2-8
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.9.2-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 20 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.2-3
- De-bootstrap for Python 3.6

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.2-2
- Rebuild for Python 3.6

* Sat Aug 27 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.9.2-1
- Update to 0.9.2
- Follow new packaging guidelines

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-10
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 06 2015 Robert Kuska <rkuska@redhat.com> - 0.9.1-8
- Enable tests

* Fri Nov 06 2015 Robert Kuska <rkuska@redhat.com> - 0.9.1-7
- Rebuilt for Python3.5 rebuild
- Disable tests as (circular dependency with python-lxml)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Aug 14 2014 Ralph Bean <rbean@redhat.com> - 0.9.1-5
- Modernize with_python3 conditional.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 15 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.9.1-3
- Enable tests again.

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4
- Bootstrap test running (circular dependency with python-lxml)

* Fri Jan 17 2014 Eduardo Echeverria <echevemaster@gmail.com> 0.9.1-1
- Update to latest upstream.
- although this package have py3 support, the resultant python3 package 
  doesn't existed, reason? On install section, py3 setup install must be first,
  if not, with every running of setup.py install, setup.py overwrite the files, 
  this behaviour has been fixed
- Workaround for python2 macro in epel versions
- use python2 macro instead of python

* Thu Jul 25 2013 Eric Smith <brouhaha@fedoraproject.org> 0.8-1
- Update to latest upstream.
- Added Python 3 support.
- Added EL6 support (uses Python 2.6 rather than 2.7).

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 09 2012 Kevin Fenzi <kevin@scrye.com> 0.7.1-3
- Add tests.

* Fri Nov 09 2012 Kevin Fenzi <kevin@scrye.com> 0.7.1-2
- Fixes from review. 

* Fri Nov 09 2012 Kevin Fenzi <kevin@scrye.com> 0.7.1-1
- Initial version for review


