%global srcname pylibmc
%global sum Memcached client for Python

Name:           python-%{srcname}
Version:        1.5.1
Release:        17%{?dist}
Summary:        %{sum}

License:        BSD
URL:            http://sendapatch.se/projects/pylibmc/
Source0:        http://pypi.python.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  libmemcached-devel
BuildRequires:  zlib-devel

%description
pylibmc is a client in Python for memcached. It is a wrapper
around TangentOrg‘s libmemcached library. The interface is 
intentionally made as close to python-memcached as possible, 
so that applications can drop-in replace it.


%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
pylibmc is a client in Python 3 for memcached. It is a wrapper
around TangentOrg‘s libmemcached library. The interface is 
intentionally made as close to python-memcached as possible, 
so that applications can drop-in replace it.


%prep
%setup -q -n %{srcname}-%{version}

%build

%py3_build

%install
%py3_install

# there is an asterisk in the name of the file,
# because sometimes the suffix of the architecture is added
chmod 755 $RPM_BUILD_ROOT%{python3_sitearch}/_pylibmc.cpython-%{python3_version_nodots}*.so

%files -n python3-%{srcname}
%doc docs/ LICENSE README.rst
%{python3_sitearch}/%{srcname}-%{version}*.egg-info
%{python3_sitearch}/%{srcname}/
%{python3_sitearch}/*.so


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-17
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-15
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-14
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.5.1-11
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-9
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.5.1-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed May 04 2016 Dominika Krejci <dkrejci@redhat.com> - 1.5.1-1
- version upgrade
- Added Python 3 support

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jan 28 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.2.3-2
- use dist macro

* Mon Jan 28 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.2.3-1
- upstream release 1.2.3
- resolves rhbz#905508

* Sat Sep 22 2012  Remi Collet <remi@fedoraproject.org> - 1.2.0-10.20110805gitf01c31
- rebuild against libmemcached.so.11 without SASL

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-9.20110805gitf01c31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 23 2012  Remi Collet <remi@fedoraproject.org> - 1.2.0-8.20110805gitf01c31
- rebuild against libmemcached.so.10 with SASL

* Sun Apr 22 2012  Remi Collet <remi@fedoraproject.org> - 1.2.0-7.20110805gitf01c31
- rebuild against libmemcached.so.10
- add upstream patch to fix build

* Sat Mar 03 2012  Remi Collet <remi@fedoraproject.org> - 1.2.0-6.20110805gitf01c31
- rebuild against libmemcached.so.9

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-5.20110805gitf01c31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Sep 17 2011  Remi Collet <remi@fedoraproject.org> - 1.2.0-4.20110805gitf01c31
- rebuild against libmemcached.so.8

* Tue Aug 09 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 1.2.0-3.20110805gitf01c31
- Changed file pylibmc.so permission

* Tue Aug 09 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 1.2.0-2.20110805gitf01c31
- Added soname files

* Fri Aug 05 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 1.2.0-1.20110805gitf01c31
- Initial RPM release
