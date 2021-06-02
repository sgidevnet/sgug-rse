# add --without testsuite option, i.e. enable testsuite by default
%bcond_without testsuite

Name:           shedskin
Version:        0.9.4
Release:        11%{?dist}
Summary:        Python to C++ compiler

# The dict implementation in shedskin/lib/builtin.cpp is under the Python
# license. The Murmurhash implementation in builtin.cpp is bundled (noted
# below) and licensed MIT.
# Other files in shedskin/lib/ are MIT, rest GPLv3
# WTFPL: print_stacktrace function in shedskin/lib/builtin.hpp
License:        GPLv3 and (MIT and Python) and WTFPL
URL:            http://code.google.com/p/shedskin/
Source0:        http://shedskin.googlecode.com/files/shedskin-%{version}.tgz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools

# Required for running the testsuite:
BuildRequires:  gc-devel
BuildRequires:  gcc-c++
BuildRequires:  pcre-devel

# Require all devel packages for making a binary
# <gc/gc_allocator.h>
Requires:       gc-devel
# <sys/types.h>
Requires:       gcc-c++
# <pcre.h>
Requires:       pcre-devel
# <Python.h>
Requires:       python2-devel

# murmurhash is bundled in shedskin/lib/buildin.cpp as a hash function
# http://sites.google.com/site/murmurhash/
# fpc exception granted at:
# https://fedorahosted.org/fpc/ticket/39
Provides:       bundled(murmurhash) = 2

%description
Shed Skin is an experimental compiler, that can translate pure, but
implicitly statically typed Python programs into optimized C++. It can
generate stand-alone programs or extension modules, that can be imported
and used in larger Python programs.


%prep
%setup -q -n %{name}-%{version}


%build
%py2_build


%install
rm -rf %{buildroot}
%py2_install


%check
%if %{with testsuite}
%{__python2} setup.py test
%endif

 

%files
%doc LICENSE README doc/
%{_bindir}/shedskin
%{python2_sitelib}/shedskin/
%{python2_sitelib}/shedskin-*.egg-info


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 14 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.9.4-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Thomas Spura <tomspur@fedoraproject.org> - 0.9.4-1
- BR gcc-c++ instead of glibc-headers (#1230497)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 12 2011 Thomas Spura <tomspur@fedoraproject.org> - 0.9-1
- update to new version

* Wed Jun 15 2011 Thomas Spura <tomspur@fedoraproject.org> - 0.8-1
- update to new version
- run tests, when building

* Wed Feb 23 2011 Thomas Spura <tomspur@fedoraproject.org> - 0.7.1-1
- update to new version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Dec 25 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.7-3
- add some missing Requires

* Thu Dec 16 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.7-2
- fix license tag (thanks Toshio Ernie Kuratomi)

* Sun Dec 12 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.7-1
- update to new version

* Wed Dec  1 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.6-2
- provide bundled(murmurhash)

* Mon Nov 29 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.6-1
- update to new version

* Sun Jun 20 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.5-1
- update to new version

* Sun Mar 28 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.4.0-1
- update to new version

* Mon Jan 18 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.3.1-3
- make %%files more explicit

* Sat Jan 16 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.3.1-2
- use GPLv3 and MIT as license

* Wed Jan 13 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.3.1-1
- new version 0.3.1

* Sat Jan 09 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.3-1
- initial spec for upcoming 0.3 version
