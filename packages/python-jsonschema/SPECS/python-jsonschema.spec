%global pypi_name jsonschema

%global common_description %{expand:
jsonschema is an implementation of JSON Schema for Python (supporting
2.7+, including Python 3).

 - Full support for Draft 7, Draft 6, Draft 4 and Draft 3
 - Lazy validation that can iteratively report all validation errors.
 - Small and extensible
 - Programmatic querying of which properties or items failed validation.}

%{?python_enable_dependency_generator}

Name:           python-%{pypi_name}
Summary:        Implementation of JSON Schema validation for Python
Version:        3.2.0
Release:        4%{?dist}
License:        MIT

URL:            https://github.com/Julian/jsonschema
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel

BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)

# test requirements
%bcond_without tests
%if %{with tests}
BuildRequires:  python3dist(attrs)
BuildRequires:  python3dist(perf)
BuildRequires:  python3dist(pyrsistent)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(twisted)
%endif

%description %{common_description}


%package -n     python3-%{pypi_name}
Summary:        %{summary}

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %{common_description}


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
PYTHONPATH=$(pwd) trial-3 %{pypi_name}
%endif


%files -n python3-%{pypi_name}
%license COPYING json/LICENSE
%doc README.rst

%{_bindir}/jsonschema

%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info/


%changelog
* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 3.2.0-4
- Rebuilt for Python 3.9

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 3.2.0-3
- Bootstrap for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 07 2019 Fabio Valentini <decathorpe@gmail.com> - 3.2.0-1
- Update to version 3.2.0.

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.2-3
- Rebuilt for Python 3.8

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.2-2
- Bootstrap for Python 3.8

* Fri Aug 02 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2-1
- Update to version 3.0.2.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 01 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.1-1
- Update to version 3.0.1.

* Sun Feb 24 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.0-1
- Update to version 3.0.0.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0~b3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.0~b3-1
- Update to version 3.0.0b3.

* Tue Jan 22 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.0~b1-1
- Update to version 3.0.0b1.

* Sat Jan 19 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.0~a5-1
- Update to version 3.0.0a5.
- Moved python2 sub-package to separate source package.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Miro Hrončok <mhroncok@redhat.com> - 2.6.0-5
- Rebuilt for Python 3.7

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.6.0-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Jan Beran <jberan@redhat.com> 2.6.0-1
- Update to 2.6.0
- Fix of missing Python 3 version executables

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 14 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.5.1-4
- Rebuild for Python 3.6

* Mon Nov 21 2016 Orion Poplawski <orion@cora.nwra.com> - 2.5.1-3
- Enable python3 builds for EPEL (bug #1395653)
- Ship python2-jsonschema
- Modernize spec
- Use %%license

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 26 2016 Lon Hohberger <lhh@redhat.com> 2.5.1-1
- Update to 2.5.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 13 2015 Robert Kuska <rkuska@redhat.com> - 2.4.0-3
- Rebuilt for Python3.5 rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Sep 06 2014 Alan Pevec <apevec@redhat.com> - 2.4.0-1
- Latest upstream

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Mar 10 2014 Pádraig Brady <pbrady@redhat.com> - 2.3.0-1
- Latest upstream

* Tue Feb 04 2014 Matthias Runge <mrunge@redhat.com> - 2.0.0-3
- fix %%{? issues in spec

* Thu Oct 17 2013 Thomas Spura <tomspur@fedoraproject.org> - 2.0.0-2
- add python3 subpackage (#1016207)
- add %%check

* Fri Aug 16 2013 Alan Pevec <apevec@redhat.com> 2.0.0-1
- Update to 2.0.0 release

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 13 2013 Pádraig Brady <P@draigBrady.com> - 1.3.0-1
- Update to 1.3.0 release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 23 2012 Pádraig Brady <P@draigBrady.com> - 0.2-1
- Initial package.

