%{?python_enable_dependency_generator}
%global srcname w3lib

Name:           python-%{srcname}
Version:        1.17.0
Release:        14%{?dist}
Summary:        Library of web-related functions

License:        BSD
URL:            https://github.com/scrapy/w3lib
Source0:        https://files.pythonhosted.org/packages/source/w/%{srcname}/%{srcname}-%{version}.tar.gz
# Usually pypi packages does not include license boilerplate.
# so, I've downloaded it from the project github repository
# wget -N https://raw.githubusercontent.com/scrapy/w3lib/master/LICENSE -O LICENSE-w3lib
Source1:        LICENSE-w3lib
BuildArch:      noarch


%description
This is a Python library of web-related functions, such as:
- Remove comments, or tags from HTML snippets
- Extract base url from HTML snippets
- Translate entites on HTML strings
- Encoding mulitpart/form-data
- Convert raw HTTP headers to dicts and vice-versa
- Construct HTTP auth header
- Converting HTML pages to unicode
- RFC-compliant url joining
- Sanitize urls (like browsers do)
- Extract arguments from urls


%package -n python3-%{srcname}
Summary:    %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
This is a Python3 library of web-related functions, such as:
- Remove comments, or tags from HTML snippets
- Extract base url from HTML snippets
- Translate entites on HTML strings
- Encoding mulitpart/form-data
- Convert raw HTTP headers to dicts and vice-versa
- Construct HTTP auth header
- Converting HTML pages to unicode
- RFC-compliant url joining
- Sanitize urls (like browsers do)
- Extract arguments from urls


%prep
%setup -qn %{srcname}-%{version}
# Remove bundled egg
rm -rf w3lib.egg-info
# copy LICENSE-w3lib file to sources as well.
cp -a %{SOURCE1} .


%build
%py3_build


%install
rm -rf %{buildroot}
%py3_install


%files -n python3-%{srcname}
%doc README.rst
%license LICENSE-w3lib
%{python3_sitelib}/w3lib/
%{python3_sitelib}/w3lib-*.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.17.0-14
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.17.0-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.17.0-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.17.0-8
- Enable python dependency generator

* Wed Jan 09 2019 Miro Hrončok <mhroncok@redhat.com> - 1.17.0-7
- Subpackage python2-w3lib has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.17.0-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.17.0-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 22 2017 Eduardo Echeverria <echevemaster@gmail.com> - 1.17.0-1
- Update tp the latest upstream version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.14.3-2
- Rebuild for Python 3.6

* Wed Jul 27 2016 Dominika Krejci <dkrejci@redhat.com> - 1.14.3-1
- Update to 1.14.3
- Add Python3

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Feb 15 2015 Eduardo Echeverria <echevemaster@gmail.com> - 1.11.0-1
- Updated to new upstream version 

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep 09 2013 Daniel Bruno <dbruno@fedoraproject.org> - 1.3-2
- Adjusting the spec for Fedora patterns

* Mon Sep 02 2013 Daniel Bruno <dbruno@fedoraproject.org> - 1.3-1 
- First version of RPM Package of w3lib
