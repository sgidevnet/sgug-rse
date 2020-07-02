%global srcname portalocker

Name:           python-%{srcname}
Version:        1.5.0
Release:        5%{?dist}
Summary:        Library to provide an easy API to file locking

License:        Python
URL:            https://github.com/WoLpH/portalocker
Source:         %{pypi_source}

BuildArch:      noarch

%description
%{summary}.

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{srcname}
%{summary}.

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version}
rm -vr *.egg-info %{srcname}_tests

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-2
- Rebuilt for Python 3.8

* Sun Aug 04 14:43:25 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.5.0-1
- Update to 1.5.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 02 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-3
- Subpackage python2-portalocker has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-6
- Rebuilt for Python 3.7

* Mon Mar 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.1-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 18 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.0.1-1
- Update to 1.0.1

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.6.1-2
- Rebuild for Python 3.6

* Tue Sep 06 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.6.1-1
- Update to 0.6.1

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.6-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jun 16 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.5.6-1
- Update to 0.5.6
- Add doc subpkg

* Sun Dec 06 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.5.4-1.gitb0de666
- Initial package
