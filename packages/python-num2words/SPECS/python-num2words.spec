# Currently disabled because the BR isn't available in Fedora
%bcond_with tests

%global pypi_name num2words

%global _description %{expand:
Convert numbers to words in multiple languages, it is a library that converts
numbers like ``42`` to words like ``forty-two``.  It supports multiple
languages (English, French, Spanish, German and Lithuanian) and can even
generate ordinal numbers like ``forty-second``.}

Name:           python-%{pypi_name}
Version:        0.5.10
Release:        6%{?dist}
Summary:        Module to convert numbers to words

License:        LGPLv2+
URL:            https://github.com/savoirfairelinux/num2words
Source0:        %{pypi_source}

BuildArch:      noarch

%description %_description

%{?python_enable_dependency_generator}

%package -n python3-%{pypi_name}
Summary:        Python 3 modules to convert numbers to words
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  %{py3_dist delegator.py}
%endif

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%if %{with tests}
%check
%{__python3} setup.py test
%endif

%files -n python3-%{pypi_name}
%doc README.rst
%license COPYING
%{_bindir}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.10-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.10-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.10-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.10-1
- Update to new version
- Use macro for description
- Use autosetup
- Use pypi source macro
- Add disabled tests: missing BR
- Add binary to file list

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 23 2018 William Moreno Reyes <williamjmorenor@gmail.com> - 0.5.7-3
- Remove python2 subpackage
  BZ#1628564

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 06 2018 William Moreno Reyes <williamjmorenor@gmail.com> - 0.5.7-1
- Update to v0.5.7
- Update summary

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.6-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.5.6-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Dec 29 2017 williamjmorenor@gmail.com - 0.5.6-1
- v0.5.6

* Sat Sep 30 2017 williamjmorenor@gmail.com - 0.5.5-1
- Update to v0.5.5 release

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 William Moreno <williamjmorenor@gmail.com> - 0.5.4-1
- Update to v0.5.4

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.5.3-11
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-10
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Feb 09 2016 William Moreno <williamjmorenor@gmail.com> - 0.5.3-9
- Fix depencies for python2 subpackage

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 21 2015 Kalev Lember <klember@redhat.com> - 0.5.3-7
- Add missing provides/obsoletes to the python2 subpackage

* Tue Nov 17 2015 William Moreno Reyes <williamjmorenor at gmail.com> - 0.5.3-6
- Diferent directories for py2 and py3

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Sep 16 2015 William Moreno Reyes <williamjmorenor at gmail.com> - 0.5.3-4
- Update python macros
- Include subpackages for python 2 and 3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Fedora <williamjmorenor@gmail.com>
- 0.5.3-2
- Fix requires python3 for python2 package

* Tue Jun 09 2015 Fedora <williamjmorenor@gmail.com>
- 0.5.3-1
- Update to 0.5.3 release

* Wed Jun 03 2015 William Moreno Reyes <williamjmorenor at gmail.com>
- 0.5.2-6
- Initial importing of #1223623

* Tue Jun 02 2015 William Moreno Reyes <williamjmorenor at gmail.com>
- 0.5.2-5
- Exclude test files

* Tue Jun 02 2015 William Moreno Reyes <williamjmorenor at gmail.com>
- 0.5.2-4
- Move test files under the %%{pypi_name} directory
- Include test files in a devel package
- Fix %%license tag

* Sat May 30 2015 William Moreno Reyes <williamjmorenor at gmail.com>
- 0.5.2-3
- Add suport for Pyhton3
- Use %%license file from Github
- Include test files in package

* Fri May 29 2015 William Moreno Reyes <williamjmorenor at gmail.com>
- 0.5.2-2
- Remove /test after %%check

* Thu May 21 2015 William Moreno Reyes <williamjmorenor at gmail.com>
- 0.5.2-1
- Initial package.
