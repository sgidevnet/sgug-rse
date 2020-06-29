Name:       python-mygpoclient
Version:    1.8
Release:    11%{?dist}
Summary:    Python module to connect to the my.gpodder.org webservice

License:    GPLv3+
URL:        http://thpinfo.com/2010/mygpoclient/ 
Source0:    http://thpinfo.com/2010/mygpoclient/mygpoclient-%{version}.tar.gz  
BuildArch:  noarch

%global _description\
%{name} is a client-library to connect the my.gpodder.org webservice.

%description %_description

%package -n python3-mygpoclient
Summary: %summary
%{?python3_provide:%python3_provide python3-mygpoclient}
BuildRequires: python3-devel
BuildRequires: python3-minimock
BuildRequires: python3-coverage
BuildRequires: python3-nose
BuildRequires: python3-simplejson

%description -n python3-mygpoclient %_description

%prep
%setup -q -n mygpoclient-%{version}
# Leave out http-tests as they currently fail occasionally (reported upstream)
rm mygpoclient/http_test.py

%build
%py3_build

%check
nosetests-3 --cover-erase --with-coverage --with-doctest --cover-package=mygpoclient

%install
%py3_install


%files -n python3-mygpoclient
%{python3_sitelib}/mygpoclient
%{python3_sitelib}/mygpoclient*.egg-info
%{_bindir}/mygpo-*
%{_mandir}/man1/mygpo-bpsync.1.gz
%exclude %{python3_sitelib}/mygpoclient/*test.py*
%doc README.md COPYING AUTHORS


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.8-11
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.8-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.8-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.8-5
- Subpackage python2-mygpoclient has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.8-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 02 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.8-1
- 1.8, python 3 support.

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.7-8
- Python 2 binary package renamed to python2-mygpoclient
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Oct 18 2013 Ville-Pekka Vainio <vpvainio AT iki.fi> 1.7-1
- New upstream release

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Aug 06 2011 Ville-Pekka Vainio <vpvainio AT iki.fi> 1.6-1
- New upstream release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 12 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 1.5-1
- New upstream release

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Apr 30 2010 Sven Lankes <sven@lank.es> - 1.4-1
- New upstream release

* Sun Mar 28 2010 Sven Lankes <sven@lank.es> - 1.2-1
- New upstream release

* Sun Jan 24 2010 Sven Lankes <sven@lank.es> - 1.0-3
- Add python-simplejson BR to allow tests to run

* Fri Jan 22 2010 Sven Lankes <sven@lank.es> - 1.0-2
- SPEC-Tweaks incorporating feedback from #fedora-de
- Rename to ease adding a python 3 variant later
- Run testsuite during build

* Fri Jan 22 2010 Sven Lankes <sven@lank.es> - 1.0-1
- initial package

