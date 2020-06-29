
# Deprecated RHEL/Fedora support dropped, no need to track package versioning there

%if 0%{?fedora} == 31
%global sqlite_version 3.29.0
%global uprel 1
%global pkg_version %{sqlite_version}-r%{uprel}
%endif

%if 0%{?fedora} >= 32
%global sqlite_version 3.32.2
%global uprel 1
%global pkg_version %{sqlite_version}-r%{uprel}
%endif

%if 0%{?rhel} >= 8
%global sqlite_version 3.26.0
%global uprel 1
%global pkg_version %{sqlite_version}-r%{uprel}
%endif

%global real_version %(eval echo %{pkg_version} | %{__sed} 's/-/./')

%filter_provides_in %{python3_sitearch}/.*\.so$
%filter_setup

Name:               python-apsw
Version:            %{real_version}
Release:            1%{?dist}
Summary:            Another Python SQLite Wrapper
License:            zlib
URL:                https://github.com/rogerbinns/apsw
Source:             https://github.com/rogerbinns/apsw/releases/download/%{pkg_version}/apsw-%{pkg_version}.zip

BuildRequires:      gcc
BuildRequires:      python%{python3_pkgversion}-devel
BuildRequires:      sqlite-devel >= %{sqlite_version}

Requires:           sqlite >= %{sqlite_version}

%description
APSW is a Python wrapper for the SQLite embedded relational database
engine. In contrast to other wrappers such as pysqlite it focuses on
being a minimal layer over SQLite attempting just to translate the
complete SQLite API into Python.

%package -n python%{python3_pkgversion}-apsw
Summary:            Another Python SQLite Wrapper
%{?python_provide:%python_provide python%{python3_pkgversion}-apsw}

%description -n python%{python3_pkgversion}-apsw
APSW is a Python %{python3_version} wrapper for the SQLite embedded relational database
engine. In contrast to other wrappers such as pysqlite it focuses on
being a minimal layer over SQLite attempting just to translate the
complete SQLite API into Python.

%prep
%autosetup -n apsw-%{pkg_version} -p1
rm -f doc/.buildinfo

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitearch} %{__python3} setup.py test

