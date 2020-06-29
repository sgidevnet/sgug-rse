%global snapdate 20110209
%global module openoffice

Name:           python-%{module}
Version:        0.1
Release:        0.35.%{snapdate}%{?dist}
Summary:        Python libraries for interacting with LibreOffice
License:        GPLv3
URL:            https://gitorious.org/openoffice-python
Source0:        https://pypi.python.org/packages/source/o/openoffice-python/%{module}-python-%{version}-%{snapdate}.tar.bz2

BuildArch:      noarch
%if 0%{?rhel} >= 7
ExclusiveArch:  noarch x86_64
%endif
BuildRequires:  python3-devel
BuildRequires:  /usr/bin/2to3


%global _description\
The library is designed to supports both writing Macros (called by OOo) and\
interacting with OOo from an external Python program (using the UNO bridge).

%description %_description

%package -n python3-%{module}
Summary:        Python 3 libraries for interacting with LibreOffice

%description -n python3-%{module}
The library is designed to supports both writing Macros (called by OOo) and
interacting with OOo from an external Python program (using the UNO bridge).


%prep
%setup -q -n %{module}-python-%{version}-%{snapdate}

# remove exec perms for docs
chmod a-x sample-scripts/*

# remove the shebang line
sed -i -e '1d' %{module}/streams.py
sed -i -e '1d' %{module}/interact.py

%build
2to3 -w -n .
%py3_build

%install
%py3_install

%files -n python3-%{module}
%license COPYING LICENSE-gpl-3.0.txt
%doc README sample-scripts
%{python3_sitelib}/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1-0.35.20110209
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.34.20110209
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1-0.33.20110209
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1-0.32.20110209
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.31.20110209
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.30.20110209
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.1-0.29.20110209
- Subpackage python2-openoffice has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Tue Jul 17 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1-0.28.20110209
- Update Python macros to new packaging standards
  (See https://fedoraproject.org/wiki/Changes/Move_usr_bin_python_into_separate_package)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.27.20110209
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1-0.26.20110209
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.1-0.25.20110209
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.24.20110209
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.1-0.23.20110209
- Python 2 binary package renamed to python2-openoffice
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.22.20110209
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.21.20110209
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1-0.20.20110209
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.19.20110209
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.18.20110209
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.17.20110209
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.16.20110209
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.15.20110209
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.1-0.14.20110209
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Thu Mar 20 2014 Dan Horák <dan[at]danny.cz> - 0.1-0.13.20110209
- updated to newer snapshot
- add python3 variant

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.12.20090228svn34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.11.20090228svn34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.10.20090228svn34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.9.20090228svn34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.8.20090228svn34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Oct 30 2010 Caolán McNamara <caolanm@redhat.com> - 0.1-0.5.20090228svn34
- Rebuild for LibreOffice

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.1-0.6.20090228svn34
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Aug 26 2009 Dan Horák <dan[at]danny.cz> 0.1-0.5.20090228svn34
- fixed Source0 URL

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.4.20090228svn34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar  6 2009 Dan Horák <dan[at]danny.cz> 0.1-0.3.20090228svn34
- check %%rhel for the ExcludeArch tag
- update to new upstream snapshot

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.2.20080929svn33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 10 2008 Dan Horák <dan[at]danny.cz> 0.1-0.1.20080929svn33.1
- there is no openoffice.org in RHEL 5 on ppc

* Tue Dec  2 2008 Dan Horák <dan[at]danny.cz> 0.1-0.1.20080929svn33
- initial Fedora version
