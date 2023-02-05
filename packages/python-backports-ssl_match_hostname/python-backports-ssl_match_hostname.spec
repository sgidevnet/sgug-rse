%global module_name backports.ssl_match_hostname

Name:           python-backports-ssl_match_hostname
Version:        3.5.0.1
Release:        12%{?dist}
Summary:        The ssl.match_hostname() function from Python 3

License:        Python
URL:            https://bitbucket.org/brandon/backports.ssl_match_hostname
Source0:        http://pypi.python.org/packages/source/b/%{module_name}/%{module_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel

%global _description\
The Secure Sockets layer is only actually secure if you check the hostname in\
the certificate returned by the server to which you are connecting, and verify\
that it matches to hostname that you are trying to reach.\
\
But the matching logic, defined in RFC2818, can be a bit tricky to implement on\
your own. So the ssl package in the Standard Library of Python 3.2 now includes\
a match_hostname() function for performing this check instead of requiring\
every application to implement the check separately.\
\
This backport brings match_hostname() to users of earlier versions of Python.\
The actual code is only slightly modified from Python 3.5.\


%description %_description

%package -n python2-backports-ssl_match_hostname
Summary: %summary
Requires:       python2-backports
%if 0%{?fedora} || 0%{?rhel} && 0%{?rhel} >= 7
# python-ipaddress has yet to be built for epel6.  When it is we can Require
# this everywhere
Requires: python2-ipaddress
%endif
Provides: python2-backports-ssl_match_hostname
%{?python_provide:%python_provide python2-backports-ssl_match_hostname}

%description -n python2-backports-ssl_match_hostname %_description

%prep
%setup -qn %{module_name}-%{version}

cp backports/ssl_match_hostname/README.txt ./
cp backports/ssl_match_hostname/LICENSE.txt ./

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}
rm -f %{buildroot}%{python2_sitelib}/backports/__init__.py*

%files -n python2-backports-ssl_match_hostname
%{!?_licensedir:%global license %%doc}
%license LICENSE.txt
%doc README.txt
%{python2_sitelib}/backports/ssl_match_hostname/
%{python2_sitelib}/backports.ssl_match_hostname-%{version}-*egg*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 25 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 3.5.0.1-10
- Use the py2 version of the macros

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.5.0.1-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sun Dec 17 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.5.0.1-6
- Python 2 binary package renamed to python2-backports-ssl_match_hostname
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.0.1-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 19 2015 Toshio Kuratomi <toshio@fedoraproject.org> - - 3.5.0.1-1
- New upstream release
- Brings IP Address ServerAltName handling
- Better fix for namespace issues that doesn't involve setuptools.

* Thu Oct 15 2015 David Sommerseth <davids@redhat.com> - 3.4.0.2-6
- Further fix namespace declaration, to be buildable on more recent Fedora 23

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Sep 17 2014 Ralph Bean <rbean@redhat.com> - 3.4.0.2-4
- Apply upstream patch to fix python namespace handling.
- Narrow down directory ownership to just the ssl_match_hostname module.

* Thu Jul 31 2014 Tom Callaway <spot@fedoraproject.org> - 3.4.0.2-3
- fix license handling

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Oct 27 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 3.4.0.2-1
- Update to upstream 3.4.0.2 for a security fix
- http://bugs.python.org/issue17997

* Mon Sep 02 2013 Ian Weller <iweller@redhat.com> - 3.4.0.1-1
- Update to upstream 3.4.0.1

* Mon Aug 19 2013 Ian Weller <iweller@redhat.com> - 3.2-0.5.a3
- Use python-backports instead of providing backports/__init__.py

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-0.4.a3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 20 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 3.2-0.3.a3
- Add patch for CVE 2013-2099 https://bugzilla.redhat.com/show_bug.cgi?id=963260

* Tue Feb 05 2013 Ian Weller <iweller@redhat.com> - 3.2-0.2.a3
- Fix Python issue 12000

* Fri Dec 07 2012 Ian Weller <iweller@redhat.com> - 3.2-0.1.a3
- Initial package build
