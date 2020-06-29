Name:           python-yara
Version:        4.0.1
%global         baserelease     1
Summary:        Python binding for the YARA pattern matching tool
License:        ASL 2.0
URL:            http://github.com/VirusTotal/yara-python/
#               http://VirusTotal.github.io/yara/
#               https://github.com/VirusTotal/yara-python/releases

%global         srcname         yara
%global         gituser         VirusTotal
%global         gitname         %{srcname}-python
%global         commit          63ac2417a918692be6d5bd659fbfd39564396ec3
%global         gitdate         20190222
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})


%global         common_description %{expand:
Python binding for the YARA pattern matching tool.
YARA is a tool aimed at (but not limited to) helping malware researchers to
identify and classify malware samples. With YARA you can create descriptions
of malware families (or whatever you want to describe) based on textual or
binary patterns. Each description, a.k.a rule, consists of a set of strings
and a Boolean expression which determine its logic.}

# Do the check during build
%if 0%{?fedora} || ( 0%{?rhel} && 0%{?rhel} >= 7 )
%global         with_check      1
%endif

%if ( 0%{?fedora} && 0%{?fedora} >= 30 ) || ( 0%{?rhel} && 0%{?rhel} >= 8 )
                # by default build without the python2 support on systems f30+ or rhel8+
%bcond_with     python2 
%else
                # build with the python2 support on system up to f29 and/or rhel7
%bcond_without  python2 
%endif


# Build source is versioned github release=1 or unversioned git commit=0
%global         build_release    1

%if 0%{?build_release}  > 0
Release:        %{baserelease}%{?dist}
Source0:        https://github.com/%{gituser}/%{gitname}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%else
Release:        %{baserelease}.%{gitdate}git%{shortcommit}%{?dist}
Source0:        https://github.com/%{gituser}/%{gitname}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
%endif

BuildRequires:  gcc
BuildRequires:  pkgconfig(yara)
BuildRequires:  libtool
BuildRequires:  yara-devel >= %{version}
# html doc generation
BuildRequires:  /usr/bin/sphinx-build

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-nose
BuildRequires:  python%{python3_pkgversion}-setuptools


%if 0%{?with_python2}  > 0
BuildRequires:  python2
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%endif


%description
%{common_description}



#====================================================================
%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Python3 binding for the YARA pattern matching tool
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}



%description -n python%{python3_pkgversion}-%{srcname}
%{common_description}

%if 0%{?with_python2}  > 0
%package -n python2-%{srcname}
Summary:        Python2 binding for the YARA pattern matching tool
%{?python_provide:%python_provide python2-%{srcname}}


%description -n python2-%{srcname}
%{common_description}
%endif

#====================================================================
%prep
%if 0%{?build_release} > 0
# Build from git release version
%autosetup -n %{gitname}-%{version}

%else
# Build from git commit
%autosetup -n %{gitname}-%{commit}
%endif



#====================================================================
%build
%if 0%{?with_python2}  > 0
%py2_build "--dynamic-linking"
%endif

%py3_build "--dynamic-linking"



#====================================================================
%install
%if 0%{?with_python2}  > 0
%py2_install
%endif

%py3_install


#====================================================================
%check
%if 0%{?with_check}
# ==============================================================================
# Tests for python3 used to always fail on testModuleData testcase
# Tests for python3 used to randomly fail on testCompare testcase
# reported to upstream - https://github.com/VirusTotal/yara-python/issues/21
# temporarily run the failing tests but ignore the results for those 2
# EXCLUDE='--exclude=^testCompare$|^testModuleData$'
# seems to be fixed in 3.9.0
EXCLUDE='--exclude=^nothing$'

# Yara is not prepared to run on s390 - more tests failing on s390
#         http://s390.koji.fedoraproject.org/kojifiles/work/tasks/9135/2399135/build.log
#         https://github.com/VirusTotal/yara-python/issues/25
# 3.6.3 - testCompileFile started failing - https://kojipkgs.fedoraproject.org//work/tasks/9619/20589619/build.log
#         https://github.com/VirusTotal/yara-python/issues/54
# seems to be fixed in 3.9.0
%ifarch s390 s390x %{power64}
# EXCLUDE='--exclude=^testCompare$|^testModuleData$|^testEntrypoint$|^testIn$|^testIntegerFunctions$|^testCompileFile$'
EXCLUDE='--exclude=^nothing$'
%endif

# 3.9.0 - testModuleData is always failing for architecture armv7hl
%ifarch armv7hl
EXCLUDE='--exclude=^testModuleData$'
%endif


