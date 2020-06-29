%{?python_enable_dependency_generator}
%global srcname MutatorMath
# upstream is not consistent on uppercase usage
%global libname mutatorMath
%global pkgname mutatormath

Name:           python-%{pkgname}
Version:        3.0.1
Release:        1%{?dist}
Summary:        Python library for piecewise linear interpolation in multiple dimensions

License:        BSD
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://github.com/LettError/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
MutatorMath is a Python library for the calculation of piecewise linear
interpolations in n-dimensions with any number of masters. It was developed for
interpolating data related to fonts, but if can handle any arithmetic object.

%package -n python3-%{pkgname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pkgname}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-defcon
BuildRequires:  python3-fontMath
BuildRequires:  python3-fonttools

%description -n python3-%{pkgname}
MutatorMath is a Python library for the calculation of piecewise linear
interpolations in n-dimensions with any number of masters. It was developed for
interpolating data related to fonts, but if can handle any arithmetic object.


%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pkgname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{libname}
%{python3_sitelib}/%{srcname}-*.egg-info

%changelog
* Sun Jun 14 2020 Athos Ribeiro <athoscr@fedoraproject.org> - 3.0.1-1
- Update version

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.2-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.2-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.2-2
- Rebuilt for Python 3.8

* Sun Aug 04 2019 Athos Ribeiro <athoscr@fedoraproject.org> - 2.1.2-1
- Update version

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 04 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.0-6
- Enable python dependency generator

* Fri Jan 04 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-5
- Subpackage python2-mutatormath has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 13 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 2.1.0-1
- Update version

* Sat Oct 07 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 2.0.6-1
- Update version

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 13 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 2.0.4-1
- Update version

* Sun Mar 19 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 2.0.3-1
- Initial package
