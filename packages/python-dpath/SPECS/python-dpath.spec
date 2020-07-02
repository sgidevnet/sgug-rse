Name:           python-dpath
Version:        1.4.0
Release:        18%{?dist}
Summary:        A library for searching dictionaries using XPath-like expressions
License:        MIT
URL:            https://github.com/akesterson/dpath-python
BuildArch:      noarch

Source0:        https://pypi.python.org/packages/source/d/dpath/dpath-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools


%global _description\
A python library for accessing and searching dictionaries via /slashed/paths ala\
xpath\
\
Basically it lets you glob over a dictionary as if it were a filesystem. It\
allows you to specify globs (ala the bash eglob syntax, through some advanced\
fnmatch.fnmatch magic) to access dictionary elements, and provides some facility\
for filtering those results.

%description %_description

%package -n python3-dpath
Summary:        A python3 library for searching dictionaries using XPath-like expressions
%{?python_provide:%python_provide python3-dpath}

%description -n python3-dpath
A python library for accessing and searching dictionaries via /slashed/paths ala
xpath

Basically it lets you glob over a dictionary as if it were a filesystem. It
allows you to specify globs (ala the bash eglob syntax, through some advanced
fnmatch.fnmatch magic) to access dictionary elements, and provides some facility
for filtering those results.


%prep
%setup -q -n dpath-%{version}

find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'

%build
%py3_build

%install
%py3_install

%files -n python3-dpath
%doc LICENSE.txt README.rst
%{python3_sitelib}/dpath*


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-18
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 05 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-16
- Subpackage python2-dpath has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-15
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-11
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.4.0-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.4.0-8
- Python 2 binary package renamed to python2-dpath
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Oct 21 2015 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4.0-1
- Update to new upstream version

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.5.70
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.4.70
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.2-0.3.70
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Apr 07 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.2-0.2.70
- Update to new upstream version

* Wed Mar 19 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.2-0.1.52.20140319gita6ce774d
- Initial packaging

