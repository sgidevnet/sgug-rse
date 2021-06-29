Name:		glue-schema
Version:	2.0.11
Release:	9%{?dist}
Summary:	LDAP schema files for the GLUE 1.3 and GLUE 2.0 Schema
License:	ASL 2.0
URL:		http://forge.ogf.org/sf/projects/glue-wg
#		The source tarball is created from a svn checkout:
#		svn export http://svn.cern.ch/guest/gridinfo/glue-schema/tags/R_2_0_11 glue-schema-2.0.11
#		tar -z -c -f glue-schema-2.0.11.tar.gz glue-schema-2.0.11
Source:		%{name}-%{version}.tar.gz
Source1:	http://www.ogf.org/documents/GFD.147.pdf
BuildArch:	noarch

%description
The GLUE specification is an information model for Grid entities such
as computing clusters and data storage facilities. As a conceptual
model, it is designed to be independent from the concrete data models
adopted for its implementation. The specification can be rendered to
several concrete data models such as XML Schema, LDAP Schema or SQL.

This package provides LDAP schema files for the GLUE 1.3 and GLUE 2.0 Schema.

%package doc
Summary:	The GLUE Schema version 2.0 specification

%description doc
The GLUE Schema version 2.0 specification (GFD.147)

%prep
%setup -q

%build 
# Nothing to build

install -m 644 -p %{SOURCE1} .

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_sysconfdir}/ldap/schema
install -m 644 -p etc/ldap/schema/* %{buildroot}/%{_sysconfdir}/ldap/schema

%files
%config(noreplace) %{_sysconfdir}/ldap
%doc debian/copyright

%files doc
%doc GFD.147.pdf

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Oct 13 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.11-1
- Update to release 2.0.11

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 14 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.10-1
- Update to release 2.0.10

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Sep 04 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.8-1
- Update to release 2.0.8

* Tue Aug 30 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.7-1
- Update to release 2.0.7

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jun 18 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.6-1
- Update to release 2.0.6
- Change license tag to ASL 2.0 to reflect upstream license change

* Thu Apr 08 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.4-2
- Add missing Group tag in doc subpackage

* Sun Apr 04 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.4-1
- Update to release 2.0.4
- Create doc subpackage containing the GLUE schema specification

* Thu Mar 25 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.3-3.448
- Use proper anonymous svn checkout instead of svnweb generated tarball

* Fri Feb 26 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.3-2.448
- Update (svn revision 448)

* Fri Feb 12 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.3-1
- Updated packaging

* Fri Jul 10 2009 Laurence Field <laurence.field@cern.ch> -  2.0.1-1
- First release
