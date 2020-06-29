%global modname prettytable


Name:		python-%{modname}
Version:	0.7.2
Release:	23%{?dist}
Summary:	Python library to display tabular data in tables

License:	BSD
Source0:    http://pypi.python.org/packages/source/P/PrettyTable/%{modname}-%{version}.tar.gz
URL:		http://pypi.python.org/pypi/PrettyTable

BuildArch:	noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools


%global _description\
PrettyTable is a simple Python library designed to make it quick and easy to\
represent tabular data in visually appealing ASCII tables. It was inspired by\
the ASCII tables used in the PostgreSQL shell psql. PrettyTable allows for\
selection of which columns are to be printed, independent alignment of columns\
(left or right justified or centred) and printing of "sub-tables" by specifying\
a row range.

%description %_description

%package -n python3-%{modname}
Summary:	Python library to display tabular data in tables
%{?python_provide:%python_provide python3-%{modname}}

%description -n python3-%{modname}
PrettyTable is a simple Python library designed to make it quick and easy to
represent tabular data in visually appealing ASCII tables. It was inspired by
the ASCII tables used in the PostgreSQL shell psql. PrettyTable allows for
selection of which columns are to be printed, independent alignment of columns
(left or right justified or centred) and printing of "sub-tables" by specifying
a row range.


%prep
%setup -q -n %{modname}-%{version}


%build
%py3_build

%check
%{__python3} %{modname}_test.py


%install
%py3_install


%files -n python3-%{modname}
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc README CHANGELOG
%{python3_sitelib}/%{modname}.py*
%{python3_sitelib}/__pycache__/%{modname}*
%{python3_sitelib}/%{modname}-%{version}*


%changelog
* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.2-23
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 17 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.2-21
- Subpackage python2-prettytable has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.2-20
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.2-19
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Miro Hrončok <mhroncok@redhat.com> - 0.7.2-15
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.7.2-14
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.7.2-12
- Python 2 binary package renamed to python2-prettytable
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 0.7.2-9
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jul 31 2014 Tom Callaway <spot@fedoraproject.org> - 0.7.2-4
- fix license handling

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Jan 07 2014 Pádraig Brady <pbrady@redhat.com> - 0.7.2-1
- Latest upstream

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug 07 2012 Ralph Bean <rbean@redhat.com> - 0.6.1-1
- New upstream version
- Added support for python3
- Included README, COPYING, and CHANGELOG in docs

* Tue Aug 07 2012 Pádraig Brady <P@draigBrady.com> - 0.6-1
- Update to 0.6

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 05 2011 Chris Lalancette <clalance@redhat.com> - 0.5-2
- BuildRequire python-setuptools

* Wed Jun 29 2011 Chris Lalancette <clalance@redhat.com> - 0.5-1
- Initial package.
