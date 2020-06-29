%global tarball_name simplemediawiki
%global full_version %{version}b2


Name:           python-%{tarball_name}
Version:        1.2.0
Release:        0.23.b2%{?dist}
Summary:        Extremely low-level wrapper to the MediaWiki API

License:        LGPLv2+
URL:            https://github.com/ianweller/python-simplemediawiki
Source0:        http://pypi.python.org/packages/source/s/%{tarball_name}/%{tarball_name}-%{full_version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-sphinx
BuildRequires:  python3-devel
BuildRequires:  python3-nose
BuildRequires:  python3-sphinx

%global _description\
The module simplemediawiki is an extremely low-level wrapper to the MediaWiki\
API. It automatically handles cookies and g zip compression so that you can\
make basic calls to the API in the easiest way possible. It also provides a\
few functions to make day-to-day API access easier.

%description %_description

%package -n python3-%{tarball_name}
Summary:        Extremely low-level wrapper to the MediaWiki API

%description -n python3-%{tarball_name}
The module simplemediawiki is an extremely low-level wrapper to the MediaWiki
API. It automatically handles cookies and g zip compression so that you can
make basic calls to the API in the easiest way possible. It also provides a
few functions to make day-to-day API access easier.

This is the Python 3 version.

%prep
%setup -qn %{tarball_name}-%{full_version}


%build
%{__python3} setup.py build build_sphinx

%install

%{__python3} setup.py install --skip-build --root %{buildroot}

%files -n python3-%{tarball_name}
%doc COPYING PKG-INFO README build/sphinx/html
%{python3_sitelib}/*

%changelog
* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-0.23.b2
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.22.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-0.21.b2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-0.20.b2
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.19.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.18.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 04 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-0.17.b2
- Subpackage python2-simplemediawiki has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Wed Jul 25 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.2.0-0.16.b2
- Use the py2 version of the macros

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.15.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-0.14.b2
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.13.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2.0-0.12.b2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.0-0.11.b2
- Python 2 binary package renamed to python2-simplemediawiki
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.10.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.9.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-0.8.b2
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-0.7.b2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.6.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-0.5.b2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-0.4.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-0.3.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.2.0-0.2.b2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Aug 12 2013 Ian Weller <iweller@redhat.com> - 1.2.0-0.1.b2
- Update to version 1.2.0b1
- Add Python 3 support

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 26 2012 Ian Weller <iweller@redhat.com> - 1.1.1-1
- Update to version 1.1.1
  - Fixes an issue where MediaWiki.parse_date doesn't actually work at all
  - Remove dependency on python-iso8601 which is no longer necessary
  - Add dependency on python-kitchen

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 28 2011 Luke Macken <lmacken@redhat.com> - 1.1-1
- Update to 1.1 (#678398)
- Require python-simplejson
- Include the README
- Build the HTML documentation

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Nov 20 2010 Abdel Martínez <potty@fedoraproject.org> - 1.0-3
- Requires (python-iso8601) added.

* Fri Nov 12 2010 Abdel Martínez <potty@fedoraproject.org> - 1.0-2
- Correcting license.
- Remove/adding variables.
- Modifying description length.
- Adding documentation.

* Wed Nov 10 2010 Abdel Martínez <potty@fedoraproject.org> - 1.0-1
- First package build.
