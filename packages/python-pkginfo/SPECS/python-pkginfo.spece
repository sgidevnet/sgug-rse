%global pypi_name pkginfo

%global common_description %{expand:
This package provides an API for querying the distutils metadata written in the
PKG-INFO file inside a source distribution (an sdist) or a binary distribution
(e.g., created by running bdist_egg). It can also query the EGG-INFO directory
of an installed distribution, and the *.egg-info stored in a "development
checkout" (e.g, created by running setup.py develop).}

Name:           python-%{pypi_name}
Summary:        Query metadata from sdists / bdists / installed packages
Version:        1.5.0.1
Release:        5%{?dist}
License:        MIT

URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        %{pypi_source}

# don't ship internal test subpackage
Patch1:         0001-disable-test-sub-package.patch

# disable one broken test
Patch2:         0002-disable-a-broken-test.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(nose)
BuildRequires:  python3dist(sphinx)

%description %{common_description}


%package -n python3-%{pypi_name}
Summary:        Query metadata from sdists / bdists / installed packages
Requires:       python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %{common_description}


%package        doc
Summary:        Documentation for python-%{pypi_name}

%description    doc %{common_description}
This package contains the documentation.


%prep
%autosetup -n %{pypi_name}-%{version} -p1

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
%py3_build

# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html

# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%py3_install


%check
%{__python3} setup.py test


%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.txt CHANGES.txt

%{_bindir}/pkginfo

%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%files -n python-%{pypi_name}-doc
%license LICENSE.txt
%doc html


%changelog
* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.0.1-5
- Revert previous changes

* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.0.1-4
- Add python3-setuptools as BR

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.0.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 24 2019 Fabio Valentini <decathorpe@gmail.com> - 1.5.0.1-1
- Update to version 1.5.0.1.

* Mon Sep 23 2019 Fabio Valentini <decathorpe@gmail.com> - 1.4.2-7
- Drop python2-pkginfo and versioned symlinks for the binary.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-2
- Rebuilt for Python 3.7

* Sat Mar 24 2018 Jeremy Cline <jeremy@jcline.org> - 1.4.2-1
- Update to latest upstream
- License change to MIT

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.3.2-4
- Rebuild for Python 3.6

* Wed Jul 20 2016 Jeremy Cline <jeremy@jcline.org> - 1.3.2-3
- Remove hard-coded Python y release versions in /usr/bin entries

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jun 09 2016 Jeremy Cline <jeremy@jcline.org> - 1.3.2-1
- Initial commit

