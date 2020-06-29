%global module_name musicbrainzngs
%{!?python3_pkgversion: %global python3_pkgversion 3}

Name:           python-musicbrainzngs
Version:        0.5
Release:        20%{?dist}
Summary:        Python bindings for MusicBrainz NGS webservice

License:        BSD and ISC
URL:            https://github.com/alastair/python-musicbrainz-ngs
Source0:        https://pypi.python.org/packages/source/m/%{module_name}/%{module_name}-%{version}.tar.gz

BuildArch:      noarch

%description
This library implements webservice bindings for the MusicBrainz NGS site, also
known as /ws/2.

For more information on the MusicBrainz webservice see:
  http://wiki.musicbrainz.org/XML_Web_Service

%package     -n python%{python3_pkgversion}-%{module_name}
Summary:        Python %{python3_pkgversion} bindings for MusicBrainz NGS webservice
%{?python_provide:%python_provide python%{python3_pkgversion}-%{module_name}}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-nose

%description -n python%{python3_pkgversion}-%{module_name}
This library implements Python %{python3_pkgversion} webservice bindings for the
MusicBrainz NGS site, also known as /ws/2.

For more information on the MusicBrainz webservice see:
  http://wiki.musicbrainz.org/XML_Web_Service

%prep
%setup -qn %{module_name}-%{version}
chmod a-x examples/*.py
sed -i '1{\@^#!/usr/bin/env python@d}' examples/*.py


%build
%py3_build


%install
%py3_install


%check
rm -rf musicbrainzngs
PYTHONPATH=%{buildroot}%{python3_sitelib} nosetests-%{python3_version}

 
%files -n python%{python3_pkgversion}-%{module_name}
%license COPYING
%doc README.md docs examples
%{python3_sitelib}/*


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5-20
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 21 2019 luto@kernel.org - 0.5-18
- Remove Python 2 subpackages (#1775085)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5-17
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5-16
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.5-13
- Drop explicit locale setting
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5-11
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.5-7
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 27 2015 Ville Skyttä <ville.skytta@iki.fi> - 0.5-4
- Add python3 subpackage, update to current python packaging guidelines

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Oct 07 2014 Andy Lutomirski <luto@mit.edu> - 0.5-2
- Remove BR: python2-devel

* Tue Oct 07 2014 Andy Lutomirski <luto@mit.edu> - 0.5-1
- Bump to 0.5.

* Fri Sep 13 2013 Ian Weller <iweller@redhat.com> - 0.4-1
- Initial package build
