%{?python_enable_dependency_generator}
%global pypi_name ldap3

Name:           python-%{pypi_name}
Version:        2.7
Release:        1%{?dist}
Summary:        Strictly RFC 4511 conforming LDAP V3 pure Python client

License:        LGPLv2+
URL:            https://github.com/cannatag/ldap3
Source0:        %{pypi_source}
Patch0002:      0002-unbundle-ordereddict.patch

BuildArch:      noarch

%global _description \
ldap3 is a strictly RFC 4510 conforming LDAP V3 pure Python client library.

%description %{_description}

%package     -n python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description -n python%{python3_pkgversion}-%{pypi_name} %{_description}

Python 3 version.

%prep
%autosetup -n %{pypi_name}-%{version} -p1

# remove bundled ordereddict
rm -vf %{pypi_name}/utils/ordDict.py

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%license COPYING.LESSER.txt
%doc README.rst
%{python3_sitelib}/%{pypi_name}-*.egg-info/
%{python3_sitelib}/%{pypi_name}/

%changelog
* Sat Jun 20 2020 Avram Lubkin <aviso@rockhopper.net> - 2.7-1
- Update to 2.7

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.6.1-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 20 2019 Miro Hrončok <mhroncok@redhat.com> - 2.6.1-2
- Subpackage python2-ldap3 has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Tue Oct 08 2019 Avram Lubkin <aviso@rockhopper.net> - 2.6.1-1
- Update to 2.6.1

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.5.1-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.5.1-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 09 2019 Miro Hrončok <mhroncok@redhat.com> - 2.5.1-7
- Readd pythno2-ldap3 (#1672052)

* Mon Feb 25 2019 Miro Hrončok <mhroncok@redhat.com> - 2.5.1-6
- Subpackage python2-ldap3 has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 26 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.5.1-4
- Enable python dependency generator

* Mon Dec 17 2018 Avram Lubkin <aviso@rockhopper.net> - 2.5.1-3
- Fix El6 requirements

* Sun Dec 16 2018 Avram Lubkin <aviso@rockhopper.net> - 2.5.1-2
- python-backports-ssl_match_hostname only required for Python 2.6

* Mon Nov 12 2018 Avram Lubkin <aviso@rockhopper.net> - 2.5.1-1
- Update to 2.5.1
- Build Python 3 packages for EPEL

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.5-2
- Rebuilt for Python 3.7

* Mon Apr 16 2018 Michal Cyprian <mcyprian@redhat.com> - 2.5-1
- Update to 2.5

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Igor Gnatenko <ignatenko@redhat.com> - 2.4.1-1
- Update to 2.4.1

* Thu Nov 16 2017 Michal Cyprian <mcyprian@redhat.com> - 2.4-1
- Update to 2.4

* Tue Oct 24 2017 Michal Cyprian <mcyprian@redhat.com> - 2.3-3
- Remove no longer necessary unbundle-ssl patch
Resolves: rhbz#1494151

* Thu Sep 21 2017 Ralph Bean <rbean@redhat.com> - 2.3-2
- Fix patch to require correct backports package name on el7.

* Wed Sep 20 2017 Michal Cyprian <mcyprian@redhat.com> - 2.3-1
- Update to 2.3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 16 2017 Michal Cyprian <mcyprian@redhat.com> - 2.2.3-1
- Update to 2.2.3

* Sun Mar 19 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.2.2-1
- Update to 2.2.2

* Thu Feb 16 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.2.1-1
- Update to 2.2.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 18 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.2.0-1
- Update to 2.2.0

* Mon Jan 02 2017 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.1.1-1
- Update to 2.1.1
- Modernize spec

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.8.6-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8.6-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Michal Cyprian <mcyprian@redhat.com> - 0.9.8.6-3
- Replace macro define with global

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

 * Wed Jul 08 2015 Michal Cyprian <mcyprian@redhat.com> - 0.9.8.6-1
 - Initial release of RPM package
