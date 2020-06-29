%global srcname photutils

Name: python-%{srcname}
Version: 0.7.2
Release: 2%{?dist}
Summary: Astropy affiliated package for image photometry tasks
License: BSD

URL: http://photutils.readthedocs.org/en/latest/index.html
Source0: %{pypi_source}
# Patch astropy version in setup.cfg
# Automatic generator doesn't like *
# https://bugzilla.redhat.com/show_bug.cgi?id=1758141
Patch1: photutils-astropy-minversion.patch

BuildRequires: gcc
BuildRequires: python3-devel

%description
Photutils contains functions for:
 * estimating the background and background rms in astronomical images
 * detecting sources in astronomical images
 * estimating morphological parameters of those sources (e.g., 
    centroid and shape parameters)
 * performing aperture and PSF photometry


%package -n python3-%{srcname}
Summary: Astropy affiliated package for image photometry tasks

BuildRequires: python3-devel
BuildRequires: python3-Cython
BuildRequires: python3-numpy
BuildRequires: python3-astropy
BuildRequires: python3-astropy-helpers
# Optional
BuildRequires: python3-scipy
BuildRequires: python3-scikit-image
BuildRequires: python3-scikit-learn
BuildRequires: python3-matplotlib
# For tests
BuildRequires: python3-pytest
BuildRequires: python3-pytest-astropy
BuildRequires: python-pytest-astropy-header

%{?python_provide:%python_provide python3-%{srcname}}

Recommends: python3-scipy
Recommends: python3-scikit-image
Recommends: python3-scikit-learn
Recommends: python3-matplotlib

%description -n python3-%{srcname}
Photutils contains functions for:
 * estimating the background and background rms in astronomical images
 * detecting sources in astronomical images
 * estimating morphological parameters of those sources (e.g., 
    centroid and shape parameters)
 * performing aperture and PSF photometry

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install
# Remove some c files after install
find %{buildroot}/%{python3_sitearch}/ -name "*.c" -delete

%check
# Empty matplotlibrc
mkdir -p matplotlib
touch matplotlib/matplotlibrc
export XDG_CONFIG_HOME=`pwd`
# Avoid writing bad pyc files
export PYTHONDONTWRITEBYTECODE=1
export PYTEST_ADDOPTS="-v -p no:cacheprovider"
pushd %{buildroot}/%{python3_sitearch}
  py.test-%{python3_version} photutils
popd


%files -n python3-%{srcname}
%doc README.rst
%license LICENSE.rst
%{python3_sitearch}/%{srcname}-%{version}-py%{python3_version}.egg-info
%{python3_sitearch}/%{srcname}

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.2-2
- Rebuilt for Python 3.9

* Mon Mar 02 2020 Sergio Pascual <sergiopr@fedoraproject.com> - 0.7.2-1
- New upstream source (0.7.2)
- Patch astropy version in setup.cfg (bz#1758141)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 27 2019 Christian Dersch <lupinix@fedoraproject.org> - 0.7.1-1
- new version
- skip tests on s390x for now (endianess issue in numpy...)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 28 2019 Christian Dersch <lupinix@mailbox.org> - 0.6-1
- new version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 03 2018 Christian Dersch <lupinix@fedoraproject.org> - 0.5-1
- new version
- drop old patches
- re-enable tests

* Mon Oct 01 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4-8
- Remove python2 subpackage (#1632572)

* Sun Jul 15 2018 Christian Dersch <lupinix@fedoraproject.org> - 0.4-7
- BuildRequires: gcc

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Christian Dersch <lupinix@mailbox.org> - 0.4-5
- Fix FTBFS with Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4-4
- Rebuilt for Python 3.7

* Wed Feb 14 2018 Christian Dersch <lupinix@mailbox.org> - 0.4-3
- Added numpy 1.14 fix https://github.com/astropy/photutils/pull/639

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 13 2017 Sergio Pascual <sergiopr@fedoraproject.com> - 0.4-1
- New upstream (0.4)

* Tue Oct 10 2017 Christian Dersch <lupinix@mailbox.org> - 0.3.2-4
- Fixed tests

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Sergio Pascual <sergiopr@fedoraproject.com> - 0.3.2-1
- New upstream (0.3.2)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Sergio Pascual <sergiopr@fedoraproject.com> - 0.3-1
- New upstream (0.3)

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-3
- Rebuild for Python 3.6

* Sat Oct 15 2016 Peter Robinson <pbrobinson@fedoraproject.org> - 0.2.2-2
- rebuilt for matplotlib-2.0.0

* Wed Jul 27 2016 Sergio Pascual <sergiopr@fedoraproject.com> - 0.2.2-1
- New upstream (0.2.2)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 06 2016 Sergio Pascual <sergiopr@fedoraproject.com> - 0.2-1
- New upstream (0.2)

* Thu Nov 26 2015 Sergio Pascual <sergiopr@fedoraproject.com> - 0.1-6
- Using new macros
- Disable tests until 0.2 is released

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 28 2015 Sergio Pascual <sergiopr@fedoraproject.com> - 0.1-3
- Use license macro

* Mon Jan 26 2015 Sergio Pascual <sergiopr@fedoraproject.com> - 0.1-2
- Disable test due to a bug (reported upstream)

* Thu Jan 08 2015 Sergio Pascual <sergiopr@fedoraproject.com> - 0.1-1
- First upstream release

* Wed Feb 26 2014 Sergio Pascual <sergiopr@fedoraproject.com> - 0.0-0.1.20140226git37a77fe
- Initial spec file

