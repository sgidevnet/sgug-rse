
%if 0%{?fedora}
%global with_python3 1
%else
%global with_python2 1
%endif

Name:           python-posix_ipc
Version:        0.9.8
Release:        24%{?dist}
Summary:        POSIX IPC primitives (semaphores and shared memory) for Python
License:        BSD
URL:            http://semanchuk.com/philip/posix_ipc/
Source0:        http://semanchuk.com/philip/posix_ipc/posix_ipc-%{version}.tar.gz

# See https://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot
BuildRequires:	gcc


%global _description\
posix_ipc is a Python module (written in C) that permits creation and\
manipulation of POSIX inter-process semaphores, shared memory and message\
queues on platforms supporting POSIX Realtime Extensions, POSIX 1003.1b-1993.\


%description %_description

%if 0%{?with_python2}
%package -n python2-posix_ipc
Summary: %summary
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%{?python_provide:%python_provide python2-posix_ipc}

%description -n python2-posix_ipc %_description
%endif  # with_python2

%if 0%{?with_python3}
%package -n python3-posix_ipc
Summary:        POSIX IPC primitives (semaphores and shared memory) for Python
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-posix_ipc %_description
%endif  # with_python3


%prep
%setup -q -n posix_ipc-%{version}
chmod 644 demo/make_all.sh
chmod 644 demo2/cleanup.py
chmod 644 demo/cleanup.py

%if 0%{?with_python3}
find . -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'
%endif # with_python3


%build
%if 0%{?with_python2}
%py2_build
%endif
%if 0%{?with_python3}
%py3_build
%endif


%install
%if 0%{?with_python2}
%py2_install
%endif
%if 0%{?with_python3}
%py3_install
%endif

%if 0%{?with_python2}
%files -n python2-posix_ipc
%doc README LICENSE demo demo2
%{python2_sitearch}/*
%endif

%if 0%{?with_python3}
%files -n python3-posix_ipc
%doc README LICENSE demo demo2
%{python3_sitearch}/*
%endif


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.8-24
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.8-22
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 05 2018 Viliam Krizan <vkrizan@redhat.com> - 0.9.8-19
- Removal of python2 subpackage as part of
  https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal
  (RHBZ #1627453)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.8-17
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.8-16
- Rebuilt for Python 3.7

* Wed Feb 14 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.9.8-15
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.9.8-13
- Python 2 binary package renamed to python2-posix_ipc
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.8-9
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Sep 10 2014 Nejc Saje <nsaje@redhat.com> - 0.9.8-4
- Introduce python3- subpackage

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 08 2014 Pádraig Brady <pbrady@redhat.com> - 0.9.8-1
- Latest upstream

* Tue Apr 08 2014 Jordan O'Mara <jomara@redhat.com> - 0.5.3-9
- Link with required threading libs

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 16 2009 Ramakrishna Reddy Yekulla <ramkrsna@fedoraproject.org> 0.5.3-1
- Initial RPM release

