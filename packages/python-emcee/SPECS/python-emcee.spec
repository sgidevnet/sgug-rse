%global srcname emcee

%global common_description                                                   \
emcee is a stable, well tested Python implementation of the affine-invariant \
ensemble sampler for Markov chain Monte Carlo (MCMC) proposed by             \
Goodman & Weare (2010). The code is open source and has already been         \
used in several published projects in the Astrophysics literature.           

Name: python-%{srcname}
Version: 3.0.0
Release: 4%{?dist}
Summary: The Python ensemble sampling toolkit for affine-invariant MCMC
License: MIT

URL: http://dan.iel.fm/emcee/current/
Source0: %{pypi_source}
BuildRequires: python3-devel 
BuildArch: noarch

%{?python_provide:%python_provide python-%{srcname}}


%global _description\
%{common_description}

%description %_description

%package -n python3-%{srcname}
Summary: The Python ensemble sampling toolkit for affine-invariant MCMC
BuildRequires: python3-numpy
BuildRequires: python3-pytest python3-scipy python3-h5py
##Requires: python3-numpy

%description -n python3-%{srcname}
%{common_description}

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
# Avoid writing bad pyc files during testing
export PYTHONDONTWRITEBYTECODE=1
export PYTEST_ADDOPTS='-p no:cacheprovider'
pushd %{buildroot}/%{python3_sitelib}
   pytest-%{python3_version} -v emcee 
popd

 
%files -n python3-%{srcname}
%doc AUTHORS.rst HISTORY.rst README.rst 
%license LICENSE
%{python3_sitelib}/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Sergio Pascual <sergiopr@fedoraproject.org> - 3.0.0-2
- New upstream source (3.0.0)
- Enable tests in python 3.8
- Updated sources

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-18
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-17
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild


* Thu Jul 11 2019 Sergio Pascual <sergiopr@fedoraproject.org> - 2.2.1-15
- Do not run the tests on python 3.8 (bz #1705929)

* Thu Jul 11 2019 Sergio Pascual <sergiopr@fedoraproject.org> - 2.2.1-13
- Add patch to fix the faulty test "test_nan_lnprob"

* Wed Feb 13 2019 Sergio Pascual <sergiopr@fedoraproject.org> - 2.2.1-12
- Allow faillures in test suite

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 08 2018 Sergio Pascual <sergiopr@fedoraproject.org> - 2.2.1-10
- Drop python2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-8
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.2.1-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.1-5
- Python 2 binary package renamed to python2-emcee
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-2
- Rebuild for Python 3.6

* Wed Jul 27 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 2.2.1-1
- New upstream source (2.2.1)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jul 14 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 2.2.0-2
- Remove reference to patch in specfile

* Wed Jul 13 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 2.2.0-1
- New upstream source (2.2.0)
- Update pypi url
- Remove numpy 1.11 patch (upstream fixed it)

* Tue Mar 29 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 2.1.0-5
- Provide python2 package
- Fix problem with numpy 1.11

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 15 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 2.1.0-1
- Initial spec
