%bcond_without tests

%global pypi_name wcwidth

Name:           python-%{pypi_name}
Version:        0.2.4
Release:        1%{?dist}
Summary:        Measures number of Terminal column cells of wide-character codes

License:        MIT
URL:            https://github.com/jquast/wcwidth
Source0:        %pypi_source
BuildArch:      noarch

%description
This API is mainly for Terminal Emulator implementors, or those writing programs
that expect to interpreted by a terminal emulator and wish to determine the
printable width of a string on a Terminal.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with tests}
BuildRequires:  python3-pytest
%endif
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This API is mainly for Terminal Emulator implementors, or those writing programs
that expect to interpreted by a terminal emulator and wish to determine the
printable width of a string on a Terminal.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%if %{with tests}
%check
%{__python3} -m pytest -v
%endif

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Fri Jun 19 2020 Avram Lubkin <aviso@rockhopper.net> - 0.2.4-1
- Update to 0.2.4

* Tue Jun 02 2020 Avram Lubkin <aviso@rockhopper.net> - 0.2.3-1
- Update to 0.2.3

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.9-3
- Rebuilt for Python 3.9

* Fri May 22 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.9-2
- Bootstrap for Python 3.9

* Sat Mar 28 2020 Avram Lubkin <aviso@rockhopper.net> - 0.1.9-1
- Update to 0.1.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.7-14
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.7-13
- Rebuilt for Python 3.8

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.7-12
- Bootstrap for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 13 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.7-10
- Subpackage python2-wcwidth has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.7-7
- Rebuilt for Python 3.7

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.1.7-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1.7-2
- Rebuild for Python 3.6

* Tue Dec 13 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.1.7-1
- Update to 0.1.7

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.6-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.1.6-2
- Provide python-wcwidth for EL6

* Sat Jan 09 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.1.6-1
- Update to new upstream
- Remove external LICENSE thanks to the new version

* Wed Jan 06 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.1.5-2
- Remove shabang from file that was not executable

* Tue Dec 29 2015 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.1.5-1
- Initial package.
