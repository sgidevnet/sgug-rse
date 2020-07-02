%global pypi_name python-editor

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           python-editor
Version:        1.0.4
Release:        6%{?dist}
Summary:        Programmatically open an editor, capture the result

License:        ASL 2.0
URL:            https://github.com/fmoo/python-editor
Source:         https://github.com/fmoo/python-editor/archive/%{version}.tar.gz
BuildArch:      noarch

%description
Programmatically open an editor, capture the result.

%package -n python3-editor
Summary:        Programmatically open an editor, capture the result.
%{?python_provide:%python_provide python3-editor}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-editor
Programmatically open an editor, capture the result.

%prep
%setup -q -n %{pypi_name}-%{upstream_version}
rm -rf %{pypi_name}.egg-info
# Change shebang according to Python version
sed -i '1s=^#!/usr/bin/\(python\|env python\)[0-9.]*=#!%{__python3}=' editor.py

%build
%py3_build

%install
%py3_install
chmod a+x $RPM_BUILD_ROOT%{python3_sitelib}/editor.py

%files -n python3-editor
%doc README.md
%license LICENSE
%{python3_sitelib}/*.egg-info/
%{python3_sitelib}/editor.py*
%{python3_sitelib}/__pycache__/*


%changelog
* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.4-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 25 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.4-4
- Subpackage python2-editor has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.4-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 2019 Kevin Fenzi <kevin@scrye.com> - 1.0.4-1
- Update to 1.0.4. Fixes bug #1671673

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-8
- Rebuilt for Python 3.7

* Thu Mar 22 2018 Jan Beran <jberan@redhat.com> - 1.0.3-7
- Fix of python3-editor requires both Python 2 and Python 3 (rhbz #1546794)

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.3-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 17 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.3-4
- Fix creation of python2- subpackage

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 27 2016 Kevin Fenzi <kevin@scrye.com> - 1.0.3-1
- Update to 1.0.3. Fixes bug #1400316

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-2
- Rebuild for Python 3.6

* Wed Nov 23 2016 Kevin Fenzi <kevin@scrye.com> - 1.0.2-1
- Update to 1.0.2

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jun 15 2016 Kevin Fenzi <kevin@scrye.com> - 1.0.1-1
- Update to 1.0.1. Fixes bug #1346641

* Sun Apr 10 2016 Kevin Fenzi <kevin@scrye.com> - 1.0-1
- Update to 1.0. Fixes bug #1323386

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 24 2015 Ralph Bean <rbean@redhat.com> - 0.4-4
- Merge branches together and bump release for bodhi updates.
- Removed empty %%check section.
- Fix incorrect usage of %%{pypi_name}.

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Aug 31 2015 Lukas Bezdicka <lbezdick@redhat.com> - 0.4-2
- fix python2 and python3 support and add support for Centos CBS
- fix description

* Wed Aug 26 2015 Lukas Bezdicka <lbezdick@redhat.com> - 0.4-1
- Bump to 0.4

* Tue Aug 25 2015 Lukas Bezdicka <lbezdick@redhat.com> - 0.3-1
- initial package
