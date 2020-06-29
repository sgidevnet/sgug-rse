
Name:           python-xmltramp
Version:        2.18
Release:        9%{?dist}
Summary:        Pythonic API for XML

License:        GPLv2
# License text is not present in the upstream file, though clearly marked as GPLv2
# See https://www.redhat.com/archives/fedora-legal-list/2008-January/msg00010.html

URL:            http://www.aaronsw.com/2002/xmltramp/
Source0:        http://www.aaronsw.com/2002/xmltramp/xmltramp-%{version}.py
Patch1:         0001-Patch-for-RHBZ-750694.patch
Patch2:         0002-fix-imports-and-syntax-for-Python-3.patch
Patch3:         0003-__str__-needs-to-return-str-not-bytes-on-Python-3.patch
Patch4:         0004-empty-slice-is-slice-None-None-None-on-Python-3.patch
Patch5:         0005-use-OrderedDict-for-attributes-and-namespaces.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description\
xmltramp is a simple Pythonic API for working with XML.

%description %_description

%package -n python3-xmltramp
Summary: %summary
%{?python_provide:%python_provide python3-xmltramp}

%description -n python3-xmltramp %_description

%prep
%setup -c -T
cp -p %{SOURCE0} xmltramp.py
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
# noarch

%install
install -Dm0644 -t %{buildroot}%{python3_sitelib}/ xmltramp.py

%check
%{__python3} xmltramp.py

%files -n python3-xmltramp
%{python3_sitelib}/xmltramp.py*
%{python3_sitelib}/__pycache__/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.18-9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.18-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.18-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.18-3
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 05 2018 Dan Callaghan <dcallagh@redhat.com> - 2.18-1
- Updated to upstream release 2.18 (only ~10 years late...)
- Minimal fixes to support Python 3

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.17-20
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.17-19
- Python 2 binary package renamed to python2-xmltramp
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.17-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.17-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.17-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 07 2013 Dan Callaghan <dcallagh@redhat.com> - 2.17-12
- Patch for RHBZ#750694

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.17-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.17-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.17-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.17-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 2.17-7
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.17-4
- Rebuild for Python 2.6

* Fri Jan 18 2008 David Malcolm <dmalcolm@redhat.com> - 2.17-3
- add comment in specfile about the License text

* Tue Nov 13 2007 David Malcolm <dmalcolm@redhat.com> - 2.17-2
- fix License tag
- fix capitalization of Summary tag
- preserve timestamp when installing

* Fri Aug  3 2007 David Malcolm <dmalcolm@redhat.com> - 2.17-1
- initial packaging