%files -n python%{python3_pkgversion}-apsw
%doc doc/*
%{python3_sitearch}/apsw*.so
%{python3_sitearch}/apsw*.egg-info


%changelog
* Fri Jun 12 2020 Denis Fateyev <denis@fateyev.com> - 3.32.2.r1-1
- Bump upstream version to 3.32.2
- Removed obsolete Python 3.9 patch

* Fri May 29 2020 Adam Williamson <awilliam@redhat.com> - 3.31.1.r1-3
- Backport upstream test improvement to fix build with Python 3.9

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.31.1.r1-2
- Rebuilt for Python 3.9

* Tue Mar 03 2020 Denis Fateyev <denis@fateyev.com> - 3.31.1.r1-1
- Bump upstream version to 3.31.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.29.0.r1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Denis Fateyev <denis@fateyev.com> - 3.30.1.r1-1
- Bump upstream version to 3.30.1
- Added patch for vtables test support
- Added EPEL8 python3.6 support

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.28.0.r1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.0.r1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.28.0.r1-2
- Work-around build issues with python3.8 (#1705460)

* Mon Jul 01 2019 Denis Fateyev <denis@fateyev.com> - 3.28.0.r1-1
- Bump upstream version to 3.28.0
- Removed deprecated Python 2 package

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0.r1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Denis Fateyev <denis@fateyev.com> - 3.24.0.r1-1
- Bump upstream version to 3.24.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0.r1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 3.22.0.r1-4
- Rebuilt for Python 3.7

* Wed Jun 20 2018 Denis Fateyev <denis@fateyev.com> - 3.23.1.r1-3
- Bump upstream version to 3.23.1

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.22.0.r1-4
- Rebuilt for Python 3.7

* Fri Mar 09 2018 Denis Fateyev <denis@fateyev.com> - 3.22.0.r1-3
- Bump upstream version to 3.22.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.1.r1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 09 2017 Denis Fateyev <denis@fateyev.com> - 3.20.1.r1-3
- Bump upstream version to 3.20.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.3.r1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.3.r1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 22 2017 Denis Fateyev <denis@fateyev.com> - 3.19.3.r1-3
- Bump upstream version to 3.19.3

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 3.18.0.r1-4
- Rebuild due to bug in RPM (RHBZ #1468476)

* Sat Apr 29 2017 Denis Fateyev <denis@fateyev.com> - 3.18.0.r1-3
- Bump upstream version to 3.18.0

* Tue Mar 07 2017 Denis Fateyev <denis@fateyev.com> - 3.17.0.r1-3
- Bump upstream version to 3.17.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.2.r1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 21 2017 Denis Fateyev <denis@fateyev.com> - 3.16.2.r1-3
- Bump upstream version to 3.16.2

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.14.1.r1-4
- Rebuild for Python 3.6

* Fri Sep 16 2016 Denis Fateyev <denis@fateyev.com> - 3.14.1.r1-3
- Bump upstream version to 3.14.1

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.0.r1-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Jun 19 2016 Denis Fateyev <denis@fateyev.com> - 3.13.0.r1-3
- Bump upstream version to 3.13.0

* Fri May 20 2016 Denis Fateyev <denis@fateyev.com> - 3.12.2.r1-3
- Bump upstream version to 3.12.2

* Fri Mar 04 2016 Denis Fateyev <denis@fateyev.com> - 3.11.0.r1-3
- Modernize the package spec, bump upstream version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.11.1.r1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - %{pkg_version}-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Sep 11 2015 Marcel Wysocki <maci@satgnu.net> - 3.8.11.1.r1-2
- Merge different versions into one spec file

* Mon Aug 24 2015 Marcel Wysocki <maci@satgnu.net> - 3.8.11.1.r1-1
- Update to 3.8.11.1-r1 for F24

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.4.3.r1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.4.3.r1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.4.3.r1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 3.8.4.3.r1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sat May 10 2014 Peter Robinson <pbrobinson@fedoraproject.org> 3.8.4.3.r1-1
- update to 3.8.4.3r1

* Tue Sep 24 2013 Marcel Wysocki <maci@satgnu.net> - 3.8.0.r2-1
- update to 3.8.0-r2

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.15.2.r1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Marcel Wysocki <maci@satgnu.net> - 3.7.15.2.r1-1
- update to 3.7.15.2-r1

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.11.r1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 19 2012 Marcel Wysocki <maci@satgnu.net> 3.7.11.r1-8
- initial python3 build

* Tue Oct 30 2012 Marcel Wysocki <maci@satgnu.net> 3.7.11.r1-7
- use python2-devel BR instead of python-devel

* Mon Oct 29 2012 Marcel Wysocki <maci@satgnu.net> 3.7.11.r1-6
- removed -doc package, not really needed

* Sun Oct 28 2012 Marcel Wysocki <maci@satgnu.net> 3.7.11.r1-5
- fixed changelog rpmlint error

* Sat Oct 27 2012 Marcel Wysocki <maci@satgnu.net> 3.7.11.r1-4
- use global instead of define macro
- filter private-shared-object-provides 
- removed python from requires

* Tue Oct 23 2012 Marcel Wysocki <maci@satgnu.net> 3.7.11.r1-3
- don't use rm macro
- remove doc/.buildinfo
- add missing dependencies

* Fri Oct 05 2012 Marcel Wysocki <maci@satgnu.net> 3.7.11.r1-2
- add missing builddep

* Thu Oct 04 2012 Marcel Wysocki <maci@satgnu.net> 3.7.11.r1-1
- fedora port
- update to 3.7.11-r1

* Wed Nov 30 2011 Dmitry Mikhirev <dmikhirev@mandriva.org> 3.7.7.1.r1-1
+ Revision: 735584
- imported package python-apsw

