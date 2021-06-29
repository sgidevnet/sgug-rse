# Created by pyp2rpm-0.5.1
%global pypi_name spec2scl

Name:           %{pypi_name}
Version:        1.2.1
Release:        6%{?dist}
Summary:        Convert RPM specfiles to be SCL ready

License:        MIT
URL:            https://github.com/sclorg/spec2scl
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%if 0%{?fedora}
BuildRequires:  python3-flexmock
BuildRequires:  python3-jinja2
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-runner
%endif

Requires:       python3-setuptools
Requires:       python3-jinja2

%description
spec2scl is a tool to convert RPM specfiles to SCL-style specfiles.


%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install
install -D -m 644 spec2scl.1 %{buildroot}%{_mandir}/man1/spec2scl.1

%check
%if 0%{?fedora}
PYTHONPATH=$(pwd) py.test-%{python3_version}
%endif

%files
%doc README.rst
%license LICENSE
%{_bindir}/%{pypi_name}
%{_mandir}/man1/spec2scl.1*
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 21 2017 Iryna Shcherbina <ishcherb@redhat.com> - 1.2.1-1
- Update to 1.2.1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 12 2017 Iryna Shcherbina <ishcherb@redhat.com> - 1.2.0-2
- Use 1.2.0 as release version

* Wed Apr 12 2017 Iryna Shcherbina <ishcherb@redhat.com> - 1.2-1
- Update to 1.2

* Thu Feb 16 2017 Iryna Shcherbina <ishcherb@redhat.com> - 1.1.4-1
- Update to 1.1.4

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Jun 29 2015 Slavek Kabrda <bkabrda@redhat.com> - 1.1.3-1
- Update to 1.1.3

* Mon Jun 22 2015 Slavek Kabrda <bkabrda@redhat.com> - 1.1.1-1
- Update to 1.1.1
- Run spec2scl on Python 3

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0a-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Robert Kuska <rkuska@redhat.com> - 1.1.0a-1
- Update to 1.1.0a

* Mon Apr 28 2014 Robert Kuska <rkuska@redhat.com> - 1.1.0-1
- Update to 1.1.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 26 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1.0.1-1
- Update to 1.0.1.

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 07 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 0.3.4-1
- Update to 0.3.4.

* Wed Dec 19 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.3.3-1
- Update to 0.3.3.

* Thu Nov 08 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.3.2-1
- Update to 0.3.2.
- Add the missing Requires: python-setuptools.

* Fri Sep 21 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.3.1-2
- Disable tests on el6 (no pytest).

* Tue Sep 18 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.3.1-1
- Initial package.
