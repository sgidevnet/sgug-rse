%global srcname booleanOperations
%global pkgname booleanoperations
# We disable tests due to missing python test dep fontPens
%global with_tests 0

Name:           python-%{pkgname}
Version:        0.9.0
Release:        3%{?dist}
Summary:        Boolean operations on paths

License:        MIT
URL:            https://pypi.org/project/%{srcname}
Source0:        https://github.com/typemytype/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
Boolean operations on paths based on a super fast polygon clipper library by
Angus Johnson.

%package -n python3-%{pkgname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pkgname}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-wheel
%if 0%{?with_tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-fonttools
BuildRequires:  python3-pyclipper
%endif

%description -n python3-%{pkgname}
Boolean operations on paths based on a super fast polygon clipper library by
Angus Johnson.


%prep
%autosetup -n %{srcname}-%{version}

%build
# Here we set upstream version based on setuptools_scm documentation
# this is done to avoid the following error:
# LookupError: setuptools-scm was unable to detect version
# since we are not importing a .git repository in the tarball
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%py3_build

%install
# Here we set upstream version based on setuptools_scm documentation
# this is done to avoid the following error:
# LookupError: setuptools-scm was unable to detect version
# since we are not importing a .git repository in the tarball
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%py3_install

%check
%if 0%{?with_tests}
# Here we set upstream version based on setuptools_scm documentation
# this is done to avoid the following error:
# LookupError: setuptools-scm was unable to detect version
# since we are not importing a .git repository in the tarball
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%{__python3} setup.py test
%endif

%files -n python3-%{pkgname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}-*.egg-info
%{python3_sitelib}/%{srcname}

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-3
- Rebuilt for Python 3.9

* Sun Mar 01 2020 Athos Ribeiro <athoscr@fedoraproject.org> - 0.9.0-2
- Remove BR on deprecated ufolib package

* Sun Mar 01 2020 Athos Ribeiro <athoscr@fedoraproject.org> - 0.9.0-1
- Update version
- Disable check section due to missing dependencies

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.8.0-4
- Subpackage python2-booleanoperations has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-2
- Rebuilt for Python 3.7

* Fri Feb 16 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 0.8.0-1
- Update version

* Mon Aug 14 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.7.1-1
- Update version
- Use lowecase string for package name

* Mon Apr 10 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.7.0-1
- Initial package
