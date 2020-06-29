%{?python_enable_dependency_generator}
%global srcname spur
%global sum Run commands locally or over SSH using the same interface
%global desc Run commands and manipulate files locally or over SSH using the same interface.

Name:           python-%{srcname}
Version:        0.3.21
Release:        7%{?dist}
Summary:        %{sum}

License:        BSD
URL:            https://github.com/mwilliamson/spur.py
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
Patch0:         python-spur-encode.patch
BuildArch:      noarch

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{sum}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose
BuildRequires:  (python3dist(paramiko) >= 1.13.1 with python3dist(paramiko) < 3)
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}


%prep
%setup -q -n %{srcname}.py-%{version}
%patch0 -p1 -b .encode
sed -i -e "s/’/'/g" README.rst


%build
%py3_build


%install
%py3_install


%check
# Tests which require SSH server
# Some tests are failing with python 3.8
# https://github.com/mwilliamson/spur.py/issues/85
nosetests-%{python3_version} -v -e testing -e ssh_tests -e local_tests


%files -n python3-%{srcname}
%license LICENSE
%doc CHANGES CONTRIBUTING.rst README.rst
%{python3_sitelib}/%{srcname}*


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.21-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.21-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 22 2019 Orion Poplawski <orion@nwra.com> - 0.3.21-4
- Exclude failing tests (bugz#1705954)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.21-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 21 2019 Orion Poplawski <orion@nwra.com> - 0.3.21-1
- Update to 0.3.21

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 30 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.20-1
- Update to 0.3.20

* Thu Dec 27 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.17-10
- Subpackage python2-spur has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.3.17-9
- Use C.UTF-8 locale
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.17-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.17-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.3.17-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3.17-2
- Rebuild for Python 3.6

* Fri Apr 29 2016 Orion Poplawski <orion@cora.nwra.com> - 0.3.17-1
- Update to 0.3.17

* Mon Apr 25 2016 Orion Poplawski <orion@cora.nwra.com> - 0.3.16-1
- Update to 0.3.16

* Tue Apr 5 2016 Orion Poplawski <orion@cora.nwra.com> - 0.3.15-1
- Initial package
