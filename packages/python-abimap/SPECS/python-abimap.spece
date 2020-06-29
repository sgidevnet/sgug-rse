%global module_name abimap

Name:           python-%{module_name}
Version:        0.3.2
Release:        5%{?dist}
License:        MIT
Summary:        A helper for library maintainers to use symbol versioning
Url:            https://github.com/ansasaki/abimap

Source:         https://files.pythonhosted.org/packages/source/a/%{module_name}/%{module_name}-%{version}.tar.gz

# This patch disables the test which depends on pytest-console-scripts
Patch0:         python-abimap-0.3.0-disable-script-test.patch
# This patch removes sphinx napoleon extension
Patch1:         python-abimap-0.3.1-remove-docs-napoleon.patch
# This patch removes sphinx rtd theme
Patch2:         python-abimap-0.3.1-remove-docs-rtd-theme.patch

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
# Required for testing
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-pytest-runner
BuildRequires:  python%{python3_pkgversion}-pytest-cov
# Not available yet, will be required once it is available in Fedora
# BuildRequires:  %%{py3_dist pytest-console-scripts}

%if 0%{?el7}
BuildRequires:  python%{python3_pkgversion}-yaml
# Required for documentation
BuildRequires:  python-sphinx
%else
BuildRequires:  python%{python3_pkgversion}-pyyaml
# Required for documentation
BuildRequires:  python%{python3_pkgversion}-sphinx
%endif

Requires:       setuptools

%description
This script allows to generate and update symbol version linker scripts which
adds version information to the exported symbols. The script is intended to be
integrated as part of a shared library build to check for changes in the set
of exported symbols and update the symbol version linker script accordingly.

%package -n python%{python3_pkgversion}-%{module_name}
Summary:        A helper for library maintainers to use symbol versioning
%{?python_provide:%python_provide python%{python3_pkgversion}-%{module_name}}

%description -n python%{python3_pkgversion}-%{module_name}
This script allows to generate and update symbol version linker scripts which
adds version information to the exported symbols. The script is intended to be
integrated as part of a shared library build to check for changes in the set
of exported symbols and update the symbol version linker script accordingly.

%package -n python-%{module_name}-doc
Summary:        Documentation for python-%{module_name}
%description -n python-%{module_name}-doc
Documentation for python-%{module_name}

%prep
%autosetup -n %{module_name}-%{version} -p1
# Remove bundled egg-info
rm -rf %{module_name}.egg-info

%build
%py3_build
%if 0%{?el7}
# Generate html docs
PYTHONPATH=${PWD}/src:${PWD}/tests \
    sphinx-build -E -b html docs html
# Generate manpage
PYTHONPATH=${PWD}/src:${PWD}/tests \
    sphinx-build -E -b man docs man
# Remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%else
# Generate html docs
PYTHONPATH=${PWD}/src:${PWD}/tests \
    sphinx-build-3 -E -b html docs html
# Generate manpage
PYTHONPATH=${PWD}/src:${PWD}/tests \
    sphinx-build-3 -E -b man docs man
# Remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%py3_install
# Install man page
mkdir -p %{buildroot}%{_mandir}/man1
install ${PWD}/man/abimap.1 %{buildroot}%{_mandir}/man1/abimap.1

%check
# Generate test data (copied bootstrap-tests from Makefile)
make -C tests ABIMAP_NAME_VERSION="abimap-%{version}" ABIMAP_VERSION="%{version}"
# Run the tests using py.test
PYTHONPATH=%{buildroot}%{python3_sitelib}:$PWD/tests \
    py.test-%{python3_version} -vv tests

%files -n python%{python3_pkgversion}-%{module_name}
%license LICENSE
%doc AUTHORS.rst CHANGELOG.rst README.rst
%{_bindir}/abimap
%dir %{python3_sitelib}/abimap
%{python3_sitelib}/abimap/*
%{python3_sitelib}/abimap-%{version}-py%{python3_version}.egg-info
%{_mandir}/man1/abimap.1*

%files -n python-%{module_name}-doc
%license LICENSE
%doc html

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-2
- Rebuilt for Python 3.8

* Mon Aug 05 2019 Anderson Sasaki <ansasaki@redhat.com> - 0.3.2-1
- Update to upstream version 0.3.2
- Fixed broken builds due to changes in warning output
- Changed tests to check error messages
- Added python 3.7 to testing matrix
- Added requirement to verify SNI when checking URLs in docs

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 27 2018 Anderson Sasaki <ansasaki@redhat.com> - 0.3.1-2
- Make the specfile compatible with EPEL7
- Fixed incompatible macros
- Fixed patch to skip a test in older pytest versions
- Added patches to remove sphinx extensions not available in EPEL7

* Mon Aug 20 2018 Anderson Sasaki <ansasaki@redhat.com> - 0.3.1-1
- Rebased to version 0.3.1
- argparse-manpage is no longer required since manpage is generated by sphinx

* Wed Aug 08 2018 Anderson Sasaki <ansasaki@redhat.com> - 0.3.0-2
- Added Requires for setuptools
- Addressed a bug in the order of releases in output map

* Mon Aug 06 2018 Anderson Sasaki <ansasaki@redhat.com> - 0.3.0-1
- Initial package.
