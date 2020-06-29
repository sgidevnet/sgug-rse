%global pypi_name lockfile

%global common_description %{expand:
The lockfile module exports a FileLock class which provides a simple API for
locking files. Unlike the Windows msvcrt.locking function, the Unix
fcntl.flock, fcntl.lockf and the deprecated posixfile module, the API is
identical across both Unix (including Linux and Mac) and Windows platforms. The
lock mechanism relies on the atomic nature of the link (on Unix) and mkdir (on
Windows) system calls.}

Name:           python-%{pypi_name}
Summary:        Platform-independent file locking module
Epoch:          1
Version:        0.11.0
Release:        18%{?dist}
License:        MIT

URL:            https://github.com/openstack/pylockfile
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel

BuildRequires:  python3dist(nose)
BuildRequires:  python3dist(pbr) >= 1.8
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%description %{common_description}


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %{common_description}


%package -n     python-%{pypi_name}-doc
Summary:        lockfile documentation
%description -n python-%{pypi_name}-doc
Documentation for lockfile


%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# pbr isn't needed at runtime:
# https://bugs.launchpad.net/pylockfile/+bug/1506679
sed -i '/pbr/d' requirements.txt


%build
%py3_build

# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 doc/source html

# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%py3_install


%check
PYTHONPATH=$(pwd) nosetests-3


%files -n python3-%{pypi_name}
%license LICENSE
%doc ACKS AUTHORS ChangeLog README.rst RELEASE-NOTES

%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE


%changelog
* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 1:0.11.0-18
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.11.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 03 2019 Fabio Valentini <decathorpe@gmail.com> - 1:0.11.0-16
- Drop python2 sub-package. See:
  https://fedoraproject.org/wiki/Changes/F31_Mass_Python_2_Package_Removal
- Refresh packaging for 2019, move docs to a sub-package.

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 1:0.11.0-15
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.11.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.11.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.11.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 1:0.11.0-11
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.11.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1:0.11.0-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1:0.11.0-8
- Python 2 binary package renamed to python2-lockfile
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.11.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.11.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1:0.11.0-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.11.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 18 2015 Slavek Kabrda <bkabrda@redhat.com> - 1:0.11.0-2
- Remove runtime dependency on pbr
Resolves: rhbz#1282571

* Fri Nov 13 2015 Slavek Kabrda <bkabrda@redhat.com> - 1:0.11.0-1
- Update to 0.11.0

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Dec 09 2014 Slavek Kabrda <bkabrda@redhat.com> - 1:0.10.2-1
- Update to 0.10.2
- Drop patches merged upstream
- Update URL and Source to point to new upstream

* Fri Jun 20 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1:0.9.1-8
- Properly list files for python3-lockfile subpackage.

* Fri Jun 20 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1:0.9.1-7
- Added python3-lockfile subpackage.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jul 24 2011 Silas Sewell <silas@sewell.org> - 1:0.9.1-1
- Update to 0.9.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 03 2010 Silas Sewell <silas@sewell.ch> - 1:0.8-1
- Update to 0.8, increase epoch

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Jul 06 2010 Silas Sewell <silas@sewell.ch> - 0.9-1
- Update to 0.9

* Tue Jul 06 2010 Silas Sewell <silas@sewell.ch> - 0.8-2
- Bump for EL6 build

* Thu Jul 23 2009 Silas Sewell <silas@sewell.ch> - 0.8-1
- Initial build
