# what it's called on pypi
%global srcname txWS
# what it's imported as
%global libname txws
# name of egg info directory
%global eggname %{srcname}
# package name fragment
%global pkgname %{libname}

%bcond_without tests

Name:             python-%{pkgname}
Version:          0.9.1
Release:          21%{?dist}
Summary:          Twisted WebSockets wrapper

License:          MIT
URL:              https://github.com/MostAwesomeDude/txWS
# PyPI tarball doesn't have tests
Source0:          %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

# Downstream-only patch.  Make sure to update when the version changes!
Patch0:           0001-Drop-vcversioner.patch

# https://github.com/MostAwesomeDude/txWS/pull/34
Patch1:           python-txws-python39.patch

BuildArch:        noarch

%global common_description %{expand:
txWS (pronounced "Twisted WebSockets") is a small, short, simple library
for adding WebSockets server support to your favorite Twisted applications.}

%description %{common_description}

%package -n python3-%{pkgname}
Summary:          %{summary}
BuildRequires:    python3-devel
BuildRequires:    %{py3_dist setuptools}
%if %{with tests}
BuildRequires:    %{py3_dist Twisted six}
%endif
%{?python_provide:%python_provide python3-%{pkgname}}

%description -n python3-%{pkgname} %{common_description}

%prep
%autosetup -p1 -n %{srcname}-%{version}
rm -rf %{eggname}.egg-info

%build
%py3_build

%install
%py3_install

%check
%if %{with tests}
PYTHONPATH=$(pwd) trial-%{python3_version} tests
%endif

%files -n python3-%{pkgname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{libname}.py
%{python3_sitelib}/__pycache__/%{libname}.cpython-%{python3_version_nodots}*.py*
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info


%changelog
* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-21
- Rebuilt for Python 3.9

* Sun Apr 12 2020 Carl George <carl@george.computer> - 0.9.1-20
- Include LICENSE file
- Fix automatic dependency generation
- Add provides for python-txws
- Run test suite

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-18
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Wed Aug 28 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-17
- Subpackage python2-txws has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-16
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-12
- Rebuilt for Python 3.7

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.9.1-11
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.1-10
- Escape macros in %%changelog

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.9.1-9
- Python 2 binary package renamed to python2-txws
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jul 12 2016 Lumir Balhar <lbalhar@redhat.com> - 0.9.1-4
- Enabled Py3 support

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Aug 20 2014 Ralph Bean <rbean@redhat.com> - 0.9.1-1
- Latest upstream.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 08 2014 Ralph Bean <rbean@redhat.com> - 0.9-1
- Protocol fixes to help support users on chrome.
- Added a disabled python3 subpackage for the future.
- Modernized python2 macros.

* Tue Jan 28 2014 Ralph Bean <rbean@redhat.com> - 0.8-2
- Patch to drop vcversioner for building in koji.

* Tue Jan 28 2014 Ralph Bean <rbean@redhat.com> - 0.8-1
- Latest upstream.

* Tue Jan 14 2014 Ralph Bean <rbean@redhat.com> - 0.7.1-4
- Update deps to use more specific twisted subpackages.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 27 2012 Ralph Bean <rbean@redhat.com> 0.7.1-1
- Upstream release.
- Use %%{capname} macro.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 29 2012 Ralph Bean <rbean@redhat.com> 0.7-5
- Resolve merge conflict between rawhide and el6.

* Mon May 21 2012 Luke Macken <lmacken@redhat.com> 0.7-4
- Remove the Twisted dependency from the setup.py, since the RHEL package does
  not contain the necessary egg-info metadata.

* Mon Apr 09 2012 Ralph Bean <rbean@redhat.com> 0.7-3
- Removed defattr in %%files section.

* Mon Apr 09 2012 Ralph Bean <rbean@redhat.com> 0.7-2
- Fixed spelling error in the specfile description.

* Thu Apr 05 2012 Ralph Bean <rbean@redhat.com>  0.7-1
- initial package for Fedora
