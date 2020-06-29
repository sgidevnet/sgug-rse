%global srcname mechanize
%global sum Stateful programmatic web browsing

Name:           python-mechanize
Version:        0.4.5
Release:        2%{?dist}
Summary:        Stateful programmatic web browsing

License:        BSD or ZPLv2.1
URL:            https://github.com/python-mechanize/
Source0:        https://github.com/python-mechanize/mechanize/archive/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
# for tests
BuildRequires:  python3-html5lib
BuildRequires:  python3-twisted
BuildRequires:  python3-zope-interface

%description
Stateful programmatic web browsing, after Andy Lester's Perl module
WWW::Mechanize.

The library is layered: mechanize.Browser (stateful web browser),
mechanize.UserAgent (configurable URL opener), plus urllib2 handlers.

Features include: ftp:, http: and file: URL schemes, browser history,
high-level hyperlink and HTML form support, HTTP cookies, HTTP-EQUIV and
Refresh, Referer [sic] header, robots.txt, redirections, proxies, and
Basic and Digest HTTP authentication.  mechanize's response objects are
(lazily-) .seek()able and still work after .close().

Much of the code originally derived from Perl code by Gisle Aas
(libwww-perl), Johnny Lee (MSIE Cookie support) and last but not least
Andy Lester (WWW::Mechanize).  urllib2 was written by Jeremy Hylton.

%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Stateful programmatic web browsing, after Andy Lester's Perl module
WWW::Mechanize.

The library is layered: mechanize.Browser (stateful web browser),
mechanize.UserAgent (configurable URL opener), plus urllib2 handlers.

Features include: ftp:, http: and file: URL schemes, browser history,
high-level hyperlink and HTML form support, HTTP cookies, HTTP-EQUIV and
Refresh, Referer [sic] header, robots.txt, redirections, proxies, and
Basic and Digest HTTP authentication.  mechanize's response objects are
(lazily-) .seek()able and still work after .close().

Much of the code originally derived from Perl code by Gisle Aas
(libwww-perl), Johnny Lee (MSIE Cookie support) and last but not least
Andy Lester (WWW::Mechanize).  urllib2 was written by Jeremy Hylton.

%prep
%autosetup -n %{srcname}-%{version}
chmod -x examples/forms/{echo.cgi,example.py,simple.py}

%build
%py3_build

%install
%py3_install

%check
chmod +x examples/forms/{echo.cgi,example.py,simple.py}
python3 run_tests.py
chmod -x examples/forms/{echo.cgi,example.py,simple.py}

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst ChangeLog COPYRIGHT
%{python3_sitelib}/mechanize*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.5-2
- Rebuilt for Python 3.9

* Wed Apr 15 2020 Mohan Boddu <mboddu@bhujji.com> - 0.4.5-1
- Update to 0.4.5

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.3-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 22 2019 Kevin Fenzi <kevin@scrye.com> - 0.4.3-1
- Update to 0.4.3. Fixs bug #1742992
- Drop python2 subpackages. Fixes bugs #1744658 #1744400

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.2-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 27 2019 Marcus A. Romer <aimylios@gmx.de> - 0.4.2-2
- Add subpackage python3-mechanize

* Sun Apr 14 2019 Kevin Fenzi <kevin@scrye.com> - 0.4.2-1
- Update to 0.4.2. Fixes bug #1699201

* Sat Mar 16 2019 Kevin Fenzi <kevin@scrye.com> - 0.4.1-1
- Update to 0.4.1. Fixes bug #1432447

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Mohan Boddu <mboddu@bhujji.com> - 0.4.0-1
- Update to version 0.4.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.3.5-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Kevin Fenzi <kevin@scrye.com> - 0.3.5-1
- Update to 0.3.5. Fixes bug #1432447

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-11
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 30 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 0.2.5-8
- Replace the python-setuptools-devel BR with python-setuptools

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug 22 2012 Luke Macken <lmacken@redhat.com> - 0.2.5-4
- Remove a couple of unit tests that are failing. Issue filed upstream.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 16 2011 Luke Macken <lmacken@redhat.com> - 0.2.5-1
- Update to 0.2.5 (#692836)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan  4 2011 Robin Lee <cheeselee@fedoraproject.org> - 0.2.4-1
- Update to 0.2.4
- Include a missed cgi script and add python-zope-interface and
  python-twisted-web2 to BR to run extra tests
- Remove executable bits from example scripts

* Thu Oct 21 2010 Luke Macken <lmacken@redhat.com> - 0.2.3-1
- Update to 0.2.3 (#3645064)

* Sat Sep 11 2010 Robin Lee <robinlee.sysu@gmail.com> - 0.2.2-1
- Update to 0.2.2
- License specified from 'BSD' to 'BSD or ZPLv2.1'
- Requires: python-clientform removed
- Add %%check section and run test suite

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 10 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.1.10-1
- Update to 0.1.10

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.1.6-0.3.b
- Rebuild for Python 2.6

* Sun Sep  2 2007 Luke Macken <lmacken@redhat.com> - 0.1.6-0.2.b
- Update for python-setuptools changes in rawhide

* Sat Mar  3 2007 Luke Macken <lmacken@redhat.com> - 0.1.6-0.1.b
- 0.1.6b

* Fri Nov 24 2006 Luke Macken <lmacken@redhat.com> - 0.1.5-0.1.b
- Rebuild for python 2.5
- 0.1.5b

* Sun Sep  3 2006 Luke Macken <lmacken@redhat.com> - 0.1.1a-5
- Rebuild for FC6

* Sun Jul  9 2006 Luke Macken <lmacken@redhat.com> - 0.1.1a-4
- Remove unnecessary python-abi requirement

* Wed May 17 2006 Luke Macken <lmacken@redhat.com> - 0.1.1a-3
- Add BuildArch: noarch (bug #192155)

* Sun May 14 2006 Luke Macken <lmacken@redhat.com> - 0.1.1a-2
- Add python-abi Requires
- Remove noarch

* Thu May 11 2006 Luke Macken <lmacken@redhat.com> - 0.1.1a-1
- Packaged for Fedora Extras
