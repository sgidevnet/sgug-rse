%global srcname Pyphen
%global modname pyphen

Name:           python-pyphen
Version:        0.9.5
Release:        3%{?dist}
Summary:        Pure Python module to hyphenate text
License:        GPLv2+ or LGPLv2+ or MPLv1.1
URL:            https://github.com/Kozea/Pyphen
Source0:        https://github.com/Kozea/%{srcname}/archive/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
# tests not packaged in release tarballs
# https://github.com/Kozea/Pyphen/issues/23
Source1:        https://raw.githubusercontent.com/Kozea/Pyphen/ad959cd78e212b6c0f851f202993d79b86a98a55/test.py

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose


%description
Pyphen is a pure Python module to hyphenate text using existing
hyphenation dictionaries, e.g., from Libreoffice language packs.


%package -n python3-pyphen
Summary:        Pure Python module to hyphenate text

%description -n python3-pyphen
Pyphen is a pure Python module to hyphenate text using existing
hyphenation dictionaries, e.g., from Libreoffice language packs.

%prep
%autosetup -n %{srcname}-%{version} -p1
cp -a %{SOURCE1} test.py

%build
%py3_build

%install
rm -rf dictionaries
%py3_install

%check
nosetests test.py


%files -n python3-pyphen
%license COPYING COPYING.GPL COPYING.LGPL COPYING.MPL
%doc README
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{srcname}-%{version}*.egg-info/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.5-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 08 2019 Felix Schwarz <fschwarz@fedoraproject.org> - 0.9.5-1
- update to new upstream version
- use dictionaries shipped by upstream instead of system-provided dicts

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-19
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-18
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 27 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-15
- Subpackage python2-pyphen has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-13
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.9.1-12
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.9.1-10
- Python 2 binary package renamed to python2-pyphen
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-7
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Aug 26 2014 Eric Smith <brouhaha@fedoraproject.org> 0.9.1-2
- No Python 3 in EL7.

* Thu Aug 07 2014 Alon Levy <alon@pobox.com> - 0.9.1-1
- Update to latest release, fixes bz 1127837 (for weasyprint 1127836)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Jul 23 2013 Eric Smith <brouhaha@fedoraproject.org> 0.7-3
- Added Python 3 support.

* Mon Jul 22 2013 Eric Smith <brouhaha@fedoraproject.org> 0.7-2
- Removed requirement for hyphen-en.
- Changed files section based on review request.

* Sun Jul 21 2013 Eric Smith <brouhaha@fedoraproject.org> 0.7-1
- initial version
