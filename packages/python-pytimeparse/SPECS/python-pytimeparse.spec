%global pypi_name pytimeparse

%if 0%{?fedora}
%bcond_without python3
%else
%bcond_with python3
%endif

%if 0%{?fedora} && 0%{?fedora} >= 30
%bcond_with python2
%else
%bcond_without python2
%endif

Name:           python-%{pypi_name}
Version:        1.1.8
Release:        6%{?dist}
Summary:        Time expression parser

License:        MIT
URL:            https://github.com/wroberts/%{pypi_name}
Source0:        %{pypi_source}
BuildArch:      noarch

%if %{with python2}
BuildRequires:  python2-devel
BuildRequires:  python2-nose
BuildRequires:  python2-setuptools
%endif

%if %{with python3}
BuildRequires:  python3-devel
BuildRequires:  python3dist(nose)
BuildRequires:  python3dist(setuptools)
%endif

%description
A small Python module to parse various kinds of time expressions.

%if %{with python2}
%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
A small Python module to parse various kinds of time expressions.

This is the Python 2 version of the package.
%endif

%if %{with python3}
%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A small Python module to parse various kinds of time expressions.

This is the Python 3 version of the package.
%endif

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Remove shebangs from Python scripts
find . -name '*.py' -exec sed -i '1 { /^#!/ d }' {} \+

%build
%if %{with python2}
%py2_build
%endif

%if %{with python3}
%py3_build
%endif

%install
%if %{with python2}
%py2_install
%endif

%if %{with python3}
%py3_install
%endif

%check
%if %{with python2}
%{__python2} setup.py test
%endif

%if %{with python3}
%{__python3} setup.py test
%endif

%if %{with python2}
%files -n python2-%{pypi_name}
%license LICENSE.rst
%doc README.rst
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%license LICENSE.rst
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.8-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.8-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.8-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 11 2019 Eli Young <elyscape@gmail.com> - 1.1.8-1
- Update to 1.1.8

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.5-14
- Subpackage python2-pytimeparse has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.5-12
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.1.5-11
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.5-7
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jun 17 2016 Pradeep Kilambi <pkilambi@redhat.com> - 1.1.5-5
- Add support so we build both py2 and py3

* Fri Apr 08 2016 Dominika Krejci <dkrejci@redhat.com> - 1.1.5-4
- Remove unnecessary shebang lines

* Mon Feb 08 2016 Matej Dujava <mdujava@redhat.com> - 1.1.5-3
- Add python3

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 04 2015 Pradeep Kilambi <pkilambi@redhat.com> - 1.1.5-1
- new version build

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 05 2015 Pradeep Kilambi <pkilambi@redhat.com> 1.1.4
- initial package release

