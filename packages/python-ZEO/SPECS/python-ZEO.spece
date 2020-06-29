%global srcname ZEO

Name:           python-%{srcname}
Version:        5.2.1
Release:        6%{?dist}
Summary:        Client-server storage implementation for ZODB

License:        ZPLv2.1
URL:            http://www.zodb.org/
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(funcsigs)
BuildRequires:  python3dist(manuel)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(msgpack)
BuildRequires:  python3dist(pbr)
BuildRequires:  python3dist(persistent)
BuildRequires:  python3dist(random2)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(transaction)
BuildRequires:  python3dist(uvloop)
BuildRequires:  python3dist(zc.lockfile)
BuildRequires:  python3dist(zconfig)
BuildRequires:  python3dist(zdaemon)
BuildRequires:  python3dist(zodb)
BuildRequires:  python3dist(zope.interface)
BuildRequires:  python3dist(zope.testing)
BuildRequires:  python3dist(zope.testrunner)

%global common_desc                                                   \
ZEO is a client-server system for sharing a single storage among many \
clients.  When you use ZEO, the storage is opened in the ZEO server   \
process.  Client programs connect to this process using a ZEO         \
ClientStorage.  ZEO provides a consistent view of the database to all \
clients.  The ZEO client and server communicate using a custom RPC    \
protocol layered on top of TCP.

%description
%{common_desc}

%package -n python3-%{srcname}
Summary:        Client-server storage implementation for ZODB

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{common_desc}

%prep
%autosetup -n %{srcname}-%{version}

# Remove a version number that leads to an attempted download from pypi
sed -i 's/msgpack < 0\.6/msgpack/' setup.py

%build
%py3_build

# Convert documentation to HTML
rst2html --no-datestamp CHANGES.rst CHANGES.html
rst2html --no-datestamp README.rst README.html
rst2html --no-datestamp src/ZEO/asyncio/README.rst README-asyncio.html
rst2html --no-datestamp src/ZEO/nagios.rst nagios.html

%install
%py3_install

# Fix scripts
for script in $(grep -Rl '^#!' %{buildroot}%{python3_sitelib}/%{srcname}); do
  sed 's,%{_bindir}/env python.*,%{_bindir}/python3,' $script > $script.new
  touch -r $script $script.new
  mv -f $script.new $script
  chmod 0755 $script
done

# Remove documentation files
rm %{buildroot}%{python3_sitelib}/%{srcname}/asyncio/README.rst
rm %{buildroot}%{python3_sitelib}/%{srcname}/nagios.rst
rm %{buildroot}%{python3_sitelib}/%{srcname}/protocol.txt

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%doc CHANGES.html nagios.html README.html README-asyncio.html
%doc src/ZEO/protocol.txt
%license COPYRIGHT.txt LICENSE.txt
%{_bindir}/runzeo
%{_bindir}/zeo-nagios
%{_bindir}/zeoctl
%{_bindir}/zeopack
%{python3_sitelib}/%{srcname}*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 5.2.1-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 5.2.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 5.2.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb  9 2019 Jerry James <loganjerry@gmail.com> - 5.2.1-1
- New upstream release
- Drop redundant Requires
- Change msgpack name fix to version fix

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 17 2018 Jerry James <loganjerry@gmail.com> - 5.2.0-4
- Drop python2 subpackage

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 5.2.0-2
- Rebuilt for Python 3.7
- Don't BR trollius on python3

* Sat Apr  7 2018 Jerry James <loganjerry@gmail.com> - 5.2.0-1
- New upstream release

* Tue Mar 27 2018 Jerry James <loganjerry@gmail.com> - 5.1.2-1
- New upstream release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 5.1.1-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Dec 23 2017 Jerry James <loganjerry@gmail.com> - 5.1.1-1
- New upstream release

* Sat Oct  7 2017 Jerry James <loganjerry@gmail.com> - 5.1.0-1
- New upstream release

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 5.0.4-2
- Rebuild for Python 3.6

* Sat Dec 10 2016 Jerry James <loganjerry@gmail.com> - 5.0.4-1
- New upstream release

* Tue Nov  1 2016 Jerry James <loganjerry@gmail.com> - 5.0.2-1
- New upstream release

* Tue Sep  6 2016 Jerry James <loganjerry@gmail.com> - 5.0.1-1
- New upstream release

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jul  4 2016 Jerry James <loganjerry@gmail.com> - 4.2.1-1
- New upstream release

* Fri Jun 17 2016 Jerry James <loganjerry@gmail.com> - 4.2.0-1
- New upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb  1 2016 Jerry James <loganjerry@gmail.com> - 4.1.0-3
- Comply with latest python packaging guidelines

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 12 2015 Jerry James <loganjerry@gmail.com> - 4.1.0-1
- New upstream release
- Name python 3 binaries according to policy
- Use license macro

* Thu Jun 12 2014 Jerry James <loganjerry@gmail.com> - 4.0.0-1
- Initial RPM