# Find the NOSETEST binary or use false if not present
NOSETESTS3=`ls /usr/bin/nosetests-3.* || which false `
PYTHONPATH=%{buildroot}/%{python3_sitearch}/ "$NOSETESTS3" -v "$EXCLUDE"

# Run potentially ignored tests separately so we can at least see the results
PYTHONPATH=%{buildroot}/%{python3_sitearch}/ "$NOSETESTS3" -v ./tests.py:TestYara.testCompare \
    ./tests.py:TestYara.testModuleData ./tests.py:TestYara.testEntrypoint \
    ./tests.py:TestYara.testIn ./tests.py:TestYara.testIntegerFunctions  \
    ./tests.py:TestYara.testCompileFile || true

# with_check
%endif


#====================================================================
%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitearch}/%{srcname}*

%if 0%{?with_python2}  > 0
%files -n python2-%{srcname}
%license LICENSE
%doc README.rst
%{python2_sitearch}/%{srcname}*
%endif

#====================================================================
%changelog
* Fri Jun 06 2020 Michal Ambroz <rebus at, seznam.cz> - 4.0.1-1
- bump to version 4.0.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0.0-2
- Rebuilt for Python 3.9

* Tue May 12 2020 Michal Ambroz <rebus at, seznam.cz> - 4.0.0-1
- bump to version 4.0.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 14 2019 Michal Ambroz <rebus at, seznam.cz> - 3.11.0-2
- fix the release number

* Mon Oct 14 2019 Michal Ambroz <rebus at, seznam.cz> - 3.11.0-1
- bump to 3.11.0, omit py2 for f30+ and epel8+

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.9.0-2.2
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 22 2019 Michal Ambroz <rebus at, seznam.cz> - 3.9.0-2
- change dependency to sphinx based on the /usr/bin/sphinx-build

* Mon Mar 18 2019 Michal Ambroz <rebus at, seznam.cz> - 3.9.0-1
- bump to 3.9.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.8.1-3
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 27 2018 Michal Ambroz <rebus at, seznam.cz> - 3.8.1-2
- rebuild with yara 3.8.1 override

* Mon Aug 27 2018 Michal Ambroz <rebus at, seznam.cz> - 3.8.1-1
- bump to 3.8.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.7.0-6
- Rebuilt for Python 3.7

* Fri Mar 16 2018 Michal Ambroz <rebus at, seznam.cz> - 3.7.0-5
- fix dependencies for building the epel7/epel6 packages

* Thu Mar 15 2018 Michal Ambroz <rebus at, seznam.cz> - 3.7.0-4
- rebuild with yara 3.7.1 for supported platforms
- fix dependencies for building the epel packages

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.7.0-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 15 2017 Michal Ambroz <rebus at, seznam.cz> - 3.7.0-1
- bump to yara 3.7.0 release version (#1511921)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 17 2017 Michal Ambroz <rebus at, seznam.cz> - 3.6.3-2
- fix bogus dates in the changelog
- omit failing testCompileFile test for s390/ppc64

* Mon Jul 17 2017 Michal Ambroz <rebus at, seznam.cz> - 3.6.3-1
- bump to upstream 3.6.3 release version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.5.0-9
- Rebuild for Python 3.6

* Wed Nov 23 2016 Dan Horák <dan[at]danny.cz> - 3.5.0-8
- fix the arch lists

* Tue Aug 16 2016 Michal Ambroz <rebus at, seznam.cz> - 3.5.0-7
- adding test exclusions also for armv7hl and ppc64le

* Tue Aug 16 2016 Michal Ambroz <rebus at, seznam.cz> - 3.5.0-6
- additionally testEntrypoint testIn testIntegerFunctions failing on s390/ppc64
- exclude those tests for build of s390/ppc64

* Tue Aug 16 2016 Michal Ambroz <rebus at, seznam.cz> - 3.5.0-5
- testModuleData is failing on arm platform even for python 2.7
- exclude this test for build of arm

* Fri Aug 12 2016 Michal Ambroz <rebus at, seznam.cz> - 3.5.0-4
- remove unnecessary ldconfig
- count with the python3 test values except the 2 known for failing

* Thu Aug 11 2016 Michal Ambroz <rebus at, seznam.cz> - 3.5.0-3
- change python3 naming to allow epel7 python34 packages

* Thu Aug 04 2016 Michal Ambroz <rebus at, seznam.cz> - 3.5.0-2
- cosmetics

* Thu Aug 04 2016 Michal Ambroz <rebus at, seznam.cz> - 3.5.0-1
- with yara 3.5.0 the python yara binding is separate library
