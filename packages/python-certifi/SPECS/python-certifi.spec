%global pypi_name certifi

Name:           python-%{pypi_name}
Version:        2020.4.5.1
Release:        1%{?dist}
Summary:        Python package for providing Mozilla's CA Bundle

License:        MPLv2.0
#https://www.mozilla.org/MPL/2.0/
URL:            http://certifi.io/en/latest/
Source0:        %pypi_source
Patch1:         certifi-2020.4.5.1-use-system-cert.patch

BuildArch:      noarch

# Require the system certificate bundle (/etc/pki/tls/certs/ca-bundle.crt)
BuildRequires: ca-certificates

%description
Certifi is a carefully curated collection of Root Certificates for validating
the trustworthiness of SSL certificates while verifying the identity of TLS
hosts. It has been extracted from the Requests project.

Please note that this Fedora package does not actually include a certificate
collection at all. It reads the system shared certificate trust collection
instead. For more details on this system, see the ca-certificates package.

%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
Requires:       ca-certificates

%description -n python%{python3_pkgversion}-%{pypi_name}
Certifi is a carefully curated collection of Root Certificates for validating
the trustworthiness of SSL certificates while verifying the identity of TLS
hosts. It has been extracted from the Requests project.

Please note that this Fedora package does not actually include a certificate
collection at all. It reads the system shared certificate trust collection
instead. For more details on this system, see the ca-certificates package.

This package provides the Python 3 certifi library.


%prep
%setup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Remove bundled Root Certificates collection
rm -rf certifi/*.pem
%patch1 -p1

#drop shebangs from python_sitearch
find %{_builddir}/%{pypi_name}-%{version} -name '*.py' \
    -exec sed -i '1{\@^#!/usr/bin/env python@d}' {} \;

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-*-py%{python3_version}.egg-info/

%changelog
* Thu Jun 04 2020 Miro Hrončok <mhroncok@redhat.com> - 2020.4.5.1-1
- Update to 2020.4.5.1 (#1843713)

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 2018.10.15-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018.10.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Miro Hrončok <mhroncok@redhat.com> - 2018.10.15-8
- Remove Python 2 subpackage (#1770744)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2018.10.15-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 2018.10.15-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.10.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.10.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018  <jdennis@redhat.com> - 2018.10.15-3
- Resolves: rhbz#1659132 Incorrect location used for system certs
  where() now returns /etc/pki/tls/certs/ca-bundle.crt

* Fri Nov 02 2018 William Moreno Reyes <williamjmorenor@gmail.com> - 2018.10.15-2
- Update spec to use %%pypi_source macro

* Tue Oct 23 2018 William Moreno Reyes <williamjmorenor@gmail.com> - 2018.10.15-1
- Update to release: 2018.10.15
- Update patch to point to system certificates

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2016.9.26-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2016.9.26-8
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2016.9.26-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 14 2017 williamjmorenor@gmail.com - 2016.9.26-6
- Fix path of .pem file
  Thanks to @carlwgeorge
  See: https://src.fedoraproject.org/rpms/python-certifi/pull-request/1

* Thu Oct 12 2017 williamjmorenor@gmail.com - 2016.9.26-5
- If fedora path to use current ca-certificates
- If epel7 follow proper file to .pem file

* Thu Oct 12 2017 Carl George <carl@george.computer> - 2016.9.26-4
- EPEL compatibility
- Include license
- Move ca-certificates requirement to subpackages

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.9.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.9.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 28 2016 Adam Williamson <awilliam@redhat.com> - 2016.9.26-1
- New release 2016.9.26

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2015.04.28-10
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2015.04.28-9
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2015.04.28-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2015.04.28-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Sep 16 2015 William Moreno Reyes <williamjmorenor at gmail.com> - 2015.04.28-6
- Update python macros
- Include subpackages for Python2 and Python3

* Thu Jul 09 2015 William Moreno Reyes <williamjmorenor at gmail.com> 
- 2015.04.28-5
- rebuilt

* Wed Jul 08 2015 William Moreno Reyes  <williamjmorenor at gmail.com> 
- 2015.04.28-4
- Initial Import of #1232433

* Mon Jul 06 2015 William Moreno Reyes <williamjmorenor at gmail.com> 
- 2015.04.28-3
- Remove shebang

* Thu Jul 02 2015 William Moreno Reyes <williamjmorenor at gmail.com> 
- 2015.04.28-2
- Remove bundle cacert.pem

* Tue Jun 16 2015 William Moreno Reyes <williamjmorenor at gmail.com> 
- 2015.04.28-1
- Initial packaging
