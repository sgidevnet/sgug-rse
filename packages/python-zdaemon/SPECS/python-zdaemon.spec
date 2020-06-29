Name:           python-zdaemon
Version:        4.2.0
Release:        14%{?dist}
Summary:        Python Daemon Process Control Library
License:        ZPLv2.1
URL:            https://pypi.io/project/zdaemon/
Source0:        https://pypi.io/packages/source/z/zdaemon/zdaemon-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-zope-testing
BuildRequires:  python3-ZConfig
BuildRequires:  python3-manuel
BuildRequires:  python3-six
BuildRequires:  python3-zc-customdoctests
BuildRequires:  python3-mock

%global _description\
Daemon process control library and tools for Unix-bases systems.

%description %_description

%package -n python3-zdaemon
Summary:        Python Daemon Process Control Library
%{?python_provide:%python_provide python3-zdaemon}

%description -n python3-zdaemon
Daemon process control library and tools for Unix-bases systems.


%prep
%setup -q -n zdaemon-%{version}
sed -i '1,1d' src/zdaemon/zdctl.py
sed -i '1,1d' src/zdaemon/zdrun.py
sed -i '1,1d' src/zdaemon/tests/nokill.py


%build
%py3_build


%install
%py3_install


%check
export PYTHONPATH="$PYTHONPATH:%{buildroot}%{python3_sitelib}"
%{__python3} build/lib/zdaemon/tests/tests.py


%files -n python3-zdaemon
%doc CHANGES.rst README.rst
%{python3_sitelib}/zdaemon
%{python3_sitelib}/zdaemon-%{version}-py?.?.egg-info
%{_bindir}/zdaemon


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.2.0-14
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.2.0-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.2.0-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.2.0-9
- Drop Python 2 subpackage

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.2.0-6
- Rebuilt for Python 3.7

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.2.0-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.2.0-3
- Python 2 binary package renamed to python2-zdaemon
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 11 2017 Ralph Bean <rbean@redhat.com> - 4.2.0-1
- new version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4.1.0-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 15 2015 Ralph Bean <rbean@redhat.com> - 4.1.0-1
- new version

* Wed Feb 18 2015 Ralph Bean <rbean@redhat.com> - 4.0.1-1
- new version

* Wed Feb 18 2015 Ralph Bean <rbean@redhat.com> - 4.0.1-1
- new version

* Tue Jun 10 2014 Ralph Bean <rbean@redhat.com> - 4.0.0-3
- python3 subpackage added
- modernized python2 macros

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jan 29 2014 Ralph Bean <rbean@redhat.com> - 4.0.0-1
- Latest upstream.

* Wed Jan 29 2014 Ralph Bean <rbean@redhat.com> - 3.0.5-3
- Enable tests.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 25 2013 Ralph Bean <rbean@redhat.com> - 3.0.5-1
- Latest upstream
- Disabled tests while waiting for python-zc-customdoctests

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Oct 16 2009 Conrad Meyer <konrad@tylerc.org> - 2.0.4-2
- Add BR on python-setuptools.

* Wed Apr 22 2009 Conrad Meyer <konrad@tylerc.org> - 2.0.4-1
- Bump to 2.0.4.

* Mon Dec 15 2008 Conrad Meyer <konrad@tylerc.org> - 2.0.2-1
- Initial package.
