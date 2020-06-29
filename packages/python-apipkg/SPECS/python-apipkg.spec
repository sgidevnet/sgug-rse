%global srcname apipkg

Name:           python-%{srcname}
Version:        1.5
Release:        10%{?dist}
Summary:        A Python namespace control and lazy-import mechanism

License:        MIT
URL:            https://github.com/pytest-dev/apipkg
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%description
With apipkg you can control the exported namespace of a python package and
greatly reduce the number of imports for your users. It is a small python
module that works on virtually all Python versions, including CPython2.3 to
Python3.1, Jython and PyPy. It co-operates well with Python's help() system,
custom importers (PEP302) and common command line completion tools.

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
With apipkg you can control the exported namespace of a python package and
greatly reduce the number of imports for your users. It is a small python
module that works on virtually all Python versions, including CPython2.3 to
Python3.1, Jython and PyPy. It co-operates well with Python's help() system,
custom importers (PEP302) and common command line completion tools.

%prep
%autosetup -n %{srcname}-%{version}

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%py3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%py3_install

%files -n python3-%{srcname}
%doc CHANGELOG README.rst
%license LICENSE
%{python3_sitelib}/%{srcname}*.egg-info
%{python3_sitelib}/%{srcname}/

%changelog
* Wed Jun 24 2020 Thomas Moschny <thomas.moschny@gmx.de> - 1.5-10
- Add explicit BR on python3-setuptools.

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5-9
- Rebuilt for Python 3.9

* Fri Feb 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.5-8
- Update URLs

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5-5
- Rebuilt for Python 3.8

* Mon Aug 12 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5-4
- Subpackage python2-apipkg has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 09 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.5-2
- Switch to upstream source
- Add license file

* Tue Feb 05 2019 Ken Dreyer <kdreyer@redhat.com> - 1.5-1
- Update to new upstream version 1.5 (rhbz#1672801)
- Update package URL and Source0
- Use setuptools_scm
- Handle README file rename

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4-10
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.4-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 14 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1.4-3
- Cleanup

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sat Oct 17 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1.4-1
- Update to new upstream version 1.4 (rhbz#1239818)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 10 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1.3-1
- Update to new upstream version 1.3 (rhbz#1199807)

* Wed Feb 18 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1.2-7
- Enable py3 package

* Fri Oct 03 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.2-6
- Update to match guidelines

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 10 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.2-1
- Update to match new guidelines
- Python3
- Update to new upstream version 1.2

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Nov 08 2010 Fabian Affolter <mail@fabian-affolter.ch> - 1.0-1
- Initial package
