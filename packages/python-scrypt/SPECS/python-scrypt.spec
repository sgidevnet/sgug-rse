%global pypi_name scrypt

%global common_desc Python scrypt bindings This is a set of Python bindings \
for the scrypt key derivation function. Scrypt is useful when encrypting \
password as it is possible to specify a *minimum* amount of time to use when \
encrypting and decrypting. If, for example, a password takes 0.05 seconds to \
verify, a user won't notice the slight delay when signing in, but doing a \
brute force search of several...


Name:           python-%{pypi_name}
Version:        0.8.0
Release:        13%{?dist}
Summary:        Bindings for the scrypt key derivation function library

License:        BSD
URL:            http://bitbucket.org/mhallin/py-scrypt
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  gcc
BuildRequires:  openssl-devel

# Missing license file: https://bitbucket.org/mhallin/py-scrypt/issues/31
# Broken tests in source tarball: https://bitbucket.org/mhallin/py-scrypt/issues/21

%description
%{common_desc}

%package -n     python3-%{pypi_name}
Summary:        Bindings for the scrypt key derivation function library
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Provides:       bundled(scrypt) = 1.2.0
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{common_desc}


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install


%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitearch}/__pycache__/%{pypi_name}*
%{python3_sitearch}/%{pypi_name}.py*
%{python3_sitearch}/_%{pypi_name}*.so
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-13
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.8.0-7
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.8.0-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jun  7 2017 Haïkel Guémar <hguemar@fedoraproject.org> - 0.8.0-2
- Add virtual provides for bundled code

* Fri Jun  2 2017 Haïkel Guémar <hguemar@fedoraproject.org> - 0.8.0-1
- Initial package.
