%{?python_enable_dependency_generator}
%global srcname defcon

# Skip tests due to missing python fontPens test requirement
%global with_check 0

Name:           python-%{srcname}
Version:        0.7.2
Release:        1%{?dist}
Summary:        A set of flexible objects for representing UFO data

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://github.com/typesupply/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
Defcon is a set of UFO (Unified Font Object) based objects optimized for use in
font editing applications. Defcon implements UFO3 as described by the UFO font
format.

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if 0%{?with_check}
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-fonttools
%endif

%description -n python3-%{srcname}
Defcon is a set of UFO (Unified Font Object) based objects optimized for use in
font editing applications. Defcon implements UFO3 as described by the UFO font
format.


%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%if 0%{?with_check}
%{__python3} setup.py test
%endif

%files -n python3-%{srcname}
%license License.txt
%doc README.rst
%{python3_sitelib}/%{srcname}-*.egg-info
%{python3_sitelib}/%{srcname}

%changelog
* Sun Jun 14 2020 Athos Ribeiro <athoscr@fedoraproject.org> - 0.7.2-1
- Update version

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-2
- Rebuilt for Python 3.9

* Sun Mar 01 2020 Athos Ribeiro <athoscr@fedoraproject.org> - 0.6.0-1
- Update version
- Skip tests due to missing dependency

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.1-5
- Enable python dependency generator

* Mon Jan 14 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-4
- Subpackage python2-defcon has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-2
- Rebuilt for Python 3.7

* Tue Apr 10 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 0.5.1-1
- Update version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 7 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.3.5-1
- Update version

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 7 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.3.4-1
- Update version

* Wed May 24 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.3.3-1
- Update version

* Mon Apr 3 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.3.2-1
- Update version

* Sun Mar 19 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.2.5-3
- Depends on the lowercase version of ufolib

* Sun Mar 19 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.2.5-2
- Improve %%description
- Remove the sum global

* Sat Mar 18 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.2.5-1
- Initial package
