%global modname ujson
%global srcname ultrajson

Name:           python-%{modname}
Version:        3.0.0
Release:        1%{?dist}
Summary:        Ultra fast JSON encoder and decoder written in pure C

License:        BSD
URL:            https://github.com/ultrajson/ultrajson
Source:         %{pypi_source %{modname}}

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  double-conversion-devel

%patchlist
0001-Use-double-conversion-from-the-system.patch

%global _description \
UltraJSON is an ultra fast JSON encoder and decoder written in\
pure C with bindings for Python.

%description %{_description}

%package -n python3-%{modname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(pytest)
%{?python_provide:%python_provide python3-%{modname}}

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
%autosetup -n %{modname}-%{version} -p1
rm -vrf deps

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitearch} %python3 -m pytest -v

%files -n python3-%{modname}
%license LICENSE.txt
%doc README.rst
%{python3_sitearch}/%{modname}-%{version}-py%{python3_version}.egg-info/
%{python3_sitearch}/%{modname}*.so

%changelog
* Sun Jun 07 2020 Kushal Das <kushal@fedoraproject.org> 3.0.0-1
- Update to 3.0.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.3-2
- Rebuilt for Python 3.9

* Tue May 12 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.0.3-1
- Update to 2.0.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.3.20170206git2f1d487
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0-0.2.20170206git2f1d487
- Subpackage python2-ujson has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0-0.1.20170206git2f1d487.9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.1.20170206git2f1d487.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.1.20170206git2f1d487.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.1.20170206git2f1d487.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0-0.1.20170206git2f1d487.5
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.0-0.1.20170206git2f1d487.4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.1.20170206git2f1d487.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.1.20170206git2f1d487.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.1.20170206git2f1d487.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Adam Williamson <awilliam@redhat.com> - 2.0-0.1.20170206git2f1d487
- Update to pre-2.0 git snapshot, removes non-standard serialization behaviour

* Sun Jan 01 2017 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.35-1
- Update to 1.35
- Run test suite
- Spec cleanups

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.33-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.33-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 06 2015 Robert Kuska <rkuska@redhat.com> - 1.33-2
- Rebuilt for Python3.5 rebuild

* Sat Aug 1 2015 Julien Enselme <jujens@jujens.eu> - 1.33-1
- Update to 1.33
- Enable python3 subpackage
- Update SPEC to match packaging guidelines

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Dec 19 2012 Kushal Das <kushal@fedoraproject.org> 1.23-1
- Intial package
