%global srcname ZODB3

Name:           python-%{srcname}
Version:        3.11.0
Release:        17%{?dist}
Summary:        Zope Object Database: Object Database and Persistence
License:        ZPLv2.1
URL:            http://www.zodb.org/
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(btrees)
BuildRequires:  python3dist(persistent)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(transaction)
BuildRequires:  python3dist(zeo)
BuildRequires:  python3dist(zodb)

%global common_desc %{expand:
The Zope Object Database provides an object-oriented database for Python
that provides a high-degree of transparency. Applications can take
advantage of object database features with few, if any, changes to
application logic. ZODB includes features such as a pluggable storage
interface, rich transaction support, and undo.}

%description
%{common_desc}

%package -n python3-%{srcname}
Summary:        Client-server storage implementation for ZODB
%{?python_provide:%python_provide python3-%{srcname}}

# This can be removed when F29 reached EOL
Obsoletes:      python2-%{srcname} < 3.11.0-12
Provides:       python2-%{srcname} = %{version}-%{release}

%description -n python3-%{srcname}
%{common_desc}

%prep
%autosetup -n %{srcname}-%{version}

# Fix encodings
for fil in HISTORY.txt; do
  iconv -f ISO-8859-1 -t UTF-8 $fil > $fil.utf8
  touch -r $fil $fil.utf8
  mv -f $fil.utf8 $fil
done

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%doc CHANGES.txt HISTORY.txt README.txt
%{python3_sitelib}/%{srcname}*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.11.0-17
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.11.0-15
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 17 2018 Jerry James <loganjerry@gmail.com> - 3.11.0-12
- Drop python2 subpackage

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.11.0-10
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.11.0-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Jerry James <loganjerry@gmail.com> - 3.11.0-5
- Rebuild for Python 3.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb  2 2016 Jerry James <loganjerry@gmail.com> - 3.11.0-3
- Comply with latest python packaging guidelines

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Oct 20 2014 Jerry James <loganjerry@gmail.com> - 3.11.0-1
- Update to 3.11.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jul 30 2013 Jerry James <loganjerry@gmail.com> - 3.10.5-5
- Adapt to versionless _docdir in Rawhide

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 10 2012 Jerry James <loganjerry@gmail.com> - 3.10.5-2
- Mass rebuild for Fedora 17
- Switch to the RPM 4.9 style of provides filtering

* Mon Nov 21 2011 Jerry James <loganjerry@gmail.com> - 3.10.5-1
- Update to 3.10.5

* Fri Nov 18 2011 Jerry James <loganjerry@gmail.com> - 3.10.4-1
- Update to 3.10.4

* Sun May  1 2011 Robin Lee <cheeselee@fedoraproject.org> - 3.10.3-2
- Enable the tests

* Wed Apr 27 2011 Jerry James <loganjerry@gmail.com> - 3.10.3-1
- Update to 3.10.3

* Sun Feb 20 2011 Robin Lee <cheeselee@fedoraproject.org> - 3.10.2-1
- Update to 3.10.2

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan  3 2011 Robin Lee <cheeselee@fedoraproject.org> - 3.10.1-1
- Update to 3.10.1

* Wed Oct 13 2010 Robin Lee <cheeselee@fedoraproject.org> - 3.10.0-1
- Update to 3.10.0 final

* Thu Sep 30 2010 Robin Lee <cheeselee@fedoraproject.org> - 3.10.0-0.6.b7
- Update to 3.10.0b7

* Wed Sep 29 2010 jkeating - 3.10.0-0.5.b6
- Rebuilt for gcc bug 634757

* Sat Sep 18 2010 Robin Lee <robinlee.sysu@gmail.com> - 3.10.0-0.4.b6
- Filter out private shared library provides
- Rearrage the documents
- Exclude the tests from installation

* Thu Sep  9 2010 Robin Lee <robinlee.sysu@gmail.com> - 3.10.0-0.3.b6
- Update to 3.10.0b6
- An unused line of comment removed
- A deeper path used in the find command

* Sat Sep  4 2010 Robin Lee <robinlee.sysu@gmail.com> - 3.10.0-0.2.b5
- Update to 3.10.0b5
- Use recommended commands to remove shebangs
- Requires python-setuptools, which is used by generated scripts

* Wed Sep  1 2010 Robin Lee <robinlee.sysu@gmail.com> - 3.10.0-0.1.b4
- Update to 3.10.0b4
- Spec cleaned up

* Tue Jun 22 2010 Robin Lee <robinlee.sysu@gmail.com> - 3.9.5-2
- Don't move the text files

* Wed Jun 16 2010 Robin Lee <robinlee.sysu@gmail.com> - 3.9.5-1
- Update to 3.9.5
- Take over the review request (#476600).
- Don't split out per-extension subpackages.
- BR: python-setuptools added
- Requires: python-zope-testing removed
- Make a -devel subpackage to contain all the header files
- Remove the C source files installed by setup.py
- Include more documents
- Don't move the executable scripts

* Wed Oct 28 2009 Conrad Meyer <konrad@tylerc.org> - 3.9.3-1
- Bumped to 3.9.3.
- Numerous minor fixes from review (#476600).
- Split into several subpackages.

* Mon Dec 15 2008 Conrad Meyer <konrad@tylerc.org> - 3.9.0-0.1.a7
- Initial package.
