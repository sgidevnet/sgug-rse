%global srcname GeoIP
%global sum Python bindings for the GeoIP geographical lookup libraries

Name:           python-GeoIP
Version:        1.3.2
Release:        16%{?dist}
Summary:        Python bindings for the GeoIP geographical lookup libraries

License:        LGPLv2+
URL:            http://www.maxmind.com/download/geoip/api/python/
Source0:        http://pypi.python.org/packages/source/G/GeoIP/GeoIP-%{version}.tar.gz

# GeoIP 1.4.8 required by v1.2.7 of this package per README
BuildRequires:  gcc
BuildRequires:  GeoIP-devel >= 1.4.8
BuildRequires:  python3-devel

%description
This package contains the Python bindings for the GeoIP API, allowing IP to
location lookups to country, city and organization level within Python code.

%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
This package contains the Python bindings for the GeoIP API, allowing IP to
location lookups to country, city and organization level within Python code.

%prep
%setup -q -n GeoIP-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%doc README.rst examples/
%license LICENSE
%{python3_sitearch}/GeoIP*.so
%{python3_sitearch}/*egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.2-16
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 13 2019 Sérgio Basto <sergio@serjux.com> - 1.3.2-14
- Remove python2 subpackage

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.2-13
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.2-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.3.2-4
- Rebuild for Python 3.6

* Thu Oct 13 2016 Sérgio Basto <sergio@serjux.com> - 1.3.2-3
- Created python2 and 3 subpackages

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Apr 24 2016 Sérgio Basto <sergio@serjux.com> - 1.3.2-1
- Update python-GeoIP to 1.3.2
- Use pypi url in Source0.
- Spec cleanup.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Nov 10 2013 Matt Domsch <mdomsch@fedoraproject.org> - 1.2.8-3
- rebuild (BZ#1028761)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May  9 2013 Matt Domsch <mdomsch@fedoraproject.org> - 1.2.8-1
- Remove unused code. ( Boris Zentner )
- Fix low memory error handling and refcount issues on error

* Thu Mar  7 2013 Matt Domsch <mdomsch@fedoraproject.org> - 1.2.7-1
- update to August 2011 release, drop our IPv6 patch

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-0.7.20090931cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-0.6.20090931cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-0.5.20090931cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-0.4.20090931cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1.2.5-0.3.20090931cvs
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Sep  1 2009 Matt Domsch <mdomsch@fedoraproject.org> - 1.2.5-0.2.20090931cvs
- fix prerelease versioning

* Mon Aug 31 2009 Matt Domsch <mdomsch@fedoraproject.org> - 1.2.5-0.1.20090931cvs
- add IPv6 functions from CVS HEAD

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 29 2008 Michael Fleming <mfleming+rpm@enlartenment.com> 1.2.4-1
- Update to 1.2.4

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.2.2-2
- Rebuild for Python 2.6

* Sun Aug 31 2008 Michael Fleming <mfleming+rpm@enlartenment.com> 1.2.2-1
- Update to 1.2.2
- Drop ccodes patch as it's been accepted upstream
- Change of license to LGPL

* Sat Feb 23 2008 Michael Fleming <mfleming+rpm@enlartenment.com> 1.2.1-12
- Include egg-info files (as generated by Python 2.5)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2.1-10
- Autorebuild for GCC 4.3

* Thu Sep 13 2007 Michael Fleming <mfleming+rpm@enlartenment.com> 1.2.1-9
- Add patch to expose country codes courtesy of Ignacio Vazquez-Adams
  (bz #243696)
- Update License tag per new guidelines
- Fix requires per python packaging guidelines.

* Sat Dec 9 2006 Michael Fleming <mfleming+rpm@enlartenment.com> 1.2.1-6
- Rebuild for python 2.5

* Mon Sep 4 2006 Michael Fleming <mfleming+rpm@enlartenment.com> 1.2.1-5
- Rebuild

* Mon Jun 19 2006 Michael Fleming <mfleming+rpm@enlartenment.com> 1.2.1-4
- Bump to create sane distro upgrade paths

* Mon Feb 20 2006 Michael Fleming <mfleming+rpm@enlartenment.com> 1.2.1-3
- Trivial spec tweaks
- Removed redundant GeoIP Requires: (rpm picks it up automatically)

* Mon Feb 20 2006 Michael Fleming <mfleming+rpm@enlartenment.com> 1.2.1-2
- Change name to -GeoIP in keeping with naming conventions.
- Fix dependency issues caused by the test scripts in %%doc.

* Sat Feb 18 2006 Michael Fleming <mfleming+rpm@enlartenment.com> 1.2.1-1
- Initial version.
