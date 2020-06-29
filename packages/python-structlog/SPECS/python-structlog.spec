%global srcname structlog
%global sum Painless structural logging

Name:           python-%{srcname}
Version:        19.2.0
Release:        3%{?dist}
Summary:        %{sum}

License:        ASL 2.0 and MIT
URL:            http://www.structlog.org/
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-twisted
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-freezegun
BuildRequires:  python%{python3_pkgversion}-pretend
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools

%if 0%{?with_python3_other}
BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  python%{python3_other_pkgversion}-freezegun
BuildRequires:  python%{python3_other_pkgversion}-pretend
BuildRequires:  python%{python3_other_pkgversion}-pytest
BuildRequires:  python%{python3_other_pkgversion}-setuptools
%endif


%description
Structlog makes structured logging in Python easy by augmenting your existing 
logger. It allows you to split your log entries up into key/value pairs and 
build them incrementally without annoying boilerplate code.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Painless structural logging
License:        ASL 2.0 and MIT
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}


%description -n python%{python3_pkgversion}-%{srcname}
Structlog makes structured logging in Python easy by augmenting your existing 
logger. It allows you to split your log entries up into key/value pairs and 
build them incrementally without annoying boilerplate code.


%if 0%{?with_python3_other}
%package -n python%{python3_other_pkgversion}-%{srcname}
Summary:        Painless structural logging
License:        ASL 2.0 and MIT
%{?python_provide:%python_provide python%{python3_other_pkgversion}-%{srcname}}


%description -n python%{python3_other_pkgversion}-%{srcname}
Structlog makes structured logging in Python easy by augmenting your existing 
logger. It allows you to split your log entries up into key/value pairs and 
build them incrementally without annoying boilerplate code.
%endif


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py3_build
%if 0%{?with_python3_other}
%py3_other_build
%endif


%install
%if 0%{?with_python3_other}
%py3_other_install
%endif
%py3_install


%check
pushd src
%{__python3} -m pytest ../tests
popd


%files -n python%{python3_pkgversion}-%{srcname}
%doc AUTHORS.rst CHANGELOG.rst README.rst PKG-INFO docs/*.rst docs/code_examples
%license LICENSE LICENSE.mit LICENSE.apache2
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py3.?.egg-info


%if 0%{?with_python3_other}
%files -n python%{python3_other_pkgversion}-%{srcname}
%doc AUTHORS.rst CHANGELOG.rst README.rst PKG-INFO docs/*.rst docs/code_examples
%license LICENSE LICENSE.mit LICENSE.apache2
%{python3_other_sitelib}/%{srcname}
%{python3_other_sitelib}/%{srcname}-%{version}-py3.?.egg-info
%endif


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 19.2.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Piotr Popieluch <piotr1212@gmail.com> - 19.2.0-1
- Update to 19.2.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 19.1.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 02 2019 Piotr Popieluch <piotr1212@gmail.com> - 19.1.0-1
- Update to 19.1.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 27 2018 Piotr Popieluch <piotr1212@gmail.com> - 18.2.0-2
- Remove Python2 subpackage

* Thu Sep 27 2018 Piotr Popieluch <piotr1212@gmail.com> - 18.2.0-1
- Update to 18.2.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 20 2018 Piotr Popieluch <piotr1212@gmail.com> - 18.1.0-1
- Update to 18.1.0

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 17.2.0-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Iryna Shcherbina <ishcherb@redhat.com> - 17.2.0-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Tue Oct 17 2017 Piotr Popieluch <piotr1212@gmail.com> - 17.2.0-1
- Update to 17.2.0
- Add MIT license
- Add EPEL 7 Python 3 package
- Remove EPEL 6 support

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 15.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Piotr Popieluch <piotr1212@gmail.com> - 15.2.0-7
- Update to new package guidelines

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 15.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 15.2.0-5
- Rebuild for Python 3.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 15.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Nov 06 2015 Piotr Popieluch <piotr1212@gmail.com> - 15.2.0-2
- Rebuilt for python 3.5

* Fri Jul 03 2015 Piotr Popieluch <piotr1212@gmail.com> - 15.2.0-1
- Update to 15.2.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Dec  4 2014 Piotr Popieluch <piotr1212@gmail.com> - 0.4.2-5
- disabled tests on epel

* Sat Nov 22 2014 Piotr Popieluch <piotr1212@gmail.com> - 0.4.2-4
- added epel support

* Tue Oct 28 2014 Piotr Popieluch <piotr1212@gmail.com> - 0.4.2-3
- Removed group
- Removed shipped .egg-info
- Added license to python3 package
- Made %%files section more verbose
- Replaced %%{python_sitelib} with %%{python2_sitelib}

* Mon Oct 20 2014 Piotr Popieluch <piotr1212@gmail.com> - 0.4.2-2
- Added python3 package
- Added %%check section

* Sat Oct 11 2014 Piotr Popieluch <piotr1212@gmail.com> - 0.4.2-1
- Initial package

