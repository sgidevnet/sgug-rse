Summary:       Grep-like tool for source code
Name:          grin
Version:       1.2.1
Release:       21%{?dist}
License:       BSD
URL:           http://pypi.python.org/pypi/grin
Source0:       https://files.pythonhosted.org/packages/source/g/grin/grin-%{version}.tar.gz
Patch1:        grin-1.2.1-git-8dd4b5.patch
Patch2:        grin-1.2.1-python3.patch
Requires:      python3-setuptools
BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-nose

%description
grin is a similar in function to GNU grep, however it is has modified
behaviour to make it simpler to use when grepping source code.

Some features grin feature are:

  * recurse directories by default
  * do not go into directories with specified names
  * do not search files with specified extensions
  * be able to show context lines before and after matched lines
  * Python regex syntax
  * unless suppressed via a command line option, display the filename 
    regardless of the number of files
  * accept a file (or stdin) with a list of newline-separated filenames
  * grep through gzipped text files
  * be useful as a library to build custom tools quickly

%prep
%setup -q
%patch1 -p1
%patch2 -p1
chmod 0644 examples/*
sed -i -e '1d' grin.py

%build
%{py3_build}

%install
%{py3_install}

%check
nosetests

%files
%license LICENSE.txt
%doc ANNOUNCE.txt examples LICENSE.txt README.rst THANKS.txt
%{_bindir}/grin
%{_bindir}/grind
%{python3_sitelib}/grin.py*
%{python3_sitelib}/grin-*-py*.egg-info/
%{python3_sitelib}/__pycache__/grin.*

%changelog
* Mon Aug 05 2019 Terje Rosten <terje.rosten@ntnu.no> - 1.2.1-21
- Convert to Python 3

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2.1-17
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Oct 01 2016 Terje Rosten <terje.rosten@ntnu.no> - 1.2.1-13
- Some clean up

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-12
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 30 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 1.2.1-9
- Replace python-setuptools-devel BR with python-setuptools

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon May 09 2011 Terje Rosten <terje.rosten@ntnu.no> - 1.2.1-2
- Add patch to work with Python 2.7 and later
- Add argparse req. if needed

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 30 2011 Terje Rosten <terje.rosten@ntnu.no> - 1.2.1-1
- 1.2.1

* Sun Dec 26 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.1.1-5
- Update python_sitelib macro
- Don't requires python-argparse (#665727)

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Feb 21 2009 Terje Rosten <terje.rosten@ntnu.no> - 1.1.1-2
- add docs
- rpmlint clean
- add %%check section

* Sat Jan 17 2009 Terje Rosten <terje.rosten@ntnu.no> - 1.1.1-1
- initial build


