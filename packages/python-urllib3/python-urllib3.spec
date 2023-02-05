%global srcname urllib3

# When bootstrapping Python, we cannot test this yet
%bcond_with tests

Name:           python-%{srcname}
Version:        1.25.7
Release:        1%{?dist}
Summary:        Python HTTP library with thread-safe connection pooling and file post

License:        MIT
URL:            https://github.com/urllib3/urllib3
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
# Unbundle ssl_match_hostname since we depend on it
Source1:        ssl_match_hostname_py3.py
BuildArch:      noarch

%description
Python HTTP module with connection pooling and file POST abilities.

%package -n python2-%{srcname}
Summary:        Python2 HTTP library with thread-safe connection pooling and file post
%{?python_provide:%python_provide python2-%{srcname}}

Requires:       ca-certificates

# Previously bundled things:
Requires:       python2-six
Requires:       python2-backports-ssl_match_hostname

# Secure extra requirements
Requires:       python2-idna
Requires:       python2-ipaddress
Requires:       python2-pysocks

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools

%description -n python2-%{srcname}
Python2 HTTP module with connection pooling and file POST abilities.


%package -n python3-%{srcname}
Summary:        Python3 HTTP library with thread-safe connection pooling and file post

BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-nose
BuildRequires:  python3-mock
BuildRequires:  python3-six
BuildRequires:  python3-pysocks
BuildRequires:  python3-pytest
BuildRequires:  python3-tornado
BuildRequires:  python3-trustme
BuildRequires:  python3-idna
%endif

Requires:       ca-certificates
Requires:       python3-idna
Requires:       python3-six
Requires:       python3-pysocks

%description -n python3-%{srcname}
Python3 HTTP module with connection pooling and file POST abilities.


%prep
%autosetup -p1 -n %{srcname}-%{version}
# Drop the dummyserver tests in koji.  They fail there in real builds, but not
# in scratch builds (weird).
rm -rf test/with_dummyserver/
# Don't run the Google App Engine tests
rm -rf test/appengine/
# Lots of these tests started failing, even for old versions, so it has something
# to do with Fedora in particular. They don't fail in upstream build infrastructure
rm -rf test/contrib/

# Tests for Python built without SSL, but Fedora builds with SSL. These tests
# fail when combined with the unbundling of backports-ssl_match_hostname
rm -f test/test_no_ssl.py

%build
%py2_build
%py3_build


%install
%py2_install
%py3_install

# Unbundle the Python 2 build
rm -rf %{buildroot}/%{python2_sitelib}/urllib3/packages/six.py*
rm -rf %{buildroot}/%{python2_sitelib}/urllib3/packages/ssl_match_hostname/

mkdir -p %{buildroot}/%{python2_sitelib}/urllib3/packages/
ln -s %{python2_sitelib}/six.py %{buildroot}/%{python2_sitelib}/urllib3/packages/six.py
ln -s %{python2_sitelib}/six.pyc %{buildroot}/%{python2_sitelib}/urllib3/packages/six.pyc
ln -s %{python2_sitelib}/six.pyo %{buildroot}/%{python2_sitelib}/urllib3/packages/six.pyo
ln -s %{python2_sitelib}/backports/ssl_match_hostname \
      %{buildroot}/%{python2_sitelib}/urllib3/packages/ssl_match_hostname

# Unbundle the Python 3 build
rm -rf %{buildroot}/%{python3_sitelib}/urllib3/packages/six.py*
rm -rf %{buildroot}/%{python3_sitelib}/urllib3/packages/__pycache__/six*
rm -rf %{buildroot}/%{python3_sitelib}/urllib3/packages/ssl_match_hostname/

mkdir -p %{buildroot}/%{python3_sitelib}/urllib3/packages/
cp -a %{SOURCE1} %{buildroot}/%{python3_sitelib}/urllib3/packages/ssl_match_hostname.py
ln -s %{python3_sitelib}/six.py %{buildroot}/%{python3_sitelib}/urllib3/packages/six.py
ln -s %{python3_sitelib}/__pycache__/six.cpython-%{python3_version_nodots}.opt-1.pyc \
      %{buildroot}/%{python3_sitelib}/urllib3/packages/__pycache__/
ln -s %{python3_sitelib}/__pycache__/six.cpython-%{python3_version_nodots}.pyc \
      %{buildroot}/%{python3_sitelib}/urllib3/packages/__pycache__/


%if %{with tests}
%check
export PREV_WD=`pwd`
cd test
PYTHONPATH=%{buildroot}%{python3_sitelib}:%{python3_sitelib} %{__python3} -m pytest -v
cd $PREV_WD
%endif


