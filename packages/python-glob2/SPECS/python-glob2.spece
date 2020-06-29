%global desc Version of the glob module that can capture patterns and supports recursive\
wildcards.
%global pkg_name glob2
%global pypi_version 0.7

Name:           python-%{pkg_name}
Version:        0.7
Release:        6%{?dist}
Summary:        Glob module recursive wildcards support

License:        BSD
URL:            https://pypi.python.org/pypi/%{pkg_name}
Source0:        https://files.pythonhosted.org/packages/d7/a5/bbbc3b74a94fbdbd7915e7ad030f16539bfdc1362f7e9003b594f0537950/glob2-0.7.tar.gz

BuildArch:      noarch

%description
%{desc}


%package -n     python3-%{pkg_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose
Requires:       python3-setuptools
%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
%{desc}

%prep
%setup -q -n %{pkg_name}-%{pypi_version}


%build
%py3_build


%install
%py3_install


%check
PYTHONPATH=build/lib %{__python3} -m unittest discover


%files -n python3-%{pkg_name}
%license LICENSE
%doc README.rst CHANGES
%{python3_sitelib}/%{pkg_name}-%{pypi_version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pkg_name}/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 13 2019 Julien Enselme <jujens@jujens.eu> - 0.7-1
- Update to 0.7

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 02 2018 Julien Enselme <jujens@jujens.eu> - 0.6.0-6
- Remove Python 2 subpackage (#1627336)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.6.0-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Julien Enselme <jujens@jujens.eu> - 0.6.0-1
- Update to 0.6.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-2
- Rebuild for Python 3.6

* Tue Nov 08 2016 Julien Enselme <jujens@jujens.eu> - 0.5.0-1
- Update to 0.5.0
- Update spec to new guidelines

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 5 2015 Julien Enselme <jujens@jujens.eu> - 0.4.1-4
- Rebuilt for python 3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 26 2015 Julien Enselme <jujens@jujens.eu> - 0.4.1.2
- Correct the source of the LICENSE

* Mon Jan 05 2015 Julien Enselme <jujens@jujens.eu> - 0.4.1-1
- Initial packaging
