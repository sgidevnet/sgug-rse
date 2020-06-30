%global pypi_name XStatic

Name:           python-%{pypi_name}
Version:        1.0.1
Release:        21%{?dist}
Summary:        XStatic base package with minimal support code

License:        MIT
URL:            http://bitbucket.org/thomaswaldmann/xstatic
Source0:        https://pypi.python.org/packages/source/X/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
The goal of XStatic family of packages is to provide static
file packages with minimal overhead - without selling you some 
dependencies you don't want.

XStatic has some minimal support code for working with the
XStatic-* packages.


%package -n python3-%{pypi_name}
Summary:       XStatic base package with minimal support code
BuildRequires: python3-devel
BuildRequires: python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}

The goal of XStatic family of packages is to provide static
file packages with minimal overhead - without selling you some
dependencies you don't want.

XStatic has some minimal support code for working with the
XStatic-* packages.


%prep
%autosetup -n %{pypi_name}-%{version}


%build
%py3_build


%install
%py3_install
mkdir %{buildroot}/%{python3_sitelib}/xstatic/pkg


%files -n python3-%{pypi_name}
%doc README.txt
%{python3_sitelib}/xstatic
%{python3_sitelib}/XStatic-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/XStatic-%{version}-py%{python3_version}-nspkg.pth


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-21
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-19
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-18
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 03 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-15
- Subpackage python2-XStatic has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-13
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.1-12
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-8
- Rebuild for Python 3.6

* Wed Aug 31 2016 Matthias Runge <mrunge@redhat.com> - 1.0.1-7
- provide python/python2
- spec cleanup

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Oct 10 2014 Matthias Runge <mrunge@redhat.com> - 1.0.1-2
- include xstatic/pkg

* Tue Jul 08 2014 Matthias Runge <mrunge@redhat.com> - 1.0.1-1
- Initial package.
