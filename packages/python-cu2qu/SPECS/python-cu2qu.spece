%global srcname cu2qu

Name:           python-%{srcname}
Version:        1.6.7
Release:        1%{?dist}
Summary:        Cubic-to-quadratic bezier curve conversion

License:        ASL 2.0
URL:            https://pypi.org/project/%{srcname}
Source0:        https://github.com/googlei18n/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz

%description
This library provides functions which take in UFO (Unified Font Object) objects
(Defcon Fonts or Robofab RFonts) and converts any cubic curves to quadratic.

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-defcon
BuildRequires:  python3-fonttools

%description -n python3-%{srcname}
This library provides functions which take in UFO (Unified Font Object) objects
(Defcon Fonts or Robofab RFonts) and converts any cubic curves to quadratic.


%prep
%autosetup -n %{srcname}-%{version}

%build
# Here we set upstream version based on setuptools_scm documentation
# this is done to avoid the following error:
# LookupError: setuptools-scm was unable to detect version
# since we are not importing a .git repository in the tarball
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
export CU2QU_WITH_CYTHON=1
%py3_build

%install
# Here we set upstream version based on setuptools_scm documentation
# this is done to avoid the following error:
# LookupError: setuptools-scm was unable to detect version
# since we are not importing a .git repository in the tarball
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%py3_install

%check
# Here we set upstream version based on setuptools_scm documentation
# this is done to avoid the following error:
# LookupError: setuptools-scm was unable to detect version
# since we are not importing a .git repository in the tarball
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

# Remove warning supression due to missing depenency
sed -i -e '/filterwarnings:/d' -e '/^\s*ignore:\.\*bytes:DeprecationWarning:fs\.base/d' setup.cfg

%{__python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst CONTRIBUTING.md
%dir %{python3_sitearch}/%{srcname}
%exclude %{python3_sitearch}/%{srcname}/*.c
%{python3_sitearch}/%{srcname}-*.egg-info
%{python3_sitearch}/%{srcname}/*.py
%{python3_sitearch}/%{srcname}/*.so
%{python3_sitearch}/%{srcname}/__pycache__
%{_bindir}/%{srcname}

%changelog
* Sun Jun 14 2020 Athos Ribeiro <athoscr@fedoraproject.org> - 1.6.7-1
- Ship cu2qu binary
- Make package arch specific

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-11
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.5.0-5
- Subpackage python2-cu2qu has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-3
- Rebuilt for Python 3.7

* Wed Apr 11 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 1.5.0-2
- Ship cu2qu binary

* Wed Apr 11 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 1.5.0-1
- Update version

* Wed Feb 21 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 1.4.0-3
- Remove test file from package

* Wed Feb 21 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 1.4.0-2
- Add python-defcon to BRs

* Wed Feb 21 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 1.4.0-1
- Update version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 24 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 1.2.0-1
- Update version

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 19 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 1.1.1-1
- Initial package