%files -n python2-%{srcname}
%license LICENSE.txt
%doc CHANGES.rst README.rst CONTRIBUTORS.txt
%{python2_sitelib}/urllib3/
%{python2_sitelib}/urllib3-*.egg-info


%files -n python3-%{srcname}
%license LICENSE.txt
%doc CHANGES.rst README.rst CONTRIBUTORS.txt
%{python3_sitelib}/urllib3/
%{python3_sitelib}/urllib3-*.egg-info


%changelog
* Tue Oct 15 2019 Jeremy Cline <jcline@redhat.com> - 1.25.6-1
- Update to v1.25.6

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 08 2019 Miro Hrončok <mhroncok@redhat.com> - 1.25.3-3
- Set RECENT_DATE not to be older than 2 years (#1727796)

* Tue May 28 2019 Jeremy Cline <jcline@redhat.com> - 1.25.3-2
- Drop the Python 2 tests since Tornado is going away

* Tue May 28 2019 Jeremy Cline <jcline@redhat.com> - 1.25.3-1
- Update to 1.25.3

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 13 2018 Jeremy Cline <jeremy@jcline.org> - 1.24.1-2
- Adjust unbundling of ssl_match_hostname

* Mon Oct 29 2018 Jeremy Cline <jeremy@jcline.org> - 1.24.1-1
- Update to v1.24.1

* Wed Jun 20 2018 Lumír Balhar <lbalhar@redhat.com> - 1.23-4
- Removed unneeded dependency python[23]-psutil

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 1.23-3
- Rebuilt for Python 3.7

* Thu Jun 14 2018 Miro Hrončok <mhroncok@redhat.com> - 1.23-2
- Bootstrap for Python 3.7

* Tue Jun 05 2018 Jeremy Cline <jeremy@jcline.org> - 1.23-1
- Update to the latest upstream release (rhbz 1586072)

* Wed May 30 2018 Jeremy Cline <jeremy@jcline.org> - 1.22-10
- Backport patch to support Python 3.7 (rhbz 1584112)

* Thu May 03 2018 Lukas Slebodnik <lslebodn@fedoraproject.org> - 1.22-9
- Do not lowercase hostnames with custom-protocol (rhbz 1567862)
- upstream: https://github.com/urllib3/urllib3/issues/1267

* Wed Apr 18 2018 Jeremy Cline <jeremy@jcline.org> - 1.22-8
- Drop the dependency on idna and cryptography (rhbz 1567862)

* Mon Apr 16 2018 Jeremy Cline <jeremy@jcline.org> - 1.22-7
- Drop the dependency on PyOpenSSL, it's not needed (rhbz 1567862)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.22-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jan 25 2018 Tomas Hoger <thoger@redhat.com> - 1.22-4
- Fix FTBFS - Move RECENT_DATE to 2017-06-30

* Fri Dec 01 2017 Jeremy Cline <jeremy@jcline.org> - 1.22-3
- Symlink the Python 3 bytecode for six (rbhz 1519147)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Jeremy Cline <jeremy@jcline.org> - 1.22-1
- Update to 1.22 (#1473293)

* Wed May 17 2017 Jeremy Cline <jeremy@jcline.org> - 1.21.1-1
- Update to 1.21.1 (#1445280)

* Thu Feb 09 2017 Jeremy Cline <jeremy@jcline.org> - 1.20-1
- Update to 1.20 (#1414775)

* Tue Dec 13 2016 Stratakis Charalampos <cstratak@redhat.com> - 1.19.1-2
- Rebuild for Python 3.6

* Thu Nov 17 2016 Jeremy Cline <jeremy@jcline.org> 1.19.1-1
- Update to 1.19.1
- Clean up the specfile to only support Fedora 26

* Wed Aug 10 2016 Kevin Fenzi <kevin@scrye.com> - 1.16-3
- Rebuild now that python-requests is ready to update.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jun 15 2016 Kevin Fenzi <kevin@scrye.com> - 1.16-1
- Update to 1.16

* Thu Jun 02 2016 Ralph Bean <rbean@redhat.com> - 1.15.1-3
- Create python2 subpackage to comply with guidelines.

* Wed Jun 01 2016 Ralph Bean <rbean@redhat.com> - 1.15.1-2
- Remove broken symlinks to unbundled python3-six files
  https://bugzilla.redhat.com/show_bug.cgi?id=1295015

* Fri Apr 29 2016 Ralph Bean <rbean@redhat.com> - 1.15.1-1
- Removed patch for ipv6 support, now applied upstream.
- Latest version.
- New dep on pysocks.

* Fri Feb 26 2016 Ralph Bean <rbean@redhat.com> - 1.13.1-3
- Apply patch from upstream to fix ipv6.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 21 2015 Ralph Bean <rbean@redhat.com> - 1.13.1-1
- new version

* Fri Dec 18 2015 Ralph Bean <rbean@redhat.com> - 1.13-1
- new version

* Mon Dec 14 2015 Ralph Bean <rbean@redhat.com> - 1.12-1
- new version

* Thu Oct 15 2015 Robert Kuska <rkuska@redhat.com> - 1.10.4-7
- Rebuilt for Python3.5 rebuild

* Sat Oct 10 2015 Ralph Bean <rbean@redhat.com> - 1.10.4-6
- Sync from PyPI instead of a git checkout.

* Tue Sep 08 2015 Ralph Bean <rbean@redhat.com> - 1.10.4-5.20150503gita91975b
- Drop requirement on python-backports-ssl_match_hostname on F22 and newer.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.4-4.20150503gita91975b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Ralph Bean <rbean@redhat.com> - 1.10.4-3.20150503gita91975b
- Apply pyopenssl injection for an outdated cpython as per upstream advice
  https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning
  https://urllib3.readthedocs.org/en/latest/security.html#pyopenssl

* Tue May 19 2015 Ralph Bean <rbean@redhat.com> - 1.10.4-2.20150503gita91975b
- Specify symlinks for six.py{c,o}, fixing rhbz #1222142.

* Sun May 03 2015 Ralph Bean <rbean@redhat.com> - 1.10.4-1.20150503gita91975b
- Latest release for python-requests-2.7.0

* Wed Apr 29 2015 Ralph Bean <rbean@redhat.com> - 1.10.3-2.20150429git585983a
- Grab a git snapshot to get around this chunked encoding failure.

* Wed Apr 22 2015 Ralph Bean <rbean@redhat.com> - 1.10.3-1
- new version

* Thu Feb 26 2015 Ralph Bean <rbean@redhat.com> - 1.10.2-1
- new version

* Wed Feb 18 2015 Ralph Bean <rbean@redhat.com> - 1.10.1-1
- new version

* Wed Feb 18 2015 Ralph Bean <rbean@redhat.com> - 1.10.1-1
- new version

* Mon Jan 05 2015 Ralph Bean <rbean@redhat.com> - 1.10-2
- Copy in a shim for ssl_match_hostname on python3.

* Sun Dec 14 2014 Ralph Bean <rbean@redhat.com> - 1.10-1
- Latest upstream 1.10, for python-requests-2.5.0.
- Re-do unbundling without patch, with symlinks.
- Modernize python2 macros.
- Remove the with_dummyserver tests which fail only sometimes.

* Wed Nov 05 2014 Ralph Bean <rbean@redhat.com> - 1.9.1-1
- Latest upstream, 1.9.1 for latest python-requests.

* Mon Aug  4 2014 Tom Callaway <spot@fedoraproject.org> - 1.8.2-4
- fix license handling

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Apr 21 2014 Arun S A G <sagarun@gmail.com> - 1.8.2-1
- Update to latest upstream version

* Mon Oct 28 2013 Ralph Bean <rbean@redhat.com> - 1.7.1-2
- Update patch to find ca_certs in the correct location.

* Wed Sep 25 2013 Ralph Bean <rbean@redhat.com> - 1.7.1-1
- Latest upstream with support for a new timeout class and py3.4.

* Wed Aug 28 2013 Ralph Bean <rbean@redhat.com> - 1.7-3
- Bump release again, just to push an unpaired update.

* Mon Aug 26 2013 Ralph Bean <rbean@redhat.com> - 1.7-2
- Bump release to pair an update with python-requests.

* Thu Aug 22 2013 Ralph Bean <rbean@redhat.com> - 1.7-1
- Update to latest upstream.
- Removed the accept-header proxy patch which is included in upstream now.
- Removed py2.6 compat patch which is included in upstream now.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 11 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.5-6
- Fix Requires of python-ordereddict to only apply to RHEL

* Fri Mar  1 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.5-5
- Unbundling finished!

* Fri Mar 01 2013 Ralph Bean <rbean@redhat.com> - 1.5-4
- Upstream patch to fix Accept header when behind a proxy.
- Reorganize patch numbers to more clearly distinguish them.

* Wed Feb 27 2013 Ralph Bean <rbean@redhat.com> - 1.5-3
- Renamed patches to python-urllib3-*
- Fixed ssl check patch to use the correct cert path for Fedora.
- Included dependency on ca-certificates
- Cosmetic indentation changes to the .spec file.

* Tue Feb  5 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.5-2
- python3-tornado BR and run all unittests on python3

* Mon Feb 04 2013 Toshio Kuratomi <toshio@fedoraproject.org> 1.5-1
- Initial fedora build.
