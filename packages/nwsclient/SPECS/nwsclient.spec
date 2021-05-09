%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:		nwsclient
Summary: 	NetWorkSpaces Client for Python
Version:	1.6.4
Release:	22%{?dist}
License:	GPLv2+
Source0:	http://downloads.sourceforge.net/nws-py/%{name}-%{version}.tar.gz
URL:		http://nws-py.sourceforge.net/
BuildArch:	noarch
BuildRequires:	python2-devel, python2-setuptools

%description
NetWorkSpaces (NWS) is a powerful, open-source software package that makes it 
easy to use clusters from within scripting languages like Python, R, and 
Matlab. It uses a Space-based approach, similar to JavaSpaces (TM) for example,
that makes it easier to write distributed applications.

NetWorkSpaces for Python is the Python API to the NetWorkSpaces server. It 
allows different Python scripts to communicate and coordinate with each other, 
and (with some restrictions) with scripts written in other languages, such as
R and Matlab.  The restriction is that only strings can be passed between 
different languages. NetWorkSpaces doesn't provide a standard way to serialize 
objects between different languages, but by allowing strings to be used, 
programmers can choose their own mechanism (XML or YAML, for example).

%prep
%setup -q

%build
%{__python2} -c 'import setuptools; execfile("setup.py")' build

%install
NWS_MAN_DIR=%{_mandir}/man1 NWS_DOC_DIR=%{_pkgdocdir} %{__python2} -c 'import setuptools; execfile("setup.py")' install --skip-build --root %{buildroot}
cp -a PKG-INFO %{buildroot}%{_pkgdocdir}/

chmod -x %{buildroot}%{_pkgdocdir}/examples/*

%files
%doc %{_pkgdocdir}/
%{_bindir}/*
%{python2_sitelib}/nws/
%{python2_sitelib}/%{name}-%{version}-py*.egg-info
%{_mandir}/man1/*

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Tom Callaway <spot@fedoraproject.org> - 1.6.4-20
- fix FTBFS

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.6.4-17
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-14
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Tom Callaway <spot@fedoraproject.org> - 1.6.4-12
- spec file cleanups

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 30 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 1.6.4-10
- Replace python-setuptools-devel BR with pyhton-setuptools

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Nov 13 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.6.4-8
- Install docs to %%{_pkgdocdir} where available (#994010).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon Oct  5 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.6.4-1
- update to 1.6.4

* Thu Aug  6 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.6.3-5
- fix FTBFS

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.6.3-2
- fix source0 url
- exclude the byte compiled binaries
- use setuptools to ensure egg-info

* Fri Oct 17 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.6.3-1
- initial version for Fedora
