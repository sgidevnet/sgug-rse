%{?python_enable_dependency_generator}
%global srcname matrix-synapse-ldap3
%global desc Allows synapse to use LDAP as a password provider.

Name:           python-%{srcname}
Version:        0.1.4
Release:        2%{?dist}
Summary:        Allows synapse to use LDAP as a password provider

License:        ASL 2.0
URL:            https://github.com/matrix-org/%{srcname}
Source0:        %{url}/archive/v%{version}/%{srcname}-v%{version}.tar.gz
BuildArch:      noarch

%description
%{desc}


%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{srcname}}


%description -n python3-%{srcname}
%{desc}


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%check
# ldaptor isn't packaged for Python 3
#PYTHONPATH=. trial-3 tests


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/*


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.4-2
- Rebuilt for Python 3.9

* Sun May 17 2020 Dan Callaghan <djc@djc.id.au> - 0.1.4-1
- new upstream release 0.1.4

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.3-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.3-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.3-4
- Subpackage python2-matrix-synapse-ldap3 has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Dec 29 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.3-3
- Enable python dependency generator

* Fri Dec 28 2018 Jeremy Cline <jeremy@jcline.org> - 0.1.3-2
- Add Python 3 subpackage

* Thu Oct 04 2018 Jeremy Cline <jeremy@jcline.org> - 0.1.3-1
- Bump to 0.1.3

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 12 2017 Jeremy Cline <jeremy@jcline.org> - 0.1.2-2
- Bump the release to rebuild on F26

* Tue Mar 07 2017 Jeremy Cline <jeremy@jcline.org> - 0.1.2-1
- Initial package
