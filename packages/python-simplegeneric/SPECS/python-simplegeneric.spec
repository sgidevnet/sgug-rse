%global pypi_name simplegeneric

Name:           python-simplegeneric
Version:        0.8.1
Release:        19%{?dist}
Summary:        Simple generic functions (similar to Python's own len(), pickle.dump(), etc.)

License:        Python or ZPLv2.1
URL:            https://pypi.org/project/simplegeneric/
Source0:        %{pypi_source %{pypi_name} %{version} zip}

BuildArch:      noarch


%description
The simplegeneric module lets you define simple single-dispatch generic
functions, akin to Python's built-in generic functions like len(), iter() and
so on. However, instead of using specially-named methods, these generic
functions use simple lookup tables, akin to those used by e.g. pickle.dump()
and other generic functions found in the Python standard library.


%package -n python3-%{pypi_name}
Summary:        Simple generic functions (similar to Python's own len(), pickle.dump(), etc.)
License:        Python or ZPLv2.1
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
The simplegeneric module lets you define simple single-dispatch generic
functions, akin to Python's built-in generic functions like len(), iter() and
so on. However, instead of using specially-named methods, these generic
functions use simple lookup tables, akin to those used by e.g. pickle.dump()
and other generic functions found in the Python standard library.



%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%build
%py3_build


%install
%py3_install


%check
PYTHONPATH=$(pwd) %{__python3} setup.py test


%files -n python3-%{pypi_name}
%doc README.txt
%{python3_sitelib}/__pycache__/simplegeneric.cpython*
%{python3_sitelib}/simplegeneric.py
%{python3_sitelib}/simplegeneric-%{version}-py?.?.egg-info/


%changelog
* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-19
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-17
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-16
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 14 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-14
- Subpackage python2-simplegeneric has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 30 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-12
- Modernize packaging

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-10
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.8.1-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Sep 29 2015 Thomas Spura <tomspur@fedoraproject.org> - 0.8.1-1
- update to 0.8.1 (no user visible changes, but packages require it on pypi)
- cleanup and use new py_build macros etc

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 0.8-5
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 27 2012 Thomas Spura <tomspur@fedoraproject.org> - 0.8-3
- be more explicit in files section
- add python3 subpackage (#785056)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 14 2011 Luke Macken <lmacken@redhat.com> - 0.8-1
- Update to 0.8 (#735066)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 30 2010 Luke Macken <lmacken@redhat.com> - 0.7-1
- Update to 0.7
- Run the unit tests

* Thu Jul 22 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild
- missing BR: python-devel

* Mon Apr 19 2010 Luke Macken <lmacken@redhat.com> - 0.6-2
- Change license from 'PSF or ZPL' to 'Python or ZPLv2.1'

* Tue Apr 13 2010 Luke Macken <lmacken@redhat.com> - 0.6-1
- Initial package
