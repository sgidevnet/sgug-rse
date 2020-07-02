%global with_python2 0

%global oname  Unipath
Summary:       Alternative to Python modules os, os.path and shutil
Name:          python-unipath
Version:       1.1
Release:       11%{?dist}
License:       MIT
URL:           https://pypi.python.org/pypi/Unipath/
Source0:       https://files.pythonhosted.org/packages/source/U/%{oname}/%{oname}-%{version}.tar.gz
BuildArch:     noarch
%if 0%{?with_python2}
BuildRequires: python2-devel
BuildRequires: python2-setuptools
%endif
BuildRequires: python3-devel
BuildRequires: python3-setuptools
%global _description\
Unipath is a package for doing pathname calculations and filesystem\
access in an object-oriented manner, an alternative to functions in\
os.path, shutil and glob, and even some functions in os.* It's based\
on Jason Orendorffs path.py but does not adhere as strictly to the\
underlying functions' syntax, in order to provide more user\
convenience and higher-level functionality. For example:\
\
 o p.mkdir() succeeds silently if the directory already exists, and\
 o p.mkdir(True) creates intermediate directories a la os.makedirs.\
 o p.rmtree(parents=True) combines shutil.rmtree, os.path.isdir,\
   os.remove, and os.removedirs, to recursively remove whatever it is\
   if it exists.\
 o p.read_file("rb") returns the file's contents in binary mode.\
 o p.needs_update([other_path1, ...]) returns True if p doesn't exist\
   or has an older timestamp than any of the others.\
 o extra convenience functions in the unipath.tools module. dict2dir\
   creates a directory hierarchy described by a dict. dump_path displays\
   an ASCII tree of a directory hierarchy.

%description %_description

%if 0%{?with_python2}
%package -n python2-unipath
Summary:        %summary
%{?python_provide:%python_provide python2-unipath}
%description -n python2-unipath %_description
%endif

%package -n     python3-unipath
Summary:        %summary
%description -n python3-unipath %_description

%prep
%setup -q -n %{oname}-%{version}

%build
%if 0%{?with_python2}
%{py2_build}
%endif
%{py3_build}

%install
%if 0%{?with_python2}
%{py2_install}
%endif
%{py3_install}

%if 0%{?with_python2}
%files -n python2-unipath
%license CHANGES
%doc BUGS.txt PKG-INFO README.html README.rst
%{python2_sitelib}/unipath/
%{python2_sitelib}/%{oname}-%{version}-py*.egg-info
%endif

%files -n python3-unipath
%license CHANGES
%doc BUGS.txt PKG-INFO README.html README.rst
%{python3_sitelib}/unipath/
%{python3_sitelib}/%{oname}-%{version}-py*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1-11
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 18 2018 Terje Rosten <terje.rosten@ntnu.no> - 1.1-5
- Drop Python 2 subpackage in rawhide

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Terje Rosten <terje.rosten@ntnu.no> - 1.1-1
- 1.1
- Modernize spec

* Wed Jan 31 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0-12
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0-11
- Python 2 binary package renamed to python2-unipath
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0-8
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Wed Oct 23 2013 Terje Rosten <terje.rosten@ntnu.no> - 1.0-1
- 1.0
- Python 3 package

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 14 2009 Terje Rosten <terje.rosten@ntnu.no> - 0.2.1-2
- Minor changes taken from review

* Sun Mar 29 2009 Terje Rosten <terje.rosten@ntnu.no> - 0.2.1-1
- initial build
