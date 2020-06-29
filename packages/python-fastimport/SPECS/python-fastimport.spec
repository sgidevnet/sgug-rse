
%global module_name fastimport

Name:           python-%{module_name}
Version:        0.9.8
Release:        10%{?dist}
Summary:        Python parser for fastimport (VCS interchange format)
License:        GPLv2+
URL:            https://launchpad.net/python-fastimport
Source0:        https://files.pythonhosted.org/packages/source/f/%{module_name}/%{module_name}-%{version}.tar.gz
BuildArch:      noarch

%description
This is the Python parser that was originally developed for bzr-fastimport, but 
extracted so it can be used by other projects.

%package -n python3-%{module_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{module_name}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-testtools
BuildRequires:  python3-nose

%description -n python3-%{module_name}
This is the Python parser that was originally developed for bzr-fastimport, but 
extracted so it can be used by other projects.

%prep
%setup -q -n %{module_name}-%{version}
# Fix shebangs
sed -i -e 's@^#!/usr/bin/python@#!%{__python3}@' bin/*

%build
%{py3_build}

%install
%{py3_install}

%check
PYTHONPATH=$RPM_BUILD_ROOT%{python3_sitelib} %{_bindir}/nosetests-3.* %{module_name}

%files -n python3-%{module_name}
%license COPYING
%doc AUTHORS NEWS README.md
%{python3_sitelib}/%{module_name}*
%{_bindir}/fast-import-filter
%{_bindir}/fast-import-info
%{_bindir}/fast-import-query

%changelog
* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.8-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.8-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.8-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.9.8-4
- Subpackage python2-fastimport has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.8-2
- Rebuilt for Python 3.7

* Mon Apr 30 2018 Dan Callaghan <dcallagh@redhat.com> - 0.9.8-1
- upstream release 0.9.8:
  https://github.com/jelmer/python-fastimport/blob/upstream/0.9.8/NEWS

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 29 2016 Thomas Spura <tomspur@fedoraproject.org> - 0.9.6-4
- Fix calling of nosetests in %%check for Python 3.X

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.6-3
- Rebuild for Python 3.6

* Mon Aug 01 2016 Dan Callaghan <dcallagh@redhat.com> - 0.9.6-2
- added Python 3 subpackage, updated to latest Python guidelines

* Mon Aug 01 2016 Dan Callaghan <dcallagh@redhat.com> - 0.9.6-1
- upstream release 0.9.6 (RHBZ#1361922)
  https://github.com/jelmer/python-fastimport/blob/fastimport-0.9.6/NEWS

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Dec 06 2013 Dan Callaghan <dcallagh@redhat.com> - 0.9.2-4
- s/python-setuptools-devel/python-setuptools/
  https://fedoraproject.org/wiki/Changes/Remove_Python-setuptools-devel

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Dan Callaghan <dcallagh@redhat.com> - 0.9.2-1
- upstream bug fix release 0.9.2

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 29 2012 Dan Callaghan <dcallagh@redhat.com> - 0.9.1-1
- upstream release 0.9.1

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 06 2011 Dan Callaghan <dcallagh@redhat.com> - 0.9.0-2
- cleaned up spec
- patch for outdated FSF address

* Thu Jun 16 2011 Dan Callaghan <dcallagh@redhat.com> - 0.9.0-1
- initial version
