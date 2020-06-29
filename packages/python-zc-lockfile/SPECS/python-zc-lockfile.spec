Name:           python-zc-lockfile
Version:        2.0
Release:        4%{?dist}
Summary:        Basic Inter-Process Locks
License:        ZPLv2.1
URL:            https://pypi.io/project/zc.lockfile/
Source0:        https://pypi.io/packages/source/z/zc.lockfile/zc.lockfile-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-zope-testing
BuildRequires:  python3-mock

%global _description\
The zc.lockfile package provides a basic portable implementation of\
interprocess locks using lock files. The purpose if not specifically\
to lock files, but to simply provide locks with an implementation based\
on file-locking primitives. Of course, these locks could be used to\
mediate access to other files. For example, the ZODB file storage\
implementation uses file locks to mediate access to file-storage\
database files. The database files and lock file files are separate files.

%description %_description

%package -n python3-zc-lockfile
Summary:        Basic Inter-Process Locks

%description -n python3-zc-lockfile
The zc.lockfile package provides a basic portable implementation of
interprocess locks using lock files. The purpose if not specifically
to lock files, but to simply provide locks with an implementation based
on file-locking primitives. Of course, these locks could be used to
mediate access to other files. For example, the ZODB file storage
implementation uses file locks to mediate access to file-storage
database files. The database files and lock file files are separate files.

%prep
%setup -q -n zc.lockfile-%{version}


%build
%py3_build


%install
%py3_install
rm -f %{buildroot}%{python3_sitelib}/zc/lockfile/*.txt

%check
%{__python3} setup.py test

%files -n python3-zc-lockfile
%doc src/zc/lockfile/*.txt
%{python3_sitelib}/zc.lockfile-*.egg-info
%{python3_sitelib}/zc.lockfile-*-nspkg.pth
%{python3_sitelib}/zc/lockfile/
%dir %{python3_sitelib}/zc/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 26 2019 Dan Radez <dradezredhat.com> - 2.0-1
- Update to 2.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 04 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-4
- Subpackage python2-zc-lockfile has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-2
- Rebuilt for Python 3.7

* Tue Apr 24 2018 Ralph Bean <rbean@redhat.com> - 1.3.0-1
- new version

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2.1-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.1-5
- Python 2 binary package renamed to python2-zc-lockfile
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-2
- Rebuild for Python 3.6

* Mon Aug 01 2016 Ralph Bean <rbean@redhat.com> - 1.2.1-1
- new version

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 10 2014 Ralph Bean <rbean@redhat.com> - 1.1.0-4
- Python3 subpackage.
- Modernize python macros.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 25 2013 Ralph Bean <rbean@redhat.com> - 1.1.0-1
- Latest upstream

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 30 2010 Robin Lee <robinlee.sysu@gmail.com> - 1.0.0-5
- Remove python-zope-filesystem from requirements
- Own %%{python_sitelib}/zc/

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Jun 17 2010 Robin Lee <robinlee.sysu@gmail.com> - 1.0.0-3
- Don't own %%{python_sitelib}/zc/, which is provided by python-zope-filesystem
- Add python-zope-filesystem as requirement
- Include more documents

* Sun Jul 5 2009 Conrad Meyer <konrad@tylerc.org> - 1.0.0-2
- Add missing BR on python-setuptools.
- Enable testing stuff as python-zope-testing is in devel.

* Mon Dec 15 2008 Conrad Meyer <konrad@tylerc.org> - 1.0.0-1
- Initial package.
